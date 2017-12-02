# -*- encoding: utf-8 -*-

INTEGER, PLUS, MINUS, DIV, MULT = "INTEGER", "PLUS", "MINUS", "DIV", "MULT"
PLUS_SYM, MINUS_SYM, DIV_SYM, MULT_SYM = "+", "-", "/", "*"

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value


    def __str__(self):
        return f"Token({self.type},{self.value})"


    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text=None):
        self.text = text
        self.current_token = None
        self.final_expr = {"l_operand":"", "r_operand":"", "operator":""}


    def error(self):
        raise Exception("parsing error")


    def reset(self):
        self.current_token = None
        self.final_expr = {"l_operand": "", "r_operand": "", "operator": ""}


    def convert_to_token(self, current_char):
        if current_char.isdigit():
            token = Token(INTEGER, current_char)
            return token
        elif current_char == PLUS_SYM:
            token = Token(PLUS, PLUS_SYM)
            return token
        elif current_char == MINUS_SYM:
            token = Token(MINUS, MINUS_SYM)
            return token
        elif current_char == MULT_SYM:
            token = Token(MULT, MULT_SYM)
            return token
        elif current_char == DIV_SYM:
            token = Token(DIV, DIV_SYM)
            return token
        elif current_char.isspace():
            return None
        self.error() # if nothing of the above the character was not recognized


    def consume(self, current_char):
        self.current_token = self.convert_to_token(current_char)
        if self.current_token is None:
            pass
        else:
            if self.current_token.type == INTEGER and self.final_expr["operator"] == '':
                self.final_expr["l_operand"] += self.current_token.value
            elif self.current_token.type == INTEGER and self.final_expr["operator"] != '':
                self.final_expr["r_operand"] += self.current_token.value
            elif self.current_token.type == PLUS or self.current_token.type == MINUS or \
                    self.current_token.type == MULT or self.current_token.type == DIV:
                self.final_expr["operator"] = self.current_token.value


    def make_operation(self):
        if self.final_expr["operator"] == PLUS_SYM:
            op = int(self.final_expr["l_operand"]) + int(self.final_expr["r_operand"])
            print(op)
        elif self.final_expr["operator"] == MINUS_SYM:
            op = int(self.final_expr["l_operand"]) - int(self.final_expr["r_operand"])
            print(op)
        elif self.final_expr["operator"] == MULT_SYM:
            op = int(self.final_expr["l_operand"]) * int(self.final_expr["r_operand"])
            print(op)
        elif self.final_expr["operator"] == DIV_SYM:
            op = int(self.final_expr["l_operand"]) / int(self.final_expr["r_operand"])
            print(op)


    def eval(self):
        self.reset() # each new expression
        for i in range(len(self.text)):
            current_char = self.text[i]
            self.consume(current_char)
        self.make_operation()


def main():
    interpreter = Interpreter()
    while True:
        try:
            user_input = input("calculate> ")
            if user_input in ["q", "quit", "exit"]:
                break
            if not user_input:
                continue
            interpreter.text = user_input
            interpreter.eval()
        except EOFError:
            break


if __name__ == '__main__':
    main()