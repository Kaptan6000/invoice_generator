# Generated by Django 4.2 on 2023-04-20 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0007_invoice_invoice_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]
