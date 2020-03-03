# Generated by Django 2.2.10 on 2020-02-27 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0011_auto_20200221_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailrecipient',
            name='is_subscribed',
        ),
        migrations.AddField(
            model_name='commentsubscription',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentsubscription',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='digestsubscription',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='digestsubscription',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='papersubscription',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='papersubscription',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='replysubscription',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='replysubscription',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='threadsubscription',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='threadsubscription',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='commentsubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('THREE_HOUR', 180), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
        migrations.AlterField(
            model_name='digestsubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('THREE_HOUR', 180), ('DAILY', 1440), ('WEEKLY', 10080)], default=1440),
        ),
        migrations.AlterField(
            model_name='papersubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('THREE_HOUR', 180), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
        migrations.AlterField(
            model_name='replysubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('THREE_HOUR', 180), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
        migrations.AlterField(
            model_name='threadsubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('THREE_HOUR', 180), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
    ]