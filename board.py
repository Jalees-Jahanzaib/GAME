import os
import config

	

class Board:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = []
		self.canvas = 1
		self.time = 0

	def create_board(self):

		for i in range(self.rows):
			self.new = []
			for j in range(self.columns):
				self.new.append(" ")
			self.matrix.append(self.new)

	def theyllprintit(self,jetpacker):
		self.time += 1
		if self.time % 3 == 0:
			self.canvas += 1
			if(self.canvas>=config.magnet_xcoo- 110 and self.canvas<=config.magnet_xcoo ):
				#savemando()
				jetpacker.get_attracted(config.magnet_xcoo,self)
		if (self.canvas >= 344):
			for i in range(self.rows):
				for j in range(444 - 55, 444 + 55):
					print(self.matrix[i][j], end='')
				print()
		else:
			for i in range(self.rows):
				for j in range(self.canvas, self.canvas + 110):
					print(self.matrix[i][j], end='')
				print()

	def revive(self, jetpacker):

		jetpacker.remove_jp(self)

		jetpacker.xcoo -= 5

		jetpacker.reapper(self)
