from django.db import models
from datetime import datetime
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
class Task(models.Model):
    GRUZ_CHOICES = [
        ('corn', 'Кукурудза'),
        ('wheat', 'Пшениця'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line to link Task to User
    misto = models.CharField('Name' , max_length=50) # field to 255chars  place = models.CharField('Place' , max_length=50)
    gruz = models.CharField('Description',max_length=10, choices=GRUZ_CHOICES)
    litres=models.CharField('Litres', max_length=5)
    price = models.CharField('Price', max_length=25)
    massa=models.CharField('Massa', max_length=50)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.misto
    class Meta:
        verbose_name = ('Ваши данные')

