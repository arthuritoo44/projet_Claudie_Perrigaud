from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

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
                'dateRanges': [{'startDate': '120daysAgo', 'endDate': 'yesterday'}],  # Date modifiées
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
        print(f'Une erreur est survenue: {err}')

get_google_analytics_data()