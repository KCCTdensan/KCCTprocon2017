import math
import numpy
import copy
class piece:
        def __init__(self,vertexes):
                self.vertexes=vertexes;
                self.length=[]
                for i,vertex in enumerate(vertexes):
                        self.length.append(numpy.linalg.norm(vertexes[(i+1)%len(vertexes)]-vertex))
                print("length",self.length)
                self.angles=[]
                self.inner_products=[]
                for i,vertex in enumerate(vertexes):
                        vec_front=vertexes[(i+1)%len(vertexes)]-vertex
                        vec_back=vertex-vertexes[(i-1+len(vertexes))%len(vertexes)]
                        inner_product=numpy.dot(vec_front,vec_back)
                        angle=math.acos(inner_product/(numpy.linalg.norm(vec_front)*numpy.linalg.norm(vec_back)))
                        self.inner_products.append(inner_product)
                        self.angles.append(angle)
                print("角度 ラジアン",self.angles)
                print("角度 度",[numpy.rad2deg(i) for i in self.angles])
                print("内積",self.inner_products)

        def is_on_grid(self):
                pass

        def is_overlapped(self,another,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
            shifted_another_piece = copy.deepcopy(another)
            shifted_another_piece.vertexes-=another.vertexes[another_vertex1] - self.vertexes[self_vertex1]

            print("自ピース=",self.vertexes)
            print("他ピース=",shifted_another_piece.vertexes)

            self_search_vertex2_list=self.vertexes[1:]+[self.vertexes[0]]
            for i,self_search_vertex1 in enumerate(self.vertexes):
                self_search_vertex2=self_search_vertex2_list[i]
                for another_search_vertex1 in shifted_another_piece.vertexes:
                    if numpy.cross(self_search_vertex2 - self_search_vertex1,another_search_vertex1 - self_search_vertex1) < 0 : 
                        return True
            return False

        def merge(self):
                pass
