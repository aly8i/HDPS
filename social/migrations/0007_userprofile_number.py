# Generated by Django 3.1.7 on 2021-05-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_post_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
