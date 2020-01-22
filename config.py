import os
class Config:
	def __init__(self):
		self._rem = 214
		self._coins =0 
		self._kills = 0 
	def get_rem(self):
		return self._rem
	def get_coins(self):
		return self._coins

	def coins_right(self, grid, obj_jp):
		if (grid[obj_jp.ycoo + 2+self._kills][obj_jp.xcoo + 3] == "$"):
			self._coins += 1
	def set_coins(self,x):
		self._coins=x
	def set_rem(self,x):
		self._rem=x
	def coins_left(self, grid, obj_jp):
		if (grid[obj_jp.ycoo + 2+self._kills][obj_jp.xcoo - 1] == "$"):
			self._coins += 1
	def coins_up(self, grid, obj_jp):
		self._coins += 1

	
normal=0
delta=0
delta1=0
magnet_xcoo=0

def savemando(jetpacker,obj_config,board):
	obj_config.coins_right(board.matrix, jetpacker)

	can_he = jetpacker.check_not_collision_right(board.matrix)

	if can_he == 1+normal:
		jetpacker.remove_jp(board)
		#jetpacker.xcoo += 3
		#jetpacker.direction = 1
		jetpacker.reapper(board)

	elif can_he == 2+normal:
		if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
		jetpacker.set_life(jetpacker.get_life()-1)	
		board.revive(jetpacker)
		jetpacker.did_he_die = 0

uptime=0
gravy=0