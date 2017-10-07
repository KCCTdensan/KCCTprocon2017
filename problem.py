import evaluation

class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame
        self.merge_history = []

    def search_match_pieces(self,frame):
        """枠にはまるピースを探索し、評価値をつけ、リストにまとめて返します。

        frame:
            フレームと結合履歴のタプル
        戻り値:
            piece,評価値,フレームの頂点1,フレームの頂点2,ピースの頂点1,ピースの頂点2のタプルのリスト

        戻り値は以下のようにpieceオブジェクトと評価値が含まれるタプルのリストになります。
        [(pieceオブジェクト0,評価値0),(pieceオブジェクト1,評価値1),...,(pieceオブジェクトn,評価値n)]
        なおリストはソートされません。
        """
        evaluation=evaluation()
        enable_pieces=[] #枠と結合可能なピース,結合する枠の頂点,結合するピースの頂点のタプルをここに格納
        for piece in self.pieces: #全てのピースをみる
            for frame_vertex in frame[0].vertexes: #フレームの頂点全てをみる
                for piece_vertex in piece.vertexes: #1ピースの頂点全てをみる

                    #回転→is_overlapped()→merge()→is_on_grid()     結合判定
                    #     ↑←frip()←←←↓                          結合判定 piece内で関数作るべき？

                    enable_pieces.append((piece,frame_vertex1,frame_vertex2,piece_vertex1,piece_vertex2))

        ret=[]
        for enable_piece in enable_pieces:
            ret.append((enable_piece[0],evaluation.calc_eval_value(frame[0],enable_piece[0].vertexes),enable_piece[1],enable_piece[2],enable_piece[3],enable_piece[4]))
        return ret

    def sorting(self,pieces):
        """枠にはまるピースのリストを評価値順に降順にソートします。
        

        pieces: 
            piece,評価値,フレームの頂点1,フレームの頂点2,ピースの頂点1,ピースの頂点2のタプルのリスト
        戻り値:
            piece,評価値,フレームの頂点1,フレームの頂点2,ピースの頂点1,ピースの頂点2のタプルのリスト
        """
        return sorted(pieces, key = lambda t: t[1], reverse = True)

    def merge_pieces(self,frame,pieces):
        """枠にはまるピースのリストを枠と結合し、リストにまとめて返します(frame)。
        frame:
            piece,結合履歴のタプル
        pieces: 
            piece,評価値,フレームの頂点1,フレームの頂点2,ピースの頂点1,ピースの頂点2のタプルのリスト
        戻り値:
            piece,評価値,結合履歴のタプルのリスト(frame)
        """
        frames=[]
        for P in pieces:
            frames += [frame[0].merge(P[0],P[2],p[4]),P[1],frame[1].append((frame[0],P[0],P[2],P[3],P[4],P[5]))]
        return frames

    def dfs_corner(self,frames,history,depth):
        """角の深さ優先探索を行います

        frames: piece
            フレームと結合履歴のタプルのリスト
        history:
            前のノードの結合履歴
        depth:
            深さ
        戻り値: bool
        """

        for frame in frames:
            match_frames=merge_pieces(frame,sorting(search_match_pieces(frame)))
            #結合可能なピースを評価値順にソートし、枠と結合する
        if len(match_frames)==0: #結合可能なピースが無い、行き止まり
            if depth==1000:#パズル完成(仮) 条件考える必要あり
                self.merge_history=history
                return true
            if depth > depth_max:
                self.merge_history=history
            return false

        #再帰部
        same_value_frames=[] #評価値が等しいframeを格納するリスト
        for i,match_frame in enumerate(match_frames): #結合後のframeを全て見る
            if match_frames[i][1]!=match_frames[i+1][1]: #評価値が等しいframeを格納し終えたとき
                if dfs(same_value_frames,same_value_frames[0][1],depth+1)==true: #それらを引数にして再帰
                    return true
            else:
                same_value_frames.append(match_frames[i]) #評価値が等しいframeを追加していく
        return false

