from django.db import models
from django.db.models.deletion import CASCADE


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()



class Question(models.Model):
    ANSWER_TYPES = (
        ('text', 'text input'),
        ('select', 'choose one'),
        ('select-multiple', 'choose any')
    )
    type = models.CharField(max_length=200, choices=ANSWER_TYPES, default='text')
    text = models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
    choices = models.TextField(blank=True, null=True)

    
