# Generated by Django 4.1.5 on 2023-01-12 06:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mini_text',
            field=ckeditor.fields.RichTextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]