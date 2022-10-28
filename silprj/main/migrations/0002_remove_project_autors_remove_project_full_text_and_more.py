# Generated by Django 4.1 on 2022-10-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='autors',
        ),
        migrations.RemoveField(
            model_name='project',
            name='full_text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='short_text',
        ),
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.CharField(default='OA', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='full_desc',
            field=models.CharField(default='It is a project', max_length=4095),
        ),
        migrations.AddField(
            model_name='project',
            name='project_name',
            field=models.CharField(default='Random project', max_length=127),
        ),
        migrations.AddField(
            model_name='project',
            name='sc_dir',
            field=models.CharField(default='OA', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='short_desc',
            field=models.CharField(default='It is a project', max_length=511),
        ),
    ]
