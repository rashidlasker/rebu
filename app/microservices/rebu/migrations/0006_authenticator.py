# Generated by Django 2.1 on 2019-03-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0005_meal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='authenticator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('authenticator', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]