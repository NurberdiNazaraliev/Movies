# Generated by Django 5.0.2 on 2024-02-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
