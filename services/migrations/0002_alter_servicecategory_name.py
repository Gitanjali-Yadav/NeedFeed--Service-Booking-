# Generated by Django 5.1.7 on 2025-03-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecategory',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
