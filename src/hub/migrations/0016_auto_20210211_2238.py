# Generated by Django 2.2 on 2021-02-11 22:38

from django.db import migrations


def create_through_relations(apps, schema_editor):
    Hub = apps.get_model('hub', 'Hub')
    HubMembership = apps.get_model('hub', 'HubMembership')
    for hub in Hub.objects.all():
        for subscriber in hub.subscribers.all():
            HubMembership(
                user=subscriber,
                hub=hub
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0015_hubmembership'),
    ]

    operations = [
        migrations.RunPython(create_through_relations, reverse_code=migrations.RunPython.noop)
    ]
