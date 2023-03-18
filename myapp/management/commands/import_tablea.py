from django.core.management.base import BaseCommand
from myapp.models import TableA
from myapp.utils import create_bigquery_client

class Command(BaseCommand):
    help = 'Import data from BigQuery TableA to local database'

    def handle(self, *args, **options):
        # Retrieve data from BigQuery
        client = create_bigquery_client()
        query_job = client.query('SELECT name, age FROM mydataset.mytable')
        rows = query_job.result()

        # Convert BigQuery rows to Django model instances and save to local database
        for row in rows:
            TableA.objects.create(name=row['name'], age=row['age'])
