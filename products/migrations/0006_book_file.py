# Generated by Django 4.1.4 on 2022-12-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_author_delete_booksearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='books'),
        ),
    ]
