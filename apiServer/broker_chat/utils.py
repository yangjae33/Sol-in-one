from socket import *

ip='3.37.67.26'
port=9000

def encoding_question(q_str):
    con=socket.create_connection((ip,port)) # 실제로는 model서버 ip/port값으로 넣기
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


def get_answer(data):
    print(data)
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((ip, port))
    print(clientSock)
    clientSock.send(data.encode('utf-8'))
    print(data.encode('utf-8'),'!!!')
    ret=clientSock.recv(1024)
    print(ret)
    return ret.split('|')


#print(get_answer("/message/?{\'data\':\'질문\'}"))


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



