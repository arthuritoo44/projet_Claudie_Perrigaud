# **Projet: Analyse et Visualisation des Données Web et Réseaux Sociaux pour le Développement de l'Activité de Sculptrice de Claudie Perrigaud** 🎨

Ce GitHub contient la totalité des versions permettant la mise en place du processus ETL nécessaire à la valorisation des données du site internet et des réseaux sociaux de Claudie Perrigaud, artiste sculptrice. À noter que le projet est actuellement en cours de développement et va être amené à évoluer continuellement.

![GitHub issues](https://img.shields.io/github/issues/arthuritoo44/projet_Claudie_Perrigaud)
![GitHub forks](https://img.shields.io/github/forks/arthuritoo44/projet_Claudie_Perrigaud)
![GitHub stars](https://img.shields.io/github/stars/arthuritoo44/projet_Claudie_Perrigaud)

## 🛠️ Prérequis

- **Python 3.x**
- **Bibliothèques Python** : Prefect, pandas, pymysql, google-auth, google-api-python-client
- **Accès à Google Analytics API**
- **Base de données MySQL**

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/arthuritoo44/projet_Claudie_Perrigaud.git


## Exécution
1. Placez les fichiers `extraction_donnees_reseaux.csv` et `extraction_donnees_site.csv` dans le même répertoire que le script `data_pipeline.py`.
2. Exécutez le script avec la commande suivante :
   python data_pipeline.py
3. Les résultats seront sauvegardés dans la base de données MySQL

## Sommaire

- [1. Introduction](#1-introduction)
- [1.1. Objectif du Projet](#11-objectif-du-projet)
- [1.2. Approche du Projet](#12-approche-du-projet)
- [1.3. Déroulé du projet](#13-déroulé-du-projet)
- [2. Mise en place du pipeline de données](#2-mise-en-place-du-pipeline-de-données)
- [2.1. Extraction des données](#21-extraction-des-données)
- [2.2. Transformation des données](#22-transformation-des-données)
- [2.3. Fusion des données](#23-fusion-des-données)
- [2.4. Chargement des données](#24-chargement-des-données)
- [2.5. Exécution du pipeline](#25-exécution-du-pipeline)

## **1. Introduction**

### **1.1 Objectif du Projet**
Le principal objectif est de **mettre en place un processus ETL** (Extract, Transform, Load) pour intégrer et analyser les données provenant de son site Web et de ses réseaux sociaux. Il sera crucial de sélectionner uniquement les données importantes afin de les exploiter par la suite.  Cette analyse sera visualisée à l'aide de Power BI pour fournir des insights exploitables qui aideront à optimiser les stratégies de marketing et à améliorer l'expérience utilisateur. Le projet inclura également l'utilisation de Git pour le suivi des modifications du code et des processus.

### **1.2 Approche du Projet**
#### Extraction des Données:
Site Web: Utilisation de l'API Google Analytics pour extraire les données de trafic du site Web. Les données extraites incluront des métriques telles que les sessions, les utilisateurs, les vues de pages, la durée moyenne des sessions, et le taux de rebond.
Réseaux Sociaux: Préparation pour l'extraction des données des réseaux sociaux, en particulier Instagram, à l'aide des API disponibles pour obtenir des métriques telles que les interactions, les mentions, et les performances des publications.


#### Transformation des Données:
Nettoyage des Données: Traitement des données extraites pour éliminer les valeurs manquantes et les anomalies.
Normalisation des données pour assurer la cohérence entre les différentes sources.
Combinaison des Données: Fusion des données du site Web et des réseaux sociaux pour obtenir une vue d'ensemble complète des performances en ligne et ainsi pouvoir établir une stratégie globale.

#### Chargement des Données:
Base de Données: Chargement des données nettoyées et combinées dans MySQL pour une analyse ultérieure.
Power BI: Intégration des données dans Power BI pour créer des tableaux de bord et des visualisations interactives.
Versionnage avec Git:
Suivi des Modifications: Utilisation de Git pour versionner les scripts ETL, les transformations de données et les configurations Power BI. Cela permet de suivre les modifications, de collaborer efficacement et de gérer les versions du projet.

#### Visualisation des Résultats:
Power BI: Création de tableaux de bord dans Power BI pour visualiser les tendances, les performances des pages, les interactions sur les réseaux sociaux, et les données combinées. Les visualisations permettront de prendre des décisions basées sur des données concrètes et d'optimiser les stratégies en ligne.

#### Bénéfices Attendus:
Vue d’Ensemble Intégrée: Une vision complète des performances du site Web et des réseaux sociaux, facilitée par la combinaison des données.
Optimisation des Stratégies: Amélioration des stratégies de publication et de marketing grâce à des insights basés sur des données intégrées et visualisées.
Suivi des Modifications: Gestion efficace des modifications et des améliorations du code et des processus grâce au versionnage Git.
Prise de Décision Éclairée: Capacités de prise de décision basées sur des visualisations claires et des analyses approfondies dans Power BI.

#### Explication des données
Ce projet a pour objectif de mettre en place un processus ETL qui permettra dans un second temps d’analyser les données afin de produire des insights. Avant toute chose, il semble nécessaire d’expliquer brièvement chaque donnée que nous allons étudier dans ce projet. A noter que ce projet est amené à évoluer en fonction des améliorations envisageables ainsi que les problématiques et les questionnements apportés par l’artiste.

##### Explication des colonnes de Données des Réseaux Sociaux :
**Couverture Facebook/Instagram**
Nombre total de personnes qui ont vu le contenu sur Facebook/Instagram.
**Visites Facebook/Instagram**
Nombre de visites sur la page Facebook/Instagram.
**Interactions Facebook/Instagram**
Nombre total d'interactions sur les publications Facebook/Instagram (likes, commentaires, partages).

##### Explication des colonnes de Données du Site Web :
**Sessions**
Nombre de sessions (visites) sur le site web.
**Total Users**
Nombre total d'utilisateurs distincts qui ont visité le site web.
**Screen Page Views**
Nombre total de pages vues (écrans) sur le site web.
**Average Session Duration**
Durée moyenne des sessions en secondes.
**Bounce Rate**
Taux de rebond, représentant le pourcentage de sessions où les utilisateurs quittent le site web après avoir vu une seule page.
**Engaged Sessions**
Nombre de sessions où les utilisateurs ont interagi de manière significative avec le site web (par exemple, pages visitées).
**New Users**
Nombre d'utilisateurs qui visitent le site web pour la première fois.
**Event Count**
Nombre total d'événements enregistrés sur le site web (comme les clics sur des boutons, les soumissions de formulaires, etc.).

### **1.3 Déroulé du projet**

Ce projet va être construit autour d’une pipeline de données et ceci s’explique par différentes raisons. Tout d’abord, il implique l'intégration de données provenant de plusieurs sources (site web et réseaux sociaux), il est donc nécessaire de mettre plusieurs processus en place permettant le recueil, la transformation ainsi que la fusion des données. 
Voici les raisons principales pour lesquelles une pipeline a été mise en place. Tout d’abord, cela va permettre d’automatiser certaines tâches répétitives et de réaliser une exécution de ce script à intervalle régulier. Dans notre cas, l’intervalle choisi est mensuel, ceci s’explique par la charge de données qui reste encore limitée. De plus, une analyse mensuelle semble être un bon compromis afin d’évaluer les résultats des différents ajustements mis en place afin d’améliorer le trafic du site internet et des réseaux sociaux de l’artiste. Ensuite, la pipeline de données assure la cohérence et la standardisation des données du fait que chaque fois que le script sera exécuté les mêmes transformations seront apportées que celle de l'échantillon précédent. Enfin, cela permet d’avoir un suivi sur la gestion des échecs afin de comprendre rapidement d'où provient le problème. Pour ce qui est de l’évolutivité du projet, il sera plus facile de rajouter des données avec un pipeline de données bien construit. 
A noter que le choix de Prefect a été privilégié plutôt qu'Apache Airflow en raison des contraintes spécifiques liée à l’utilisation d’Airflow avec l'environnement Windows. Prefect a ainsi été choisi comme alternative notamment en raison de sa simplicité d'utilisation et de sa compatibilité avec les environnements Windows.

## **2. Mise en place du pipeline de données**
Cette partie va récapituler les différentes étapes et les raisons pour lesquelles elles ont été mises en œuvre, ainsi que les choix techniques et les défis rencontrés. Avant de créer le script de pipeline complet, chaque partie du processus a été testée séparément. Cela permet de vérifier le bon fonctionnement de chaque composant et d'identifier les éventuelles problématiques pouvant apparaître avant d'intégrer toutes les étapes en un seul flux de travail. Afin de mieux comprendre la façon dont a été mis en place le pipeline, vous pouvez ouvrir le script data_pipeline.py qui contient la totalité du script qui va être détaillé par la suite. Avant toute chose, décrivons brièvement les tâches effectuées dans ce script.

#### Extraction des Données :
Le script pour extraire les données du site web à partir de Google Analytics a été testé pour s'assurer que les données étaient correctement récupérées et sauvegardées en format CSV. Cette partie peut être amenée à évoluer afin d’intégrer de nouveaux indicateurs à l’analyse. Pour ce qui est des données des réseaux sociaux, elles sont pour le moment extraites via des fichiers csv.
Transformation des Données : Les données manquantes ont été supprimées via la suppression des colonnes représentées. Ceci s’explique par le fait que les données manquantes été très importantes dans ces colonnes. Pour ce qui est du type des données, le format date était différent entre les deux sources de données, il a donc été harmonisé avant la fusion des données.

#### Fusion des Données :
Le script pour fusionner les données extraites avec celles des réseaux sociaux a été testé pour vérifier que les données étaient correctement combinées et nettoyées. Cette étape est cruciale car elle permet de créer une base de données prête à l’analyse

#### Chargement dans MySQL :
Le script pour insérer les données dans la base de données MySQL a été testé pour garantir que les données étaient correctement insérées dans la base de données sans erreurs.

### **2.1 Extraction des données**
L'extraction des données du site web via l'API Google Analytics est essentielle pour obtenir des métriques précises sur la performance du site. Étant donné que l’abonnement de l’artiste n’inclut pas la possibilité d’utiliser les API du site internet (squarespace), le choix s’est porté sur google analytics qui est relativement simple d’initialisation et d’utilisation et qui regroupe toutes les métriques importantes. Cette étape est automatisée pour se dérouler chaque mois afin de fournir des nouvelles données fraîches pour l'analyse.
```python
@task
def get_google_analytics_data():
    SERVICE_ACCOUNT_FILE = 'C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/projet-claudie-perrigaud-8e14bf43e103.json'
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    PROPERTY_ID = '452047964'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('analyticsdata', 'v1beta', credentials=credentials)
```

Dans cette première section, j’ai implémenté une tâche qui extrait les données de Google Analytics en utilisant l’API de Google Analytics. Cela permet d'automatiser la collecte des métriques du site web de Claudie Perrigaud.

La première étape consiste à utiliser un fichier de compte de service (SERVICE_ACCOUNT_FILE) pour authentifier l’accès à l’API Google Analytics. Ce fichier est généré au format json depuis Google Cloud Platform et contient toutes les informations d'identification nécessaires pour accéder aux données de Google Analytics. Il y a également Le paramètre SCOPES qui est défini en readonly ce qui signifie que le script peut uniquement lire les données présentes dans Google Analytics. Pour ce qui est de l’identification du site internet de Claudie Perrigaud sur Google Analytics, c’est l’objet PROPERTY_ID qui nous en informe. Il s'agit d'un identifiant unique associé à chaque compte Google Analytics, permettant de spécifier le site web dont nous souhaitons extraire les données. Enfin, on utilise les informations d’identification (credentials) pour construire le service API. A noter que même si nous utilisons la version beta, elle contient la totalité des outils nécessaires au bon fonctionnement de notre projet.

```python
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
        print(f'Une erreur est survenue: {err}')
```

La deuxième partie d’extraction des données du site internet consiste à renseigner les métriques, dimensions, la période de temps pour ainsi exporter les données dans un fichier csv.
Nous rentrons ensuite dans le script les différentes métriques que nous souhaitons analyser ainsi que la période de temps sur laquelle récupérer les données, ici mensuel, à l’aide de la clé de dictionnaire python suivante: 'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}]. Notre projet contient plusieurs métriques pour une seule dimension à savoir la date.

Il m’a semblé intéressant d’utiliser un bloc try-except afin de gérer les erreurs pouvant survenir. Dans le cas ou l’on fait face à une erreur, elle sera capturée par l’exception: except HttpError as err: print(f'Une erreur est survenue: {err}')
Le script exporte ensuite les résultats de la requête dans un fichier csv avec en en-tête les métriques déterminées précédemment. Un message de confirmation mentionnant que l’export des données dans le fichier csv a réussi permet d’avoir une visibilité immédiate du résultat de la requête.

### **2.2 Transformation des données**

La partie transformation et nettoyage des données a été directement imbriqué avec la seconde tâche de fusion des données. Pour ce qui est des valeurs manquantes, après études des données, nous remarquons qu’elles peuvent être remplacées par 0 au lieu d’être supprimées et ainsi perdre de l’information. Ceci étant effectuée via cette commande : donnees_fusionnees.fillna(0, inplace=True).
Ensuite, il a été nécessaire d’harmoniser les dates en leur attribuant le même format via cette fonction :
```python
reseaux['date'] = pd.to_datetime(reseaux['date'], format='%d/%m/%Y') 
site['date'] = pd.to_datetime(site['date'], format='%Y%m%d')
```
Cette fonction Pandas est indispensable afin d’effectuer la fusion des deux tables.

## **2.3 Fusion des données**
```python
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
    # Remplacement des valeurs manquantes par 0
    donnees_fusionnees.fillna(0, inplace=True)

    # Sauvegarde des données fusionnées
    donnees_fusionnees.to_csv('C:/Users/arthu/OneDrive/Documents/Projet_Claudie_Perrigaud/donnees_fusionnees.csv', index=False)

    print("Fusion des données réalisée avec succès.")

    return donnees_fusionnees
```
La fonction merge_data est ensuite implémentée via Prefect, elle représente la deuxième étape de ce processus ETL. Elle se charge de fusionner les données provenant des réseaux sociaux et du site web avant leur stockage dans la base de données MySQL. Plusieurs fonctions Pandas sont utilisées dans cette tâche, la fonction pd.read_csv() permet le chargement des données des deux sources. La méthode pd.merge() est ensuite implémentée avec une jointure externe how=’outer’, cela signifie que la totalité des lignes des deux fichiers seront intégrées. Pour terminer, le fichier avec les données fusionnées est ensuite sauvegardé au format csv dans le répertoire du projet.

### **2.4 Chargement des données**
```python
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
```
La dernière étape du pipeline de traitement est orchestrée autour de la fonction save_to_mysql permettant le stockage dans une base de données MySQL.
Après s’être connectée à la base de données initialisée pour cette table, une table dynamique est créée de manière à ce que les données précédentes soient sauvegardées à chaque nouvelle exécution. Chaque table portera donc un nom unique généré à partir de la date et l’heure du jour de l’exécution du script. 

```python
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
```
La table est ensuite créé avec toutes les colonnes nécessaires pour accueillir les données. Elles sont insérées via une requête SQL INSERT INTO et la méthode cursor.execute() parcours chaque ligne du dataframe et insère les valeurs. Les données insérées sont ensuite validées via la commande connection.commit() qui permet l’enregistrement permanent dans la table MySQL. La connexion est ensuite fermée afin de libérer les ressources et éviter des connexions inutiles. Cette étape permet l’enregistrement dans une base de données MySQL avec un système assez flexible permettant une persistance des données et un historique bien défini.


### **2.5 Exécution du pipeline**

```python
@flow
def data_pipeline():
    get_google_analytics_data()
    merged_data = merge_data()
    save_to_mysql(merged_data)

# Exécution du flux
if __name__ == "__main__":
    data_pipeline()
```

Pour terminer, les différentes étapes initialisées précédemment sont intégrées dans la fonction data_pipeline qui est un outil de gestion de workflows dans Prefect afin d’automatiser l'enchaînement des différentes tâches.
A la suite de cela, le bloc final permet de lancer le pipeline de données dès lors que le script est exécuté.
