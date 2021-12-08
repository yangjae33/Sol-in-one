from socket import *
import json

BROKER_IP='3.37.67.26'
BROKER_PORT=9001


def encoding_question(q_str):
    con=socket.create_connection((BROKER_IP,BROKER_PORT)) # 실제로는 model서버 ip/port값으로 넣기
    con.send(q_str.encode())
    ret=con.recv(1024)
    return int(ret)


# def get_answer(data):
#     print(data)
#     con=socket.create_connection((ip,port)) # 실제로는 model서버 ip/port값으로 넣기
#     print(con)
#     con.send(data.encode())
#     print(data.encode(),'!!!')
#     ret=con.recv(1024)
#     print(ret)
#     return ret.split('|')


''' data['question'] = '금리가 가장 저렴함 상품이 뭐야?' '''
def get_answer(requestMsg):
    data = "/message?/" + requestMsg.replace('\n','') + '\n'
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((BROKER_IP, BROKER_PORT))
    clientSock.sendall(data.encode('utf-8'))
    ret=str(clientSock.recv(1024), 'utf-8')

    return json.loads(ret)



# ip='localhost'
# port=8090
#
# server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 객체 생성
# server.bind((ip, port))
#
# server.listen(20)
#
# def server(client):
#     data = client.recv(1024) # client로 부터 1024바트만큼 데이터를 받아 옴
#     print(data)
#     client.send(data) # 클라이언트에게 데이터 값을 돌려 줌
#
# while True:
#     client, addr = server.accept() #서버소켓에 클라이언트가 연결되면 클라이언트 소켓, 주소를 반환
#     server(client) #핸들러 함수에 처리를 넘김



