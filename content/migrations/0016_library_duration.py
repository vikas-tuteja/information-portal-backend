# Generated by Django 3.1.4 on 2021-01-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20210106_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='duration',
            field=models.FloatField(default=0.0),
        ),
    ]
