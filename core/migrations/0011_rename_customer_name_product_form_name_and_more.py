# Generated by Django 4.2.8 on 2023-12-24 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_contact_time_alter_product_form_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_form',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product_form',
            old_name='product_name',
            new_name='product',
        ),
    ]
