#---STACKS & VARS---

variables = {}
operators = []
opers = []
quad = []
jumps = []
temps = ['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10']
tempCont = 0
quadLoc = 0

#---QUADRUPLE GENERATION---

def printQuad():
    global quadLoc
    for i in range(quadLoc):
        print(str(i) + ' ' + quad[i])

def genQuad():
    global tempCont
    global quadLoc
    op = opers.pop()
    op2 = operators.pop()
    op1 = operators.pop()

    if op == '=':
        quadString = str(op) + ' ' + str(op2) + ' ' + str(op1)
    else:
        quadString = str(op) + ' ' + str(op1) + ' ' + str(op2) + ' ' + str(temps[tempCont])
        operators.append(temps[tempCont])
        tempCont += 1

    quad.append(quadString)

    quadLoc += 1

#---IF---

def ifStart():
    global quadLoc
    jumps.append(quadLoc)
    quad.append('gotoF ' + str(operators[-1]) + ' _')

    quadLoc += 1

def ifEnd():
    global quadLoc
    jumpTo = jumps.pop()
    jumps.append(quadLoc)
    quad.append('goto ' + '_')

    quadLoc += 1
    rellenar(jumpTo, quadLoc)

def elseEnd():
    jumpTo = jumps.pop()
    rellenar(jumpTo, quadLoc)

    # jumpTo = jumps.pop()
    # rellenar(jumpTo, quadLoc)

def rellenar(D, cont):
    relleno = quad[D]
    relleno = relleno.replace("_", str(cont))
    quad[D] = relleno

#---WHILE---

def whileStart():
    global quadLoc
    jumps.append(quadLoc)
    quad.append('gotoF ' + str(operators[-1]) + ' _')

    quadLoc += 1

def whileEnd():
    jumpTo = jumps.pop()
    retornar(jumpTo, quadLoc)

def retornar(f, cont):
    retorno = quad[f]
    retorno = retorno.replace("_", str(cont))
    quad[f] = retorno

#---DO WHILE---

def doStart():
    jumps.append(quadLoc)

def doEnd():
    global quadLoc
    quad.append('gotoF ' + str(operators[-1]) + ' ' + str(jumps.pop()))

    quadLoc += 1

#---FOR---

def forQuad():
    global quadLoc
    exp1 = operators.pop()
    id = operators[-1]

    quad.append('= ' + str(exp1) + ' ' + str(id))

    quadLoc += 1

def forStart():
    global quadLoc
    global tempCont
    exp2 = operators.pop()
    id = operators[-1]
    jumps.append(quadLoc)

    quad.append('<= ' + str(id) + ' ' + str(exp2) + ' ' + temps[tempCont])
    operators.append(temps[tempCont])

    tempCont += 1
    quadLoc += 1

    forGoto()

def forGoto():
    global quadLoc
    quad.append('gotoF ' + str(operators.pop()) + ' _')

    quadLoc += 1

def forEnd():
    global quadLoc
    retorno = jumps.pop()

    quad.append('goto ' + str(retorno))

    quadLoc += 1
    
    rellena = quad[retorno + 1]
    rellena = rellena.replace('_', str(quadLoc))
    quad[retorno + 1] = rellena