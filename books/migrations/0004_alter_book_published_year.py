# Generated by Django 5.1.3 on 2024-11-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_publication_year_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(),
        ),
    ]
