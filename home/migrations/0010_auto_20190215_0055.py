# Generated by Django 2.1.7 on 2019-02-15 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190215_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='mainpage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Posting'),
        ),
    ]