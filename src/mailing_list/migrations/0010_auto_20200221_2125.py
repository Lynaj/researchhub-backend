# Generated by Django 2.2.10 on 2020-02-21 21:25

from django.db import migrations
import django.db.models.deletion
import mailing_list.models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0009_auto_20200221_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsubscription',
            name='email_recipient',
        ),
        migrations.RemoveField(
            model_name='digestsubscription',
            name='email_recipient',
        ),
        migrations.RemoveField(
            model_name='papersubscription',
            name='email_recipient',
        ),
        migrations.RemoveField(
            model_name='replysubscription',
            name='email_recipient',
        ),
        migrations.RemoveField(
            model_name='threadsubscription',
            name='email_recipient',
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='comment_subscription',
            field=mailing_list.models.SubscriptionField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_recipient', to='mailing_list.CommentSubscription'),
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='digest_subscription',
            field=mailing_list.models.SubscriptionField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_recipient', to='mailing_list.DigestSubscription'),
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='paper_subscription',
            field=mailing_list.models.SubscriptionField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_recipient', to='mailing_list.PaperSubscription'),
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='reply_subscription',
            field=mailing_list.models.SubscriptionField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_recipient', to='mailing_list.ReplySubscription'),
        ),
        migrations.AddField(
            model_name='emailrecipient',
            name='thread_subscription',
            field=mailing_list.models.SubscriptionField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_recipient', to='mailing_list.ThreadSubscription'),
        ),
    ]
