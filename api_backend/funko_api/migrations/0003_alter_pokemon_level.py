# Generated by Django 5.0.3 on 2024-05-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funko_api', '0002_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
