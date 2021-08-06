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
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, related_name='questions')
    choices = models.TextField(blank=True, null=True)

    def get_clean_choices(self):
        """ Return split and stripped list of choices with no null values. """
        if self.choices is None:
            return []
        choices_list = []
        for choice in self.choices.split(','):
            choice = choice.strip()
            if choice:
                choices_list.append(choice)
        return choices_list
    
    def __str__(self):
        return self.text

    
class Response(models.Model):
    session_id = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    body = models.TextField()