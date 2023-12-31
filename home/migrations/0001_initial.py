# Generated by Django 5.0 on 2023-12-20 08:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Natoshi",
            fields=[
                ("nid", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.IntegerField()),
                ("gutno", models.IntegerField()),
                ("crop", models.CharField(max_length=100)),
                ("area", models.FloatField()),
                ("village", models.CharField(max_length=100)),
                ("remarks", models.CharField(max_length=100)),
                ("owner", models.CharField(max_length=100)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "db_table": "Natoshi",
                "managed": False,
            },
        ),
    ]
