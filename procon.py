import re
import math
import numpy

from piece import piece
import GUI

class problem:
        def __init__(self,pieces,frame):
                self.pieces=pieces
                self.frame=frame

import QR
QR.read_QR()

pieces_data="8:5 7 1 6 5 4 5 0 2 6 0:3 0 0 4 4 0 5:5 2 5 0 5 5 0 5 8 2 8:3 6 2 0 7 0 0:5 6 5 0 0 13 0 9 2 9 5:4 0 0 4 0 4 5 0 3:8 5 1 5 0 7 0 7 3 0 3 0 0 2 0 2 1:4 0 0 3 0 3 3 0 3:9 11 0 11 2 13 2 13 0 16 0 16 10 0 10 0 3 4 0".split(":")
pieces=[]
for piece_data_str in pieces_data[1:]:
        coordinate_data_str=re.match(r"\d+ ((\d+ \d+ ?)+)",piece_data_str).group(1)
        coordinates_str=re.findall(r"(\d+) (\d+) ?",coordinate_data_str)
        vertexes=numpy.array([numpy.array((int(x),int(y))) for x,y in coordinates_str])
        print(vertexes)
        pieces.append(piece(vertexes))








root_problem=problem(pieces[:-1],pieces[-1])
GUI.draw_piece(root_problem)