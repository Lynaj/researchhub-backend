# Generated by Django 2.2.6 on 2019-10-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hub',
            name='is_locked',
            field=models.BooleanField(default=True),
        ),
    ]