# Generated by Django 3.2.9 on 2021-11-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Console', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='password',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instance',
            name='username',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
