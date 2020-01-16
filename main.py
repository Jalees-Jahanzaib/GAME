from board import Board
import os
from boys import Boys
from jetpacker import JetPacker
from Scenery import Scenery
from getch import _getChUnix as getChar
from config import Config
import signal
from alarmexception import AlarmException
from colorama import init,Fore
init()
objB=Board(30,500)
import time
obj_B.create_board()
obj_jp = JetPacker(25,0,1)
obj_jp.starting_position(objB.matrix)
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
	can_he=1

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
		

		prev_yc=obj_jp.yc
		
		while(obj_jp.yc != prev_yc-8 and # 8 units; checking if there's anything above
			objB.matrix[obj_jp.yc-1][obj_jp.xc+2] == " " and
			objB.matrix[obj_jp.yc-1][obj_jp.xc+1] == " " and
			objB.matrix[obj_jp.yc-1][obj_jp.xc] == " "): 

			obj_jp.jetpackerDisappear(objB)
			obj_jp.yc -= 1

			obj_jp.reappear(objB)

x=time.time()
y=x #copy
z=x #copy
while True: # The Game Loop
	os.system('clear')

	obj_config.rem = 150 - (round(time.time()) - round(x))
	print("TIME REMAINING:", obj_config.rem, end = '\t \t')
	print("LIVES:", obj_jp.life, end = '\t \t')
	print("COINS:", obj_config.coins, end = '\t \t')
	print("KILLS: ", obj_config.kills)

	if(obj_config.rem==0 or obj_jp.life == 0):
		print("GAME OVER")
		quit()


	if(obj_jp.xc<55):
		objB.printboard(0)
	elif(obj_jp.xc>=55 and obj_jp.xc<444):
		objB.printboard(obj_jp.xc)
	else:
		objB.printboard(444)
	
	movemario()
	

	if(objB.matrix[obj_jp.yc+3][obj_jp.xc]==" " # simulate gravity
		and objB.matrix[obj_jp.yc+3][obj_jp.xc+1]==" "
		and objB.matrix[obj_jp.yc+3][obj_jp.xc+2]==" " 
		and True):
			
		obj_jp.jetpackerDisappear(objB)
		obj_jp.yc+=1
		obj_jp.jetpackerDisappear(objB)


	if(obj_jp.xc==497):
		print("WELL DONE!")
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		break;
      
