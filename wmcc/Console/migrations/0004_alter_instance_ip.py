# Generated by Django 3.2.9 on 2021-11-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Console', '0003_instance_instance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='ip',
            field=models.TextField(default='X.X.X.X (Booting Instance)'),
        ),
    ]