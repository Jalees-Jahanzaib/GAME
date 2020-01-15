from boys import Character_Structure

class Jet_Packer(Character_Structure):
    def __init__(self,yc,xc,direction):
        Character_Structure.__init__(self,yc,xc,direction)
        self.__shape1 = [ [" ", 'O', " "], ["[", "|", "<"], [" ", "^", " "] ]
        self.__shape2 = [ [" ", 'O', " "], [">", "|", "]"], [" ", "^", " "] ]
        self.__shape3= [ ["| ", 'O', " |"], ["{", "|", "}"], [" ", "^", " "] ]
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
        elif (grid[self.yc + 1][self.xc + 3] == "*" 
			or grid[self.yc+2][self.xc+3] == "*"):
            return 2
        else:
            return 3
  
    def jetpackerDisappear(self, obj_board):
        for i in range(self.yc, self.yc+3):
            for j in range(self.xc, self.xc+3):
                obj_board.matrix[i][j] = " "
    def reappear(self, obj_board):
        for i in range(self.yc, self.yc+3, 1):
            for j in range(self.xc, self.xc+3, 1):
                    obj_board.matrix[i][j] = self.__shape1[i-self.ycoo][j-self.xcoo]
                