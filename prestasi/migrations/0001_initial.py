# Generated by Django 2.1.7 on 2019-02-14 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostingPrestasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(max_length=5000)),
                ('gambar', models.ImageField(upload_to='upload')),
                ('jadwal_publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
