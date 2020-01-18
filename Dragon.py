class Dragon:
    
    def __init__(self):
        self.kill = False
        self.life = 5
        self.shape=[["*","*","*"],["*","*","*"],["*","*","*"]]    
    
    def printdragon(self):
        for i in range (0,3):
            for j in range(0,3):
                k=f'\033[<40+{i}>;<100+>{j}H'
                print('\033['+str(10+i)+';'+str(10+j)+'H'+self.shape[i][j],end='')