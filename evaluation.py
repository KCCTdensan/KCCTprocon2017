class evaluation:
    def __point_in_rect(pointr1,pointr2,pointp):
        if pointr1[0]<=pointr2[0]:
            if not((pointr1[0]<=pointp[0])and(pointp[0]<=pointr2[0])):
                return False
        if pointr2[0]<=pointr1[0]:
            if not((pointr2[0]<=pointp[0])and(pointp[0]<=pointr1[0])):
                return False
        if pointr1[1]<=pointr2[1]:
            if not((pointr1[1]<=pointp[1])and(pointp[1]<=pointr2[1])):
                return False
        if pointr2[1]<=pointr1[1]:
            if not((pointr2[1]<=pointp[1])and(pointp[1]<=pointr1[1])):
                return False        
        return True

    def __point_on_line(pointl1,pointl2,pointp):
        if((pointp[0]==pointl1[0]and pointp[1]==pointl1[1])or(pointp[0]==pointl2[0]and pointp[1]==pointl2[1])):
            return True
        if not evaluation.__point_in_rect(pointl1,pointl2,pointp):
            return False
        if (pointl1[0]==pointp[0]and pointl2[0]==pointp[0])or(pointl1[1]==pointp[1]and pointl2[1]==pointp[1]):
            return True
        return(((pointl2[0]-pointl1[0])/(pointp[0]-pointl1[0]))==((pointl2[1]-pointl1[1])/(pointp[1]-pointl1[1])))

    def __linea_on_lineb(pointla1,pointla2,pointlb1,pointlb2):
        return(evaluation.__point_on_line(pointlb1,pointlb2,pointla1)and evaluation.__point_on_line(pointlb1,pointlb2,pointla2))

    def calc_num_of_overlapped_lines(frame_vertexes,piece_vertexes):
        """枠の各辺とピースの各辺が重なる数を返します。

        frame_vertexes:
            枠の各頂点の座標の配列
        piece_vertexes:
            ピースの各頂点の座標の配列
            
        frameとpiece_vertexesに渡す配列の座標は(x,y)で表され、順番になっている必要があります。
        また、piece_vertexesに渡す各頂点の座標は枠(frame)に対して正確な位置である必要があります。
        """
        ret=0
        verf=len(frame_vertexes)
        verp=len(piece_vertexes)
        for i in range(verf):
            for j in range(verp):
                if evaluation.__linea_on_lineb(piece_vertexes[j],piece_vertexes[(j+1)%verp],frame_vertexes[i],frame_vertexes[(i+1)%verf]):
                    ret+=1
        return ret

    def calc_num_of_matched_vertexes(frame_vertexes,piece_vertexes):
        """枠の各頂点の座標とピースの各頂点の座標が重なる数を返します。
        
        frame_vertexes:
            枠の各頂点の座標の配列
        piece_vertexes:
            ピースの各頂点の座標の配列

        frameとpiece_vertexesに渡す配列の座標は(x,y)で表される必要があります。
        また、piece_vertexesに渡す各頂点の座標は枠(frame)に対して正確な位置である必要があります。
        """
        return len(set(map(tuple,frame_vertexes))&set(map(tuple,piece_vertexes)))

    def calc_eval_value(frame_vertexes,piece_vertexes):
        """枠に対するピースの位置の評価値を返します。

        frame_vertexes:
            枠の各頂点の座標の配列
        piece_vertexes:
            ピースの各頂点の座標の配列
            
        評価値は[枠の各辺とピースの各辺が重なる数]+[枠の各頂点の座標とピースの各頂点の座標が重なる数]
        frameとpiece_vertexesに渡す配列の座標は(x,y)で表され、順番になっている必要があります。
        また、piece_vertexesに渡す各頂点の座標は枠(frame)に対して正確な位置である必要があります。
        """
        return evaluation.calc_num_of_matched_vertexes(frame_vertexes,piece_vertexes)+evaluation.calc_num_of_overlapped_lines(frame_vertexes,piece_vertexes)