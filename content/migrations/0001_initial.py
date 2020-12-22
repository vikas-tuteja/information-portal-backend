# Generated by Django 3.1.4 on 2020-12-21 09:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='content/images/')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('audio_file', models.FileField(help_text='Allowed type - .mp3, .wav, .ogg', upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('active_from', models.DateTimeField(blank=True, null=True)),
                ('active_till', models.DateTimeField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.status')),
                ('sub_category', models.ManyToManyField(to='category.SubCategory')),
            ],
            options={
                'verbose_name_plural': 'Library',
                'db_table': 'library',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('views', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
                ('active_from', models.DateTimeField(blank=True, null=True)),
                ('active_till', models.DateTimeField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.status')),
                ('sub_category', models.ManyToManyField(to='category.SubCategory')),
            ],
            options={
                'db_table': 'content',
            },
        ),
    ]
