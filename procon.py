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
root_problem=copy.copy(root_problem)
root_problem.pieces=copy.copy(root_problem.pieces)
root_problem.pieces.pop(0)
root_problem.merge_history.append((root_problem,root_problem.pieces[1],0,1,0,1))

gui=GUI.GUI(root_problem)

#GUIデバッグ
gui.draw_history(root_problem)

def search():
    #TODO:探索処理はここに
    pass
searching_thread=threading.Thread(target=search) 
searching_thread.start()


gui.root.mainloop()
depth_max=0