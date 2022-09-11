from enum import Enum

class State(Enum):
    s0 = 'S0'
    nxtlit = 'nxtlit'
    error = 'error'
    stop = 'stop'
class Lexer:
    def __init__(self,input):
        self.current_state = State.s0
        self.input = input
        self.output = []
    def lexer(self):
        pass

if __name__ == '__main__':
    input_symbols = []
    with open("Lab_1\\LB_IIPS\\Lb1\\lab_1.txt",'r') as f:
        for i in f.read():
            input_symbols.append(i)
    lex = Lexer(input_symbols)
    lex.lexer()