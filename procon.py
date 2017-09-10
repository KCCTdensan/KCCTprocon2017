import re
import math
import numpy

import GUI

class problem:
        def __init__(self,pieces,frame):
                self.pieces=pieces
                self.frame=frame

import QR
root_problem=problem(*QR.read_QR())
GUI.draw_piece(root_problem)