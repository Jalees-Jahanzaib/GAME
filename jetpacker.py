from boys import Character_Structure

class Jet_Packer(Character_Structure):
    def __init__(self,yc,xc,direction):
        Character_Structure.__init__(self,yc,xc,direction)
        self.__shape1 = [ ["|", 'O', "|"], [" ", "\\", " "], ["^", " ", "^"] ]
        self.__shape2 = [ ["|", "O", "|"], [" ", "/", " "], ["^", " ", "^"] ]
        self.life=3
        self.allowed_collision=[" ","$"]
        self.coins=0
        self.death=0
        self.power_up=False
    def starting_p(self,grid):
        for i in range(25,28,1):
            for j in range(0,3,1):
                grid[i][j]=self.__shape1[i-25][j]
    def check_not_collision_right(self, grid):
        if (grid[self.yc][self.xc+3] in self.allowed_collision 
			and grid[self.yc+1][self.xc+3] in self.allowed_collision
			and grid[self.yc+2][self.xc+3] in self.allowed_collision):
            return 1
        elif (grid[self.yc + 1][self.xc + 3] == "@" 
			or grid[self.yc+2][self.xc+3] == "@"):
            return 2
        else:
            return 3
    def check_not_collision_left(self, grid):
        if (grid[self.yc][self.xc-1] in self.allowed_collision 
			and grid[self.yc+1][self.xc-1] in self.allowed_collision
			and grid[self.yc+2][self.xc-1] in self.allowed_collision
			and self.xc-1 != -1): # last condition for not going out of the board at -1th column
         return 1
        elif (grid[self.yc + 1][self.xc - 1] == "@" 
			or grid[self.yc+2][self.xc - 1] == "@"):
            return 2
        else:
            return 3
        def disappear_mario(self, obj_board):
            for i in range(self.yc, self.yc+3):
                for j in range(self.xc, self.xc+3):
                    obj_board.matrix[i][j] = " "
        def reappear_mario(self, obj_board):
            for i in range(self.yc, self.yc+3, 1):
                for j in range(self.xc, self.xc+3, 1):
                    if self.direction == 1:
                        obj_board.matrix[i][j] = self.__shape1[i-self.ycoo][j-self.xcoo]
                    else:
                        obj_board.matrix[i][j] = self.__shape2[i-self.ycoo][j-self.xcoo]
        def check_enemy_collision(self, obj_board, obj_enemy, obj_config):
            if(obj_board.matrix[self.yc+3][self.xc]=="@" # simulate gravity
               or obj_board.matrix[self.yc+3][self.xc+1]=="@"
               or obj_board.matrix[self.yc+3][self.xc+2]=="@"):
                obj_enemy.disappear_enemy(obj_board.matrix)
                obj_enemy.killed = 1
                obj_config.kills += 1