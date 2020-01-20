import os


class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []
        self.canvas = 0
        self.time = 0

    def create_board(self):

        for i in range(self.rows):
            self.new = []
            for j in range(self.columns):
                self.new.append(" ")
            self.matrix.append(self.new)

    def theyllprintit(self):
        self.time += 1
        if self.time % 3 == 0:
            self.canvas += 1
        if (self.canvas == 444):
            for i in range(self.rows):
                for j in range(444 - 55, 444 + 55):
                    print(self.matrix[i][j], end='')
                print()

        for i in range(self.rows):
            for j in range(self.canvas, self.canvas + 110):
                print(self.matrix[i][j], end='')
            print()

    def revive(self, jetpacker):

        jetpacker.remove_jp(self)

        jetpacker.xcoo -= 5

        jetpacker.reapper(self)
