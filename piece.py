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
        """
		ピースの頂点がグリッド上に存在するかどうか判定します
		"""
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

    def merge(self,another,self_vertex1,another_vertex1):
        dx = self.vertexes[self_vertex1,0] - another.vertexes[another_vertex1,0]
        dy = self.vertexes[self_vertex1,1] - another.vertexes[another_vertex1,1]
        for i in another.vertexes:
            another.vertexes[0] += dx
            another.vertexes[1] += dy
        #以下Cwiseはself視点
        Cwiseself = self_vertex1 + 1
        CwiseA = another_vertex1 - 1
        if Cwiseself >= self.vertexes.shape[0]:
            Cwiseself = 0
        if CwiseA < 0:
            CwiseA = another.vertexes.shape[0] -1
        samelistS = []
        samelistA = []
        while (self.vertexes[Cwiseself] == another.vertexes[CwiseA]).all():
            samelistS.append(Cwiseself)
            samelistA.append(CwiseA)
            Cwiseself += 1
            CwiseA -= 1
            if Cwiseself >= self.vertexes.shape[0]:
                Cwiseself = 0
            if CwiseA < 0:
                CwiseA = another.vertexes.shape[0] - 1
        aCwiseself = self_vertex1 - 1
        aCwiseA = another_vertex1 + 1
        if aCwiseself < 0:
            aCwiseself = self.vertexes.shape[0] -1
        if aCwiseA >= another.vertexes.shape[0]:
            aCwiseA = 0
        while (self.vertexes[aCwiseself] == another.vertexes[aCwiseA]).all():
            samelistS.append(aCwiseself)
            samelistA.append(aCwiseA)
            aCwiseself -= 1
            aCwiseA += 1
            if aCwiseself < 0:
                aCwiseself = self.vertexes.shape[0] -1
            if aCwiseA >= another.vertexes.shape[0]:
                aCwiseA = 0
        samelistS.append(self_vertex1)
        samelistA.append(another_vertex1)
        bond = []
        SA = 0
        num = 0
        while True:
            if SA == 0:
                if num in samelistS:
                    if (self.angles[num] + another.angles[samelistA[samelistS.index(num)]] == 360) or (self.angles[num] + another.angles[samelistA[samelistS.index(num)]] == 180):
                        num = samelistA[samelistS.index(num)] + 1
                        SA = 1
                        if num >= another.vertexes.shape[0]:
                            num = 0
                    else:
                        bond.append(self.vertexes[num])
                        num = samelistA[samelistS.index(num)] + 1
                        SA = 1
                        if num >= another.vertexes.shape[0]:
                            num = 0
                else:
                    bond.append(self.vertexes[num])
                    num += 1
                    if num >= self.vertexes.shape[0]:
                        num = 0
            else:
                if num in samelistA:
                    if (another.angles[num] + self.angles[samelistS[samelistA.index(num)]] == 360) or (another.angles[num] + self.angles[samelistS[samelistA.index(num)]] == 180):
                        num = samelistS[samelistA.index(num)] + 1
                        SA = 0
                        if num >= self.vertexes.shape[0]:
                            num = 0
                    else:
                        bond.append(another.vertexes[num])
                        num = samelistS[samelistA.index(num)] + 1
                        SA = 0
                        if num >= self.vertexes.shape[0]:
                            num = 0
                else:
                    bond.append(another.vertexes[num])
                    num += 1
                    if num >= another.vertexes.shape[0]:
                        num = 0
            if (SA == 0) and (num == 0):
                break
            
        return piece(numpy.array(bond))

    def rotate(self):
        print("PaperyKettleAsata TEST")

    def flip(self):
        self.vertexes[:,0]*=-1
        self.vertexes[:,0]-=min(self.vertexes[:,0])