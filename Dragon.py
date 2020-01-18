class Dragon:
    
    def __init__(self):
        self.kill = False
        self.life = 5
        self.shape=[["*","*","*"],["*","*","*"],["*","*","*"]]   
        self.onboard=False 
    
    def printdragon(self):
        for i in range (0,3):
            for j in range(0,3):
                print('\033['+str(26+i)+';'+str(115+j)+'H'+self.shape[i][j],end='')  
                
                
                
