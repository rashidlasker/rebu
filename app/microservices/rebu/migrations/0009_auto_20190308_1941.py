# Generated by Django 2.1 on 2019-03-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0008_auto_20190308_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
