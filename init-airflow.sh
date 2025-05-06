#!/bin/bash
# Installer pymysql avant de démarrer Airflow
pip install pymysql

# Lancer Airflow après l'installation
exec "$@"
