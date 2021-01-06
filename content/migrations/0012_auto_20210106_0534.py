# Generated by Django 3.1.4 on 2021-01-06 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20210105_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='show_summary',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='library',
            name='show_summary',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='summary',
            field=models.TextField(blank=True, help_text='Please enter a minimum of 180 characters', null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='summary',
            field=models.TextField(blank=True, help_text='Please enter a minimum of 180 characters', null=True),
        ),
    ]
