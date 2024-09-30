import socket

server_ip = "127.0.0.1"
server_port = 8080
listen_num = 5
buffer_size = 1024

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server.bind((server_ip, server_port))

tcp_server.listen(listen_num)

while True:
    client, address = tcp_server.accept()
    print("Connection from", address)

    data = client.recv(buffer_size)
    print("Received:", data)

    client.send(data)

    client.close()