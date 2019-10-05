# Generated by Django 2.2.5 on 2019-10-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REprop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='id',
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='prop_number',
            field=models.IntegerField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
