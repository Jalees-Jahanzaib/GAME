import os
class Config:
	def __init__(self):
		self.rem = 150
		self.coins =0 
		self.kills = 0 

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			pass
		try:
			import unicodedata
			unicodedata.numeric(s)
			return True
		except (TypeError, ValueError):
			pass

		return False

	def coins_right(self, grid, obj_mario):
		if (grid[obj_mario.ycoo + 2][obj_mario.xcoo + 3] == "$"):
			self.coins += 1

	def coins_left(self, grid, obj_mario):
		if (grid[obj_mario.ycoo + 2][obj_mario.xcoo - 1] == "$"):
			self.coins += 1
	def coins_up(self, grid, obj_mario):
		self.coins += 1

	

delta=0
delta1=0
magnet_xcoo=0

def savemando(jetpacker,obj_config,board):
	obj_config.coins_right(board.matrix, jetpacker)

	can_he = jetpacker.check_not_collision_right(board.matrix)

	if can_he == 1:
		jetpacker.remove_jp(board)
		#jetpacker.xcoo += 3
		#jetpacker.direction = 1
		jetpacker.reapper(board)

	elif can_he == 2:
		if jetpacker.powermode == True: # powermode is for the shield
				print("ttt")
				jetpacker.powermode = False
				jetpacker.life += 1
		jetpacker.life -= 1
		board.revive(jetpacker)
		jetpacker.did_he_die = 0
	