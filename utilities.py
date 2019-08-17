from abc import ABCMeta, abstractmethod
from constants import *

class Drawing(metaclass=ABCMeta):
    def __init__(self, *args):
        self.coordinates = args

    @abstractmethod
    def paint(self):    pass


class Canvas(Drawing):
    def paint(self):
        width, height = self.coordinates
        topBotLine = HORIZONTAL_LINE+HORIZONTAL_LINE * width+HORIZONTAL_LINE+'\n'
        space = ' ' * width
        with (open('output.txt', 'w')) as file:
            file.write(topBotLine)
            for i in range(height):
                file.write(VERTICAL_LINE+space+VERTICAL_LINE+'\n')
            file.write(topBotLine)


class Line(Drawing):
    def paint(self):
        x1, y1, x2, y2 = self.coordinates
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        horizonFlag = True if y1 == y2 else False
        root = []
        result = []
        with (open('output.txt')) as file:
            for offset, line in enumerate(file):
                lineList = list(line)
                if horizonFlag and offset == y1:
                    if x1 > x2:
                        x1, x2 = x2, x1
                    for i in range(x1, x2+1):
                        lineList[i] = CHARACTER_X
                elif not horizonFlag and offset in range(y1, y2+1):
                    lineList[x1] = CHARACTER_X
                root.append(lineList)     
        for i in root:
            i = ''.join(i)
            result.append(i)
        result = ''.join(result)
        with (open('output.txt', 'w')) as file:
            file.write(result)


class Rectangle(Drawing):
    def paint(self):
        x1, y1, x2, y2 = self.coordinates
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        crd1, crd2, crd3, crd4 = (x1, y1), (x2, y1), (x1, y2), (x2, y2)
        line = Line()
        for args in (crd1, crd2), (crd2, crd4), (crd4, crd3), (crd3, crd1):
            argsArray = []
            for setArgs in args:
                for i in setArgs:
                    argsArray.append(i)
            argsArray = tuple(argsArray)
            line.__init__(*argsArray)
            line.paint()


class Bucket(Drawing):    pass


if __name__ == '__main__':
    c = Canvas(20, 20)
    c.paint()
    l = Line(6, 2, 2, 2)
    l.paint()
    l2 = Line(2, 2, 2, 4)
    l2.paint()
    r = Rectangle(20, 1, 17, 3)
    r.paint()
