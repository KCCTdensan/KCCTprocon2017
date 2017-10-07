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

    def search_match_pieces(self,frame):
        """枠にはまるピースを探索し、評価値をつけ、リストにまとめて返します。

        frame:
            枠
        戻り値:
            piece,評価値,フレームの頂点,ピースの頂点のタプルのリスト

        戻り値は以下のようにpieceオブジェクトと評価値が含まれるタプルのリストになります。
        [(pieceオブジェクト0,評価値0),(pieceオブジェクト1,評価値1),...,(pieceオブジェクトn,評価値n)]
        なおリストはソートされません。
        """
        enable_pieces=[] #枠と結合可能なピース,結合する枠の頂点,結合するピースの頂点のタプルをここに格納
        for piece in self.pieces: #全てのピースをみる
            for frame_vertex in frame.vertexes: #フレームの頂点全てをみる
                for piece_vertex in piece.vertexes: #1ピースの頂点全てをみる

                    #回転→is_overlapped()→merge()→is_on_grid()     結合判定
                    #     ↑←frip()←←←↓                          結合判定

                    enable_pieces.append((piece,frame_vertex,piece_vertex))

        ret=[]
        for enable_piece in enable_pieces:
            ret.append((enable_piece[0],calc_eval_value(enable_piece[0].vertexes),enable_piece[1],enable_piece[2]))
        return ret

    def sorting(self,pieces):
        """枠にはまるピースのリストを評価値順に降順にソートします。
        

        pieces: 
            pieceと評価値のタプルのリスト
        戻り値:
            pieceのリスト
        """
        return [piece for (piece, value) in sorted(pieses, key = lambda t: t[1], reverse = True)]

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

    def dfs_corner(self,frame,depth):
        """角の深さ優先探索を行います

        frame: piece
            フレーム
        depth:
            深さ
        戻り値: bool
        """

        match_frames=merge_pieces(sorting(search_match_pieces()))#結合可能なピースを評価値順にソートし、枠と結合する
		#if len(match_frames)==0: 結合可能なピースが無い
		#	if パズル完成:
        	#       	GUI更新
		#		return true
		#	else
        	#       if depth > depth_max:
        	#           	GUI更新
		#		return false
		#for i in match_frames
		#	if dfs(self,match_frames[i],depth+1)=true
		#		return true;
		#return false

