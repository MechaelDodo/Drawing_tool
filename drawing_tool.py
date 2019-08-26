from modules.utilities import Canvas, Line, Rectangle, BucketFill
import sys

if __name__ == '__main__':
    C = Canvas()
    L = Line()
    R = Rectangle()
    B = BucketFill()
    paintDict = {'C': C, 'L': L, 'R': R, 'B': B, 'E': 'Exit'}
    inpStr = 'Enter the command (C - Canvas, L - Line, R - Rectangle, B - Bucket Fill,):'
    exitStr = '\n--Enter "E" to exit--'
    while True:
        print(exitStr)
        args = tuple(input(inpStr))
        
        try:
            command = paintDict[args[0]]
        except KeyError:
            print('This command does not exist', file=sys.stderr)
            continue
        if command == 'Exit':
            break
        try:
            args = (int(arg) if arg.isdigit() else arg for arg in ''.join(args[1:]).split())
            command.__init__(*args)
            command.paint()
        except (ValueError, TypeError)  as Er:
            if Er.__class__.__name__ == 'ValueError':
                print('ValueError:', Er, file=sys.stderr)
            else:
                print('TypeError', file=sys.stderr)
            
