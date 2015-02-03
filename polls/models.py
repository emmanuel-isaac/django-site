import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return 'Question: {}\nPublication Date: {}'.format(self.question_text, self.pub_date)

class Choice(models.Model):
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  def __str__(self):
    return self.choice_text
  votes = models.IntegerField(default=0)