# Generated by Django 2.1 on 2019-04-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0010_auto_20190309_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='authenticator',
            name='user_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
