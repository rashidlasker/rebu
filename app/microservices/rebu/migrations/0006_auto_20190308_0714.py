# Generated by Django 2.1 on 2019-03-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0005_meal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='authenticator',
            fields=[
                ('user_id', models.CharField(max_length=30)),
                ('authenticator', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=100),
            preserve_default=False,
        ),
    ]
