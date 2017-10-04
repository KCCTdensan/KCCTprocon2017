import re
import math
import numpy

import GUI
from problem import problem
from piece import piece
import QR
root_problem=problem(*QR.read_QR())
root_piece=piece(numpy.array([(0,64),(0,0),(46,59),(46,64)]))
root_problem.pieces.append(root_piece)
print(root_problem.calc_eval_value(root_piece.vertexes))
gui=GUI.GUI(root_problem)