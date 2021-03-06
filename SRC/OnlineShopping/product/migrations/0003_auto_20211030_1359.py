# Generated by Django 3.2.5 on 2021-10-30 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_is_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_sub',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='product.category'),
        ),
    ]
