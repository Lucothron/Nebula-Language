from ply import *
import ply.lex as lex
import ply.yacc as yacc
import sys

keywords = (
    'PROGRAM','PEND','SUBPROCEDURE','SUBEND','END','LET',
    'DIM','AS','IN','INT','FLOAT','VEC','MAT',
    'PRINT','IF','THEN','ELSE','ENDIF','WHILE',
    'WEND','DO','LOOP','FOR','NEXT','GOSUB',
)

tokens = keywords + (
    'EQUAL','PLUS','MINUS','MULT','POWER','DIV','LPAREN',
    'RPAREN','LBRACK','RBRACK','LT','LE','GT','GE','EQ','NE',
    'COLON','COMMA','AND','OR','NOT','NINT','NFLOAT','ID','COMMENT'
)

t_ignore = ' \t\r\f\v'

t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_POWER = r'\^'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_COLON = r':'
t_COMMA = r','

def t_NINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_error(t):
    print("ILLEGAL CHARACTER %s" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()