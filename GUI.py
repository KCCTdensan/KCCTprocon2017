import tkinter
import numpy

def draw_piece(problem):
    ZOOM = 10

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width = 1000, height = 500)
    x = 0
    for piece in problem.pieces:
        canvas.create_polygon([[(p[0] + x) * ZOOM ,p[1] * ZOOM] for p in piece.vertexes])
        x+=numpy.amax(piece.vertexes,axis=0)[0] + 1
    canvas.pack()
    root.mainloop()