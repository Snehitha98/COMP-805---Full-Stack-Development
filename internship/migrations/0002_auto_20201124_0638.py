# Generated by Django 3.1.3 on 2020-11-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipassignment',
            name='semester',
            field=models.CharField(blank=True, max_length=30, verbose_name='Semester'),
        ),
    ]
