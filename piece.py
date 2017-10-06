import math
import numpy
import copy
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
        """枠selfに対して結合した時にピースが重なるか判定します

        another: piece
            ピース
        self_vertex1:
            枠の辺の頂点の番号，ピースの頂点 another_vertex1と重なる．
        self_vertex2:
            枠の辺のもうひとつの頂点の番号
        another_vertex1:
            ピースの辺の頂点の番号
        another_vertex2:
            ピースの辺のもうひとつの頂点の番号
        """
        shifted_another_piece_vertexes=another.vertexes-(another.vertexes[another_vertex1]-self.vertexes[self_vertex1])
        self_search_vertex2_list=numpy.concatenate((self.vertexes[1:],self.vertexes[0:1]))
        for i,self_search_vertex1 in enumerate(self.vertexes):
            self_search_vertex2=self_search_vertex2_list[i]
            if numpy.any(numpy.cross(self_search_vertex2- self_search_vertex1,shifted_another_piece_vertexes-self_search_vertex1)<0):
                return True
        return False

    def merge(self):
        print("Yuelia35 Test")

    def move(self,another,self_vertex,another_vertex):
        """枠(another)の頂点に合うようにピース(self)を平行移動

        another: piece
            ピース
        self_vertex1:
            結合するピースの頂点
        another_vertex1:
            結合する枠の頂点
        """
        moved_self_piece_vertexes = self.vertexes - (self.vertexes[self_vertex] - another.vertexes[another_vertex])

    def rotate(self):
        print("PaperyKettleAsata TEST")

    def flip(self):
        self.vertexes[:,0]*=-1
        self.vertexes[:,0]-=min(self.vertexes[:,0])