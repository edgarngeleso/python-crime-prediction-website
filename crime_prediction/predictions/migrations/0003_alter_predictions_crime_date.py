# Generated by Django 4.0.5 on 2022-07-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0002_rename_date_predictions_crime_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='crime_date',
            field=models.DateField(),
        ),
    ]
