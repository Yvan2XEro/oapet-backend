# Generated by Django 3.2.4 on 2021-07-11 19:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0001_initial'),
        ('weekschedule', '0002_week_is_generated'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='level_class',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='teaching.class'),
            preserve_default=False,
        ),
    ]