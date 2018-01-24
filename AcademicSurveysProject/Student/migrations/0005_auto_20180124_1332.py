# Generated by Django 2.0.1 on 2018-01-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_auto_20180122_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='primary_email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.CharField(max_length=30, unique=True, verbose_name='ID number'),
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
    ]