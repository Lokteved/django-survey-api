from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models import Max


class Respondent(models.Model):
    slug = models.SlugField(max_length=10, unique=True, blank=True)

    def save(self, **kwargs):
        if not self.slug:
            max = Respondent.objects.aggregate(id_max=Max('id'))['id_max']
            self.slug = "{}{:05d}".format('id', max if max is not None else 1)
        super().save(*kwargs)



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
    
    def __str__(self):
        return self.text

    
class Response(models.Model):
    user_id = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    body = models.TextField()