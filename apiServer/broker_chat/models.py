from django.db import models

# Create your models here.
class Question(models.Model):
    content=models.TextField()

class Answer(models.Model):
    q_idx=models.IntegerField(default=-1)
    question=models.TextField(default='')
    answer=models.TextField(default='')
    chatbot_id=models.TextField(default='')
    chatbot_name=models.TextField(default='')
    accuracy=models.TextField(default='')

    #     ret['answer']=ans['answer']
    #     ret['chatbot_id']=CHAT_MAPPING[ans['chatbot_id']][0]
    #     ret['chatbot_name']=CHAT_MAPPING[ans['chatbot_id']][1]
    #     ret['reliability']=ans['accuracy']

    def get_json_format(self):
        ret={}
        ret['q_idx']=self.q_idx
        ret['question']=self.question
        ret['answer']=self.answer
        ret['chatbot_id']=self.chatbot_id
        ret['chatbot_name']=self.chatbot_name
        ret['accuracy']=self.accuracy
        return ret