# Generated by Django 2.2.6 on 2019-10-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reputation',
            field=models.IntegerField(default=1),
        ),
    ]