# Generated by Django 4.2 on 2023-04-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='id',
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]