'''
질문에 대한 답변을 미리 저장해 놓고 있는 테이블이 있음 (Answer)
만약 동일한 질문이 들어왔을 경우에 바로 답변을 하고
기존에 없던 질문이라 판단되면 Broker 서버로 부터 응답받은 답변을 반환
'''
import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Answer


# to-be 버전
CHAT_MAPPING={'22':['cBWAkfuKLnRsumcU6Z4j', 'MOLI'], '33':['FMBsMyWGx4LpTtX619Pi', 'ORORA'], '44':['DVkuJGchRdn8hxiuWbon','NEXT']}
def Chatbot(request):
    question_dict=request.body.decode('utf-8')
    question=json.loads(question_dict)['question']
    q_idx = encoding_question(question_dict['question']) ## 만들어야 함
    #q_idx = '123456711'  # 삭제 예정


    old_ans = Answer.objects.filter(q_idx=q_idx)
    ret = dict({})

    '''만약 이미 해당 질문에 대한 답이 있는 경우 그것을 제공, 단 정확도가 70% 이상이어야 함'''
    if old_ans.exists() and float(old_ans[0].accuracy)>=0.7:
        print('캐시테이블서 반환')
        return JsonResponse(old_ans[0].get_json_format(), safe=False)


    ans = get_answer(question_dict)
    # ans={
    #     'answer':'머니버스를 이용하세요',
    #     'chatbot_id':'22',
    #     'accuracy':'0.7'
    # } #삭제 예정


    ret['answer']=ans['answer']
    ret['chatbot_id']=CHAT_MAPPING[ans['chatbot_id']][0]
    ret['chatbot_name']=CHAT_MAPPING[ans['chatbot_id']][1]
    ret['reliability']=ans['accuracy']

    Answer.objects.create(q_idx=q_idx,
                          question=question,
                          answer=ret['answer'],
                          chatbot_id=ret['chatbot_id'],
                          chatbot_name=ret['chatbot_name'],
                          accuracy=ret['reliability'])

    return JsonResponse(ret, safe=False)


def reflectReaction(request):
    body_dict=json.loads(request.body.decode('utf-8')) # 필드값 question, reaction (front로 부터 받기)
    question=body_dict['question']
    reaction=body_dict['reaction']

    q_idx = encoding_question(question) ### 만들어야 함
    q_obj = Answer.objects.get(q_idx=q_idx)

    gj = 1 - float(q_obj.accuracy)
    if reaction == 'Good':

        q_obj.accuracy=str(float(q_obj.accuracy)+gj*0.1)
    elif reaction == 'Bad':
        q_obj.accuracy=str(float(q_obj.accuracy)-gj*0.1)

    q_obj.save()
    print(q_obj.accuracy,'@@@@')
    return HttpResponse('success')




# # simple 버전
# CHAT_MAPPING={'22':['cBWAkfuKLnRsumcU6Z4j', 'MOLI'], '33':['FMBsMyWGx4LpTtX619Pi', 'ORORA'], '44':['DVkuJGchRdn8hxiuWbon','NEXT']}
# def Chatbot(request):
#     print(request.body.decode('utf-8'),'!!! 질문 내용')
#
#
#     # ans = get_answer(request.body.decode('utf-8'))
#
#     ans={
#         'answer':'머니버스를 이용하세요',
#         'chatbot_id':'22',
#         'accuracy':'0.7'
#     }
#
#     ret=dict({})
#     ret['answer']=ans['answer']
#     ret['chatbot_id']=CHAT_MAPPING[ans['chatbot_id']][0]
#     ret['chatbot_name']=CHAT_MAPPING[ans['chatbot_id']][1]
#     ret['reliability']=ans['accuracy']
#
#     return JsonResponse(ret, safe=False)
