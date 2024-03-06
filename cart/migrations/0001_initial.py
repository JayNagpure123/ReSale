# Generated by Django 4.1.7 on 2024-03-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_amount', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('packed', 'packed'), ('shipped', 'shipped'), ('on the way', 'on the way'), ('delivered', 'delivered')], default='pending', max_length=50)),
                ('customer_mobile', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField(default=0.0)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]