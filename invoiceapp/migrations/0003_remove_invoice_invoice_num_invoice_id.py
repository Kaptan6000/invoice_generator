# Generated by Django 4.2 on 2023-04-20 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0002_remove_invoice_id_invoice_invoice_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_num',
        ),
        migrations.AddField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
