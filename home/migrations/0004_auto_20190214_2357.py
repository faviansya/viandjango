# Generated by Django 2.1.7 on 2019-02-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_youtubevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='statuspublih',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='youtubevideo',
            name='statuspublih',
            field=models.BooleanField(default=False),
        ),
    ]