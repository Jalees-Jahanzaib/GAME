from colorama import Fore, Back, Style
import os

class Character_Structure:
    def __init__(self,xc,yc,direction):
        self.xc=xc
        self.yc=yc
        self.dirction=direction
class Boys(Character_Structure):
 	def __init__(self, yc, xc, dire):
		Main_person.__init__(self, yc, xc, dire)
		self.__shape = [ ["+", "+"], ["@", "@"] ]
		self.allowed_collision = [ " " ]
		self.hit_with_mario = [ "^" ]
		self.killed = 0

	def starting_position1(self, grid):
		for i in range(self.yc,self.yc+4):
				grid[i][self.xc] = '+'
	def starting_position2(self, grid):
		for i in range(self.xc,self.xc+6):
				grid[self.yc][i] = '+'

class Bullet:
	def __init__(self, dire,xc,yc):
		self.direction=dire
		self.shape1='o'
		self.xc=xc
		self.yc=yc
	def put_bullet(self,grid):
		if self.xc+4<=499:
			self.xc=self.xc+4
				
			grid[self.yc][self.xc] = self.shape1
		
	

		
	def removebullet(self,grid):
		
		
		grid[self.yc][self.xc] = " "
	def move(self,grid):
		self.removebullet(grid)
		self.put_bullet(grid)



    