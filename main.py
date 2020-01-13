from board import Board
from boys import Boys
from jetpacker import Jet_Packer
from Scenery import Scenery
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
objB.printboard(55)

enemy1 = Enemy(26,70,1)
enemy2 = Enemy(26,210,1)
enemy3 = Enemy(26,280,1)
enemy4 = Enemy(26,350,1)
enemy5 = Enemy(26,400,1)

enemies = []
enemies.append(enemy1) 
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)

for en in enemies:
	en.starting_position(obj_board.matrix)
