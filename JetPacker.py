import random
import os
from beams import Structure
import colors
listnum=[]
class JetPacker(Structure):
	
	def __init__(self, ycoo, xcoo, dire): 
		
		Structure.__init__(self, ycoo, xcoo, dire)
		self._powermode=False
		self._life = 100
		self._allowed_collision = [ " ", colors.color_text("$","Yellow"),"8" ]
		self.__shape2 = [ [" ", 'O', " "], [">", "|", "]"], [" ", "^", " "] ]
		self._did_he_die = 0
		self.mode = False
		self.keypress=True
		self.__shape3=[["!","!",'!'],["!","!",'!'],["!","!",'!']]
		self._falsecheck=0
		self.__shape1 = [ [" ", 'O', " "], ["[", "|", "<"], [" ", "^", " "] ]

	def set_did_he_die(self,x):
		self._did_he_die =x
	def get_powermode(self):
		return self._powermode
	def set_powermode(self,x):
		self._powermode=x
	def get_life(self):
		return self._life
	def set_life(self,x):
		self._life=x
	def set_coins(self,x):
		self._coins=x
	def starting_position(self, grid):
		
		for i in range(25+self._falsecheck,28+self._falsecheck,1):
			for j in range(0, 3, 1):
				grid[i][j] = colors.color_text(self.__shape1[i-25][j+self._falsecheck] ,"Cyan")
	listnum.append("1")
	def check_not_collision_right(self, grid):
		
		if (grid[self.ycoo+self._falsecheck][self.xcoo+3+self._falsecheck] in self._allowed_collision
			and True
			and grid[self.ycoo+1][self.xcoo+3] in self._allowed_collision
			and grid[self.ycoo+2+self._falsecheck][self.xcoo+3+self._falsecheck] in self._allowed_collision and True):

			return 1
		listnum.append("1")

		
		if ('+' in grid[self.ycoo + 1][self.xcoo + 3] 			or '+' in grid[self.ycoo+2][self.xcoo+3] 			 or '+' in grid[self.ycoo][self.xcoo+3] ):
			return 2
	
		else:
			return 3
	listnum.append("3")	
	def check_not_collision_left(self, grid):

		if (grid[self.ycoo+self._falsecheck][self.xcoo-1+self._falsecheck] in self._allowed_collision 
			and grid[self.ycoo+1+self._falsecheck][self.xcoo-1] in self._allowed_collision
			and True
			and grid[self.ycoo+2][self.xcoo-1+self._falsecheck] in self._allowed_collision
			and self.xcoo-1!= -1 and True):

			return 1

		if ('+' in grid[self.ycoo + 1][self.xcoo -1] 			or '+' in grid[self.ycoo+2][self.xcoo-1] 			 or '+' in grid[self.ycoo][self.xcoo-1] ):

			
			return 2

		else:
			return 3
	listnum.append("3")	

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
				self._life -= 1
				board.revive(self)
				self._did_he_die = 0
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
				self._life -= 1
				board.revive(self)
				self._did_he_die = 0
				break
			
	
		
	def remove_jp(self, obj_board):
		listnum.append("2")
		for i in range(self.ycoo, self.ycoo+3):
			listnum.append("3")
			for j in range(self.xcoo, self.xcoo+3):
				obj_board.matrix[i][j+self._falsecheck] = " "
	listnum.append("5")
	def reapper(self, obj_board):
		
		for i in range(self.ycoo, self.ycoo+3+self._falsecheck, 1):
			for j in range(self.xcoo, self.xcoo+3+self._falsecheck, 1):
				if self.direction == 1+self._falsecheck and self._powermode==False and True:
						obj_board.matrix[i][j+self._falsecheck] = colors.color_text(self.__shape1[i-self.ycoo][j-self.xcoo],"Cyan") 
				elif self.direction == -1 and self._powermode==False and True:
					obj_board.matrix[i][j+self._falsecheck] = colors.color_text(self.__shape2[i-self.ycoo][j-self.xcoo],"Cyan") 
				elif  self._powermode==True:
					obj_board.matrix[i][j] = colors.color_text(self.__shape3[i-self.ycoo][j-self.xcoo],"Cyan") 
	listnum.append("3")	
			
	def check_enemy_collision(self, obj_board):
		if '+' in obj_board.matrix[self.ycoo+3][self.xcoo] 			or '+' in obj_board.matrix[self.ycoo+3][self.xcoo+1]			or '+' in obj_board.matrix[self.ycoo+3][self.xcoo+2]:
			self._life -= 1
			obj_board.revive(self)
			self._did_he_die = 0
	def check_in_canvas(self,obj_board):
		if self.xcoo<=obj_board.get_canvas()+1:
				self.remove_jp(obj_board)
				self.xcoo=obj_board.get_canvas()+1
				self.reapper(obj_board)
		return self.xcoo
	def get_attracted(self,x,obj_board):
		self.remove_jp(obj_board)
		if(self.xcoo<x):
			self.xcoo+=3
		elif(self.xcoo>x):
			self.xcoo-=3
		self.reapper(obj_board)




