# Generated by Django 2.2.5 on 2021-01-04 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bpub_data',
            new_name='bpub_date',
        ),
    ]
