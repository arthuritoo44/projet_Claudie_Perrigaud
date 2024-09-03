import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Chemin vers le fichier JSON de clé du compte de service
SERVICE_ACCOUNT_FILE = 'C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/projet-claudie-perrigaud-8e14bf43e103.json'

# Scopes pour l'API Google Analytics
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

# ID de la propriété Google Analytics
PROPERTY_ID = '452047964'

# Charger les informations d'identification du compte de service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Créer un service Google Analytics
service = build('analyticsdata', 'v1beta', credentials=credentials)

# Fonction pour obtenir les rapports
def get_report():
    try:
        return service.properties().runReport(
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
    except HttpError as err:
        print(f'An error occurred: {err}')
        return None

# Appeler la fonction et écrire les résultats dans un fichier CSV
def export_to_csv(report, filename="extraction_donnees_site.csv"):
    if report:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            
            # Écrire les en-têtes de colonnes
            header = [dimension['name'] for dimension in report.get('dimensionHeaders', [])] + \
                     [metric['name'] for metric in report.get('metricHeaders', [])]
            writer.writerow(header)
            
            # Écrire les données
            rows = report.get('rows', [])
            for row in rows:
                data_row = [value.get('value', '') for value in row.get('dimensionValues', [])] + \
                          [value.get('value', '') for value in row.get('metricValues', [])]
                writer.writerow(data_row)

        print(f"Les données ont été exportées avec succès vers {filename}")

# Exécuter la récupération et l'exportation des données
report = get_report()
export_to_csv(report)
