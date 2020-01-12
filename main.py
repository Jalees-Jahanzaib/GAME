from board import Board
from boys import Boys
from jetpacker import Jet_Packer
objB=Board(30,500)

objB.create_board()
obj_jp = Jet_Packer(25,0,1)
obj_jp.starting_p(objB.matrix)
objB.printboard(70)