from django.core.management.base import BaseCommand
from myapp.utils import create_bigquery_client

class Command(BaseCommand):
    help = 'Upload dummy ad data to the GoogleAds table in BigQuery'

    def handle(self, *args, **options):
        # Upload some dummy ad data to the GoogleAds table
        client = create_bigquery_client()
        table = client.get_table('mydataset.GoogleAds')
        rows = [
            (1, 'Ad 1', 100, 10, 50.0, 5),
            (2, 'Ad 2', 200, 20, 100.0, 10),
            (3, 'Ad 3', 300, 30, 150.0, 15),
        ]
        errors = client.insert_rows(table, rows)

        if not errors:
            self.stdout.write(self.style.SUCCESS('Successfully uploaded ad data to GoogleAds table.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to upload ad data to GoogleAds table.'))
