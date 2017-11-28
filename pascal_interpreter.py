
INTEGER, PLUS, MINUS, EOF = "INTEGER", "PLUS", "MINUS", "EOF"

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value


    def __str__(self):
        return f"Token({self.type}, {self.value})"


    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text=None):
        self.text = text
        self.pos = 0
        self.current_token = None


    def error(self):
        raise Exception("parsing error")


    def get_next_token(self):
        text = self.text
        # check for eof or eol
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        current_char = text[self.pos]
        if current_char.isdigit():
            try:
                token = Token(INTEGER, int(current_char))
                self.pos += 1
                return token
            except Exception:
                self.error()
        elif current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)
        # if we get here the character wasn't recognized
        self.error()


    def consume_token(self, type_expected):
        if self.current_token.type == type_expected:
            self.current_token = self.get_next_token()
        else:
            self.error()


    def parse(self):
        self.pos = 0 # restart position each time parse is called (each user input)
        r_oper = ""
        self.current_token = self.get_next_token()
        l_oper = str(self.current_token.value)
        self.consume_token(INTEGER)
        op = None
        for _ in range(len(self.text) - 1):
            elem = self.current_token
            if elem.type == INTEGER and op is None:
                l_oper += str(elem.value)
                self.consume_token(INTEGER)
            elif elem.type == INTEGER and op is not None:
                r_oper += str(elem.value)
                self.consume_token(INTEGER)
            else:
                op = self.current_token
                self.consume_token(PLUS)
        return int(l_oper) + int(r_oper)


def main():
    interpreter = Interpreter()
    while True:
        try:
            user_input = input("my_calc>")
        except EOFError:
            break
        if user_input in ["exit", "quit", "q"]:
            break
        if not user_input:
            continue
        interpreter.text = user_input
        print(interpreter.parse())


if __name__ == "__main__":
    main()