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
    ('left', 'MULT', 'DIV')
)

variables = {}

#---DECLARATION---

def p_START(p):
    '''
    START : PROGRAM V P S PEND
    '''
    print("\tNO SYNTAX ERRORS")
    print(variables)

#---VARIABLES---

def p_V_DIM(p):
    '''
    V : DIM ID AS VARTYPE V
    '''
    p[0] = ('LET', p[2], p[4])
    if p[2] not in variables.keys():
        variables[p[2]] = p[4]
    else:
        print("\tVARIABLE ALREADY EXISTS")

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
    P : SUBPROCEDURE LPAREN ID RPAREN V P S SUBEND
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
    S : IF LPAREN LOGE RPAREN THEN S IFELSE ENDIF S
    '''

def p_S_IFELSE(p):
    '''
    IFELSE : ELSE THEN S
    |
    '''

def p_S_WHILE(p):
    '''
    S : WHILE LPAREN LOGE RPAREN S WEND S
    '''

def p_S_DO(p):
    '''
    S : DO COLON S WHILE LPAREN LOGE RPAREN S
    '''

def p_S_FOR(p):
    '''
    S : FOR LPAREN LOGE COMMA LOGE RPAREN S
    '''

def p_S_OPERATION(p):
    '''
    S : E
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
    p[0] = p[1]

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
    VECDEF : VEC LBRACK VAR RBRACK
    '''
    p[0] = p[1]

def p_MATDEF(p):
    '''
    MATDEF : MAT LBRACK VAR RBRACK LBRACK VAR RBRACK
    '''
    p[0] = p[1]

def p_VECTOR(p):
    '''
    VECTOR : ID LBRACK NUMTYPE RBRACK
    '''

def p_MATRIX(p):
    '''
    MATRIX : ID LBRACK NUMTYPE COMMA NUMTYPE RBRACK
    '''

def p_RELEXPR(p):
    '''
    RELEXPR : LT
    | LE
    | GT
    | GE
    | EQ
    | NE
    '''

def p_EMPTY(p):
    '''
    EMPTY : 
    '''
    pass

#---MATH---

def p_E(p):
    '''
    E : E PLUS T
    | E MINUS T
    '''

def p_E1(p):
    '''
    E : T
    '''

def p_T(p):
    '''
    T : T MULT F
    | T DIV F
    '''

def p_T1(p):
    '''
    T : F
    '''

def p_F(p):
    '''
    F : LPAREN E RPAREN
    '''

def p_FVAR(p):
    '''
    F : NINT
    | NFLOAT
    | VECTOR
    | MATRIX
    | ID
    '''

#---LOGICAL EXPRESSION---

def p_LOGE(p):
    '''
    LOGE : LOGE OR LOGT
    '''

def p_LOGE1(p):
    '''
    LOGE : NOT LOGT
    | LOGT
    '''

def p_LOGT(p):
    '''
    LOGT : LOGT AND LOGF
    '''

def p_LOGT1(p):
    '''
    LOGT : LOGF
    '''

def p_LOGF(p):
    '''
    LOGF : VAR RELEXPR VAR
    '''

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