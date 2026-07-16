import socket

host=input("Enter IP: ")

for port in range(1,101):
    s=socket.socket()
    s.settimeout(0.5)

    if s.connect_ex((host,port))==0:
        print("Open Port:",port)

    s.close()
