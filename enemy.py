import os
from random import randint
import colors
import config
class Main_person:
	def __init__(self, ycoo, xcoo, dire):
		self.xcoo = xcoo
		self.ycoo = ycoo
		self.shape3 = [["+", " ", " "], [" ", "+", " "], [" ", " ", "+"]]
		self.direction = dire


class Enemy(Main_person):
	def __init__(self, ycoo, xcoo,dire):
		Main_person.__init__(self, ycoo, xcoo,dire)
		self.allowed_collision = [" "]
		self.dire=dire
	def create_fire(self,num,grid):
		if num==1:
			self.starting_position1(grid)
		elif num==2:
			self.starting_position2(grid)
		elif num==3:
			self.starting_position3(grid)
	def starting_position1(self, grid):
		for i in range(self.ycoo, self.ycoo + 4):
			grid[i][self.xcoo] = colors.color_text('+',"Red")

	def starting_position2(self, grid):
		for i in range(self.xcoo, self.xcoo + 6):
			grid[self.ycoo][i] = colors.color_text('+',"Red")

	def starting_position3(self, grid):
		for i in range(self.ycoo, self.ycoo + 3, 1):
			for j in range(self.xcoo, self.xcoo + 3, 1):
				grid[i][j] = colors.color_text(self.shape3[i - self.ycoo][j - self.xcoo],"Red")

	def remove_position1(self, grid):
		for i in range(self.ycoo, self.ycoo + 4):
			grid[i][self.xcoo] = " "

	def remove_position2(self, grid):
		for i in range(self.xcoo, self.xcoo + 6):
			grid[self.ycoo][i] = " "

	def remove_position3(self, grid):
		for i in range(self.ycoo, self.ycoo + 3, 1):
			for j in range(self.xcoo, self.xcoo + 3, 1):
				grid[i][j] = " "   
				

class Bullet:
	def __init__(self, dire, xcoo, ycoo):
		self.direction = dire
		self.shape1 = '0'
		self.xcoo = xcoo
		self.ycoo = ycoo

	def put_bullet(self, grid):
		if self.xcoo + 4 <= 499:
			self.xcoo = self.xcoo + 1

			grid[self.ycoo][self.xcoo] = self.shape1

	def removebullet(self, grid):

		grid[self.ycoo][self.xcoo] = " "

	def move(self, grid):
		if self.xcoo<=499:
			self.removebullet(grid)
			self.put_bullet(grid)
	# def killbullet(self,bullet):
	# 	bullet.remove(self)

	def bullethits(self, grid,bullet):
	
		if '+' in grid[self.ycoo][self.xcoo+1]:
			xcoo=self.xcoo+1
			ycoo=self.ycoo
			print(ycoo,xcoo)
			if '+' in grid[self.ycoo+1][self.xcoo+1] or  '+' in grid[self.ycoo-1][self.xcoo+1]:
				while('+' in grid[ycoo][self.xcoo+1]):
					grid[ycoo][self.xcoo+1]=' '
					ycoo+=1
				ycoo=self.ycoo-1
				while('+' in grid[ycoo][self.xcoo+1]):
					grid[ycoo][self.xcoo+1]=' '
					ycoo-=1
			elif '+' in grid[self.ycoo][self.xcoo+1] or  '+' in grid[self.ycoo][self.xcoo]:
				while('+' in grid[ycoo][xcoo]):
					grid[ycoo][xcoo]=' '
					xcoo+=1
				xcoo=self.xcoo
				while('+' in grid[ycoo][xcoo]):
					grid[ycoo][xcoo]=' '
					xcoo-=1
			else:
				while('+' in grid[ycoo][xcoo]):
						grid[ycoo][xcoo]=' '
						xcoo+=1
						ycoo+=1
				xcoo=self.xcoo
				ycoo=self.ycoo-1
				while('+' in grid[ycoo][xcoo]):
					grid[ycoo][xcoo]=' '
					xcoo-=1
					ycoo-=1
				
			grid[self.ycoo][self.xcoo]=' '
			# self.killbullet(bullet)
			return 1
			# getx=-1
			# for i in listx:
			# 	if xcoo+1 == i  :
			# 		getx=i
			# 		self.killbullet(bullet)
			# if getx!=-1:
			# 	for i in range(getx, getx + 6):
			# 		grid[listy[idx]][i] = " "		
		


class Magnet:
	def __init__(self):
		self.shape1 = [["M", " ", "M"], ["M", " ", "M"], ["M", "M", "M"]]
		self.random1 = randint(0, 5)
		config.magnet_xcoo=self.random1+100

	def printmagnet(self, grid):
		
			startie= self.random1+100
			startje = self.random1+10
			for i in range(3):
				for j in range(3):
					try:
						grid[startje+ i][startie+j] = self.shape1[i ][j]
					except:
						print(i,j,len(grid),len(grid[0]))

	def removemagent(self, grid):
		for i in range(10, 23):
			for j in range(40, 143):
				grid[i][j] = " "
