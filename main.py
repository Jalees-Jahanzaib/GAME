import signal
import os
import time
from colorama import init, Fore,Back
init()

from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from JetPacker import JetPacker 
from scenery import Scenery
from enemy import Enemy, Bullet,Magnet
from Dragon import Dragon,DragonFire
from config import Config
import config
board = Board(30,500)
board.create_board()

jetpacker = JetPacker(25,0,1)
D1=Dragon()
D2=[]
jetpacker.starting_position(board.matrix)

obj_scenery = Scenery()
m1=Magnet()
obj_scenery.create_ground(board.matrix)
obj_scenery.create_sky(board.matrix)
obj_scenery.create_clouds(board.matrix, 2, 11)
obj_scenery.create_coins_platforms(board)
enemy1 = Enemy(20,70,1)
enemy2 = Enemy(20,210,1)
enemy3 = Enemy(20,280,1)
enemy4 = Enemy(20,350,1)
enemy5 = Enemy(20,400,1)
enemy11 = Enemy(20,150,1)
enemy21 = Enemy(20,240,1)
enemy31 = Enemy(20,100,1)
bullets=[]
enemies = []
# enemies.append(enemy1) 
enemies.append(enemy2)
enemies.append(enemy3)
enemies.append(enemy4)
enemies.append(enemy5)
enemies2 = []
enemies2.append(enemy11) 
enemies2.append(enemy21) 
enemies2.append(enemy31) 
for en in enemies:
	en.starting_position1(board.matrix)
for en in enemies2:
	en.starting_position2(board.matrix)
enemy1.starting_position3(board.matrix)
obj_config = Config()
def selfmotion():
	if jetpacker.mode==False:

		obj_config.coins_right(board.matrix, jetpacker)
		

		can_he=jetpacker.check_not_collision_right(board.matrix)

		
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo+=1
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.powermode==True:
				jetpacker.powermode=False
				jetpacker.life+=1
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0


		else:
			pass
	elif jetpacker.mode==True:
		
		obj_config.coins_right(board.matrix, jetpacker)
		

		can_he=jetpacker.check_not_collision_right(board.matrix)

		
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo+=3
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0


		else:
			pass




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

	if char == 'd' and jetpacker.mode==False:
		m1.printmagnet(board.matrix)

		obj_config.coins_right(board.matrix, jetpacker)
		

		can_he=jetpacker.check_not_collision_right(board.matrix)

		
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo+=1
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.powermode==True:
				print("ttt")
				jetpacker.powermode=False
				jetpacker.life+=1
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0


		else:
			pass
	if char == 'd' and jetpacker.mode==True:
		m1.printmagnet(board.matrix)
		obj_config.coins_right(board.matrix, jetpacker)
		

		can_he=jetpacker.check_not_collision_right(board.matrix)

		
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo+=3
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0


		else:
			pass
	if char == 'a' and jetpacker.mode==False:
		
		obj_config.coins_left(board.matrix, jetpacker)
		can_he=jetpacker.check_not_collision_left(board.matrix)

		
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo -= 1
			jetpacker.direction = -1
			jetpacker.reapper(board)

		elif can_he == 2:
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0

		else:
			pass		
	if char == 'a' and jetpacker.mode==True:
	
		obj_config.coins_left(board.matrix, jetpacker)
		can_he=jetpacker.check_not_collision_left(board.matrix)

	
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo -= 3
			jetpacker.direction = -1
			jetpacker.reapper(board)

		elif can_he == 2:
			jetpacker.life -= 1
			board.revive(jetpacker)
			jetpacker.did_he_die = 0

		else:
			pass				
	if char == 'q':
		quit()
	
	if char == 'w':
	
		prev_ycoo=jetpacker.ycoo
		
		while(jetpacker.ycoo != prev_ycoo-8 and # 8 units; checking if there's anything above
			board.matrix[jetpacker.ycoo-1][jetpacker.xcoo+2] == " " and
			board.matrix[jetpacker.ycoo-1][jetpacker.xcoo+1] == " " and
			board.matrix[jetpacker.ycoo-1][jetpacker.xcoo] == " "): 

			jetpacker.remove_jp(board)
			jetpacker.ycoo -= 1

	if char=="m":
		en1=Bullet(jetpacker.direction,jetpacker.xcoo,jetpacker.ycoo)
		en1.put_bullet(board.matrix)
		bullets.append(en1)
	if char=="p":
		jetpacker.mode=True
		jetpacker.direction=1
	if char=="x" and jetpacker.keypress:
		jetpacker.powermode=True
		jetpacker.keypress=False
		#print("y")
		config.delta=time.time()
		config.delta1=time.time()


x1=time.time()
x2=time.time()
x3=0

startime=0
config.delta=0
while True:
	if startime==0:
		os.system('clear')
		startime+=1
	print('\033[0;0H',end='')
	obj_config.rem = 150 - (round(time.time()) - round(x1))
	print("TIME REMAINING:", obj_config.rem, end = ' \t \t')
	print("LIVES:", jetpacker.life, end = '\t \t')
	print("COINS:", obj_config.coins, end = '\t \t\n')



	if(obj_config.rem==0 or jetpacker.life == 0):
		print("GAME OVER") 
		quit()
	if(jetpacker.powermode==True):
		if ((10 - ((time.time()) - (config.delta))) <=0):
			jetpacker.powermode=False
			config.delta=0
	if ((60 - ((time.time()) - (config.delta1))) <=0):
		jetpacker.keypress=True
		config.delta1=0
	if ((3 - ((time.time()) - (x2))) <=0):
		m1.printmagnet(board.matrix)
	






	if(jetpacker.xcoo<55):
		board.theyllprintit(0)
	elif(jetpacker.xcoo>=55 and jetpacker.xcoo<444):
		board.theyllprintit(jetpacker.xcoo)
	else:
		board.theyllprintit(444)
	if D1.onboard==False:
		selfmotion()
	motion()
	# m1.removemagent(board.matrix)
	for i in bullets:
		i.bullethits(board.matrix)
	for i in bullets:
		i.move(board.matrix)
	x3+=1
	jetpacker.check_enemy_collision(board)
	# jetpacker.check_magent(board)
	jetpacker.check_not_collision_down(board.matrix,obj_config)
	jetpacker.check_not_collision_up(board.matrix,obj_config)
	if jetpacker.xcoo>=390:
		D1.reprintdragon(jetpacker)
		D1.movement(jetpacker)
		D1.onboard=True
		if x3%30==1:
			x4=DragonFire(jetpacker)
			D2.append(x4)
		for i in D2:
			i.move(board.matrix,jetpacker)

	if(board.matrix[jetpacker.ycoo-1][jetpacker.xcoo+1] == "*"):
		print("GAME OVER")
		quit()

	if(board.matrix[jetpacker.ycoo+3][jetpacker.xcoo]==" " # simulate gravity
		and board.matrix[jetpacker.ycoo+3][jetpacker.xcoo+1]==" "
		and board.matrix[jetpacker.ycoo+3][jetpacker.xcoo+2]==" " 
		and True):
			
		jetpacker.remove_jp(board)
		jetpacker.ycoo+=1
		jetpacker.reapper(board)

	if(jetpacker.xcoo>497):
		print("NOICE!")
		
		break;








