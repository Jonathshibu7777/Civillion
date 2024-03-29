# Generated by Django 5.0.2 on 2024-02-26 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMTsApp', '0009_tbl_syllabus'),
        ('Guest', '0002_tbl_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50)),
                ('test_period', models.CharField(max_length=50)),
                ('test_description', models.CharField(max_length=50)),
                ('test_amount', models.CharField(max_length=50)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMTsApp.tbl_place')),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMTsApp.tbl_subcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='tbl_categories',
        ),
    ]
