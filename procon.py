import re
import math
import numpy

import GUI
from problem import problem


import piece
a=piece.piece(numpy.array([[0,0],[10,0],[10,10],[0,10]]))
b=piece.piece(numpy.array([[0,0],[10,10],[0,10]]))
print(a.is_overlapped(b,1,2,0,2))
#b=piece.piece(numpy.array([[0,0],[10,10],[0,10]]))
#print(a.is_overlapped(b,1,2,0,2))
import datetime
start=datetime.datetime.today()
for i in range(1000):
    a.is_overlapped(b,1,2,0,2)
print(datetime.datetime.today()-start)


#import QR
#root_problem=problem(*QR.read_QR())
#root_problem.pieces.append(a)
#root_problem.pieces.append(b)
#gui=GUI.GUI(root_problem)