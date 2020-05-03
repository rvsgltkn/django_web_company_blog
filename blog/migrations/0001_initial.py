# Generated by Django 2.0.13 on 2020-05-03 00:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'adek_about',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('image_url', models.FileField(upload_to='uploads/gallery/')),
            ],
            options={
                'db_table': 'adek_gallery',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('introduction', models.CharField(blank=True, max_length=200, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('image_url', models.FileField(upload_to='uploads/index/')),
            ],
            options={
                'db_table': 'adek_index',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'adek_language',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('introduction', models.CharField(blank=True, max_length=200, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('image_url', models.FileField(upload_to='uploads/service/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Language')),
            ],
            options={
                'db_table': 'adek_services',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('image_url', models.FileField(upload_to='uploads/testimonial/')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Language')),
            ],
            options={
                'db_table': 'adek_testimonial',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='index',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Language'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Language'),
        ),
        migrations.AddField(
            model_name='about',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Language'),
        ),
    ]
