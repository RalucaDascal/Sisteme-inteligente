# Generated by Django 3.2.4 on 2021-06-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airTemperature', models.FloatField(default=0)),
                ('pressure', models.FloatField(default=0)),
                ('humidity', models.FloatField(default=0)),
                ('precipitation', models.FloatField(default=0)),
                ('visibility', models.FloatField(default=0)),
                ('waterTemperature', models.FloatField(default=0)),
                ('waveDirection', models.FloatField(default=0)),
                ('waveHeight', models.FloatField(default=0)),
                ('windWaveDirection', models.FloatField(default=0)),
                ('windDirection', models.FloatField(default=0)),
                ('windSpeed', models.FloatField(default=0)),
                ('wavePeriod', models.FloatField(default=0)),
            ],
        ),
    ]
