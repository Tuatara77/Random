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
        # self.geometry("640x512+0+0")

        self.messagebox = tk.Text(self, width=68, font=0)
        self.textbox = tk.Entry(self, width=68, font=0)

        self.messagebox.pack(expand=True)
        self.textbox.pack(expand=True)

        self.textbox.bind("<Return>", send)
        
        self.messagebox['state'] = "disabled"
        self.textbox.focus()
        
    def update(self, name, text):
        self.messagebox['state'] = "normal"
        self.messagebox.insert(END, chars=f"{name}:\n{text}\n\n")
        self.messagebox['state'] = "disabled"
        self.textbox.delete(0,END)


def send(event=None):
    msg = window.textbox.get()

    if msg == "EXIT":
        # exitt = input("Do you want to disconnect? (y/n) ").lower()
        exitt = "y"
        if exitt == "y":
            soc.send(f"{NAME}{SEPARATOR}{STOPMESSAGE}".encode())
            soc.close()
            window.destroy()
    else:
        # window.update(NAME, msg)
        soc.send(f"{NAME}{SEPARATOR}{msg}".encode())


def receive():
    name, message = soc.recv(BUFFERSIZE).decode().split(SEPARATOR)
    window.update(name, message)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((IP, PORT))

receiver = threading.Thread(target=receive, daemon=True)

NAME = input("Input your name: ")

window = TkinterWindow()

receiver.start()

window.mainloop()
