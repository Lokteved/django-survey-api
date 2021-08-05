from django.db import models
from django.db.models.deletion import CASCADE


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField()


class Question(models.Model):
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)


class Choice(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    
