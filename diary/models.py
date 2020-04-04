from django.db import models
from django.utils import timezone
# Create your models here.

class Day(models.Model):
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')
    date = models.DateField('日付', default=timezone.now)
