#Lucas Ortiz Duhart - A00826544
#Analizador de Lexico y Sintaxis

import ply.lex as lex
import ply.yacc as yacc
import sys
from nebulaLex import tokens
import os
import codecs
import re

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('left', 'POWER'),
)

#---DECLARATION---

def p_START(p):
    '''
    START : PROGRAM V P S PEND
    '''
    print("\tNO SYNTAX ERRORS")

#---VARIABLES---

def p_V_DIM(p):
    '''
    V : DIM ID AS VARTYPE V
    '''

def p_V_LET(p):
    '''
    V : LET ID EQUAL VAR V S
    '''

def p_V_EMPTY(p):
    '''
    V : EMPTY
    '''

#---PROCEDURES---

def p_P_SUB(p):
    '''
    P : SUBPROCEDURE LPAREN ID RPAREN V P S END
    '''

def p_P_INP(p):
    '''
    P : IN LPAREN NUMTYPE RPAREN S
    '''

def p_P_PRINT(p):
    '''
    P : PRINT LPAREN NUMTYPE RPAREN S
    '''

def p_P_EMPTY(p):
    '''
    P : EMPTY
    '''

#---STATEMENTS

def p_S_IF(p):
    '''
    S : IF LPAREN RELEXPR RPAREN THEN S IFELSE END S
    '''

def p_S_IFELSE(p):
    '''
    IFELSE : ELSE THEN S
    |
    '''

def p_S_WHILE(p):
    '''
    S : WHILE LPAREN RELEXPR RPAREN S WEND S
    '''

def p_S_DO(p):
    '''
    S : DO COLON S WHILE LPAREN RELEXPR RPAREN S
    '''

def p_S_FOR(p):
    '''
    S : FOR LPAREN RELEXPR RPAREN S END S
    '''

def p_S_OPERATION(p):
    '''
    S : O
    '''

def p_S_EMPTY(p):
    '''
    S : EMPTY
    '''

#---RESOURCES---

def p_VARTYPE(p):
    '''
    VARTYPE : INT
    | FLOAT
    | VECDEF
    | MATDEF
    '''

def p_NUMTYPE(p):
    '''
    NUMTYPE : ID
    | NINT
    | NFLOAT
    '''

def p_VAR(p):
    '''
    VAR : NINT
    | NFLOAT
    | VECTOR
    | MATRIX
    | ID
    '''

def p_VECDEF(p):
    '''
    VECDEF : VEC LBRACK RBRACK
    '''

def p_MATDEF(p):
    '''
    MATDEF : MAT LBRACK RBRACK
    '''

def p_VECTOR(p):
    '''
    VECTOR : LBRACK NUMTYPE RBRACK
    '''

def p_MATRIX(p):
    '''
    MATRIX : LBRACK NUMTYPE COMMA NUMTYPE RBRACK
    '''

def p_RELEXPR(p):
    '''
    RELEXPR : VAR LT VAR
    | VAR LE VAR
    | VAR GT VAR
    | VAR GE VAR
    | VAR EQ VAR
    | VAR NE VAR
    '''

def p_O_EQUAL(p):
    '''
    O : O EQUAL O
    '''

def p_O_MATHTIER1(p):
    '''
    O : O PLUS TIER1
    | O MINUS TIER1
    '''

def p_O_MATHTIER2(p):
    '''
    TIER1 : TIER1 MULT TIER2
    | TIER1 DIV TIER2
    '''

def p_O_MATHTIER3(p):
    '''
    TIER2 : LPAREN O RPAREN
    '''

def p_O_T1(p):
    '''
    O : TIER1
    '''

def p_O_T2(p):
    '''
    TIER1 : TIER2
    '''

def p_O_T3(p):
    '''
    TIER2 : VAR
    '''

def p_EMPTY(p):
    '''
    EMPTY : 
    '''
    pass

def p_error(p):
    print("\tSYNTAX ERROR", p)
    print("\tERROR ON LINE: "+str(p.lineno))

#cargar archivo de prueba
test = os.getcwd()+"\\test.txt"
fp = codecs.open(test, "r", "utf-8")
rdFile = fp.read()
fp.close()
parser = yacc.yacc()
testRes = parser.parse(rdFile)
print(testRes)