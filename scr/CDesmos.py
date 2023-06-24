from Interpreter import *
import sys

def Usage():
    print("USAGE: python CDesmos.py [Source] [Output]")

if len(sys.argv) == 3:
    tokens = Lex(Read(sys.argv[1]))
    Compile(tokens)
else:
    Usage()
