import math
import numpy
import copy
class piece:
    def __init__(self,vertexes):
        self.vertexes = vertexes
        self.angles = []
        for i,vertex in enumerate(vertexes):
            vec_front = vertexes[(i + 1) % len(vertexes)] - vertex
            vec_back = vertexes[(i - 1 + len(vertexes)) % len(vertexes)] - vertex
            inner_product = numpy.dot(vec_front,vec_back)
            angle = math.acos(inner_product / (numpy.linalg.norm(vec_front) * numpy.linalg.norm(vec_back)))
            if self.is_cross(vertexes,vertex,vec_front + vec_back,i) == False:
                angle = 2 * math.pi - angle
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

    def move(self,anotherD,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        """
        anotherピースを移動させる
        selfとanotherのvertex1が重なりかつ指定する4つの頂点が一直線上になるように移動する
        回転がうまく行けば多分これもうまくいく

        anotherD:piece
            ピース
        self_vertex1:
            selfピースの頂点の番号 anotherピースの頂点another_vertex1と重なるように移動する
        self_vertex2:
            selfピースのもう一つの頂点の番号
        another_vertex1:
            anotherピースの頂点の番号
        another_vertex2:
            anotherピースのもう一つの頂点の番号
        """
        #変数の書き換えを防ぐ
        another = anotherD
        #回転
        another = another.rotate(self,self_vertex1,self_vertex2,another_vertex1,another_vertex2)
        #selfとanotherの差を取得
        dx = self.vertexes[self_vertex1,0] - another.vertexes[another_vertex1,0]
        dy = self.vertexes[self_vertex1,1] - another.vertexes[another_vertex1,1]
        #移動
        another.vertexes[:,0] += dx
        another.vertexes[:,1] += dy
        return another

    def merge(self,anotherD,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        """
        selfのピースとanotherのピースを結合
        selfとanotherのvertex1が重なりかつ指定する4つの頂点が一直線上になるように結合する
        回転がうまく行けばこれもうまく行ける

        anotherD:piece
            ピース
        self_vertex1:
            selfピースの頂点の番号 anotherピースの頂点another_vertex1と重なるように結合する
        self_vertex2:
            selfピースのもう一つの頂点の番号
        another_vertex1:
            anotherピースの頂点の番号
        another_vertex2:
            anotherピースのもう一つの頂点の番号
        """
        #まず移動
        another = self.move(anotherD,self_vertex1,self_vertex2,another_vertex1,another_vertex2)

        #テスト
        #print(another.vertexes[0,0],anotherD.vertexes[0,0])

        #ピース移動後に重複する頂点を探してselfの頂点はsamelistS,anotherの頂点はsamelistAに
        #CwiseはClockwise(外回り)aCwiseはantiClockwise(内回り)の略
        #以下Cwiseはself視点(anotherにとってのaCwiseになる)
        #vertex1からCwise,aCwise各方向に重複する頂点がなくなるまで探す

        #(a)Cwiseself/Aは判定を行う頂点の番号 この番号の頂点が重複したらsamelist行き
        Cwiseself = self_vertex1 + 1
        CwiseA = another_vertex1 - 1
        #ピースの頂点の数を超えないように
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
        #頂点も重複するので
        samelistS.append(self_vertex1)
        samelistA.append(another_vertex1)
        #接着(結合)開始
        bond = []
        #self.vertexes[0]から順に外回りに新ピースの頂点を記録していく
        #記録する頂点がselfかanotherか 0はself 1はanother
        SA = 0
        #記録する頂点番号
        num = 0
        while True:
            if SA == 0:
                #selfの頂点を記録する
                #頂点が重複しているなら
                if num in samelistS:
                    '''
                    if (self.angles[num] + another.angles[samelistA[samelistS.index(num)]] == 360) or (self.angles[num] + another.angles[samelistA[samelistS.index(num)]] == 180):
                        num = samelistA[samelistS.index(num)] + 1
                        SA = 1
                        if num >= another.vertexes.shape[0]:
                            num = 0
                    else:
                    '''
                    #新ピースの頂点一覧行き(仮)
                    #そしてanotherの頂点を記録し始める
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
                #anotherの頂点を記録する
                #頂点が重複しているなら
                if num in samelistA:
                    '''
                    if (another.angles[num] + self.angles[samelistS[samelistA.index(num)]] == 360) or (another.angles[num] + self.angles[samelistS[samelistA.index(num)]] == 180):
                        num = samelistS[samelistA.index(num)] + 1
                        SA = 0
                        if num >= self.vertexes.shape[0]:
                            num = 0
                    else:
                    '''
                    #新ピースの頂点一覧行き(仮)
                    #そしてselfの頂点を記録し始める
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
            #self[0]に戻ってきたら(新ピースに必要な頂点をすべて記録したら)break
            if (SA == 0) and (num == 0):
                break
        #角度がpiなど頂点としての体を成していない頂点を削除

        print("D E B U G",bond)#ただのarray[[x y],[],[],[].....]じゃないとだめなのに中にまたarrayが入ってる
        ret = piece(numpy.array(bond))
        invalid = []
        for i in range(ret.vertexes.shape[0]):
            print(ret.angles[i])
            if (ret.angles[i] == math.pi) or (ret.angles[i] == math.pi * 2) or (ret.angles[i] == 0):
                invalid.append(i)
        invalid.reverse()
        for i in invalid:
            ret.angles = numpy.delete(ret.angles,i)
            ret.vertexes = numpy.delete(ret.vertexes,i,0)
        #お出口は後ろ側です(結合済みピースを返します)
        return ret

    def rotate(self,another,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
        #辺のベクトルをもとめる！
        vecter_self = self.vertexes[self_vertex2]-self.vertexes[self_vertex1];
        vecter_another = another.vertexes[another_vertex2]-another.vertexes[another_vertex1];

        #ベクトルの内積をもとめる！・・・は説明変数無しに1行にまとめる!
        #ベクトルの大きさをもとめる！・・・も説明変数無しに1行にまとめる!
        #θをもとめる！
        rotate_angle = math.acos(numpy.dot(vecter_self,vecter_another) / (numpy.linalg.norm(vecter_self) * numpy.linalg.norm(vecter_another)))

        #回転行列をもとめる！
        rotate_matrix = numpy.matrix([
            [numpy.cos(rotate_angle) , -numpy.sin(rotate_angle)],
            [numpy.sin(rotate_angle) , numpy.cos(rotate_angle)]
            ])

        #回転行列で回転後の座標をもとめる！
        shifted_another_piece=copy.deepcopy(another)
        shifted_another_piece.vertexes=shifted_another_piece.vertexes-(another.vertexes[another_vertex1]-self.vertexes[self_vertex1])
        shifted_another_piece.vertexes=(rotate_matrix*shifted_another_piece.vertexes.T).T
        return shifted_another_piece

    def flip(self):
        self.vertexes[:,0]*=-1
        self.vertexes[:,0]-=min(self.vertexes[:,0])

    def is_cross(self,vertexes,origin,vec_sum,e):
        count = 0
        vertexes_shifted=vertexes-origin
        len_shifted = len(vertexes_shifted)
        vec_sum = vec_sum*100
        for i in range(1,len_shifted - 2):
            vertex_1 = vertexes_shifted[(e + i) % len_shifted]
            vertex_2 = vertexes_shifted[(e + i + 1) % len_shifted]
            vertex_3 = vertexes_shifted[(e + i + 2) % len_shifted]
            ax = 0
            ay = 0
            bx = vec_sum[0]
            by = vec_sum[1]
            cx = vertex_1[0]
            cy = vertex_1[1]
            dx = vertex_2[0]
            dy = vertex_2[1]
            ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
            tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
            tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
            td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
            #通常交差
            if (tc * td < 0) and (ta * tb < 0):
                count+=1
            #頂点パターン1-3
            if (td == 0):
                #交差パターン3
                if(ta == 0 and tb == 0 and tc == 0 and td == 0):
                    count = count
                #交差パターン2
                elif(self.is_cross_2(ax,ay,bx,by,cx,cy,vertex_3[0],vertex_3[1])):
                    count = count
                #交差パターン1
                else:
                    count +=1
        return count % 2 == 0

    def is_cross_2(self,ax,ay,bx,by,cx,cy,dx,dy):
        ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
        tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
        tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
        td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

        return (tc * td < 0) and (ta * tb < 0)