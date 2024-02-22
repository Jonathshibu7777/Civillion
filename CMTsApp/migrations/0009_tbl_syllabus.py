# Generated by Django 5.0.2 on 2024-02-21 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMTsApp', '0008_rename_course_duretion_tbl_course_course_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMTsApp.tbl_course')),
                ('Department_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMTsApp.tbl_department')),
                ('Semester_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMTsApp.tbl_semester')),
            ],
        ),
    ]