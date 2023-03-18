from google.cloud import bigquery

def create_bigquery_client():
    """
    Creates a BigQuery client using the application default credentials.
    """
    return bigquery.Client()

def create_bigquery_dataset(client, dataset_id):
    """
    Creates a BigQuery dataset.
    """
    dataset = bigquery.Dataset(client.dataset(dataset_id))
    dataset.location = 'US'
    return client.create_dataset(dataset)

def create_bigquery_table(client, table_id, schema):
    """
    Creates a BigQuery table.
    """
    table_ref = client.dataset('mydataset').table(table_id)
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    return table
