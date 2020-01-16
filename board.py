import os
class Board:
	
	def __init__(self, rows, columns): 
		self.rows = rows
		self.columns = columns
		self.matrix = []

	def create_board(self):

		for i in range (self.rows):                             
			self.new = []                 
			for j in range (self.columns):   
				self.new.append(" ")      
			self.matrix.append(self.new)

	def theyllprintit(self, a):
		if(a==0):
			for i in range(self.rows):
				for j in range(a,a+110):
					print(self.matrix[i][j],end='')
				print()
		
		elif(a == 444): 
			for i in range(self.rows):
				for j in range(444-55, 444+55): 
					print(self.matrix[i][j],end='')
				print()

		else:  
			for i in range(self.rows):
				for j in range(a-55, a+55): 
					print(self.matrix[i][j],end='')
				print()

	def spawn_mario(self, obj_mario): 

		obj_mario.disappear_mario(self)
						
		obj_mario.ycoo -= 14
		obj_mario.xcoo -= 5

		obj_mario.reappear_mario(self)



		