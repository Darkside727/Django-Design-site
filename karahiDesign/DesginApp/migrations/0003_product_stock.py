# Generated by Django 3.0.7 on 2020-10-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DesginApp', '0002_category_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DesginApp.Stock'),
        ),
    ]
