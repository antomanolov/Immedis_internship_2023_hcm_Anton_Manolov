# Generated by Django 4.2.6 on 2023-11-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_alter_customusermodel_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='first_name',
            field=models.CharField(max_length=51, null=True),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='last_name',
            field=models.CharField(max_length=51, null=True),
        ),
    ]
