class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame

    def calc_num_of_tangent_point(self,piece_vertexes):
        """
        """
        vernum=len(piece_vertexes)
        sides=[]
        for i in piece_vertexes:
            sides+=[[piece_vertexes[(i+1)%vernum][0]-piece_vertexes[i][0],piece_vertexes[(i+1)%vernum][0]-piece_vertexes[i][0]]]


    def calc_eval_value(self,piece_vertexes):
        """結合するピースの位置に対する評価値を返します。

        piece_vertexes:
            ピースの各頂点の座標の配列

        評価値は、枠の各頂点の座標とピースの各頂点の座標が重複する数で表されます。
        各頂点の座標は枠に対して正確な位置である必要があります。
        """
        return calc_num_of_match_vertexes(piece_vertexes)

    def search_match_pieces(self):
        """枠にはまるピースを探索し、評価値をつけ、リストにまとめて返します。
        
        戻り値:
            pieceと評価値のタプルのリスト

        戻り値は以下のようにpieceオブジェクトと評価値が含まれるタプルのリストになります。
        [(pieceオブジェクト0,評価値0),(pieceオブジェクト1,評価値1),...,(pieceオブジェクトn,評価値n)]
        なおリストはソートされません。
        """
        ret=[]
        #...
        return ret

    def sorting(self,pieces):
        """枠にはまるピースのリストを評価値順に降順にソートします。
        

        pieces: 
            pieceと評価値のタプルのリスト
        戻り値:
            pieceと評価値のタプルのリスト
        """
        return [sorted(pieses, key = lambda t: t[1], reverse = True)]

    def merge_pieces(self,pieces):
        """枠にはまるピースのリストを枠と結合し、リストにまとめて返します(frame)。

        pieces: 
            pieceのリスト
        戻り値:
            pieceのリスト(frame)
        """
        frame=[]
        for P in pieces:
            frame +=[self.frame.merge(P)]

        return frame

    def dfs_corner(self,frames,depth):
        """角の深さ優先探索を行います

        frames: piece
            評価値が同じフレームのリスト
        depth:
            深さ
        戻り値: bool
        """

        for i in frames:
            match_frames=merge_pieces(sorting(search_match_pieces(frames[i])))#結合可能なピースを評価値順にソートし、枠と結合する
        
        if len(match_frames)==0: #結合可能なピースが無い、行き止まり
            pass
		#	if パズル完成:
        #       GUI更新
		#		return true
        #   if depth > depth_max:
        #       GUI更新
		#	return false

        #再帰部
        #same_value_frames=[] #評価値が等しいframeを格納するリスト
		#for i in match_frames: #結合後のframeを全て見る
        #   if match_frames[i][1]!=match_frames[i+1][1]: #評価値が等しいframeを格納し終えたとき
        #       if dfs(same_value_frames,depth+1)==true #それらを引数にして再帰
        #           return true
        #   else:
        #       same_value_frames.append(match_frames[i]) #評価値が等しいframeを追加していく
		#return false

