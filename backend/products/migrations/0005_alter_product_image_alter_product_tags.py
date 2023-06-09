# Generated by Django 4.2 on 2023-05-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/default/default.png', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='products.tag'),
        ),
    ]
