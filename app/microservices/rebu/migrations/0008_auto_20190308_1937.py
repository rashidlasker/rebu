# Generated by Django 2.1 on 2019-03-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0007_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='user_id',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]