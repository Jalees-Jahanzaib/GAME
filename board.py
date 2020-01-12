import numpy as np

class Board:


    def __init__(self,rows,colummns):
        self.rows=rows
        self.colummns=colummns
        self.matrix=[]
    def create_board(self):
        self.matrix=np.full((self.rows,self.colummns)," ")
    def printboard(self , coordinate):
        if coordinate==0:
             for i in range(self.rows):
                for j in range(coordinate,coordinate+110):
                     print(self.matrix[i][j],end='')
                print()


        elif coordinate==444:
            for i in range(self.rows):
                for j in range(444-55,444+55):
                    print(self.matrix[i][j],end='')
                print()
        else:
            for i in range(self.rows):
                for j in range(coordinate-55,coordinate+55):
                    print(self.matrix[i][j],end='')
                print()





       

    