from django.db import models
import datetime


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=600)
    date = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.name


def filter_by_date(date):
   return Buyer\
          .objects\
          .filter(post_date__year=date.year,
                  post_date__month=date.month,
                  post_date__day=date.day)