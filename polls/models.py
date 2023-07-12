from datetime import timedelta

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return f'{self.id} - {self.question_text}'

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Choice #{self.id}'
