
import json
import os
import socket
import pickle
import sys
#import aiml
import base64
import socket

HOST = '3.37.67.26'
PORT = 9001


while True:
    data = dict()
    user_input = input()
    data["question"] = user_input
    requestMsg = "/message?/" + json.dumps(data,ensure_ascii=False) + "\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(requestMsg.encode('utf-8'))
        received = str(s.recv(1024), "utf-8")

        answer = json.loads(received.replace('\r\n', ''))
        print(answer)
        s.close()

