# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 01:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EducationalYear', '0001_initial'),
        ('Department', '0001_initial'),
        ('Course', '0001_initial'),
        ('Home', '0001_initial'),
        ('AcademicYear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('secondary_email', models.EmailField(max_length=100)),
                ('status', models.CharField(choices=[('fr', 'Fresh'), ('gr', 'Graduated'), ('ot', 'Other')], default='fr', max_length=2)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='AcademicYear.AcademicYear')),
                ('courses', models.ManyToManyField(related_name='students', to='Course.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Department.Department')),
                ('educational_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='EducationalYear.EducationalYear')),
            ],
        ),
    ]
