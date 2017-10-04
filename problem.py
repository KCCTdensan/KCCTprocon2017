class problem:
        def __init__(self,pieces,frame):
                self.pieces=pieces
                self.frame=frame
        def serach_360deg_corner(self):
                pass

        def calc_eval_value(self,piece_vertexes):
                """ 結合するピースの位置に対する評価値を返します。

                piece_vertexes:
                   ピースの各頂点の座標の配列

                評価値は、枠の各頂点の座標とピースの各頂点の座標が重複する数で表されます。
                各頂点の座標は枠に対して正確な位置である必要があります。
                """
                return len(set(map(tuple,self.frame.vertexes))&set(map(tuple,piece_vertexes)))