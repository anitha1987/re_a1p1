# Generated by Django 2.2.5 on 2019-10-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REprop', '0003_auto_20191005_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='prop_number',
            field=models.IntegerField(max_length=50),
        ),
    ]