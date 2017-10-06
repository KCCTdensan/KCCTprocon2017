import tkinter
import numpy
import threading

class GUI(threading.Thread):
    def draw_history(self,problem):
        """
        ピース結合の履歴(手順)を描画します．

        problem: problem
        """
        zoom=self.zoom_scale.get()
        self.history_depth.configure(to=(len(problem.merge_history)-1))
        self.draw_piece(problem.merge_history[self.history_depth.get()][0],zoom,5,50*zoom)
        self.draw_piece(problem.merge_history[self.history_depth.get()][1],zoom,200,50*zoom)


    def draw_piece(self,piece,zoom,x,y):
        self.canvas.create_polygon([[(p[0] + x) * zoom,p[1] * zoom+y] for p in piece.vertexes],fill="",outline="black")

        self.canvas.create_rectangle((piece.vertexes[0][0] + x) * zoom,piece.vertexes[0][1] * zoom+y,(piece.vertexes[0][0] + x) * zoom + 4,piece.vertexes[0][1] * zoom + 4+y,fill="blue")
        self.canvas.create_rectangle((piece.vertexes[1][0] + x) * zoom,piece.vertexes[1][1] * zoom+y,(piece.vertexes[1][0] + x) * zoom + 4,piece.vertexes[1][1] * zoom + 4+y,fill="yellow")

        for i,vert in enumerate(piece.vertexes):
            self.canvas.create_text((vert[0]+x)*zoom,vert[1]*zoom+y,text=i,font=("MS gothic", "10"),fill="blue")

    def draw(self,zoom):
        zoom = float(zoom)
        self.canvas.delete(tkinter.ALL)
        x = 5
        for piece in self.problem.pieces:
            self.draw_piece(piece,zoom,x,10)
            x+=numpy.amax(piece.vertexes,axis=0)[0] + 1
        self.draw_piece(self.problem.frame,zoom,5,50*zoom)

    def __init__(self,problem):
        threading.Thread.__init__(self)
        self.problem = problem

        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", lambda :self.root.quit())

        self.zoom_scale = tkinter.Scale(self.root, label = '倍率', orient = 'h',
               from_ = 2, to = 20, command = self.draw,resolution=0.1)
        self.canvas = tkinter.Canvas(self.root, scrollregion=("0", "0",  "10000",  "0"),width = 1000, height = 500)
        self.canvas_scrollbar = tkinter.Scrollbar(self.root, orient = 'h', command = self.canvas.xview)
        self.canvas.configure(xscrollcommand = self.canvas_scrollbar.set)
        
        self.history_depth = tkinter.Scale(self.root, label = '履歴', orient = 'h',
               from_ = 0, to = 0, command = self.draw_history)

        self.zoom_scale.pack(fill="x")
        self.history_depth.pack(fill="x")
        self.canvas.pack(fill="both")
        self.canvas_scrollbar.pack(fill="x",side="bottom")

        self.start()

    def run(self):

        self.draw(2)

        self.root.mainloop()