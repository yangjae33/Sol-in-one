# -*- encoding: utf-8 -*-

import base64
import os
import threading
import json
import random
import socket
import pickle
import threading
import sys
import Word2Vec
import aiml

# -*- coding: utf-8 -*- 
from time import time


W2V = Word2Vec.Word2Vec()

def predict_category(s, train, model):
    pred = model.predict([s])
    return pred[0]

#train data from chatbots
def training():
    # aiml dont have to train
    print("Running...")
    return 'Training is finished'

#register chatbot
def registerChatbot(chatbots, data):
    chatbots.lock.acquire()
    key = data["key"]
    del data["key"]
    chatbots[key] = ChatbotInfo(data)
    chatbots.lock.release()
    print({"contents" : "chatbot registered"})
    return {"contents" : "chatbot registered"}


#deregister chatbot
def deregisterChatbot(chatbots, data):
    chatbots.lock.acquire()
    key = data["key"]
    if key in chatbots.keys():
        del chatbots[key]
    chatbots.lock.release()
    print({"contents" : "chatbot deregistered"})
    return {"contents" : "chatbot deregistered"}

#dispatch message
def dispatchMessage(chatbots, data):

    kern = aiml.Kernel()

    kern.verbose(False)
    brainLoaded = False
    forceReload = False
    while not brainLoaded:
        if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
            kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
            brainLoaded = True
            kern.saveBrain("standard.brn")
        else:
            try:
                kern.bootstrap(brainFile = "standard.brn")
                brainLoaded = True
            except:
                forceReload = True

    # Enter the main input/output loop.
    # print("\nINTERACTIVE MODE (ctrl-c to exit)")

    response = dict()
    print(data['question'])
    data['question']
    response["message"] = kern.respond(data["contents"].replace(" ","")).strip()
    response["chatbot_id"] = 2;
    response["accuracy"] = 0.77
    print(response)
    return response

#get information of registered chatbot
def getChatbotInfo(chatbots, data):
    #video name for which chatbot is purposed
    video_name = data["contents"]["video_name"]

    #name of chatbot which is beeing added
    chatbot_name = data["contents"]["chatbot_name"]

    #number of chatbot class; used for predicting chatbot
    class_number = 1

    #training data file
    file = video_name + "_train_data.txt"

    #if training data exists
    if os.path.isfile("data_in/"+file):
        #open training data file
        train_file = open("data_in/" + file, 'r')

        #find first line of file
        first_line = train_file.readlines(1)

        #if file is empty
        if not first_line:
            #open file for writing new data
            train_file = open("data_in/" + file, 'w')

            #write train data of chatbot line by line with class number
            for item in data["contents"]["chatbot_info"]["train_data"]:
                train_file.writelines(item.replace('\n','') + "\t" + str(class_number) + "\n")
                chatbot_status = str(class_number)

        #if file has data
        else:
            #read last line
            last_line = train_file.readlines()[-1]

            #split line by '\t' to find last chatbot's class number
            split_line = last_line.split('\t')
            class_num = split_line[-1].replace('\n','')

            #count new chatbot's class
            class_number = int(class_num) + 1
            chatbot_status = str(class_number)

            #open training data file for apending new data line by line with class number
            train_file = open("data_in/"+file, 'a')
            for item in data["contents"]["chatbot_info"]["train_data"]:
                train_file.writelines(item.replace('\n','') + "\t" + str(class_number) + "\n")

    #if training data file does not exist
    else:
        #open training data file for writing new data line by line with class number
        train_file = open("data_in/"+file, 'w')
        for item in data["contents"]["chatbot_info"]["train_data"]:
            train_file.writelines(item.replace('\n','') + "\t" + str(class_number) + "\n")
            chatbot_status = str(class_number)
            print("chatbot class: ", chatbot_status)

    #json for new registered chatbot information
    chatbot_class = {chatbot_status: data["contents"]["chatbot_info"]}
    chatbot_class[chatbot_status]["chatbot_name"] = chatbot_name

    #read file of chatbot information file
    with open('data_in/chatbot_info_file.json', 'r', encoding='utf8') as f:
        old_info = json.load(f)

    #if current video is in chatbot information file, append new data
    if video_name in old_info:
        old_info[video_name].update(chatbot_class)

    #if current video is not in chatbot information file, add new data
    else:
        old_info[video_name] = chatbot_class

    #open chatbot information file for writing, write chatbot inforamtion
    with open('data_in/chatbot_info_file.json', 'w') as output:
        json.dump(old_info, output)

    #trained model file
    trained_model = 'data_out/'+video_name+'_model.pkl'

    #print if trained model is saved or not
    if os.path.isfile(trained_model):
        pass
    else:
        print("Training is required!")


#send reques to predicted chatbot
def sendRequest(method, data, address, PORT):
    requestMsg = method + json.dumps(data) + "\n"
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((address, PORT))
            s.sendall(requestMsg.encode("utf-8"))
            received = str(s.recv(1024), "utf-8")
    except socket.error as e:
        print("챗봇이 존재하지 않거나 꺼져있다")
        received = -1
    return received


class ServerThread(threading.Thread):
    def __init__(self, server):
        super(ServerThread, self).__init__()
        self.server = server

    def run(self):
        self.server.serve_forever()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


class ChatbotInfo():
    def __init__(self, attrs):
        self.ts = time()
        self.address = tuple(attrs["addr"])
        self.attrs = attrs


    def __str__(self):
        return "{0}, {1}".format(self.ts, self.attrs)


class ChatbotDict(dict):
    def __init__(self):
        self.lock = threading.Lock()
