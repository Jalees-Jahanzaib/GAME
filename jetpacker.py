from enemy import Main_person
class JetPacker(Main_person):
	
	
	def __init__(self, yc, xc, dire): 
		
		Main_person.__init__(self, yc, xc, dire)
		self.__shape1 = [ [" ", 'O', " "], ["[", "|", "<"], [" ", "^", " "] ]
		self.__shape2 = [ [" ", 'O', " "], [">", "|", "]"], [" ", "^", " "] ]
		self.life = 5
		self.allowed_collision = [ " ", "$" ]
		self.coins = 0
		self.did_he_die = 0

	def starting_position(self, grid):
		
		for i in range(25,28,1):
			for j in range(0, 3, 1):
				grid[i][j] = self.__shape1[i-25][j]

	def check_not_collision_right(self, grid):
		
		if (grid[self.yc][self.xc+3] in self.allowed_collision 
			and grid[self.yc+1][self.xc+3] in self.allowed_collision
			and grid[self.yc+2][self.xc+3] in self.allowed_collision):

			return 1
		
		
		elif (grid[self.yc + 1][self.xc + 3] == "+" 
			or grid[self.yc+2][self.xc+3] == "+"):
			return 2
		
		else:
			return 3
		
	def check_not_collision_left(self, grid):

		if (grid[self.yc][self.xc-1] in self.allowed_collision 
			and grid[self.yc+1][self.xc-1] in self.allowed_collision
			and grid[self.yc+2][self.xc-1] in self.allowed_collision
			and self.xc-1 != -1): # last condition for not going out of the board at -1th column

			return 1

		elif (grid[self.yc + 1][self.xc - 1] == "+" 
			or grid[self.yc+2][self.xc - 1] == "+"):
			
			return 2

		else:
			return 3
	
	def jetpackerDisappear(self, obj_board):
		for i in range(self.yc, self.yc+3):
			for j in range(self.xc, self.xc+3):
				obj_board.matrix[i][j] = " "

	def reappear(self, obj_board):
		for i in range(self.yc, self.yc+3, 1):
			for j in range(self.xc, self.xc+3, 1):
				if self.direction == 1:
						obj_board.matrix[i][j] = self.__shape1[i-self.yc][j-self.xc]
				else:
					obj_board.matrix[i][j] = self.__shape2[i-self.yc][j-self.xc]
