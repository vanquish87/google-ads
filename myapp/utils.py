from google.cloud import bigquery

def create_bigquery_client():
    # Create a BigQuery client
    client = bigquery.Client()
    return client
