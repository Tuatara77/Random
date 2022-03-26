import socket
import threading

HOST = ""  # who can connect to the server (blank means all)
PORT = 12345
BUFFERSIZE = 1024
QUEUESIZE = 5

STOPMESSAGE = "#64STOPorAng3"
SEPARATOR = "|"

running = True

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen(QUEUESIZE)

connectionlist = []

def listener():
    global running
    while running:
        while len(connectionlist) <= 3:
            clientsocket, clientaddress = soc.accept()
            if clientsocket:
                print(f"Connected to {clientaddress}")
                connectionlist.append(clientsocket)
                if len(connectionlist) == 1: receiver1.start()
                if len(connectionlist) == 2: receiver2.start()
                if len(connectionlist) == 3: receiver3.start()
                clientsocket = False


# def receiver():
#     global running
#     while 1:
#         name, msg = soc.recv(BUFFERSIZE).decode().split(SEPARATOR)
#         if msg == STOPMESSAGE:
#             print(f"{name[:-2]} left")
#             soc.send(f"{name[:-2]}{SEPARATOR}left".encode())
#             #remove connection somehow
#             running = len(connectionlist)
#             break
#         print(f"{name}{msg}")
#         soc.send(f"{name}{SEPARATOR}{msg}".encode())


def bouncer(sock):
    global running
    while True:
        name, msg = sock.recv(BUFFERSIZE).decode().split(SEPARATOR)
        if msg == STOPMESSAGE:
            print(f"{name[:-2]} left")
            for socke in connectionlist:
                if sock != socke: socke.send(f"{name[:-2]}{SEPARATOR}left".encode())
            connectionlist.remove(sock)
            running = len(connectionlist)
            break
        print(f"{name}{msg}")
        for socke in connectionlist:
            # if sock != socke: 
            socke.send(f"{name}{SEPARATOR}{msg}".encode())
            # else: socke.send(f"{name}{SEPARATOR}".encode())


listenerthread = threading.Thread(target=listener, daemon=True)
listenerthread.start()

receiver1 = threading.Thread(target=lambda: bouncer(connectionlist[0]), daemon=True)
receiver2 = threading.Thread(target=lambda: bouncer(connectionlist[1]), daemon=True)
receiver3 = threading.Thread(target=lambda: bouncer(connectionlist[2]), daemon=True)

# receiver1 = threading.Thread(target=receiver, daemon=True)
# receiver1 = threading.Thread(target=receiver, daemon=True)
# receiver1 = threading.Thread(target=receiver, daemon=True)

while running: # just to keep the program alive while the threads are running
    a = True