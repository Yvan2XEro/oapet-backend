# Generated by Django 3.2.4 on 2021-06-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_duration', models.IntegerField(default=60)),
                ('pause_duration', models.IntegerField(default=30)),
                ('Monday', models.BooleanField(default=True)),
                ('Tuesday', models.BooleanField(default=True)),
                ('Wdnesday', models.BooleanField(default=True)),
                ('Thursday', models.BooleanField(default=True)),
                ('Friday', models.BooleanField(default=True)),
                ('Saturday', models.BooleanField(default=True)),
                ('Sunday', models.BooleanField(default=True)),
            ],
        ),
    ]
