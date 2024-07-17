# Generated by Django 5.0.6 on 2024-07-17 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('no_of_guests', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('booking_date', models.DateTimeField()),
                ('menu_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
        ),
    ]
