# Generated by Django 2.0.7 on 2018-07-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DyttItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('film_name', models.CharField(max_length=100)),
                ('publish_time', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=150)),
                ('trans_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=30)),
                ('decade', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('film_type', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('subtitles', models.CharField(max_length=50)),
                ('IMDB_score', models.CharField(max_length=30)),
                ('douban_score', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=100)),
                ('format', models.CharField(max_length=30)),
                ('resolution', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=300)),
                ('magnet_link', models.CharField(max_length=100)),
                ('thunder_link', models.CharField(max_length=100)),
                ('image_link', models.CharField(max_length=100)),
                ('introduction', models.CharField(max_length=500)),
            ],
        ),
    ]
