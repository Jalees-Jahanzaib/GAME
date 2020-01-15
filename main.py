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
import time
objB.create_board()
obj_jp = Jet_Packer(25,0,1)
obj_jp.starting_p(objB.matrix)
obj_scenery=Scenery()

obj_scenery.create_ground(objB.matrix)
obj_scenery.create_sky(objB.matrix)
obj_scenery.create_clouds(objB.matrix, 2, 11)

obj_config = Config()

def movemario():
	''' moves Mario'''
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

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

	char = user_input()

	if char == 'd':
		obj_config.coins_right(objB.matrix, obj_jp)
		can_he=obj_jp.check_not_collision_right(objB.matrix)

	if can_he == 1:
		obj_jp.jetpackerDisappear(objB)
		obj_jp.xc+=1
		obj_jp.direction = 1
		obj_jp.reappear(objB)

	elif can_he == 2:
		obj_jp.life -= 1
		objB.rebirth(obj_jp)
		obj_jp.death = 0
    
        
        
	if char == 'a':
		
		obj_config.coins_left(objB.matrix, obj_jp)
		can_he=obj_jp.check_not_collision_left(objB.matrix)

		if can_he == 1:
			obj_jp.jetpackerDisappear(objB)
			obj_jp.xc -= 1
			obj_jp.direction = -1
			obj_jp.reappear(objB)

		elif can_he == 2:
			obj_jp.life -= 1
			objB.rebirth(obj_jp)
			obj_jp.death = 0

		else:
			callerr=1
				
	if char == 'q':
		quit()
	
	if char == 'w':
		

		prev_ycoo=obj_jp.ycoo
		
		while(obj_jp.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
			obj_board.matrix[obj_jp.ycoo-1][obj_jp.xcoo+2] == " " and
			obj_board.matrix[obj_jp.ycoo-1][obj_jp.xcoo+1] == " " and
			obj_board.matrix[obj_jp.ycoo-1][obj_jp.xcoo] == " "): 

			obj_jp.jetpackerDisappear(obj_board)
			obj_jp.ycoo -= 1

			obj_jp.reappear(obj_board)

x=time.time()
y=x #copy
z=x #copy

    
objB.printboard(55)          