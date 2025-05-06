from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import csv
import pymysql
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_google_analytics_data():
    SERVICE_ACCOUNT_FILE = '/opt/airflow/google_credentials/projet-claudie-perrigaud-8e14bf43e103.json' #adapt path for docker container
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    PROPERTY_ID = '452047964'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('analyticsdata', 'v1beta', credentials=credentials)

    try:
        response = service.properties().runReport(
            property='properties/' + PROPERTY_ID,
            body={
                'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
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
                'dimensions': [
                    {'name': 'date'}
                ]
            }
        ).execute()

        with open('/opt/airflow/data/extraction_donnees_site.csv', mode="w", newline="") as file: #adapt path for docker container
            writer = csv.writer(file)
            header = [dimension['name'] for dimension in response.get('dimensionHeaders', [])] + \
                      [metric['name'] for metric in response.get('metricHeaders', [])]
            writer.writerow(header)
            rows = response.get('rows', [])
            for row in rows:
                data_row = [value.get('value', '') for value in row.get('dimensionValues', [])] + \
                           [value.get('value', '') for value in row.get('metricValues', [])]
                writer.writerow(data_row)

        print("Les données ont été exportées avec succès vers extraction_donnees_site.csv")

    except HttpError as err:
        print(f'Une erreur est survenue: {err}')

def merge_data():
    reseaux = pd.read_csv('/opt/airflow/data/extraction_donnees_reseaux.csv', sep=',') #adapt path for docker container
    site = pd.read_csv('/opt/airflow/data/extraction_donnees_site.csv', sep=',') #adapt path for docker container

    reseaux['date'] = pd.to_datetime(reseaux['date'], format='%d/%m/%Y')
    site['date'] = pd.to_datetime(site['date'], format='%Y%m%d')

    donnees_fusionnees = pd.merge(reseaux, site, on='date', how='outer')
    donnees_fusionnees.fillna(0, inplace=True)
    donnees_fusionnees.to_csv('/opt/airflow/data/donnees_fusionnees.csv', index=False) #adapt path for docker container

    print("Fusion des données réalisée avec succès.")
    return donnees_fusionnees

def save_to_mysql(dataframe):
    connection = pymysql.connect(
        host='mysql_host', #adapt to your mysql host. if using docker network, use mysql container name.
        user='root',
        password='Mecano44!',
        database='projet_claudie_perrigaud'
    )

    table_name = "analyse_donnees_" + datetime.now().strftime('%Y%m%d_%H%M%S')
    try:
        with connection.cursor() as cursor:
            create_table_query = f"""
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
            """
            cursor.execute(create_table_query)

            insert_query = f"""
            INSERT INTO {table_name} (
                date, couverture_facebook, visites_facebook, interactions_facebook,
                couverture_instagram, interactions_instagram, visites_instagram,
                sessions, totalUsers, screenPageViews, averageSessionDuration,
                bounceRate, engagedSessions, newUsers, eventCount
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for _, row in dataframe.iterrows():
                cursor.execute(insert_query, tuple(row))

        connection.commit()
        print("Les données ont été enregistrées dans la base de données MySQL avec succès.")

    finally:
        connection.close()

with DAG(
    dag_id='data_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@monthly',
    catchup=False,
) as dag:
    extract_ga_task = PythonOperator(
        task_id='extract_google_analytics',
        python_callable=get_google_analytics_data,
    )
    merge_data_task = PythonOperator(
        task_id='merge_data',
        python_callable=merge_data,
    )
    save_to_mysql_task = PythonOperator(
        task_id='save_to_mysql',
        python_callable=save_to_mysql,
        op_kwargs={'dataframe': '{{ ti.xcom_pull(task_ids="merge_data") }}'},
    )
    extract_ga_task >> merge_data_task >> save_to_mysql_task