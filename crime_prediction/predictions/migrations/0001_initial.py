# Generated by Django 4.0.5 on 2022-07-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('predicted_case', models.CharField(max_length=300)),
            ],
        ),
    ]