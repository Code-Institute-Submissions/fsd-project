# Generated by Django 3.0.7 on 2020-07-20 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=80)),
                ('address2', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=80)),
                ('county', models.CharField(max_length=40)),
                ('eircode', models.CharField(blank=True, max_length=20, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(editable=False, max_length=50, verbose_name='Product name')),
                ('price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6)),
                ('quantity', models.IntegerField(default=0, editable=False)),
                ('order_reference', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
            ],
        ),
    ]
