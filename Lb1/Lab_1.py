from enum import Enum
import re

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
    def S0(self,s):
        if s.isdigit() == True:
            self.current_state = State.error
            exit
        elif s == ' ' or s == '\n':
            self.current_state = State.s0
            exit
        elif s.isalpha() == True:
            self.current_state = State.nxtlit
            self.output.append(s)
            exit
        else:
            self.current_state = State.error
            exit
    def NXTLIT(self,s):
        if s.isdigit() == True:
            self.current_state = State.nxtlit
            self.output.append(s)
            exit
        elif s == ' ' or s == '\n':
            self.current_state = State.s0
            print('Token: '+''.join(self.output))
            self.output.clear()
            exit
        elif s.isalpha() == True:
            self.current_state = State.nxtlit
            self.output.append(s)
            exit
        else:
            self.current_state = State.error
            exit
    def ERROR(self):
        print('Error: invalid character')
        self.output.clear()
        self.current_state = State.s0
        exit

    def lexer(self):
        for s in self.input:
            match self.current_state:
                case State.s0:
                    self.S0(s)
                    continue
                case State.nxtlit:
                    self.NXTLIT(s)
                    continue
                case State.error:
                    self.ERROR(s)
                    continue
        print('Token: '+''.join(self.output))
        self.output.clear()
        self.current_state = State.stop
        print('Successfully')


if __name__ == '__main__':
    input_symbols = []
    with open("LB_IIPS\\Lb1\\lab_1.txt",'r') as f:
        for i in f.read():
            input_symbols.append(i)
    if len(input_symbols) > 0:
        lex = Lexer(input_symbols)
        lex.lexer()
    else:
        print('File is empty')