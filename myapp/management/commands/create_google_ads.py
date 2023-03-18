from django.core.management.base import BaseCommand
from myapp.utils import create_bigquery_client
from google.cloud import bigquery


class Command(BaseCommand):
    help = 'Create the GoogleAds table in BigQuery'

    def handle(self, *args, **options):
        # Create a BigQuery table for storing ad data
        client = create_bigquery_client()
        schema = [
            bigquery.SchemaField('ad_id', 'INTEGER'),
            bigquery.SchemaField('ad_name', 'STRING'),
            bigquery.SchemaField('impressions', 'INTEGER'),
            bigquery.SchemaField('clicks', 'INTEGER'),
            bigquery.SchemaField('cost', 'FLOAT'),
            bigquery.SchemaField('conversions', 'INTEGER'),
            bigquery.SchemaField('cpa', 'FLOAT'),
            bigquery.SchemaField('cpc', 'FLOAT'),
            bigquery.SchemaField('roas', 'FLOAT'),
        ]
        table = bigquery.Table('mydataset.GoogleAds', schema=schema)
        table = client.create_table(table)

        self.stdout.write(self.style.SUCCESS('Successfully created GoogleAds table.'))
