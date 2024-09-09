# Projet data Claudie Perrigaud

Ce github contient la totalité des versions permettant la mise en place du processus ETL nécessaire à la valorisation des données du site internet et des réseaux sociaux de Claudie Perrigaud, artiste sculptrice.

## Processus d'éxecution du projet
### 1.Fusion des Données des Réseaux Sociaux et Site Web

#### Description
Le script fusion_donnees.py fusionne les données des réseaux sociaux et du site web, puis effectue une analyse simple.

#### Exécution
1. Placez les fichiers `extraction_donnees_reseaux.csv` et `extraction_donnees_site.csv` dans le même répertoire que le script.
2. Exécutez le script avec `python fusion_donnees.py`.
3. Les résultats seront sauvegardés dans `description_donnees.csv`.
