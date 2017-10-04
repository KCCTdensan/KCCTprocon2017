class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame

    def calc_eval_value(self,piece_vertexes):
        """ 結合するピースの位置に対する評価値を返します。

        piece_vertexes:
            ピースの各頂点の座標の配列

        評価値は、枠の各頂点の座標とピースの各頂点の座標が重複する数で表されます。
        各頂点の座標は枠に対して正確な位置である必要があります。
        """
        return len(set(map(tuple,self.frame.vertexes))&set(map(tuple,piece_vertexes)))

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
        """枠にはまるピースのリストを評価値順にソートします。
        

        pieces: 
            pieceと評価値のリスト
        戻り値:
            pieceのリスト
        """
        pass

    def marge_pieces(self,pieces):
        """枠にはまるピースのリストを枠と結合し、リストにまとめて返します(frame)。

        pieces: 
            pieceのリスト
        戻り値:
            pieceのリスト(frame)
        """
        pass

    def dfs_corner(self,frame,depth):
        """角の深さ優先探索を行います

        frame: piece
            フレーム
        depth:
            深さ
        戻り値: bool
        """

        match_frames=marge_pieces(sorting(search_match_pieces()))#結合可能なピースを評価値順にソートし、枠と結合する
		#if 結合可能なピースが無い:
		#	if パズル完成:
        #       GUI更新
		#		return true
		#	else
        #       if depth > depth_max
        #           GUI更新
		#		return false
		#for i in flames
		#	if dfs(self,frame,depth+1)=true
		#		return true;
		#return false

