# Generated by Django 4.1.4 on 2022-12-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_alter_product_image_alter_product_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Book',
        ),
    ]
