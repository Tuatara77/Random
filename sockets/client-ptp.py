import socket
import threading
import tkinter as tk
from tkinter import END

IP, PORT = "127.0.0.1", 12345
BUFFERSIZE = 1024

STOPMESSAGE = "#64STOPorAng3"
SEPARATOR = "|"

WINDOWX, WINDOWY = 640, 512
OFFSETX, OFFSETY = 0,0

class TkinterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Messagebox")
        self.geometry(f"{WINDOWX}x{WINDOWY}+{OFFSETX}+{OFFSETY}")

        self.messagebox = tk.Text(self, width=68, font=0)
        self.textbox = tk.Entry(self, width=68, font=0)

        self.messagebox.pack(expand=True)
        self.textbox.pack(expand=True)
        
        self.messagebox['state'] = "disabled"
        self.textbox.focus()
        
    def update(self, name, text):
        self.messagebox['state'] = "normal"
        self.messagebox.insert(END, chars=f"{name}:\n{text}\n\n")
        self.messagebox['state'] = "disabled"
        self.textbox.delete(0,END)


class Connection:
    def __init__(self, ip: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))
    
    def recv(self, buffersize): return self.sock.recv(buffersize)
    def send(self, data): self.sock.send(data)
    def close(self): self.sock.close()


class Program:
    def __init__(self, ip: str, port: int):
        self.alive = True
        self.window = TkinterWindow()
        self.conn = Connection(ip, port)
        self.receiver = threading.Thread(target=self.receive, daemon=True)
        self.receiver.start()
        self.window.textbox.bind("<Return>", self.sendevent)
    
    def receive(self):
        while self.alive:
            name, message = self.conn.recv(BUFFERSIZE).decode().split(SEPARATOR)
            self.window.update(name, message)
    
    def send(self):
        msg = self.window.textbox.get()

        if msg == "EXIT":
            self.conn.send(f"{NAME}{SEPARATOR}{STOPMESSAGE}".encode())
            self.alive = False
            self.window.destroy()
            self.conn.close()
        else: self.conn.send(f"{NAME}{SEPARATOR}{msg}".encode())

    def sendevent(self, event): self.send()


NAME = "desktop" #input("Input your name: ")

program = Program(IP, PORT)

program.window.mainloop()