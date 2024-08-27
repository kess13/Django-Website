from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    GRUZ_CHOICES = [
        ('corn', 'Кукурудза'),
        ('wheat', 'Пшениця'),
    ]

    # Existing fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line to link Task to User
    misto = models.CharField('Name', max_length=50,null=True, blank=True)  # Field to 255 chars
    gruz = models.CharField('Description', max_length=10, choices=GRUZ_CHOICES)
    litres = models.CharField('Litres', max_length=20,null=True, blank=True)
    price = models.CharField('Price', max_length=25,null=True, blank=True)
    massa = models.CharField('Massa', max_length=50,null=True, blank=True)
    punkt = models.CharField('Punkt', max_length=50,null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    derzh_nomer = models.CharField('derzh_nomer', max_length=50,null=True, blank=True)
    ttn_nomer = models.CharField('ttn_nomer', max_length=50,null=True, blank=True)
    skilki_vantazhu = models.CharField('skilki_vantazhu', max_length=50,null=True, blank=True)
    odometr_vizd = models.CharField('odometr_vizd', max_length=50,null=True, blank=True)
    odometr_viezd = models.CharField('odometr_viezd', max_length=50,null=True, blank=True)
    zaprawka_time = models.CharField('zaprawka_time', max_length=50,null=True, blank=True)
    zavantazhennya_datetime = models.DateTimeField('Дата и время завантаженя', null=True, blank=True)
    rozvantazhennya_datetime = models.DateTimeField('Дата и время розвантаження', null=True, blank=True)
    rozvantazhennya_mistse = models.CharField('Місце розвантаження', max_length=255, null=True, blank=True)
    odometr_viyizd = models.CharField('Покази одометра при виїзді', max_length=50, null=True, blank=True)
    odometr_zayizd = models.CharField('Покази одометра при заїзді', max_length=50, null=True, blank=True)
    zapravka_datetime = models.DateTimeField('Заправка дата час', null=True, blank=True)
    prymitky = models.TextField('Примітки', null=True, blank=True)

    def __str__(self):
        return self.misto

    class Meta:
        verbose_name = ('Ваши данные')
        verbose_name_plural = ('Ваши данные')
