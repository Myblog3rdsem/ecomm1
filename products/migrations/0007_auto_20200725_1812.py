# Generated by Django 3.0.7 on 2020-07-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200607_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(null=True, upload_to='images/dynamic/products/brands'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='images/dynamic/products/categories'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='images/dynamic/products/subcategories'),
        ),
    ]