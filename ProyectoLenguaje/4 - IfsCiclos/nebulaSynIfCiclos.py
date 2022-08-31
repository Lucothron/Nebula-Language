#Lucas Ortiz Duhart - A00826544
#Analizador de Lexico y Sintaxis
#    • NEBULA •

import ply.lex as lex
import ply.yacc as yacc
import sys
from nebulaLex import tokens
from nebulaFunctions import *
import os
import codecs
import re

dimensions = []
dimType = 0

#---DECLARATION---

def p_START(p):
    '''
    START : V PROC PROGRAM X PEND
    '''
    print("\t***NO SYNTAX ERRORS***")
    #printQuad()
    #print(variables)
    execQuad()
    print(variables)
    #print(procedures)

#---VARIABLES---

def p_X(p):
    '''
    X : V P S
    '''

def p_V_DEF(p):
    '''
    V : DEF VARAUX X
    '''

def p_VARAUX(p):
    '''
    VARAUX : ID AS VARTYPE
    '''
    global dimType
    if p[1] not in variables.keys():
        variables[p[1]] = [p[3], dimType]
        dimType = 0
    else:
        print("\tVARIABLE ALREADY EXISTS")

def p_V_LET(p):
    '''
    V : LET VARASSIGN X
    '''

def p_VARASSIGN(p):
    '''
    VARASSIGN : VARID EQUAL E
    '''
    opers.append('=')
    genQuad()

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

def p_V_EMPTY(p):
    '''
    V : EMPTY
    '''

#---PROCEDURES---

def p_P_SUB(p):
    '''
    P : CALL SUBAUX X
    '''

def p_SUBAUX(p):
    '''
    SUBAUX : ID
    '''
    subStart(p[1])

def p_PROC(p):
    '''
    PROC : PROCEDURE PROCAUX LCURL X RCURL PROCAUX2 PROC
    | 
    '''

def p_PROCAUX(p):
    '''
    PROCAUX : ID
    '''
    procStart(p[1])

def p_PROCAUX2(p):
    '''
    PROCAUX2 :
    '''
    procEnd()

def p_P_INP(p):
    '''
    P : IN INPAUX X
    '''

def p_INPAUX(p):
    '''
    INPAUX : LPAREN VARID RPAREN
    '''
    quadInp()

def p_P_PRINT(p):
    '''
    P : PRINT PRINTAUX X
    '''

def p_PRINTAUX(p):
    '''
    PRINTAUX : LPAREN VAR RPAREN
    '''
    quadPrint()

def p_PRINTAUX2(p):
    '''
    PRINTAUX : LPAREN APOS ID APOS RPAREN
    '''
    quadPrint2(p[3])

def p_P_EMPTY(p):
    '''
    P : EMPTY
    '''

#---STATEMENTS

def p_S_IF(p):
    '''
    S : IF IFAUX LCURL X RCURL IFAUX2 X
    '''

def p_IFAUX(p):
    '''
    IFAUX : LPAREN LOGE RPAREN
    '''
    ifStart()

def p_IFAUX2(p):
    '''
    IFAUX2 : IFELSE
    | IFAUX3
    '''

def p_IFAUX3(p):
    '''
    IFAUX3 :
    '''
    ifEnd()

def p_S_IFELSE(p):
    '''
    IFELSE : ELSEAUX LCURL X RCURL IFAUX3
    '''

def p_ELSEAUX(p):
    '''
    ELSEAUX : ELSE
    '''
    elseStart()

def p_S_WHILE(p):
    '''
    S : WHILE WHILEAUX LCURL X RCURL WHILEAUX2 X
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
    S : DO DOAUX LCURL X RCURL WHILE DOAUX2 X
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
    S : FOR FORAUX LCURL X RCURL FORAUX2 X
    '''

def p_FORAUX(p):
    '''
    FORAUX : LPAREN FORASSIGN COMMA LOGE RPAREN
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

def p_VARTYPE(p):
    '''
    VARTYPE : INT
    | FLOAT
    | VECDEF
    | MATDEF
    | CUBEDEF
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
    | CUBEE
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

def p_DIMTYPE(p):
    '''
    DIMTYPE : INT
    | FLOAT
    '''
    global dimType
    dimType = p[1]

def p_VECDEF(p):
    '''
    VECDEF : VEC LBRACK NINT RBRACK OF TYPE DIMTYPE
    '''
    p[0] = p[1]
    opers.append('vec')
    dimQuad(p[3], 0, 0)

def p_MATDEF(p):
    '''
    MATDEF : MAT LBRACK NINT COMMA NINT RBRACK OF TYPE DIMTYPE
    '''
    p[0] = p[1]
    opers.append('mat')
    dimQuad(p[3], p[5], 0)

def p_CUBEDEF(p):
    '''
    CUBEDEF : CUBE LBRACK NINT COMMA NINT COMMA NINT RBRACK OF TYPE DIMTYPE
    '''
    p[0] = p[1]
    opers.append('cube')
    dimQuad(p[3], p[5], p[7])

def p_VECTOR(p):
    '''
    VECTOR : ID LBRACK NUMTYPE RBRACK
    '''

def p_MATRIX(p):
    '''
    MATRIX : ID LBRACK NUMTYPE COMMA NUMTYPE RBRACK
    '''

def p_CUBE(p):
    '''
    CUBEE : ID LBRACK NUMTYPE COMMA NUMTYPE COMMA NUMTYPE RBRACK
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
    | VECTOR
    | MATRIX
    | CUBEE
    | ID
    '''
    print(p[1])
    varT = type(p[1])
    if varT == str:
        if p[1] in variables.keys():
            operators.append(p[1])
    else:
        operators.append(p[1])

    print(operators)

def p_VARF(p):
    '''
    F : NFLOAT
    '''
    print('float')
    print(p[1])
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