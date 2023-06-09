# Generated by Django 4.1.7 on 2023-03-31 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('aircraft_type', models.CharField(max_length=100)),
                ('max_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airline_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('airline_name', models.CharField(max_length=100)),
                ('website_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aircraft_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.aircraft')),
                ('airline_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.airline')),
                ('arrival_airport_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='flights.airport')),
                ('departure_airport_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport', to='flights.airport')),
            ],
        ),
    ]
