# Generated by Django 3.1.4 on 2021-01-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_auto_20210113_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='duration',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
