# Generated by Django 2.2.17 on 2020-12-12 10:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models

import app.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.GeometryField(blank=True, geography=True, null=True, srid=4326)),
                ('name', models.CharField(max_length=255)),
                ('facade', models.ImageField(blank=True, upload_to=app.utils.RandomPath('branches/facades'))),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
