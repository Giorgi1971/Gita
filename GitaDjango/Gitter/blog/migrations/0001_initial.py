# Generated by Django 4.0.2 on 2022-03-04 20:46

import builtins
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=124)),
                ('text', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.ForeignKey(on_delete=builtins.any, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=builtins.any, related_name='comments', to='blog.post')),
            ],
        ),
    ]
