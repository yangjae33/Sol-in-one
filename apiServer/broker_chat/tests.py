import json
import os
import socket
import pickle
import sys
#import aiml
import base64
import socket

HOST = '3.37.67.26'
PORT = 9000

data = dict()
data["contents"] = 'question'

requestMsg = "/message?/" + json.dumps(data) + "\n"
print(requestMsg)
requestMsg = '/message?/{"contents": "question"}\n'
print(requestMsg)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(requestMsg.encode('utf-8'))
received = str(s.recv(1024), "utf-8")

answer = json.loads(received.replace('\r\n', ''))
print(answer)


print(answer)