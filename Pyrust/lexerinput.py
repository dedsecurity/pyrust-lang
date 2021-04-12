import math
import os

print("Pyrust 1.0.0 (April 1 2021, 15:36:02)")

while True:
    string = input('\033[32mpyrust> \033[m')

    pi = ""

    if string == "pi":
        print(math.pi)
    elif string == "exit":
        break
    elif string == "print":
        print("<built-in function print>")
    elif string == "cls":
        os.system("cls")
    elif string == "import __hello__":
        print("Hello World")
    elif string == "print()":
        p = input("")
        print(f"'{p}'")
        
    symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',', '+', '-', '*'] # single-char keywords
    other_symbols = ['\\', '/*', '*/'] # multi-char keywords
    keywords = ['public', 'class', 'void', 'main', 'String', 'int','input','print']
    num = ['0','1','2','3','4','5','6','7','8','9']
    KEYWORDS = symbols + other_symbols + keywords + num

    white_space = ' '
    lexeme = ''

    for i,char in enumerate(string):
        if char == '*':
            if string[i-1] == '/':
                lexeme += '/*'
            elif string[i+1] == '/':
                lexeme += '*/'
            else:
                lexeme += '*'
        elif char == '/':
            if string[i+1] != '*' and string[i-1] != '*':
                lexeme += '/'
            else:
                continue
        else:
            if char != white_space:
                lexeme += char # adding a char each time
            if (i+1 < len(string)): # prevents error
                if string[i+1] == white_space or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
                    if lexeme != '':
                        print(lexeme.replace('\n', '<newline>'))
                        lexeme = ''


