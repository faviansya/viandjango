# Generated by Django 2.1.7 on 2019-02-14 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontenblog',
            name='deskripsi1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='kontenblog',
            name='deskripsi2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='kontenblog',
            name='deskripsi3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='kontenblog',
            name='deskripsi4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='kontenblog',
            name='deskripsi5',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='kontenblog',
            name='deskripsi',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]