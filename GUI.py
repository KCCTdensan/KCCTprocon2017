import tkinter
import numpy

class GUI():
    def draw(self,zoom):
        zoom = float(zoom)
        self.canvas.delete(tkinter.ALL)
        x = 0
        for piece in self.problem.pieces:
            self.canvas.create_polygon([[(p[0] + x) * zoom,p[1] * zoom] for p in piece.vertexes])
            x+=numpy.amax(piece.vertexes,axis=0)[0] + 1
        self.canvas.create_polygon([[p[0] * zoom,(p[1] + 30) * zoom] for p in self.problem.frame.vertexes])

    def __init__(self,problem):
        self.problem = problem
        self.root = tkinter.Tk()

        self.zoom_scale = tkinter.Scale(self.root, label = '倍率', orient = 'h',
               from_ = 2, to = 20, command = self.draw,resolution=0.1)
        self.canvas = tkinter.Canvas(self.root, scrollregion=("0", "0",  "10000",  "0"),width = 1000, height = 500)
        self.canvas_scrollbar = tkinter.Scrollbar(self.root, orient = 'h', command = self.canvas.xview)
        self.canvas.configure(xscrollcommand = self.canvas_scrollbar.set)

        self.zoom_scale.pack(fill="x")
        self.canvas.pack(fill="both")
        self.canvas_scrollbar.pack(fill="x",side="bottom")

        self.draw(2)

        self.root.mainloop()