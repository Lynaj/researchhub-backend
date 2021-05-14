# Generated by Django 2.2 on 2020-10-27 21:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_auto_20200319_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='extra',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='notification',
            name='paper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='paper.Paper'),
        ),
    ]
