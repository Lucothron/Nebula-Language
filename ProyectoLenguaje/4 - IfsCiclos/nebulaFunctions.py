#---STACKS & VARS---

variables = {}
dimVariables = {}
varSize = []
procedures = {}
operators = []
opers = []
quad = []
jumps = []
execP = []
temps = [
    'T1','T2','T3','T4','T5','T6','T7','T8','T9','T10',
    'T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'
        ]
T = {
    "T1": 0,
    "T2": 0,
    "T3": 0,
    "T4": 0,
    "T5": 0,
    "T6": 0,
    "T7": 0,
    "T8": 0,
    "T9": 0,
    "T10": 0,
    "T11": 0,
    "T12": 0,
    "T13": 0,
    "T14": 0,
    "T15": 0,
    "T16": 0,
    "T17": 0,
    "T18": 0,
    "T19": 0,
    "T20": 0,
}
tempCont = 0
quadLoc = 0

#---QUADRUPLE GENERATION---

def printQuad(): 
    global quadLoc
    quad.append('end')
    quadLoc += 1   
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

def dimQuad(x, y, z):
    global quadLoc
    op = opers.pop()
    
    if op == 'vec':
        quadString = str(op) + ' ' + str(x)
    elif op == 'mat':
        quadString = str(op) + ' ' + str(x) + ' ' + str(y)
    elif op == 'cube':
        quadString = str(op) + ' ' + str(x) + ' ' + str(y) + ' ' + str(z)
    
    quad.append(quadString)

    quadLoc += 1


#---SUBPROCEDURES---

def procStart(name):
    global quadLoc

    procedures[name] = quadLoc + 1

    jumps.append(quadLoc)
    quad.append('goto _')

    quadLoc += 1

def procEnd():
    global quadLoc
    quad.append('endproc')
    jumpTo = jumps.pop()
    
    rellenar(jumpTo, quadLoc + 1)

    quadLoc += 1

def subStart(name):
    global quadLoc

    if name in procedures:
        dir = procedures[name]
        quad.append('call ' + str(dir))

        quadLoc += 1
    
    else:
        print('PROCEDURE DOES NOT EXIST')
    
#---PRINT---

def quadPrint():
    global quadLoc
    op = operators.pop()
    quad.append('print ' + str(op))

    quadLoc += 1

def quadPrint2(thing):
    global quadLoc
    quad.append('print ' + str(thing))

    quadLoc += 1

#---READ---

def quadInp():
    global quadLoc
    op = operators.pop()
    quad.append('read ' + str(op))

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
    rellenar(jumpTo, quadLoc)

def elseStart():
    global quadLoc
    jumpTo = jumps.pop()
    quad.append('goto _')
    jumps.append(quadLoc)

    rellenar(jumpTo, quadLoc + 1)

    quadLoc += 1

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
    rellenar(jumpTo, quadLoc)

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
    jumps.append(quadLoc - 1)

    quad.append('gotoF ' + str(temps[tempCont - 1]) + ' _')

    operators.append(temps[tempCont])

    quadLoc += 1

def forEnd():
    global quadLoc
    retorno = jumps.pop()

    quad.append('goto ' + str(retorno))

    quadLoc += 1
    
    rellena = quad[retorno + 1]
    rellena = rellena.replace('_', str(quadLoc))
    quad[retorno + 1] = rellena

#---EXECUTION---

def execQuad():
    global quadLoc
    quad.append('end')
    quadLoc += 1
    PC = 0
    exec = True
    while(exec):
        #print(PC)
        statement = quad[PC]
        statement = statement.split()
        #print(statement)
        opCode = statement[0]

#       ---CALL---

        if opCode == 'call':
            dir = statement[1]

            execP.append(PC + 1)
            PC = int(dir)

#       ---ENDPROC---

        elif opCode == 'endproc':
            PC = int(execP.pop())

#       ---PRINT---

        elif opCode == 'print':
            var = statement[1]

            if var in variables.keys():
                toPrint = variables[var]
                print(toPrint[1])
            else:
                print(var)

            PC += 1

#       ---READ---

        elif opCode == 'read':
            var = statement[1]

            read = input()
            readType = type(read)

            if readType == str:
                temp = variables[var]
                temp[1] = read
                variables[var] = temp

            PC += 1

#       ---EQUAL---

        elif opCode == '=':
            var = statement[2]
            val = statement[1]

            if val in T.keys():
                val = T[val]
            elif val in variables.keys():
                temp = variables[val]
                val = temp[1]

            if var in variables.keys():
                temp = variables[var]
                temp[1] = val
                variables[var] = temp

                PC += 1
                #print(variables[var])
        
#       ---SUM---

        elif opCode == '+':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]
            
            res = int(var1) + int(var2)

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('SUM')
                # print(T[dest])

#       ---SUB---

        elif opCode == '-':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]
            
            res = int(var1) - int(var2)

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('SUB')
                # print(T[dest])

#       ---MULT---

        elif opCode == '*':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]
            
            res = int(var1) * int(var2)

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('MULT')
                # print(T[dest])

#       ---DIV---

        elif opCode == '/':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]
            
            res = int(var1) / int(var2)

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('DIV')
                # print(T[dest])

#       ---LT---

        elif opCode == '<':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) < int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('LT')
                # print(T[dest])

#       ---LE---

        elif opCode == '<=':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) <= int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('LE')
                # print(T[dest])

#       ---GT---

        elif opCode == '>':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) > int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('GT')
                # print(T[dest])

#       ---GE---

        elif opCode == '>=':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) >= int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('GE')
                # print(T[dest])

#       ---EQ---

        elif opCode == '==':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) == int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('EQ')
                # print(T[dest])

#       ---NE---

        elif opCode == '!=':
            var1 = statement[1]
            var2 = statement[2]
            dest = statement[3]

            if var1 in variables.keys():
                tempVal = variables[var1]
                var1 = tempVal[1]
            elif var1 in T.keys():
                var1 = T[var1]

            if var2 in variables.keys():
                tempVal = variables[var2]
                var2 = tempVal[1]
            elif var2 in T.keys():
                var2 = T[var2]

            if int(var1) != int(var2):
                res = 1
            else:
                res = 0

            if dest in T.keys():
                T[dest] = res

                PC += 1
                # print('NE')
                # print(T[dest])

#       ---gotoF---

        elif opCode == 'gotoF':
            check = statement[1]
            dest = statement[2]

            if check in T.keys():
                check = T[check]

            if check == 1:
                PC += 1
            else:
                PC = int(dest)

#       ---goto---

        elif opCode == 'goto':
            dest = statement[1]

            PC = int(dest)

#       ---end---

        elif opCode == 'end':
            exec = False

        # print(variables)
        # print(T)