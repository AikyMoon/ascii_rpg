import keyboard
import os

from time import sleep
from sys import platform

from objects import *

clear = lambda: os.system('cls') if platform == 'win32' else os.system('clear')
