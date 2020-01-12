from colorama import Fore, Back, Style
import os

class Character_Structure:
    def __init__(self,xc,yc,direction):
        self.xc=xc
        self.yc=yc
        self.dirction=direction
class Boys(Character_Structure):
    def __init__(self,xc,yc,direction):
        Character_Structure.__init__(self,xc,yc,direction)
        self.__shape=[["@","@"],["@","@"]]
        self.allowed_collision=[" "]
        self.hit_JP=["^"]
        self.killed=0
    def starting_position(self, grid):
        for i in range(self.yc,self.yc+2):
            for j in range(self.xc,self.xc+2):
                grid[i][j] = self.__shape[i-self.yc][j-self.xc]
    def disappear_enemy(self, grid):
        for i in range(self.yc, self.yc+2, 1):
            for j in range(self.xc, self.xc+2, 1):
                grid[i][j] = " "
        def reappear_enemy(self, grid):
            for i in range(self.yc, self.yc + 2, 1):
                for j in range(self.xc, self.xc + 2, 1):
                    grid[i][j] = self.__shape[i - self.yc][j - self.xc]
    def move(self,obj_board,obj_mario):
        if(self.direction == 1):
            if(obj_board.matrix[self.yc + 1][self.xc + 2] in self.allowed_collision):
                self.disappear_enemy(obj_board.matrix)
                self.xc += 1 
                self.reappear_enemy(obj_board.matrix)
            elif( obj_board.matrix[self.yc + 1][self.xc + 2] in self.hit_JP or 
				  obj_board.matrix[self.yc + 1][self.xc - 1] in self.hit_JP ):
                obj_mario.life -= 1
            else:
                self.direction = -1 # reverse the direction!
                self.disappear_enemy(obj_board.matrix)
                self.xc -= 1
                self.reappear_enemy(obj_board.matrix)
        else:
            if(obj_board.matrix[self.yc + 1][self.xc - 1] in self.allowed_collision):
                self.disappear_enemy(obj_board.matrix)
                self.xc -= 1 
                self.reappear_enemy(obj_board.matrix)
            elif(obj_board.matrix[self.yc + 1][self.xc - 1] in self.hit_with_mario or 
				obj_board.matrix[self.yc + 1][self.xc + 2] in self.hit_with_mario):
                obj_mario.life -= 1
            else:
                self.direction = 1
                self.disappear_enemy(obj_board.matrix)
                self.xc += 1
                self.reappear_enemy(obj_board.matrix)
        return 0






    