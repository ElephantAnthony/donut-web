# Generated by Django 4.0.2 on 2022-08-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_article_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
