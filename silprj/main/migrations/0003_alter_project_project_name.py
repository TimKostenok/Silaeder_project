# Generated by Django 3.2.12 on 2022-10-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_project_autors_remove_project_full_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default='Random project', max_length=127, unique=True),
        ),
    ]