from board import Board
from boys import Boys
from jetpacker import Jet_Packer
from Scenery import Scenery
from getch import *
from config import Config
import signal
from alarmexception import AlarmException
from coloroma import init,Fore
init()
objB=Board(30,500)

objB.create_board()
obj_jp = Jet_Packer(25,0,1)
obj_jp.starting_p(objB.matrix)
obj_scenery=Scenery()

obj_scenery.create_ground(objB.matrix)
obj_scenery.create_sky(objB.matrix)
obj_scenery.create_clouds(objB.matrix, 2, 11)
obj_scenery.create_tunnels(objB.matrix, 23, 19)
obj_scenery.create_bricks(objB.matrix, 19, 57)
obj_scenery.create_mountain(objB.matrix, 3, 294)
obj_scenery.put_barrier(objB.matrix)
obj_scenery.create_springs(objB)
obj_scenery.create_holes(objB)
obj_scenery.create_coins_platforms(objB)

Boys1 = Boys(26,70,1)
Boys2 = Boys(26,210,1)
Boys3 = Boys(26,280,1)
Boys4 = Boys(26,350,1)
Boys5 = Boys(26,400,1)

obj_config = Config()

def moveJP():
    def alarmhandler(signum,frame):
    