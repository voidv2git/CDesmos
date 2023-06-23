import Desmos

def Read(fileName):
    print("Reading Source.")
    return open(fileName, "r").read() + "\n"

def Error(message, exitCode):
    print(message)
    exit(exitCode)

def Lex(source):
    print("Lexing Source.")
    tokens = []
    token = ""
    isString = False

    i = 0
    while i < len(source): 
        if source[i] == " " or source[i] == "\n":
            if not isString:
                tokens.append(token)
                token = ""
        elif source[i] == "#":
            while source[i] != "\n":
                i += 1
        elif source[i].isupper():
            c = source[i]

            token += source[i]
            token += "_{"
            i += 1

            while source[i] != "_":
                token += source[i]
                i += 1

                if i == len(source):
                    Error(f"Subscript Not Found On Variable '{c}'.", 1)

            token += "}"
        else:
            token += source[i]

            if source[i] == '"':
                if isString:
                    tokens.append(token)
                    token = ""
                
                isString = not isString
    
        i += 1

    return tokens

def Parse(tokens):
    print("Parsing Tokens.")
    i = 0

    while i < len(tokens):
        if tokens[i] == "define":
            pass
        elif tokens[i] == "include":
            pass
        elif tokens[i].startswith('"') and tokens[i].endswith('"'):
            pass
        elif tokens[i] != "":
            Error(f"Unknown Token '{tokens[i]}'.", 1)

        i += 1

def Compile(tokens):
    api = Desmos.API()
    defined = {}

    i = 0
    id = 1

    while i < len(tokens):
        if tokens[i] == "define":
            defined[tokens[i + 1]] = tokens[i + 2]
            i += 2
        elif tokens[i] == "include":
            fileName = tokens[i + 1][1:-1]
            del tokens[i:i+2]
            Compile(Lex(Read(fileName)) + tokens)
            return
        elif tokens[i].startswith('"') and tokens[i].endswith('"'):
            latex = tokens[i][1:-1]

            for define in defined:
                latex = latex.replace(define, defined[define][1:-1])

            api.SetExpression(str(id), latex.replace(" ", ""))
            id += 1

        i += 1

    api.Compile("index.html")
    print("Compilation Finished.")