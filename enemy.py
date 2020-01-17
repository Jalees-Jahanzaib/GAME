from colorama import init, Fore
init()
import os

class Main_person:
	def __init__(self,ycoo,xcoo,dire):
		self.xcoo = xcoo
		self.ycoo = ycoo
		self.direction = dire

class Enemy(Main_person):
	
	def __init__(self, ycoo, xcoo, dire):
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.allowed_collision = [ " " ]
		self.hit_with_mario = [ "^" ]
		self.killed = 0

	def starting_position1(self, grid):
		for i in range(self.ycoo,self.ycoo+4):
				grid[i][self.xcoo] = '+'
	def starting_position2(self, grid):
		for i in range(self.xcoo,self.xcoo+6):
				grid[self.ycoo][i] = '+'

	def disappear_enemy(self, grid):
		for i in range(self.ycoo, self.ycoo+2, 1):
			for j in range(self.xcoo, self.xcoo+2, 1):
				grid[i][j] = " "

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
		
	def printmagnet(self,grid):
		for i in range(20,23,1):
			for j in range(15, 18, 1):
				grid[i][j] =Fore.RED + self.shape1[i-20][j-15] + '\x1b[0m'
	def removemagent(self,grid):
		for i in range(20,23):
			for j in range(40,43):
				grid[i][j]=" "