# Generated by Django 3.2.9 on 2021-11-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.TextField(default='Ubuntu Server 20.04 LTS')),
                ('ip', models.TextField()),
                ('booted', models.BooleanField(default=False)),
            ],
        ),
    ]