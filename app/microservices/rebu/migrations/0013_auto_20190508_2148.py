# Generated by Django 2.1 on 2019-05-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0012_recommendations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recommendations',
            new_name='recommendation',
        ),
    ]
