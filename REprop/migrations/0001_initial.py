# Generated by Django 2.2.5 on 2019-09-14 21:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.CharField(max_length=50)),
                ('maxPrice', models.IntegerField()),
                ('minPrice', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_number', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Condo', 'Condo'), ('House', 'House'), ('Apartment', 'Apartment')], default='Condo', max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('squarefeet', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('bed', models.CharField(max_length=50)),
                ('bath', models.CharField(max_length=50)),
                ('build', models.CharField(max_length=50)),
                ('purpose', models.CharField(choices=[('For Sale', 'For Sale'), ('For Lease', 'For Lease')], default='For Sale', max_length=10)),
                ('status', models.BooleanField(default='True')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='REprop.Customer')),
            ],
        ),
    ]
