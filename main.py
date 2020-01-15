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
while True: # The Game Loop
	os.system('clear')

	obj_config.rem = 150 - (round(time.time()) - round(x))
	print("TIME REMAINING:", obj_config.rem, end = '\t \t')
	print("LIVES:", obj_mario.life, end = '\t \t')
	print("COINS:", obj_config.coins, end = '\t \t')
	print ("Lives of Boss Enemy:", obj_bossenemy.boss_life)
	print("KILLS: ", obj_config.kills)

	if(time.time() - y >= 0.05): #move basic enemies every 0.5 sec
		y=time.time()
		for en in list(enemies):
			if(en.killed==0):
				en.move(obj_board,obj_mario)
			else:
				enemies.remove(en)

	if(time.time() - z >= 2 and obj_mario.abducted == False and obj_bossenemy.boss_kill is False): 
		''' This checks if 3 seconds have passed, so as to switch the boss enemy to abduction mode'''
		z=time.time()
		if(obj_bossenemy.boss_type == 0):
			obj_bossenemy.boss_type = 1
			obj_bossenemy.remove_boss_abduct(obj_board.matrix)
			obj_bossenemy.put_boss(obj_board.matrix)
		else:
			obj_bossenemy.boss_type=0
			obj_bossenemy.remove_boss(obj_board.matrix)
			obj_bossenemy.put_boss_abduct(obj_board.matrix)
	
	if(obj_bossenemy.boss_kill is True):
		obj_bossenemy.remove_boss_abduct(obj_board.matrix)
		obj_bossenemy.remove_boss(obj_board.matrix)

	
	
	if(obj_mario.ycoo == 26): # Fell into a hole!
		obj_mario.life -= 1
		os.system('afplay ./music/mario_dies.wav&')
		obj_board.spawn_mario(obj_mario)

	if(obj_config.rem==0 or obj_mario.life == 0):
		print("GAME OVER")
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		quit()


	if(obj_mario.xcoo<55):
		obj_board.theyllprintit(0)
	elif(obj_mario.xcoo>=55 and obj_mario.xcoo<444):
		obj_board.theyllprintit(obj_mario.xcoo)
	else:
		obj_board.theyllprintit(444)
	
	movemario()
	
	if(obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo]== obj_scenery.spring or 
		obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+1]== obj_scenery.spring or 
		obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+2]==obj_scenery.spring ):
		
		os.system('afplay ./music/jump.wav&')
		obj_board.jump_higher(obj_mario)

	if(obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo] == "|" and 
		obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+2] == "|"):

		obj_mario.abducted = True

	if(obj_mario.abducted is True):
		
		obj_mario.disappear_mario(obj_board)
		obj_mario.ycoo = obj_mario.ycoo - 1
		obj_mario.reappear_mario(obj_board)

		if(obj_board.matrix[obj_mario.ycoo-1][obj_mario.xcoo+1] == "*"):
			print("GAME OVER")
			os.system("killall afplay")
			os.system('afplay ./music/game_over.wav&')
			quit()

	if(obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo]==" " # simulate gravity
		and obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+1]==" "
		and obj_board.matrix[obj_mario.ycoo+3][obj_mario.xcoo+2]==" " 
		and obj_mario.abducted is False):
			
		obj_mario.disappear_mario(obj_board)
		obj_mario.ycoo+=1
		obj_mario.reappear_mario(obj_board)

	for en in list(enemies):
		obj_mario.check_enemy_collision(obj_board, en, obj_config)

	if(obj_mario.xcoo==497):
		print("WELL DONE!")
		os.system("killall afplay")
		os.system('afplay ./music/game_over.wav&')
		break;
      
