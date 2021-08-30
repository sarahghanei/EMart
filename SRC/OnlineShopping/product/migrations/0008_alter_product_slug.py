# Generated by Django 3.2.5 on 2021-08-23 08:07

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(allow_unicode=True, blank=True, editable=False,
                                                            populate_from=['name'], unique=True),
        ),
    ]
