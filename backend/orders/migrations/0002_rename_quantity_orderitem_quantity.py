# Generated by Django 4.2 on 2023-05-02 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]