from django.db import models

# Create your models here.
class Question(models.Model):
    content=models.TextField()

class Answer(models.Model):
    question_val=models.IntegerField()
    chatbot_id=models.IntegerField()
    content=models.TextField()
    reliability=models.FloatField()