import random
import os
from enemy import Main_person
import colors
class JetPacker(Main_person):
	
	def __init__(self, ycoo, xcoo, dire): 
		
		Main_person.__init__(self, ycoo, xcoo, dire)
		self.__shape1 = [ [" ", 'O', " "], ["[", "|", "<"], [" ", "^", " "] ]
		self.__shape2 = [ [" ", 'O', " "], [">", "|", "]"], [" ", "^", " "] ]
		self.__shape3=[["!","!",'!'],["!","!",'!'],["!","!",'!']]
		self.powermode=False
		self.life = 100
		self.allowed_collision = [ " ", colors.color_text("$","Yellow") ]
		self.coins = 0
		self.did_he_die = 0
		self.mode = False
		self.keypress=True

	def starting_position(self, grid):
		
		for i in range(25,28,1):
			for j in range(0, 3, 1):
				grid[i][j] = colors.color_text(self.__shape1[i-25][j] ,"Cyan")

	def check_not_collision_right(self, grid):
		
		if (grid[self.ycoo][self.xcoo+3] in self.allowed_collision 
			and grid[self.ycoo+1][self.xcoo+3] in self.allowed_collision
			and grid[self.ycoo+2][self.xcoo+3] in self.allowed_collision):

			return 1
		
		
		if ('+' in grid[self.ycoo + 1][self.xcoo + 3] 			or '+' in grid[self.ycoo+2][self.xcoo+3] 			 or '+' in grid[self.ycoo][self.xcoo+3] ):
			return 2
	
		else:
			return 3
		
	def check_not_collision_left(self, grid):

		if (grid[self.ycoo][self.xcoo-1] in self.allowed_collision 
			and grid[self.ycoo+1][self.xcoo-1] in self.allowed_collision
			and grid[self.ycoo+2][self.xcoo-1] in self.allowed_collision
			and self.xcoo-1 != -1): # last condition for not going out of the board at -1th column

			return 1

		if ('+' in grid[self.ycoo + 1][self.xcoo -1] 			or '+' in grid[self.ycoo+2][self.xcoo-1] 			 or '+' in grid[self.ycoo][self.xcoo-1] ):

			
			return 2

		else:
			return 3

	def check_not_collision_down(self, grid,obj_config,board):

		if '$' in grid[self.ycoo-1][self.xcoo]:
			grid[self.ycoo-1][self.xcoo]=' '
			obj_config.coins_up(grid,self)

		if  '$' in grid[self.ycoo-1][self.xcoo+1]:
			grid[self.ycoo-1][self.xcoo+1]=' '
			obj_config.coins_up(grid,self)

		if '$' in  grid[self.ycoo-1][self.xcoo+2]:
			grid[self.ycoo-1][self.xcoo+2]=' '
			obj_config.coins_up(grid,self)
		for i in range(3):
			if ('+' in grid[self.ycoo -1][self.xcoo + i] 			):
				self.life -= 1
				board.revive(self)
				self.did_he_die = 0
				break

	def check_not_collision_up(self, grid,obj_config,board):

		if '$' in grid[self.ycoo+3][self.xcoo]: 
			grid[self.ycoo+3][self.xcoo]=' '
			obj_config.coins_up(grid,self)

		if  '$' in grid[self.ycoo+3][self.xcoo+1]:
			grid[self.ycoo+3][self.xcoo+1]=' '
			obj_config.coins_up(grid,self)

		if  '$' in grid[self.ycoo+3][self.xcoo+2]:
			grid[self.ycoo+3][self.xcoo+2]=' '
			obj_config.coins_up(grid,self)
		for i in range(3):
			if ('+' in grid[self.ycoo +3][self.xcoo + i]):
				self.life -= 1
				board.revive(self)
				self.did_he_die = 0
				break
			
	""" def check_not_collision_down(self,grid,obj_config, board):
		if '$' in grid[self.ycoo-1][self.xcoo]: 
			grid[self.ycoo+3][self.xcoo]=' '
			obj_config.coins_up(grid,self)

		elif  '$' in grid[self.ycoo-1][self.xcoo+1]:
			grid[self.ycoo-1][self.xcoo+1]=' '
			obj_config.coins_up(grid,self)

		elif  '$' in grid[self.ycoo-1][self.xcoo+2]:
			grid[self.ycoo-1][self.xcoo+2]=' '
			obj_config.coins_up(grid,self)
		if '+' in grid[self.ycoo-1][self.xcoo] or '+' in grid[self.ycoo-2][self.xcoo] or '+' in  grid[self.ycoo-3][self.xcoo]:
			self.life -= 1
			board.revive(self)
			self.did_he_die = 0

		elif '+' in grid[self.ycoo-1][self.xcoo+1] or '+' in  grid[self.ycoo-2][self.xcoo+1] or '+' in  grid[self.ycoo-3][self.xcoo+1]:
			self.life -= 1
			board.revive(self)
			self.did_he_die = 0
		elif '+' in grid[self.ycoo-1][self.xcoo+2] or '+' in  grid[self.ycoo-2][self.xcoo+2] or '+' in  grid[self.ycoo-3][self.xcoo+2]:
			self.life -= 1
			board.revive(self)
			self.did_he_die = 0 """

		
	def remove_jp(self, obj_board):
		for i in range(self.ycoo, self.ycoo+3):
			for j in range(self.xcoo, self.xcoo+3):
				obj_board.matrix[i][j] = " "

	def reapper(self, obj_board):
		for i in range(self.ycoo, self.ycoo+3, 1):
			for j in range(self.xcoo, self.xcoo+3, 1):
				if self.direction == 1 and self.powermode==False:
						obj_board.matrix[i][j] = colors.color_text(self.__shape1[i-self.ycoo][j-self.xcoo],"Cyan") 
				elif self.direction == -1 and self.powermode==False:
					obj_board.matrix[i][j] = colors.color_text(self.__shape2[i-self.ycoo][j-self.xcoo],"Cyan") 
				elif  self.powermode==True:
					obj_board.matrix[i][j] = colors.color_text(self.__shape3[i-self.ycoo][j-self.xcoo],"Cyan") 
				
	def check_enemy_collision(self, obj_board):
		if '+' in obj_board.matrix[self.ycoo+3][self.xcoo] 			or '+' in obj_board.matrix[self.ycoo+3][self.xcoo+1]			or '+' in obj_board.matrix[self.ycoo+3][self.xcoo+2]:
			self.life -= 1
			obj_board.revive(self)
			self.did_he_die = 0
	def check_in_canvas(self,obj_board):
		if self.xcoo<=obj_board.get_canvas()+1:
				self.remove_jp(obj_board)
				self.xcoo=obj_board.get_canvas()+1
				self.reapper(obj_board)
		return self.xcoo
	def get_attracted(self,x,obj_board):
		self.remove_jp(obj_board)
		if(self.xcoo<x):
			self.xcoo+=5
		elif(self.xcoo>x):
			self.xcoo-=5
		self.reapper(obj_board)




