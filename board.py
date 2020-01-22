import os
import config

	

class Board:
	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self.matrix = []
		self._canvas = 1
		self._time = 0
	def get_matrix(self):
		return self.matrix
	def get_canvas(self):
		return self._canvas
	def set_canvas(self,x):
		self._canvas=x
	def create_board(self):

		for i in range(self._rows):
			self.new = []
			for j in range(self._columns):
				self.new.append(" ")
			self.matrix.append(self.new)

	def theyllprintit(self,jetpacker):
		self._time += 1
		if self._time % 3 == 0:
			self._canvas += 1
			if(self._canvas>=config.magnet_xcoo- 110 and self._canvas<=config.magnet_xcoo ):
				#savemando()
				jetpacker.get_attracted(config.magnet_xcoo,self)
		if (self._canvas >= 344):
			for i in range(self._rows):
				for j in range(444 - 55, 444 + 55):
					print(self.matrix[i][j], end='')
				print()
		else:
			for i in range(self._rows):
				for j in range(self._canvas, self._canvas + 110):
					print(self.matrix[i][j], end='')
				print()

	def revive(self, jetpacker):

		jetpacker.remove_jp(self)

		jetpacker.xcoo -= 5

		jetpacker.reapper(self)
