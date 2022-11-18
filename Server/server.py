# === TCP Server ===
# 导入Socket库
from socket import *

IP = ''         # 主机地址为空，表示绑定本机所有网络接口IP地址
PORT = 50000    # 服务端口号
BUFLEN = 512    # Socket缓冲区大小

# 实例化Socket对象
listenSocket = socket(AF_INET, SOCK_STREAM) # AF_INET表示网络层使用IP协议，SOCK_STREAM表示传输层使用TCP协议
listenSocket.bind((IP, PORT))               # 绑定IP和端口

# 使Socket进入监听状态，最多接受8个等待连接的Client
listenSocket.listen(8)
print(f'Server listening at port {PORT}')

dataSocket, addr = listenSocket.accept()
print('Client connected:', addr)

while True:
    recv_msg = dataSocket.recv(BUFLEN)  # 读取Client发送的消息
    if not recv_msg:                    # 如果消息为空表示连接已关闭，退出循环    
        break

    msg = recv_msg.decode()             # 将收到的消息解码为字符串
    print(f'Message received: {msg}')

    # 编码，向Client发送消息
    dataSocket.send(f'Server message received: {msg}'.encode())

# 调用close()关闭Socket
dataSocket.close()
listenSocket.close()