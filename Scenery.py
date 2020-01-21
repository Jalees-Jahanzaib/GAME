import random
import os
from colorama import init, Fore
init()


class Scenery:
    def __init__(self):
        self.__sky = Fore.RED + "^" + '\033[42m' + '\033[0m'
        self.brick_score = 51
        self.__ground1 = Fore.GREEN + "^" + '\x1b[0m'
        self.__cloud = []

    def create_ground(self, grid):
        for i in range(500):
            grid[29][i] = self.__ground1
            grid[28][i] = Fore.GREEN + "^" + '\x1b[0m'

    def create_sky(self, grid):
        for i in range(500):
            grid[0][i] = self.__sky

    def create_clouds(self, grid, c, d):
        with open("./clouds.txt") as obj:
            for line in obj:
                self.__cloud.append(line.strip('\n'))

        while (d < 271):
            e = d
            f = c
            for i in range(4):
                for j in range(16):
                    grid[c][d] = Fore.BLUE + self.__cloud[i][j] + '\x1b[0m'
                    d += 1
                d = e
                c += 1
            c = f + random.randint(0, 2)
            d += 37 + random.randint(10, 50)

    def create_coins_platforms(self, obj_board):

        for i in range(115, 130):
            obj_board.matrix[16][i] = Fore.YELLOW + "$" + '\x1b[0m'
        for i in range(115, 130):
            obj_board.matrix[17][i] = Fore.YELLOW + "$" + '\x1b[0m'

        for i in range(320, 334):
            obj_board.matrix[23][i] = Fore.YELLOW + "$" + '\x1b[0m'
            obj_board.matrix[21][i] = Fore.YELLOW + "$" + '\x1b[0m'
            obj_board.matrix[22][i] = Fore.YELLOW + "$" + '\x1b[0m'
