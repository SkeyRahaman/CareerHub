from django.db import models


# Create your models here.
class Subscribe(models.Model):
    NEWSLETTER_OPTIONS = [
        ('W','Weekly'),
        ('M','Monthly'),  #Database, UI
        ('D', 'Daily')
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=2, choices=NEWSLETTER_OPTIONS, default='M')
    email = models.CharField(max_length=100)
