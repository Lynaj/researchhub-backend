# Generated by Django 2.2.5 on 2019-10-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='previous',
            field=models.ManyToManyField(blank=True, default=None, related_name='_summary_previous_+', to='summary.Summary'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='current',
            field=models.BooleanField(default=True),
        ),
    ]