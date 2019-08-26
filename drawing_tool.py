from modules.utilities import Canvas, Line, Rectangle, BucketFill
import sys

if __name__ == '__main__':
    C = Canvas()
    L = Line()
    R = Rectangle()
    B = BucketFill()
    paintDict = {'C': C, 'L': L, 'R': R, 'B': B, 'E': 'Exit'}
    inpStr1 = 'Enter the command'
    inpStr2 = '(C - Canvas, L - Line, R - Rectangle, B - Bucket Fill,):'
    exitStr = '\n--Enter "E" to exit--'
    while True:
        print(exitStr)
        args = tuple(input(inpStr1+inpStr2))

        try:
            command = paintDict[args[0]]
        except KeyError:
            print('This command does not exist', file=sys.stderr)
            continue
        if command == 'Exit':
            break
        try:
            args = ''.join(args[1:]).split()
            args = (int(arg) if arg.isdigit() else arg for arg in args)
            command.__init__(*args)
            command.paint()
        except (ValueError, TypeError) as Er:
            if Er.__class__.__name__ == 'ValueError':
                print('ValueError:', Er, file=sys.stderr)
            else:
                print('TypeError', file=sys.stderr)
