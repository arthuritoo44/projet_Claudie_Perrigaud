FROM apache/airflow:2.6.0

# Install MySQL dependencies
RUN pip install pymysql mysql-connector-python

# Install Google Analytics API dependencies
RUN pip install \
    google-api-python-client \
    google-auth \
    google-auth-httplib2 \
    google-auth-oauthlib
