import re
import math
import numpy

import GUI
from problem import problem

import QR

from piece import piece

root_problem=problem(*QR.read_QR())
gui=GUI.GUI(root_problem)
test_piece=piece(numpy.array([(0.0,0.0),(1.0,1.0),(2.0,2.0),(3.0,3.0)]))
if test_piece.is_on_grid():
    print("aiueo")