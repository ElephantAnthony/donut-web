# Generated by Django 4.0.2 on 2022-08-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0019_article_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='receipt',
            field=models.ImageField(null=True, upload_to='articlereceipt/'),
        ),
    ]
