class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame

    def search_360deg_corner(self):
        print("kumataro TEST")

    def search_match_pieces(self):
        """枠にはまるピースを探索し、リストにまとめて返します。
        """
        pass

    def ranking(self,pieces):
        """枠にはまるピースのリストを評価値順にソートします。
        

        pieces: 
            pieceのリスト
        """
        pass

    def marge_pieces(self,pieces):
        """枠にはまるピースのリストを枠と結合し、リストにまとめて返します。

        pieces: 
            pieceのリスト(frame)
        """
        pass

    def dfs_corner(self,frame,depth):
        """角の深さ優先探索を行います

        frame: piece
            フレーム
        depth:
            深さ
        """

        match_frames=marge_pieces(ranking(search_match_pieces()))#結合可能なピースを評価値順にソートし、枠と結合する
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