# Generated by Django 2.2.7 on 2019-11-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0013_auto_20191030_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='plain_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='reply',
            name='plain_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='thread',
            name='plain_text',
            field=models.TextField(blank=True, default=''),
        ),
    ]