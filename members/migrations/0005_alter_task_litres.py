# Generated by Django 5.0.7 on 2024-08-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_task_punkt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='litres',
            field=models.CharField(max_length=20, verbose_name='Litres'),
        ),
    ]
