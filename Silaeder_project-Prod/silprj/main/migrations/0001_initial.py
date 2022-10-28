# Generated by Django 4.1 on 2022-10-25 17:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('reward_photo', models.FileField(upload_to='reward_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('short_text', models.CharField(max_length=511)),
                ('full_text', models.CharField(max_length=4095)),
                ('icon', models.FileField(upload_to='icons')),
                ('autors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]