#! /usr/bin/python

import sys
import subprocess
import socket

port = 1234
host = "00.00.00.00"

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind((host, port))
soc.listen(10)
conn, addr = soc.accept()
Rip, Rport = addr
Lip, Lport = conn.getsockname()
print(" Server Connected to :: {}".format(Rip))
conn.send("this is connected sucessfully\n".encode())
conn.send(f"{Lip} :: ".encode())


while 1:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode().strip()

    if data == "quit":
        print(f"{Rip} :: bye bye....")
        conn.send(f"{Lip} :: bye bye.... ".encode())
        conn.close()
        conn, addr = soc.accept()
        print(" Server Connected to :: {}".format(Rip))
        conn.send("this is connected sucessfully\n".encode())
        Rip, Rport = addr
        Lip, Lport = conn.getsockname()
        conn.send(f"{Lip} :: ".encode())

    elif data == "close":
        conn.send(f"{Rip} :: Server is closing  :: bye bye guy :: ＞﹏＜".encode())
        conn.close()
        soc.close()
        print("Server is closing  :: bye bye guy :: ＞﹏＜")
        break
    else:
        print(f"{Rip} :: {data}")
        conn.send(f"{Lip} :: ".encode())
