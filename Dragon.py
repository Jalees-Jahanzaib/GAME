from colorama import init, Fore,Back
init()

class Dragon:
    
    def __init__(self):
        self.kill = False
        self.life = 5
        self.shape=[["D","R","A"],["G","O","N"],["F","L","Y"]]   
        self.onboard=False
        self.blank=" "
    
    def printdragon(self):
        for i in range (0,3):
            for j in range(0,3):
                print('\033['+str(26+i)+';'+str(111+j)+'H'+self.shape[i][j],end='') 
    def reprintdragon(self,jetpacker):
        for i in range (0,3):
            for j in range(0,3):
                print('\033['+str(jetpacker.ycoo+i)+';'+str(111+j)+'H'+self.shape[i][j],end='') 
    def removedragon(self,jetpacker):
        for i in range (0,30):
            for j in range(0,3):
                print('\033['+str(i)+';'+str(111+j)+'H'+ self.blank,end='') 
    def movement(self,jetpacker):
        self.removedragon(jetpacker)
        self.reprintdragon(jetpacker)
class DragonFire:
    def __init__(self,jetpacker):
        self.shape1=Back.RED + '+' + Back.RESET
        self.xcoo=495
        self.num=0
        
    def put_bullet(self,grid,jetpacker):
        if self.xcoo-4>=0:
            self.xcoo=self.xcoo-1
        if self.num==0:
            self.num=jetpacker.ycoo       
            grid[jetpacker.ycoo][self.xcoo] = self.shape1
        else:
            grid[self.num][self.xcoo] = self.shape1
    def removebullet(self,grid,jetpacker):
        grid[self.num][self.xcoo] = " "
    def move(self,grid,jetpacker):
        self.removebullet(grid,jetpacker)
        self.put_bullet(grid,jetpacker)

        
                
