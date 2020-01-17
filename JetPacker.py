import random
import os
from colorama import init, Fore,Back
init()
from enemy import Main_person
class JetPacker(Main_person):
	
	def __init__(self, ycoo, xcoo, dire): 
		
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.__shape1 = [ [" ", 'O', " "], ["[", "|", "<"], [" ", "^", " "] ]
		self.__shape2 = [ [" ", 'O', " "], [">", "|", "]"], [" ", "^", " "] ]
		self.life = 5
		self.allowed_collision = [ " ", "$" ]
		self.coins = 0
		self.did_he_die = 0
		self.mode = False

	def starting_position(self, grid):
		
		for i in range(25,28,1):
			for j in range(0, 3, 1):
				grid[i][j] =self.__shape1[i-25][j]

	def check_not_collision_right(self, grid):
		
		if (grid[self.ycoo][self.xcoo+3] in self.allowed_collision 
			and grid[self.ycoo+1][self.xcoo+3] in self.allowed_collision
			and grid[self.ycoo+2][self.xcoo+3] in self.allowed_collision):

			return 1
		
		
		elif (grid[self.ycoo + 1][self.xcoo + 3] == "+" 
			or grid[self.ycoo+2][self.xcoo+3] == "+" or grid[self.ycoo][self.xcoo+3] == "+"):
			return 2
	
		else:
			return 3
		
	def check_not_collision_left(self, grid):

		if (grid[self.ycoo][self.xcoo-1] in self.allowed_collision 
			and grid[self.ycoo+1][self.xcoo-1] in self.allowed_collision
			and grid[self.ycoo+2][self.xcoo-1] in self.allowed_collision
			and self.xcoo-1 != -1): # last condition for not going out of the board at -1th column

			return 1

		elif (grid[self.ycoo + 1][self.xcoo - 1] == "+" 
			or grid[self.ycoo+2][self.xcoo - 1] == "+"  or grid[self.ycoo][self.xcoo - 1] == "+"):
			
			return 2

		else:
			return 3

	def check_not_collision_down(self, grid,obj_config):

		if grid[self.ycoo-1][self.xcoo]=='$':
			grid[self.ycoo-1][self.xcoo]=' '
			obj_config.coins_up(grid,self)

		elif grid[self.ycoo-1][self.xcoo+1]=='$':
			grid[self.ycoo-1][self.xcoo+1]=' '
			obj_config.coins_up(grid,self)

		elif grid[self.ycoo-1][self.xcoo+2]=='$':
			grid[self.ycoo-1][self.xcoo+2]=' '
			obj_config.coins_up(grid,self)
	def check_not_collision_up(self, grid,obj_config):

		if grid[self.ycoo+3][self.xcoo]=='$':
			grid[self.ycoo+3][self.xcoo]=' '
			obj_config.coins_up(grid,self)

		elif grid[self.ycoo+3][self.xcoo+1]=='$':
			grid[self.ycoo+3][self.xcoo+1]=' '
			obj_config.coins_up(grid,self)

		elif grid[self.ycoo+3][self.xcoo+2]=='$':
			grid[self.ycoo+3][self.xcoo+2]=' '
			obj_config.coins_up(grid,self)
			


		
	def remove_jp(self, obj_board):
		for i in range(self.ycoo, self.ycoo+3):
			for j in range(self.xcoo, self.xcoo+3):
				obj_board.matrix[i][j] = " "

	def reapper(self, obj_board):
		for i in range(self.ycoo, self.ycoo+3, 1):
			for j in range(self.xcoo, self.xcoo+3, 1):
				if self.direction == 1 and self.mode == False:
						obj_board.matrix[i][j] = self.__shape1[i-self.ycoo][j-self.xcoo]
				else:
					obj_board.matrix[i][j] = self.__shape2[i-self.ycoo][j-self.xcoo]
	def check_enemy_collision(self, obj_board):
		if(obj_board.matrix[self.ycoo+3][self.xcoo]=="+" # simulate gravity
		or obj_board.matrix[self.ycoo+3][self.xcoo+1]=="+"
		or obj_board.matrix[self.ycoo+3][self.xcoo+2]=="+"):
			self.life -= 1
			obj_board.revive(self)
			self.did_he_die = 0
	def check_money(self, obj_config, obj_board):
		if(obj_board.matrix[self.ycoo+3][self.xcoo]=="$"# simulate gravity
		or obj_board.matrix[self.ycoo+3][self.xcoo+1]=="$"
		or obj_board.matrix[self.ycoo+3][self.xcoo+2]=="$"):
			obj_config.coins_up(obj_board.matrix,self)
			self.did_he_die = 0
	def check_magent(self,obj_board):
		if(obj_board.matrix[self.ycoo+3+1][self.xcoo]=="#"# simulate gravity
		    or obj_board.matrix[self.ycoo+3+1][self.xcoo+1]=="#"
		    or obj_board.matrix[self.ycoo+3+1][self.xcoo+2]=="#"):
			self.ycoo+=3
		
		





