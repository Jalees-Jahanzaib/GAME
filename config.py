
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

	def coins_right(self, grid, obj_jp):
		if (grid[obj_jp.yc + 2][obj_jp.xc + 3] == "$"):
			self.coins += 1

	def coins_left(self, grid, obj_mario):
		if (grid[obj_jp.yc + 2][obj_jp.xc - 1] == "$"):
			self.coins += 1




