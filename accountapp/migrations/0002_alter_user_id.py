# Generated by Django 4.0.2 on 2022-11-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]