'''
질문에 대한 답변을 미리 저장해 놓고 있는 테이블이 있음 (Answer)
만약 동일한 질문이 들어왔을 경우에 바로 답변을 하고
기존에 없던 질문이라 판단되면 Broker 서버로 부터 응답받은 답변을 반환
'''
import json

from django.core import serializers
from django.http import JsonResponse
from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Answer


# # to-be 버전
# def Chatbot(request):
#     data = json.loads(request.body)
#     q = '12345678'  # encoding_question(data['content']) -- 질문에 대한 해쉬값을 우선 전달 받음
#
#     is_answer = Answer.objects.filter(question_val=q).exists()
#     '''만약 이미 해당 질문에 대한 답이 있는 경우 그것을 제공'''
#     if is_answer:
#         old_a = Answer.objects.filter(question_val=q)
#         return JsonResponse(serializers.serialize('json', old_a), safe=False)
#
#     '''없던 질문이라면 새로이 등록'''
#     _, a, chatIdx, reliability = q, '머니버스를 이용하세요', 2, 0.7  # get_answer(data)  -- ... 챗봇 서버로 부터 응답을 받음
#     new_a = Answer.objects.create(question_val=q,
#                                   chatbot_id=chatIdx,
#                                   content=a,
#                                   reliability=reliability)
#
#     return JsonResponse(serializers.serialize('json', [new_a]), safe=False)


# simple 버전
CHAT_MAPPING={'22':['cBWAkfuKLnRsumcU6Z4j', 'MOLI'], '33':['FMBsMyWGx4LpTtX619Pi', 'ORORA'], '44':['DVkuJGchRdn8hxiuWbon','NEXT']}
def Chatbot(request):
    print(request.body.decode('utf-8'),'!!! 질문 내용')


    ans = get_answer(request.body.decode('utf-8'))

    # ans={
    #     'answer':'머니버스를 이용하세요',
    #     'chatbot_id':'22',
    #     'reliability':0.7
    # }
    print(ans,'!@#!@#@#')
    ret=dict({})
    ret['answer']=ans['answer']
    ret['chatbot_id']=CHAT_MAPPING[ans['chatbot_id']][0]
    ret['chatbot_name']=CHAT_MAPPING[ans['chatbot_id']][1]
    ret['reliability']=ans['accuracy']
    print(ret,'!!!!!')
    return JsonResponse(ret, safe=False)
