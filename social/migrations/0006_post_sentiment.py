# Generated by Django 3.1.7 on 2021-04-10 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20210131_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sentiment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
