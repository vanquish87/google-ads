from django.contrib import admin
from django.db import connections

from myapp.models import TableA
from myapp.bq import create_bigquery_client

class TableAAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

    def get_queryset(self, request):
        # Connect to BigQuery and retrieve data for TableA
        client = create_bigquery_client()
        query = 'SELECT name, age FROM `myproject.mydataset.mytable`'
        rows = client.query(query).result()

        # Convert BigQuery rows to a Django QuerySet
        qs = []
        for row in rows:
            qs.append(TableA(name=row['name'], age=row['age']))
        return qs

    def save_model(self, request, obj, form, change):
        # Save the model to BigQuery
        client = create_bigquery_client()
        table_ref = client.dataset('mydataset').table('mytable')
        table = client.get_table(table_ref)
        row = {
            'name': obj.name,
            'age': obj.age,
        }
        errors = client.insert_rows(table, [row])
        if errors:
            raise Exception(errors)

admin.site.register(TableA, TableAAdmin)
