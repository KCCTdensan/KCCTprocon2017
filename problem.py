class problem:
    def __init__(self,pieces,frame):
        self.pieces = pieces
        self.frame = frame
    def serach_360deg_corner(self):
        print("kumataro TEST")

    def dfs_corner(self,frame):
        pass
		#結合可能なケースを探す
		#if ケースが無い:
		#	if パズル完成:
		#		return true
		#	else
		#		return false
		#評価値をつける
		#評価値順にソート
		#for i in ケースの数
		#	if dfs(self,self.frame.marge())=true
		#		return true;
		#return false