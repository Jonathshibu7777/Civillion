# Generated by Django 5.0.2 on 2024-02-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMTsApp', '0005_tbl_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
