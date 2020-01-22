import colors
class Dragon:
	
	def __init__(self):
		self.life = 5
		self.shape=[list("@@ _   "),
					list("()(_)  "),
					list("|| ||\\ ")]
		#[["D","R","A"],["G","O","N"],["F","L","Y"]]   
		self.onboard=False
		self.blank=" "
		self.xcoo=0
		self.ycoo=0
	
	def printdragon(self):
		for i in range (0,3):
			for j in range(0,len(self.shape[0])):
				print('\033['+str(26+i)+';'+str(111+j)+'H'+colors.color_text(self.shape[i][j],"Pink"),end='') 
	def reprintdragon(self,jetpacker):
		for i in range (0,3):
			for j in range(0,len(self.shape[0])):
				print('\033['+str(jetpacker.ycoo+i)+';'+str(111+j)+'H'+colors.color_text(self.shape[i][j],"Pink"),end='')
				self.ycoo=jetpacker.ycoo+i
				self.xcoo=111+j
	def removedragon(self,jetpacker):
		for i in range (0,30):
			for j in range(0,len(self.shape[0])):
				print('\033['+str(i)+';'+str(111+j)+'H'+ self.blank,end='') 
	def movement(self,jetpacker):
		self.removedragon(jetpacker)
		self.reprintdragon(jetpacker)
	def hitdragon(self,bullet,board):
		#print(bullet.xcoo-board.canvas,self.ycoo- bullet.ycoo)
		#print()
		#if (bullet.xcoo-board.canvas==110 and self.ycoo==bullet.ycoo)           or (bullet.xcoo-board.canvas==110 and self.ycoo==bullet.ycoo-1)or (bullet.xcoo-board.canvas==110 and self.ycoo==bullet.ycoo-2) :
		if(bullet.xcoo-board.canvas==110 and self.ycoo- bullet.ycoo==2):
			self.life-=1
	def living(self):
		if self.life<=0:
			return 0   
		return 1
	
class DragonFire:
	def __init__(self,jetpacker):
		self.shape1= colors.color_text("+","Red") 
		self.xcoo=495
		self.num=0
		
	def put_bullet(self,grid,jetpacker,board):
		if (self.xcoo-1=="o" or self.xcoo-1 =="<" or self.xcoo-1=="^") or (self.num-1=="o" or self.num-1 =="<" or self.num-1=="^"):
			if jetpacker.powermode==True:
				jetpacker.powermode=False
				jetpacker.life+=1
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0
		if (self.num+1=="o" or self.num+1 =="<" or self.num+1=="^") or (self.xcoo+1=="o" or self.xcoo+1 =="<" or self.xcoo+1=="^"):
			if jetpacker.powermode==True:
				jetpacker.powermode=False
				jetpacker.life+=1
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0
		if self.xcoo-1>=0:
			self.xcoo=self.xcoo-1
		
		if self.num==0:
			self.num=jetpacker.ycoo+1       
			grid[jetpacker.ycoo+1][self.xcoo] = colors.color_text(self.shape1,"Pink")
		else:
			grid[self.num][self.xcoo] = colors.color_text(self.shape1,"Pink")
	def removebullet(self,grid,jetpacker):
		grid[self.num][self.xcoo] = " "
	def move(self,grid,jetpacker,board):
		self.removebullet(grid,jetpacker)
		self.put_bullet(grid,jetpacker,board)

		
				
