# Generated by Django 2.1.7 on 2019-02-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190215_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parents',
            field=models.IntegerField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
