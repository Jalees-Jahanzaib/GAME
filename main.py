import signal
import os
import time
from colorama import init, Fore
init()

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from jetpacker import JetPacker 
from Scenery import Scenery
from boys import Boys,Bullet
from config import Config

obj_board = Board(30,500)
obj_board.create_board()

obj_jp = JetPacker(25,0,1)
obj_jp.starting_position(obj_board.matrix)

obj_scenery = Scenery()

obj_scenery.create_ground(obj_board.matrix)
obj_scenery.create_sky(obj_board.matrix)
obj_scenery.create_clouds(obj_board.matrix, 2, 11)
obj_scenery.create_coins_platforms(obj_board)
enemy1 = Boys(20,70,1)
enemy2 = Boys(20,210,1)
enemy3 = Boys(20,280,1)
enemy4 = Boys(20,350,1)
enemy5 = Boys(20,400,1)
enemy11 = Boys(20,150,1)
enemy21 = Boys(20,240,1)
enemy31 = Boys(20,100,1)
bullets=[]
enemies = []
enemies.append(enemy1) 
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)
enemies2 = []
enemies2.append(enemy11) 
enemies2.append(enemy21) 
enemies2.append(enemy31) 
for en in enemies:
	en.starting_position1(obj_board.matrix)
for en in enemies2:
	en.starting_position2(obj_board.matrix)

obj_config = Config()

def motion():
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
		obj_config.coins_right(obj_board.matrix, obj_jp)
		can_he=obj_jp.check_not_collision_right(obj_board.matrix)

		
		if can_he == 1:
			obj_jp.jetpackerDisappear(obj_board)
			obj_jp.xc+=1
			obj_jp.direction = 1
			obj_jp.reappear(obj_board)

		elif can_he == 2:
			obj_jp.life -= 1
			obj_board.revive(obj_jp)
			obj_jp.did_he_die = 0


		else:
			os.system('afplay ./music/bump.wav&')

	if char == 'a':
		
		obj_config.coins_left(obj_board.matrix, obj_jp)
		can_he=obj_jp.check_not_collision_left(obj_board.matrix)

		
		if can_he == 1:
			obj_jp.jetpackerDisappear(obj_board)
			obj_jp.xc -= 1
			obj_jp.direction = -1
			obj_jp.reappear(obj_board)

		elif can_he == 2:
			obj_jp.life -= 1
			obj_board.revive(obj_jp)
			obj_jp.did_he_die = 0

		else:
			os.system('afplay ./music/bump.wav&')
				
	if char == 'q':

		quit()
	
	if char == 'w':
		if(True): #standing on surface

			prev_ycoo=obj_jp.ycoo
			
			while(obj_jp.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
				obj_board.matrix[obj_jp.ycoo-1][obj_jp.xc+2] == " " and
				obj_board.matrix[obj_jp.ycoo-1][obj_jp.xc+1] == " " and
				obj_board.matrix[obj_jp.ycoo-1][obj_jp.xc] == " "): 

				obj_jp.jetpackerDisappear(obj_board)
				obj_jp.ycoo -= 1

				obj_jp.reappear(obj_board)

			
	if char=="m":
		en1=Bullet(obj_jp.direction,obj_jp.xc,obj_jp.ycoo)
		en1.put_bullet(obj_board.matrix)
		bullets.append(en1)

x=time.time()
y=x #copy
z=x #copy




while True:
	os.system('clear')

	obj_config.rem = 150 - (round(time.time()) - round(x))
	print("TIME REMAINING:", obj_config.rem, end = '\t \t')
	print("LIVES:", obj_jp.life, end = '\t \t')
	print("COINS:", obj_config.coins, end = '\t \t')
	print("KILLS: ", obj_config.kills)

	
	if(obj_jp.ycoo == 26): # Fell into a hole!
		obj_jp.life -= 1
		obj_board.revive(obj_jp)

	if(obj_config.rem==0 or obj_jp.life == 0):
		print("GAME OVER")
		quit()


	if(obj_jp.xc<55):
		obj_board.printboard(0)
	elif(obj_jp.xc>=55 and obj_jp.xc<444):
		obj_board.printboard(obj_jp.xc)
	else:
		obj_board.printboard(444)
	
	motion()
	for i in bullets:
		i.move(obj_board.matrix)


	if(obj_board.matrix[obj_jp.ycoo-1][obj_jp.xc+1] == "*"):
		print("GAME OVER")
		quit()

	if(obj_board.matrix[obj_jp.ycoo+3][obj_jp.xc]==" " # simulate gravity
		and obj_board.matrix[obj_jp.ycoo+3][obj_jp.xc+1]==" "
		and obj_board.matrix[obj_jp.ycoo+3][obj_jp.xc+2]==" " 
		and True):
			
		obj_jp.jetpackerDisappear(obj_board)
		obj_jp.ycoo+=1
		obj_jp.reappear(obj_board)

	if(obj_jp.xc==497):
		print("WELL DONE!")
		break;









												  




 

