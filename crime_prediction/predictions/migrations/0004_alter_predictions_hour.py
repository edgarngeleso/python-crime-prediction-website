# Generated by Django 4.0.5 on 2022-07-15 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_alter_predictions_crime_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='hour',
            field=models.TimeField(),
        ),
    ]
