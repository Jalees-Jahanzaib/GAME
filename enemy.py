from colorama import init, Fore,Back
init()
import os
from random import randint

class Main_person:
	def __init__(self,ycoo,xcoo,dire):
		self.xcoo = xcoo
		self.ycoo = ycoo
		self.shape3=[["+"," "," "],[" ","+"," "],[" "," ","+"]]
		self.direction = dire
class Enemy(Main_person):
	
	def __init__(self, ycoo, xcoo, dire):
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.allowed_collision = [ " " ]
		self.hit_with_mario = [ "^" ]
		self.killed = 0

	def starting_position1(self, grid):
		for i in range(self.ycoo,self.ycoo+4):
				grid[i][self.xcoo] =Back.RED + '+' + Back.RESET
				x0=Back.RESET+" "
	def starting_position2(self, grid):
		for i in range(self.xcoo,self.xcoo+6):
				grid[self.ycoo][i] = Back.RED + '+' + Back.RESET
    
	def starting_position3(self, grid):
		for i in range(self.ycoo, self.ycoo+3, 1):
			for j in range(self.xcoo, self.xcoo+3, 1):
				grid[i][j] =Back.RED + self.shape3[i-self.ycoo][j-self.xcoo] + Back.RESET

	def reappear_enemy(self, grid):
		for i in range(self.ycoo, self.ycoo + 2, 1):
			for j in range(self.xcoo, self.xcoo + 2, 1):
				grid[i][j] = self.__shape[i - self.ycoo][j - self.xcoo]
class Bullet:
	def __init__(self, dire,xcoo,ycoo):
		self.direction=dire
		self.shape1='0'
		self.xcoo=xcoo
		self.ycoo=ycoo
	def put_bullet(self,grid):
		if self.xcoo+4<=499:
			self.xcoo=self.xcoo+4
				
			grid[self.ycoo][self.xcoo] = self.shape1					
	def removebullet(self,grid):
		
		
		grid[self.ycoo][self.xcoo] = " "
	def move(self,grid):
		self.removebullet(grid)
		self.put_bullet(grid)
	def bullethits(self,grid):
		if self.xcoo+1=='+':
			grid[self.ycoo][self.xcoo+1]=' '
class Magnet:
	def __init__(self):
		self.shape1=[["#"," ","#"],["#"," ","#"],["#","#","#"]]
		self.random1=randint(0,5)
		
	def printmagnet(self,grid):
		for i in range(20-self.random1,23-self.random1,1):
			for j in range(15-self.random1, 18-self.random1, 1):
				grid[i][j] =Fore.MAGENTA + self.shape1[i-20+self.random1][j-15+self.random1] + '\x1b[0m'

	def removemagent(self,grid):
		for i in range(20,23):
			for j in range(40,43):
				grid[i][j]=" "
