from django.db import models
import datetime


class Publication(models.Model):
    """Publication data"""

    title = models.CharField('header', max_length=100)
    description = models.TextField('text')
    author = models.CharField('author', max_length=100)
    date = models.DateField('date', default=datetime.date.today())

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
