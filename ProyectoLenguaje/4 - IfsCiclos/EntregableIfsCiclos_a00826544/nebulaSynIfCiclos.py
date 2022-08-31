#Lucas Ortiz Duhart - A00826544
#Analizador de Lexico y Sintaxis
#    • ☼ NEBULA ☼ •

import ply.lex as lex
import ply.yacc as yacc
import sys
from nebulaLex import tokens
from nebulaFunctions import *
import os
import codecs
import re

#---DECLARATION---

def p_START(p):
    '''
    START : PROGRAM V P S PEND
    '''
    print("\t***NO SYNTAX ERRORS***")
    printQuad()
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
    S : IF IFAUX LCURL V S RCURL IFAUX2 IFELSE V S
    '''

def p_IFAUX(p):
    '''
    IFAUX : LPAREN LOGE RPAREN
    '''
    ifStart()

def p_IFAUX2(p):
    '''
    IFAUX2 : 
    '''
    ifEnd()

def p_S_IFELSE(p):
    '''
    IFELSE : ELSE LCURL V S RCURL ELSEAUX
    |
    '''

def p_ELSEAUX(p):
    '''
    ELSEAUX : 
    '''
    elseEnd()

def p_S_WHILE(p):
    '''
    S : WHILE WHILEAUX LCURL V S RCURL WHILEAUX2 V S
    '''

def p_WHILEAUX(p):
    '''
    WHILEAUX : LPAREN LOGE RPAREN
    '''
    jumps.append(quadLoc)
    whileStart()

def p_WHILEAUX2(p):
    '''
    WHILEAUX2 : 
    '''
    whileEnd()

def p_S_DO(p):
    '''
    S : DO DOAUX LCURL V S RCURL WHILE DOAUX2 V S
    '''

def p_DOAUX(p):
    '''
    DOAUX : 
    '''
    doStart()

def p_DOAUX2(p):
    '''
    DOAUX2 : LPAREN LOGE RPAREN
    '''
    doEnd()

def p_S_FOR(p):
    '''
    S : FOR FORAUX LCURL V S RCURL FORAUX2 V S
    '''

def p_FORAUX(p):
    '''
    FORAUX : LPAREN FORASSIGN COMMA E RPAREN
    '''
    forStart()

def p_FORAUX2(p):
    '''
    FORAUX2 : 
    '''
    forEnd()

def p_FORASSIGN(p):
    '''
    FORASSIGN : VARID EQUAL E
    '''
    forQuad()

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
    opers.append('=')
    genQuad()

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
    opers.append(p[2])
    genQuad()

def p_E1(p):
    '''
    E : T
    '''

def p_T(p):
    '''
    T : T MULT F
    | T DIV F
    '''
    opers.append(p[2])
    genQuad()

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
    opers.append(p[2])
    genQuad()

def p_LOGF_LE(p):
    '''
    LOGF : VAR LE VAR
    '''
    opers.append(p[2])
    genQuad()

def p_LOGF_GT(p):
    '''
    LOGF : VAR GT VAR
    '''
    opers.append(p[2])
    genQuad()

def p_LOGF_GE(p):
    '''
    LOGF : VAR GE VAR
    '''
    opers.append(p[2])
    genQuad()

def p_LOGF_EQ(p):
    '''
    LOGF : VAR EQ VAR
    '''
    opers.append(p[2])
    genQuad()

def p_LOGF_NE(p):
    '''
    LOGF : VAR NE VAR
    '''
    opers.append(p[2])
    genQuad()

def p_LOGF1(p):
    '''
    LOGF : LPAREN LOGE RPAREN
    '''

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
#print(testRes)