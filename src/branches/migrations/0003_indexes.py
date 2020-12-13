# Generated by Django 2.2.17 on 2020-12-13 16:03

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0002_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AddIndex(
            model_name='branch',
            index=django.contrib.postgres.indexes.GistIndex(fields=['location'], name='branch_location_gist_index'),
        ),
    ]
