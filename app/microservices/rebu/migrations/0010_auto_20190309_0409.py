# Generated by Django 2.1 on 2019-03-09 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rebu', '0009_auto_20190308_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='cook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rebu.user'),
        ),
    ]