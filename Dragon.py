import colors
class Dragon:
	
	def __init__(self):
		self._life = 5
		self._shape=[list("@@ _   "),
					list("()(_)  "),
					list("|| ||\\ ")]
		#[["D","R","A"],["G","O","N"],["F","L","Y"]]   
		self._onboard=False
		self._blank=" "
		self._xcoo=0
		self._ycoo=0
	
	def printdragon(self):
		for i in range (0,3):
			for j in range(0,len(self._shape[0])):
				print('\033['+str(26+i)+';'+str(111+j)+'H'+colors.color_text(self._shape[i][j],"Pink"),end='') 
	def reprintdragon(self,jetpacker):
		for i in range (0,3):
			for j in range(0,len(self._shape[0])):
				print('\033['+str(jetpacker.ycoo+i)+';'+str(111+j)+'H'+colors.color_text(self._shape[i][j],"Pink"),end='')
				self._ycoo=jetpacker.ycoo+i
				self._xcoo=111+j
	def removedragon(self,jetpacker):
		for i in range (0,30):
			for j in range(0,len(self._shape[0])):
				print('\033['+str(i)+';'+str(111+j)+'H'+ self._blank,end='') 
	def movement(self,jetpacker):
		self.removedragon(jetpacker)
		self.reprintdragon(jetpacker)
	def hitdragon(self,bullet,board):
		#print(bullet.xcoo-board.canvas,self._ycoo- bullet.ycoo)
		#print()
		#if (bullet.xcoo-board.canvas==110 and self._ycoo==bullet.ycoo)           or (bullet.xcoo-board.canvas==110 and self._ycoo==bullet.ycoo-1)or (bullet.xcoo-board.canvas==110 and self._ycoo==bullet.ycoo-2) :
		if(bullet.xcoo-board.get_canvas()==110 and self._ycoo- bullet.ycoo==2):
			self._life-=1
	def living(self):
		if self._life<=0:
			return 0   
		return 1
	def get_life(self):
		x=self._life
		return x
	
class DragonFire:
	def __init__(self,jetpacker):
		self._shape1= colors.color_text("+","Red") 
		self._xcoo=495
		self._num=0
		
	def put_bullet(self,grid,jetpacker,board):
		if (self._xcoo-1=="o" or self._xcoo-1 =="<" or self._xcoo-1=="^") or (self._num-1=="o" or self._num-1 =="<" or self._num-1=="^"):
			if jetpacker.get_powermode() == True: # powermode is for the shield
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)
		if (self._num+1=="o" or self._num+1 =="<" or self._num+1=="^") or (self._xcoo+1=="o" or self._xcoo+1 =="<" or self._xcoo+1=="^"):
			if jetpacker.get_powermode() == True: # powermode is for the shield
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)
		if self._xcoo-1>=0:
			self._xcoo=self._xcoo-1
		
		if self._num==0:
			self._num=jetpacker.ycoo+1       
			grid[jetpacker.ycoo+1][self._xcoo] = colors.color_text(self._shape1,"Pink")
		else:
			grid[self._num][self._xcoo] = colors.color_text(self._shape1,"Pink")
	def removebullet(self,grid,jetpacker):
		grid[self._num][self._xcoo] = " "
	def move(self,grid,jetpacker,board):
		self.removebullet(grid,jetpacker)
		self.put_bullet(grid,jetpacker,board)

		
				
