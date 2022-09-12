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
        for s in self.input:
            if self.current_state == State.s0:
                if s.isdigit() == True:
                    self.current_state = State.error
                    continue
                elif s == ' ' or s == '\n':
                    self.current_state = State.s0
                    continue
                elif s.isalpha() == True:
                    self.current_state = State.nxtlit
                    self.output.append(s)
                    continue
                else:
                    self.current_state = State.error
                    continue
            elif self.current_state == State.nxtlit:
                if s.isdigit() == True:
                    self.current_state = State.nxtlit
                    self.output.append(s)
                    continue
                elif s == ' ' or s == '\n':
                    self.current_state = State.s0
                    print('Token: '+''.join(self.output))
                    self.output.clear()
                    continue
                elif s.isalpha() == True:
                    self.current_state = State.nxtlit
                    self.output.append(s)
                    continue
                else:
                    self.current_state = State.error
                    continue
            elif self.current_state == State.error:
                print('Error: invalid character')
                if len(self.output) > 0: 
                    print('Token: '+''.join(self.output))
                self.output.clear()
                self.current_state = State.s0
                continue
        print('Token: '+''.join(self.output))
        self.output.clear()
        self.current_state = State.stop
        print('Successfully')


if __name__ == '__main__':
    input_symbols = []
    with open("Lab_1\\LB_IIPS\\Lb1\\lab_1.txt",'r') as f:
        for i in f.read():
            input_symbols.append(i)
    if len(input_symbols) > 0:
        lex = Lexer(input_symbols)
        lex.lexer()
    else:
        print('File is empty')