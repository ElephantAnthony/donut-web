

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='article/')),
                ('content', models.TextField(null=True)),
                ('price', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='articlereceipt/')),
                ('hit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PriceCategory',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pricecategory', serialize=False, to='articleapp.article')),
                ('food', models.IntegerField(blank=True, default=0, null=True)),
                ('clothing', models.IntegerField(blank=True, default=0, null=True)),
                ('shelter', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('state', models.CharField(default='a', max_length=1)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign', to='articleapp.article')),
                ('participants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaign', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlecategory', to='articleapp.articlecategory'),
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to=settings.AUTH_USER_MODEL),
        ),
    ]
