# Generated by Django 4.2 on 2023-05-03 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_quantity_orderitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='dateTime',
            new_name='date',
        ),
    ]