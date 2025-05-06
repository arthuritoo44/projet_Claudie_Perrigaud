from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from datetime import datetime
import pandas as pd
import csv
import pymysql
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import logging
import os

default_args = {
    'owner': 'airflow',
    'retries': 1,
}

# Fonction pour extraire les données Google Analytics
def get_google_analytics_data():
    SERVICE_ACCOUNT_FILE = '/opt/airflow/google_credentials/projet-claudie-perrigaud-8e14bf43e103.json'
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    PROPERTY_ID = '452047964'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('analyticsdata', 'v1beta', credentials=credentials)

    try:
        logging.info("Début de l'extraction des données Google Analytics.")
        response = service.properties().runReport(
            property='properties/' + PROPERTY_ID,
            body={
                'dateRanges': [{'startDate': '2025-01-14', 'endDate': '2025-04-04'}],
                'metrics': [
                    {'name': 'sessions'},
                    {'name': 'totalUsers'},
                    {'name': 'screenPageViews'},
                    {'name': 'averageSessionDuration'},
                    {'name': 'bounceRate'},
                    {'name': 'engagedSessions'},
                    {'name': 'newUsers'},
                    {'name': 'eventCount'}
                ],
                'dimensions': [{'name': 'date'}]
            }
        ).execute()

        file_path = '/opt/airflow/data/extraction_donnees_site.csv'
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            header = [d['name'] for d in response.get('dimensionHeaders', [])] + \
                     [m['name'] for m in response.get('metricHeaders', [])]
            writer.writerow(header)

            for row in response.get('rows', []):
                row_data = [v['value'] for v in row['dimensionValues']] + \
                           [v['value'] for v in row['metricValues']]
                writer.writerow(row_data)

        logging.info(f"Données exportées vers {file_path}")

    except HttpError as err:
        logging.error(f'Erreur HttpError : {err}', exc_info=True)
        raise
    except Exception as e:
        logging.error(f'Erreur inattendue : {e}', exc_info=True)
        raise

# Fonction pour fusionner les données
def merge_data(ti):
    reseaux_path = '/opt/airflow/data/extraction_donnees_reseaux_2025.csv'
    site_path = '/opt/airflow/data/extraction_donnees_site.csv'

    reseaux = pd.read_csv(reseaux_path, sep=',')
    site = pd.read_csv(site_path, sep=',')

    reseaux['date'] = pd.to_datetime(reseaux['date'], dayfirst=True, errors='coerce')
    site['date'] = pd.to_datetime(site['date'], format='%Y%m%d')

    donnees_fusionnees = pd.merge(reseaux, site, on='date', how='outer')
    donnees_fusionnees.fillna(0, inplace=True)

    fusion_path = '/opt/airflow/data/donnees_fusionnees_test.csv'
    donnees_fusionnees.to_csv(fusion_path, index=False)

    ti.xcom_push(key='fusion_path', value=fusion_path)
    logging.info(f"Fusion terminée, données enregistrées dans {fusion_path}")

def save_to_mysql(ti):
    fusion_path = ti.xcom_pull(task_ids='fusion_donnees', key='fusion_path')
    dataframe = pd.read_csv(fusion_path)

    connection = pymysql.connect(
        host='mysql',
        user='root',
        password='Mecano44!',
        database='projet_claudie_perrigaud',
        port=3306
    )

    table_name = "analyse_donnees_" + datetime.now().strftime('%Y%m%d_%H%M%S')

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    date DATE,
                    couverture_facebook FLOAT,
                    visites_facebook INT,
                    interactions_facebook INT,
                    couverture_instagram FLOAT,
                    interactions_instagram INT,
                    visites_instagram INT,
                    sessions INT,
                    totalUsers INT,
                    screenPageViews INT,
                    averageSessionDuration FLOAT,
                    bounceRate FLOAT,
                    engagedSessions INT,
                    newUsers INT,
                    eventCount INT
                );
            """)

            insert_query = f"""
                INSERT INTO {table_name} (
                    date, couverture_facebook, visites_facebook, interactions_facebook,
                    couverture_instagram, interactions_instagram, visites_instagram,
                    sessions, totalUsers, screenPageViews, averageSessionDuration,
                    bounceRate, engagedSessions, newUsers, eventCount
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for _, row in dataframe.iterrows():
                cursor.execute(insert_query, tuple(row))

        connection.commit()
        logging.info(f"Données insérées dans la table {table_name}.")

    finally:
        connection.close()

with DAG(
    dag_id='extract',
    default_args=default_args,
    description='Extraction des données GA4',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    extract_task = PythonOperator(
        task_id='extract_google_analytics_data',
        python_callable=get_google_analytics_data
    )

    merge_task = PythonOperator(
        task_id='fusion_donnees',
        python_callable=merge_data
    )

    save_to_mysql_task = PythonOperator(
        task_id='save_to_mysql',
        python_callable=save_to_mysql,
    )

    extract_task >> merge_task >> save_to_mysql_task
