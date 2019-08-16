from abc import ABCMeta, abstractmethod
from constants import *

class Drawing(metaclass=ABCMeta):
    def __init__(self, *args):
        self.characters = args

    @abstractmethod
    def paint(self):    pass


class Canvas(Drawing):
    def paint(self):
        width, height = self.characters
        topBotLine = HOTIZONTAL_LINE+HOTIZONTAL_LINE * width+HOTIZONTAL_LINE+'\n'
        space = ' ' * width
        with (open('output.txt', 'w')) as file:
            file.write(topBotLine)
            for i in range(height):
                file.write(VERTICAL_LINE+space+VERTICAL_LINE+'\n')
            file.write(topBotLine)
            
            


class Line(Drawing):    pass


class Rectangle(Drawing):    pass


class Bucket(Drawing):    pass


if __name__ == '__main__':
    c = Canvas(20, 4)
    c.paint()
