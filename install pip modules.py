import os

os.system("pip install --upgrade pip")

try: import pygame
except ModuleNotFoundError: os.system("pip install pygame")

try: import keyboard
except ModuleNotFoundError: os.system("pip install keyboard")

try: import mouse
except ModuleNotFoundError: os.system("pip install mouse")

try: import numpy
except ModuleNotFoundError: os.system("pip install numpy")

try: import cv2
except ModuleNotFoundError: os.system("pip install opencv-python")

try: import Pillow
except: ModuleNotFoundError: os.system("pip install Pillow")

try: import pyautogui
except ModuleNotFoundError: os.system("pip install pyautogui")

try: import pytube
except ModuleNotFoundError: os.system("pip install pytube")
