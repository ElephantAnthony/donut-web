# Generated by Django 4.0.2 on 2022-08-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0011_remove_campaign_clothing_remove_campaign_food_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='clothing',
        ),
        migrations.RemoveField(
            model_name='article',
            name='food',
        ),
        migrations.RemoveField(
            model_name='article',
            name='shelter',
        ),
        migrations.AddField(
            model_name='campaign',
            name='clothing',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='food',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='shelter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]