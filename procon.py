import re
import math
import numpy
import threading

import GUI
import problem

#is_overlappedデバッグ
#import piece
#a=piece.piece(numpy.array([[0,0],[10,0],[10,10],[0,10]]))
#b=piece.piece(numpy.array([[0,0],[10,10],[0,10]]))
#print(a.is_overlapped(b,0,3,0,2))

import QR
root_problem=problem.problem(*QR.read_QR())

#GUIデバッグ
root_problem.merge_history=[(root_problem,root_problem.pieces[0],0,1,0,1)]
import copy
TEST_next_problem=copy.deepcopy(root_problem)
TEST_next_problem.pieces.pop(0)
TEST_next_problem.merge_history=[(root_problem,root_problem.pieces[0],0,1,0,1),(TEST_next_problem,TEST_next_problem.pieces[1],0,1,0,1)]

gui=GUI.GUI(root_problem)

#GUIデバッグ
gui.draw_history(TEST_next_problem)

def search():
    #TODO:探索処理はここに
    pass
searching_thread=threading.Thread(target=search) 
searching_thread.start()


gui.root.mainloop()
depth_max=0