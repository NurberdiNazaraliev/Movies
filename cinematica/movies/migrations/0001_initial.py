# Generated by Django 5.0.2 on 2024-02-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('duration', models.PositiveIntegerField()),
            ],
        ),
    ]