import os
class Config:
	'''Miscellaneous Stuff '''
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
			os.system('afplay ./music/coin.wav&')

	def coins_left(self, grid, obj_mario):
		if (grid[obj_mario.ycoo + 2][obj_mario.xcoo - 1] == "$"):
			self.coins += 1
			os.system('afplay ./music/coin.wav&')

