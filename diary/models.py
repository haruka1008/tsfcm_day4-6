from django.db import models
from django.utils import timezone

app_name = 'diary'

class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.title
