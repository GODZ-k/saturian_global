# Generated by Django 4.2.8 on 2024-01-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_form',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]