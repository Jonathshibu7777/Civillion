# Generated by Django 5.0.2 on 2024-02-21 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMTsApp', '0003_tbl_productcompany_tbl_shop_tbl_product_tbl_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='tbl_product',
            name='Company_Name',
        ),
        migrations.RemoveField(
            model_name='tbl_stock',
            name='pro_id',
        ),
        migrations.DeleteModel(
            name='tbl_Shop',
        ),
        migrations.DeleteModel(
            name='tbl_ProductCompany',
        ),
        migrations.DeleteModel(
            name='tbl_Product',
        ),
        migrations.DeleteModel(
            name='tbl_stock',
        ),
    ]
