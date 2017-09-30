import numpy as np

class problem:
        def __init__(self,pieces,frame):
                self.pieces=pieces
                self.frame=frame
        def serach_360deg_corner(self):
                pass

        def calc_eval_value(self,piece_vertexes):
                return len(set(map(tuple(self.frame)))&map(tuple(piece_vertexes)))