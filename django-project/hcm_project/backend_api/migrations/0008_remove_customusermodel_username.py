# Generated by Django 4.2.6 on 2023-11-01 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_alter_customusermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusermodel',
            name='username',
        ),
    ]
