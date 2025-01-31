# Generated by Django 4.1.3 on 2022-11-12 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articleapp', '0002_alter_article_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to=settings.AUTH_USER_MODEL),
        ),
    ]
