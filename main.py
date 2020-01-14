from board import Board
import os
from boys import Boys
from jetpacker import Jet_Packer
from Scenery import Scenery
from getch import *
from config import Config
import signal
from alarmexception import AlarmException
from colorama import init,Fore
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

def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
# char = user_input()

# 	if char == 'd':
# 		obj_config.coins_right(objB.matrix, obj_mario)
# 		can_he=obj_mario.check_not_collision_right(objB.matrix)

# 		if(objB.matrix[obj_mario.yc-5][obj_mario.xc + 1] == 'B'):
# 			objB.matrix[obj_mario.yc-5][obj_mario.xc + 1] = " "

		
# 		if can_he == 1:
# 			obj_mario.disappear_mario(objB)
# 			obj_mario.xcoo+=1
# 			obj_mario.direction = 1
# 			obj_mario.reappear_mario(objB)

# 		elif can_he == 2:
# 			obj_mario.life -= 1
# 			os.system('afplay ./music/mario_dies.wav&')
# 			objB.spawn_mario(obj_mario)
# 			obj_mario.did_he_die = 0


# 		else:
# 			os.system('afplay ./music/bump.wav&')

# 	if char == 'a':
		
# 		obj_config.coins_left(objB.matrix, obj_mario)
# 		can_he=obj_mario.check_not_collision_left(objB.matrix)

# 		if(objB.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] == 'B'):
# 			objB.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = " "
		
# 		if can_he == 1:
# 			obj_mario.disappear_mario(objB)
# 			obj_mario.xcoo -= 1
# 			obj_mario.direction = -1
# 			obj_mario.reappear_mario(objB)

# 		elif can_he == 2:
# 			obj_mario.life -= 1
# 			os.system('afplay ./music/mario_dies.wav&')
# 			objB.spawn_mario(obj_mario)
# 			obj_mario.did_he_die = 0

# 		else:
# 			os.system('afplay ./music/bump.wav&')
				
# 	if char == 'q':
# 		os.system("killall afplay")
# 		os.system('afplay ./music/game_over.wav&')
# 		quit()
	
# 	if char == 'w':
# 		if(obj_board.matrix[obj_mario.ycoo + 3][obj_mario.xcoo] == "-"): #standing on surface

# 			prev_ycoo=obj_mario.ycoo
			
# 			while(obj_mario.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
# 				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+2] == " " and
# 				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+1] == " " and
# 				obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo] == " "): 

# 				obj_mario.disappear_mario(obj_board)
# 				obj_mario.ycoo -= 1

# 				obj_mario.reappear_mario(obj_board)

# 			os.system('afplay ./music/jump.wav&')
# 			obj_config.check_brick_collision(obj_scenery, obj_board, obj_mario)

# 	if char == 's':
# 		obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo + 1] = 'B'
# 		os.system('afplay ./music/bullet.wav&')

# 		bosskill = obj_bossenemy.check_boss_kill(obj_board, obj_mario)
# 		# if(bosskill is False):
# 		# 	obj_board.matrix[obj_mario.ycoo-5][obj_mario.xcoo] = " "
# 		# else:
# 		if bosskill is True:
# 			if(obj_bossenemy.boss_life == 1):
# 				obj_bossenemy.boss_kill = True
# 				obj_scenery.remove_barrier(obj_board.matrix)
# 			else:
# 				obj_bossenemy.boss_life -= 1

# x=time.time()
# y=x #copy
# z=x #copy


# os.system('afplay ./music/theme.mp3&')
    
objB.printboard(55)          