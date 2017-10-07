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
import copy
root_problem.merge_history=[]
root_problem.merge_history.append((copy.deepcopy(root_problem.frame),root_problem.pieces[0],0,1,0,1))
root_problem.frame.vertexes[0]=numpy.array([5,5])
root_problem.pieces.pop(0)

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
