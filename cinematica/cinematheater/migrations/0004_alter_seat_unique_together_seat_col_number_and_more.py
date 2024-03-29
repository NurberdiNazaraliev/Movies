# Generated by Django 5.0.2 on 2024-02-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinematheater', '0003_seat'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='seat',
            name='col_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('room', 'row_number', 'col_number')},
        ),
    ]
