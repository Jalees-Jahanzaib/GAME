from colorama import Fore, Back, Style
import os

class Character_Structure:
    def __init__(self,xc,yc):
        self.xc=xc
        self.yc=yc
class Enemy(Character_Structure):
    def __init__