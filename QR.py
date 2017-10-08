import os
import re
import numpy
from piece import piece
import glob

def read_QR():
    #f = os.popen("zbarcam --raw")
    f=[]
    #for file in glob.glob("C:\\Users\\admin\\Desktop\\IMG_*.JPG"):
    #    for st in os.popen("zbarimg --raw -q " + file ):
    #        print(file)
    #        f.append(st.split("\n")[0])
    f=["15:9 0 0 26 0 26 5 18 5 18 17 15 24 10 24 4 20 0 20:6 0 0 4 0 10 4 9 8 4 6 0 6:6 0 0 4 0 9 2 8 6 6 16 0 16:11 0 0 6 0 5 4 4 12 24 18 34 12 38 9 38 17 46 17 46 22 0 22:5 1 0 8 2 17 3 20 14 0 8:5 1 5 2 0 7 2 7 11 0 9:5 1 0 10 0 12 8 5 7 0 5:4 2 0 7 0 9 8 0 8:4 0 0 7 1 9 10 0 9:9 0 12 3 5 11 0 27 0 38 7 37 12 27 6 11 6 1 16:6 10 0 19 0 12 6 10 10 1 14 0 10:5 0 4 9 0 12 7 6 11 2 12:9 0 5 8 5 8 0 32 0 32 7 24 7 24 12 8 12 0 17:6 0 5 4 4 10 0 14 7 6 11 2 14:5 0 5 4 2 8 0 13 10 3 16", "15:10 0 10 2 6 9 0 16 0 26 6 25 10 24 15 22 24 7 24 3 17:4 0 2 4 0 9 9 5 12:10 0 0 15 0 13 9 20 11 35 13 42 12 52 9 52 17 5 17 5 9:8 0 7 8 7 8 0 31 0 31 5 16 19 11 19 0 12:4 2 0 7 2 7 11 0 9:5 2 0 9 3 9 12 5 11 0 9:5 1 0 10 1 12 9 7 8 0 5:5 1 5 2 0 7 0 9 10 0 9:4 0 0 12 3 15 11 0 9:4 0 0 5 1 8 11 0 9:7 0 15 15 1 34 0 42 0 42 5 23 5 1 20:6 0 0 10 0 10 6 12 12 3 13 1 5:5 0 15 22 0 36 0 24 6 16 15:5 0 1 9 0 14 8 10 9 3 11:4 0 2 7 0 10 9 3 10","8:4 0 0 6 0 6 6 0 6:4 0 0 6 0 9 5 2 6:4 0 1 7 0 10 7 5 9:5 0 3 4 2 9 0 13 9 3 12:5 27 0 27 4 19 4 0 5 0 0:7 0 17 12 17 12 9 8 0 27 0 27 22 0 22:6 0 0 25 0 25 18 6 18 3 11 0 6:5 8 6 20 0 25 0 25 15 0 15:8 0 0 100 0 100 64 73 64 73 59 46 59 46 64 0 64"]
    #f=["8:5 7 1 6 5 4 5 0 2 6 0:3 0 0 4 4 0 5:5 2 5 0 5 5 0 5 8 2 8:3 6 2 0 7 0 0:5 6 5 0 0 13 0 9 2 9 5:4 0 0 4 0 4 5 0 3:8 5 1 5 0 7 0 7 3 0 3 0 0 2 0 2 1:4 0 0 3 0 3 3 0 3:9 11 0 11 2 13 2 13 0 16 0 16 10 0 10 0 3 4 0"]
    pieces=[]
    for pieces_data in f:
        print(pieces_data)
        for piece_data_str in pieces_data.split(":")[1:]:
                coordinate_data_str=re.match(r"\d+ ((\d+ \d+ ?)+)",piece_data_str).group(1)
                coordinates_str=re.findall(r"(\d+) (\d+) ?",coordinate_data_str)
                vertexes=numpy.array([numpy.array((int(x),int(y))) for x,y in coordinates_str])
                print(vertexes)
                pieces.append(piece(vertexes))
        print("count",len(pieces))
    return pieces[:-1],pieces[-1]