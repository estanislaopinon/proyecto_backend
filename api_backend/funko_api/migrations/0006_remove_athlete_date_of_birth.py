# Generated by Django 5.0.3 on 2024-05-29 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0005_athlete_alter_pokemon_subtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='date_of_birth',
        ),
    ]
