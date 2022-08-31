#Lucas Ortiz Duhart - A00826544
#Analizador de Lexico y Sintaxis

import ply.lex as lex
import ply.yacc as yacc
import sys
from nebulaLex import tokens
import os
import codecs
import re

variables = {}
operators = []
quad = []
temps = ['T1','T2','T3','T4','T5','T6','T7','T8']
tempCont = 0

def genQuad(op):
    global tempCont
    op2 = operators.pop()
    op1 = operators.pop()

    quad.append(op)
    quad.append(op1)
    quad.append(op2)
    if op == '=':
        quad.append(op1)
    else:
        quad.append(temps[tempCont])
        operators.append(temps[tempCont])
        tempCont += 1

    print(quad)
    list.clear(quad)

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
    V : DIM VARAUX V
    '''

def p_V_LET(p):
    '''
    V : LET VARASSIGN V S
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
    S : IF LPAREN LOGE RPAREN LCURL V S RCURL IFELSE S
    '''

def p_S_IFELSE(p):
    '''
    IFELSE : ELSE LCURL S RCURL
    |
    '''

def p_S_WHILE(p):
    '''
    S : WHILE LPAREN LOGE RPAREN LCURL V S RCURL S
    '''

def p_S_DO(p):
    '''
    S : DO COLON V S WHILE LPAREN LOGE RPAREN S
    '''

def p_S_FOR(p):
    '''
    S : FOR LPAREN LOGE COMMA LOGE RPAREN LCURL V S RCURL
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

def p_VARAUX(p):
    '''
    VARAUX : ID AS VARTYPE
    '''
    if p[1] not in variables.keys():
        variables[p[1]] = p[3]
    else:
        print("\tVARIABLE ALREADY EXISTS")

def p_VARID(p):
    '''
    VARID : ID
    '''
    varT = type(p[1])
    if varT == str:
        if p[1] in variables.keys():
            operators.append(p[1])
        else:
            print("\tVARIABLE DOES NOT EXIST")
    else:
        operators.append(p[1])

def p_VARASSIGN(p):
    '''
    VARASSIGN : VARID EQUAL E
    '''
    operation = '='
    genQuad(operation)

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
    varT = type(p[1])
    if varT == str:
        if p[1] in variables.keys():
            operators.append(p[1])
        else:
            print("\tVARIABLE DOES NOT EXIST")
    else:
        operators.append(p[1])

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
    operation = p[2]
    genQuad(operation)

def p_E1(p):
    '''
    E : T
    '''

def p_T(p):
    '''
    T : T MULT F
    | T DIV F
    '''
    operation = p[2]
    genQuad(operation)

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
    varT = type(p[1])
    if varT == str:
        if p[1] in variables.keys():
            operators.append(p[1])
        else:
            print("\tVARIABLE DOES NOT EXIST")
    else:
        operators.append(p[1])

#---LOGICAL EXPRESSION---

# def p_LOGVAR(p):
#     '''
#     LOGVAR : LOGE
#     '''

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

def p_LOGF_LT(p):
    '''
    LOGF : VAR LT VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF_LE(p):
    '''
    LOGF : VAR LE VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF_GT(p):
    '''
    LOGF : VAR GT VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF_GE(p):
    '''
    LOGF : VAR GE VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF_EQ(p):
    '''
    LOGF : VAR EQ VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF_NE(p):
    '''
    LOGF : VAR NE VAR
    '''
    operation = p[2]
    genQuad(operation)

def p_LOGF1(p):
    '''
    LOGF : LPAREN LOGE RPAREN
    '''

# def p_RELEXPR(p):
#     '''
#     RELEXPR : LT
#     | LE
#     | GT
#     | GE
#     | EQ
#     | NE
#     '''

def p_error(p):
    print("\tSYNTAX ERROR", p)
    print("\tERROR ON LINE: "+str(p.lineno))

#---LOAD TEST FILE---
test = os.getcwd()+"\\test.txt"
fp = codecs.open(test, "r", "utf-8")
rdFile = fp.read()
fp.close()
parser = yacc.yacc()
testRes = parser.parse(rdFile)
print(testRes)