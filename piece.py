import math
import numpy
class piece:
    def __init__(self,vertexes):
        self.vertexes = vertexes
        self.angles = []
        for i,vertex in enumerate(vertexes):
            vec_front = vertexes[(i + 1) % len(vertexes)] - vertex
            vec_back = vertex - vertexes[(i - 1 + len(vertexes)) % len(vertexes)]
            inner_product = numpy.dot(vec_front,vec_back)
            angle = math.acos(inner_product / (numpy.linalg.norm(vec_front) * numpy.linalg.norm(vec_back)))
            self.angles.append(angle)
        print("角度 度",[numpy.rad2deg(i) for i in self.angles])

    def is_on_grid(self):
        return numpy.allclose(self.vertexes,numpy.floor(self.vertexes))

    def is_overlapped(self,another,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        pass

    def merge(self):
        print("Yuelia35 Test")

    def rotate(self):
        print("PaperyKettleAsata TEST")

    def flip(self):
        self.vertexes[:,0]*=-1
        self.vertexes[:,0]-=min(self.vertexes[:,0])