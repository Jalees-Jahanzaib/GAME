import colors 
import random
import os
import enemy



class Scenery:
    def __init__(self):
        self.__sky = colors.color_text("^","Blue") #Fore.RED + "^" + '\033[42m' + '\033[0m'
        self.brick_score = 51
        self.__ground1 = colors.color_text("^",'Water Color')#'' + "^" + '\x1b[0m'
        self.__cloud = []

    def create_ground(self, grid):
        for i in range(500):
            grid[29][i] = self.__ground1
            grid[28][i] = colors.color_text("^","Water Color") #+ "^" + '\x1b[0m'

    def create_sky(self, grid):
        for i in range(500):
            grid[1][i] = self.__sky

    def create_coins_platforms(self, obj_board):

        for i in range(115, 130):
            obj_board.matrix[16][i] = colors.color_text("$","Yellow")
        for i in range(115, 130):
            obj_board.matrix[17][i] = colors.color_text("$","Yellow")

        for i in range(320, 334):
            obj_board.matrix[23][i] = colors.color_text("$","Yellow")
            obj_board.matrix[21][i] = colors.color_text("$","Yellow")
            obj_board.matrix[22][i] = colors.color_text("$","Yellow")
    def create_magnet(self,obj_board):
        m=enemy.Magnet()
        m.printmagnet(obj_board.matrix)