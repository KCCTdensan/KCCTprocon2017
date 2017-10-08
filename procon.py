import re
import math
import numpy
import threading

import GUI
import problem
import piece

#is_overlappedデバッグ
#import piece
#a=piece.piece(numpy.array([[0,0],[10,0],[10,10],[0,10]]))
#b=piece.piece(numpy.array([[0,0],[10,10],[0,10]]))
#print(a.is_overlapped(b,0,3,0,2))

import QR
root_problem=problem.problem(*QR.read_QR())

gui=GUI.GUI(root_problem)
root_problem.gui_api=gui

#GUIデバッグ
#import copy
#root_problem.merge_history.append((copy.deepcopy(root_problem.frame),root_problem.pieces[0],0,1,0,1))
#root_problem.frame.vertexes[0]=numpy.array([5,5])
#root_problem.pieces.pop(0)
#root_problem.merge_history.append((copy.deepcopy(root_problem.frame),root_problem.pieces[0],0,1,0,1))
#gui.draw_history(root_problem)

def search():
    root_problem.dfs_corner([(root_problem.frame,[])],[],0)
searching_thread=threading.Thread(target=search) 
searching_thread.start()

gui.root.mainloop()
depth_max=0

testpiece_ver=numpy.array([(0,0),(10,0),(10,10),(0,10)])
print(piece.piece.is_cross(testpiece_ver,testpiece_ver[0],testpiece_ver[-1]+testpiece_ver[1],0) )