import signal
import os
import time
from random import randint
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from JetPacker import JetPacker
from scenery import Scenery
from enemy import Enemy, Bullet, Magnet
from Dragon import Dragon, DragonFire
from config import Config
import config

def savemando():
	obj_config.coins_right(board.matrix, jetpacker)

	can_he = jetpacker.check_not_collision_right(board.matrix)

	if can_he == 1:
		jetpacker.remove_jp(board)
		#jetpacker.xcoo += 3
		#jetpacker.direction = 1
		jetpacker.reapper(board)

	elif can_he == 2:
		if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
		jetpacker.set_life(jetpacker.get_life()-1)	
		board.revive(jetpacker)
		jetpacker.set_did_he_die(0)
	

# import simpleaudio as sa

# filename = 'audio.mp3'
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
board = Board(30, 500)
board.create_board()

jetpacker = JetPacker(25, 0, 1)
D1 = Dragon()
D2 = []
jetpacker.starting_position(board.matrix)

obj_scenery = Scenery()
#m1 = Magnet()
obj_scenery.create_ground(board.matrix)
obj_scenery.create_sky(board.matrix)
#bj_scenery.create_clouds(board.matrix, 2, 11)
obj_scenery.create_coins_platforms(board)
obj_scenery.create_magnet(board)
bullets = []
enemies = []
listx=[]
listy=[]

for i in range(0, 25):
	intnum = randint(1, 3)
	intx = randint(10, 300)
	inty = randint(10, 20)
	listx.append(intx)
	listy.append(inty)
	inte = Enemy(inty, intx, 1)
	inte.create_fire(intnum, board.matrix)
	enemies.append(inte)

obj_config = Config()


def motion(x5):
	def alarmhandler(signum, frame):

		raise AlarmException

	def user_input(timeout=0.15):
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

	if char == 'd' and jetpacker.mode == False:
		#m1.printmagnet(board.matrix)
		obj_config.coins_right(board.matrix, jetpacker)
		can_he = jetpacker.check_not_collision_right(board.matrix)
		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo += 1
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)

		else:
			pass
	if char == 'd' and jetpacker.mode == True:
		#m1.printmagnet(board.matrix)
		obj_config.coins_right(board.matrix, jetpacker)

		can_he = jetpacker.check_not_collision_right(board.matrix)

		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo += 3
			jetpacker.direction = 1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False) 
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)

		else:
			pass
	if char == 'a' and jetpacker.mode == False:

		obj_config.coins_left(board.matrix, jetpacker)
		can_he = jetpacker.check_not_collision_left(board.matrix)

		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo -= 2
			jetpacker.direction = -1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)

		else:
			pass
	if char == 'a' and jetpacker.mode == True:

		obj_config.coins_left(board.matrix, jetpacker)
		can_he = jetpacker.check_not_collision_left(board.matrix)

		if can_he == 1:
			jetpacker.remove_jp(board)
			jetpacker.xcoo -= 3
			jetpacker.direction = -1
			jetpacker.reapper(board)

		elif can_he == 2:
			if jetpacker.get_powermode() == True: # powermode is for the shield
				print("ttt")
				jetpacker.set_powermode(False)
				jetpacker.set_life(jetpacker.get_life()+1)
			jetpacker.set_life(jetpacker.get_life()-1)	
			board.revive(jetpacker)
			jetpacker.set_did_he_die(0)

		else:
			pass
	if char == 'q':
		quit()

	if char == 'w':
		config.uptime=time.time()
		config.gravy=0
		prev_ycoo = jetpacker.ycoo
		#jetpacker.check_not_collision_downstar(board.matrix,board)
		while (jetpacker.ycoo != prev_ycoo - 8
			and board.matrix[jetpacker.ycoo - 1][jetpacker.xcoo + 2] == " "
			and board.matrix[jetpacker.ycoo - 1][jetpacker.xcoo + 1] == " "
			and board.matrix[jetpacker.ycoo - 1][jetpacker.xcoo] == " "):

			jetpacker.remove_jp(board)
			jetpacker.ycoo -= 1

	if char == "m":
		en1 = Bullet(jetpacker.direction, jetpacker.xcoo, jetpacker.ycoo)
		en1.put_bullet(board.matrix)
		bullets.append(en1)
	if char == "p":
		jetpacker.mode = True
	if char == "x" and jetpacker.keypress:
		jetpacker.set_powermode(True)
		jetpacker.keypress = False
		config.delta = time.time()
		config.delta1 = time.time()


x1 = time.time()
x2 = time.time()
x3 = 0
x4 = 0
x5=0
startime=0
config.delta = 0
config.uptime=0
aaaaaa=[0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
while True:
	if(config.uptime!=0 and time.time()-config.uptime>=aaaaaa[config.gravy]):
		config.gravy+=1
		if(config.gravy>8):
			config.gravy=8
		config.uptime=time.time()
		for i in range(2):
			if('$' in board.matrix[jetpacker.ycoo + 3][jetpacker.xcoo+i]):
				Config.set_coins(Config.get_coins()+1)
		if (board.matrix[jetpacker.ycoo + 3][jetpacker.xcoo] ==" "  
			and board.matrix[jetpacker.ycoo + 3][jetpacker.xcoo + 1] == " "
			and board.matrix[jetpacker.ycoo + 3][jetpacker.xcoo + 2] == " "
			and True):

			jetpacker.remove_jp(board)
			jetpacker.ycoo += 1
			jetpacker.reapper(board)

	if startime == 0:
		os.system('clear')
		startime += 1
	time.sleep(0.05)
	print('\033[0;0H', end='')
	obj_config.set_rem(216 - (round(time.time()) - round(x1)))
	print("TIME REMAINING:", obj_config.get_rem(), end=' \t \t')
	print("LIVES:", jetpacker.get_life(), end=' \t \t')
	print("COINS:", obj_config.get_coins(), end='\t \t')
	print("Dragon Life:", D1.get_life(), end='\t \t')
	# for i in range(0,len(listx)):
	# 	print(listx[i],end='\n')

	if (obj_config.get_rem() == 0 or jetpacker.get_life() == 0):
		os.system('clear')
		print("\n\n\n\n\t\t\t\tGAME OVER")
		quit()
	if (jetpacker.get_powermode() == True):
		if ((10 - ((time.time()) - (config.delta))) <= 0):
			jetpacker.set_powermode(False)
			config.delta = 0
	if ((60 - ((time.time()) - (config.delta1))) <= 0):
		jetpacker.keypress = True
		config.delta1 = 0
	#m1.printmagnet(board.matrix)

	board.theyllprintit(jetpacker)

	motion(x5)

	for i in bullets:
		D1.hitdragon(i,board)
		for en in enemies:
			if i.bullethits(board.matrix, bullets)==1:
				bullets.remove(i)
				break
	x4 = jetpacker.check_in_canvas(board)
	x4 = jetpacker.check_in_canvas(board)
	config.savemando(jetpacker,obj_config,board)
	for i in bullets:
		if i.xcoo <= 499:
			i.move(board.matrix)
	x3 += 1
	jetpacker.check_enemy_collision(board)
	# jetpacker.check_magent(board)
	jetpacker.check_not_collision_down(board.matrix, obj_config,board)
	jetpacker.check_not_collision_up(board.matrix, obj_config,board)
	if jetpacker.xcoo >= 400:
		D1.reprintdragon(jetpacker)
		D1.movement(jetpacker)
		D1.onboard = True
		
		if x3 % 15 == 1:
			x4 = DragonFire(jetpacker)
			D2.append(x4)
		for i in D2:
			i.move(board.matrix, jetpacker, board)

	if (board.matrix[jetpacker.ycoo - 1][jetpacker.xcoo + 1] == "*"):
		print("GAME OVER")
		quit()

	

	if (jetpacker.xcoo > 497 or not D1.living()):
		print('\033[0;0H', end='')
		os.system('clear')

		print("NOICE!")

		break
