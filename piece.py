import math
import numpy
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
            A = self_vertex1 - another_vertex1
            B = self_vertex2 - another_vertex2
            print(A)
            print(B)
            if numpy.allclose(A,B):
                vertex_increment = self_vertex1 - another_vertex1
            else:
                vertex_increment = self_vertex1 - another_vertex2

            another_piece = another
            self_piece = self

            if (vertex_increment >= 0).all():
                for vertex in another.vertexes:
                    another_piece.vertexes += vertex_increment
            else:
                for vertex in self.vertexes:
                    self_piece.vertexes += vertex_increment
            
            for i,self_search_vertex1 in enumerate(self_piece.vertexes):
                if (self_search_vertex1 != self_piece.vertexes[-1]).all():
                    self_search_vertex2 = self_piece.vertexes[i+1]
                else:
                    self_search_vertex2 = self_piece.vertexes[0]
                for k,another_search_vertex1 in enumerate(another_piece.vertexes):
                    if (another_search_vertex1 != another_piece.vertexes[-1]).all():
                        another_search_vertex2 = another_piece.vertexes[i+1]
                    else:
                        another_search_vertex2 = another_piece.vertexes[0]
                    t_a = (self_search_vertex1[0] - self_search_vertex2[0]) * (another_search_vertex1[1] - self_search_vertex1[1]) + (self_search_vertex1[1] - self_search_vertex2[1]) * (self_search_vertex1[0] - another_search_vertex1[0])
                    t_b = (self_search_vertex1[0] - self_search_vertex2[0]) * (another_search_vertex2[1] - self_search_vertex1[1]) + (self_search_vertex1[1] - self_search_vertex2[1]) * (self_search_vertex1[0] - another_search_vertex2[0])
                    t_c = (another_search_vertex1[0] - another_search_vertex2[0]) * (self_search_vertex1[1] - another_search_vertex1[1]) + (another_search_vertex1[1] - another_search_vertex2[1]) * (another_search_vertex1[0] - self_search_vertex1[0])
                    t_d = (another_search_vertex1[0] - another_search_vertex2[0]) * (self_search_vertex2[1] - another_search_vertex1[1]) + (another_search_vertex1[1] - another_search_vertex2[1]) * (another_search_vertex1[0] - self_search_vertex2[0])
                    if t_a * t_b < 0 and t_c * t_d < 0: return True
            return False

        def merge(self):
                pass