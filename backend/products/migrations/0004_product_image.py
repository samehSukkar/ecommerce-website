# Generated by Django 4.2 on 2023-05-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_tag_product_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='\\photos\\Screenshot 2023-05-03 142259.png', upload_to=''),
        ),
    ]
