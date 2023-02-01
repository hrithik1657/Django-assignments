# Generated by Django 2.2.1 on 2023-01-27 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('box_office_collection_in_crores', models.FloatField()),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_one_count', models.IntegerField(default=0)),
                ('rating_two_count', models.IntegerField(default=0)),
                ('rating_three_count', models.IntegerField(default=0)),
                ('rating_four_count', models.IntegerField(default=0)),
                ('rating_five_count', models.IntegerField(default=0)),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='imdb_1.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('is_debut_movie', models.BooleanField(default=False)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_1.Actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_1.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='imdb_1.MovieCast', to='imdb_1.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_1.Director'),
        ),
    ]
