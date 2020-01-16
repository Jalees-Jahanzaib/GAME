from colorama import Fore, Back, Style
import os

class Character_Structure:
    def __init__(self,xc,yc,direction):
        self.xc=xc
        self.yc=yc
        self.dirction=direction
class Boys(Character_Structure):
 	def __init__(self, ycoo, xcoo, dire):
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.__shape = [ ["+", "+"], ["@", "@"] ]
		self.allowed_collision = [ " " ]
		self.hit_with_mario = [ "^" ]
		self.killed = 0

	def starting_position1(self, grid):
		for i in range(self.ycoo,self.ycoo+4):
				grid[i][self.xcoo] = '+'
	def starting_position2(self, grid):
		for i in range(self.xcoo,self.xcoo+6):
				grid[self.ycoo][i] = '+'





    