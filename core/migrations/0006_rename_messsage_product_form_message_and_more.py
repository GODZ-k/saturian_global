# Generated by Django 4.2.8 on 2023-12-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_contact_messsage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_form',
            old_name='messsage',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='messsage',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
