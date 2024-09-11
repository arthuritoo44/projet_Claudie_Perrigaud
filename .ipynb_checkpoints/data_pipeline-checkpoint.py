from prefect import flow, task
import pandas as pd
import csv
import pymysql
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import timedelta
from datetime import datetime


@task
def get_google_analytics_data():
    SERVICE_ACCOUNT_FILE = 'C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/projet-claudie-perrigaud-8e14bf43e103.json'
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

        with open('C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/extraction_donnees_site.csv', mode="w", newline="") as file:
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
        print(f'An error occurred: {err}')

@task
def merge_data():
    # Chargement des données
    reseaux = pd.read_csv('C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/extraction_donnees_reseaux.csv', sep=',')
    site = pd.read_csv('C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/extraction_donnees_site.csv', sep=',')

    # Conversion des colonnes de date au format datetime
    reseaux['date'] = pd.to_datetime(reseaux['date'], format='%d/%m/%Y')
    site['date'] = pd.to_datetime(site['date'], format='%Y%m%d')

    # Fusion des deux DataFrames
    donnees_fusionnees = pd.merge(reseaux, site, on='date', how='outer')
    
    # Suppression des lignes contenant des valeurs manquantes
    donnees_fusionnees.dropna(inplace=True)

    # Sauvegarde des données fusionnées
    donnees_fusionnees.to_csv('C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/donnees_fusionnees.csv', index=False)

    print("Fusion des données réalisée avec succès.")

    return donnees_fusionnees  

@task
def save_to_mysql(dataframe):
    # Configuration de la connexion à MySQL
    connection = pymysql.connect(
        host='localhost',         
        user='root',              
        password='Mecano44!',      
        database='projet_claudie_perrigaud'    
    )
    
    # Nom de table dynamique avec la date et l'heure pour éviter la suppression des données
    table_name = "analyse_donnees_" + datetime.now().strftime('%Y%m%d_%H%M%S')
    try:
        with connection.cursor() as cursor:
            # Création de la table avec toutes les colonnes nécessaires
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

            # Insertion des données
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

        # Commit des modifications
        connection.commit()
        print("Les données ont été enregistrées dans la base de données MySQL avec succès.")

    finally:
        connection.close()


@flow
def data_pipeline():
    get_google_analytics_data()
    merged_data = merge_data()
    save_to_mysql(merged_data)

# Exécution du flux
if __name__ == "__main__":
    data_pipeline()
