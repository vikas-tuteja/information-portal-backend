# Generated by Django 3.1.4 on 2021-01-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_library_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]