# Generated by Django 4.2.8 on 2023-12-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_messsage_product_form_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
    ]
