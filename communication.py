import socket


def build_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(15)
    sock.connect(("54.187.16.171", 1336))
    return sock


def send_and_receive(sock, request):
    sock.sendall(request.encode())
    return sock.recv(2048).decode()
