# Generated by Django 2.2.6 on 2019-10-04 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_auto_20191004_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='tagline',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]