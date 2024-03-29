# Generated by Django 5.0.2 on 2024-02-11 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinematheater', '0004_alter_seat_unique_together_seat_col_number_and_more'),
        ('movies', '0007_remove_movie_is_hidden'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=6),
        ),
        migrations.CreateModel(
            name='MovieShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinematheater.room')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.ManyToManyField(to='cinematheater.seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinematheater.movieshow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
