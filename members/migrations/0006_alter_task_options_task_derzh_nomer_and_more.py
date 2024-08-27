# Generated by Django 5.0.7 on 2024-08-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_task_litres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Ваши данные', 'verbose_name_plural': 'Ваши данные'},
        ),
        migrations.AddField(
            model_name='task',
            name='derzh_nomer',
            field=models.CharField(default=1, max_length=50, verbose_name='derzh_nomer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='odometr_viezd',
            field=models.CharField(default='', max_length=50, verbose_name='odometr_viezd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='odometr_viyizd',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Покази одометра при виїзді'),
        ),
        migrations.AddField(
            model_name='task',
            name='odometr_vizd',
            field=models.CharField(default='', max_length=50, verbose_name='odometr_vizd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='odometr_zayizd',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Покази одометра при заїзді'),
        ),
        migrations.AddField(
            model_name='task',
            name='prymitky',
            field=models.TextField(blank=True, null=True, verbose_name='Примітки'),
        ),
        migrations.AddField(
            model_name='task',
            name='rozvantazhennya_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время розвантаження'),
        ),
        migrations.AddField(
            model_name='task',
            name='rozvantazhennya_mistse',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Місце розвантаження'),
        ),
        migrations.AddField(
            model_name='task',
            name='skilki_vantazhu',
            field=models.CharField(default='', max_length=50, verbose_name='skilki_vantazhu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='ttn_nomer',
            field=models.CharField(default='', max_length=50, verbose_name='ttn_nomer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='zapravka_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Заправка дата час'),
        ),
        migrations.AddField(
            model_name='task',
            name='zaprawka_time',
            field=models.CharField(default='', max_length=50, verbose_name='zaprawka_time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='zavantazhennya_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время завантаженя'),
        ),
    ]