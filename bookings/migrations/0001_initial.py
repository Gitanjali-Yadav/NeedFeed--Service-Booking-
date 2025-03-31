# Generated by Django 5.1.7 on 2025-03-20 09:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField()),
                ('address', models.TextField()),
                ('special_instructions', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('O', 'Ongoing'), ('D', 'Completed'), ('X', 'Cancelled')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('S', 'Success'), ('F', 'Failed'), ('P', 'Pending')], max_length=20)),
                ('payment_method', models.CharField(max_length=50)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
            ],
        ),
    ]
