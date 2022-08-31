import ply.yacc as yacc
import ply.lex as lex
import sys


keywords = (
    'DIM', 'LET', 'PROGRAM', 'END'
)

tokens = keywords + (
    'EQUALS', 'PLUS', 'MINUS', 'MULT', 'POWER', 'DIV', 'LPAREN', 'RPAREN',
    'LT', 'LE', 'GT', 'GE', 'NE', 'ID', 'FLOAT'
)

t_ignore = r' '

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_POWER = r'\^'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'<>'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_FLOAT(t):
    r'\d+'
    t.value = float(t.value)
    return t

def t_error(t):
    print("ILLEGAL CHARACTER")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    #('right', 'UMINUS'),
)

def p_S(p):
    '''
    S : PROGRAM program END
    '''

def p_program(p):
    '''
    program : definition
    | command
    | operation
    '''

def p_dim(p):
    '''
    definition : DIM ID
    '''
    print("\tINPUT SUCCESFUL")

def p_let(p):
    '''
    command : LET ID EQUALS FLOAT
    '''
    print("\tINPUT SUCCESFUL")

def p_binaryOp(p):
    '''
    operation : ID PLUS ID
    | ID MINUS ID
    | ID MULT ID
    | ID DIV ID
    | ID POWER ID
    '''

def p_error(p):
    print("\tSYNTAX ERROR")

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)