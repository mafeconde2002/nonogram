import arboles
import re
import copy



#Los numeros en P(i) suman 0
def case_0(letras):
    regla = "^^~{0}~{1}~{2}".format(letras[0],letras[1],letras[2])
    return regla
#Los numeros en P(i) suman 1
def case_1(letras):
    regla = "°°^^{0}~{1}~{2}^^~{0}{1}~{2}^^~{0}~{1}{2}".format(letras[0],letras[1],letras[2])
    return regla

#Los numeros en P(i) suman 2
def case_2(letras):
    regla =  "°^^{0}{1}~{2}^^~{0}{1}{2}".format(letras[0],letras[1],letras[2]) 
    return regla
        
#Los numeros en P(i) suman 3
def case_3(letras):
    regla = "^^{0}{1}{2}".format(letras[0],letras[1],letras[2])
    return regla
        
#Hay dos casilas rellenadas en p(i)
def case_6(letras):
    regla = "^^{0}~{1}{2}".format(letras[0],letras[1],letras[2])
    return regla

def case_p(letras):
    regla = "°°°^^^{0}~{1}~{2}~{3}^^^~{0}~{1}~{2}{3}^^^~{0}~{1}{2}~{3}^^^~{0}{1}~{2}~{3}".format(letras[0],letras[1],letras[2],letras[3])
    return regla

def CondInicial(c,l):
    if len(c) == 2:
        if (c[0] == 0 and c[1] == 0):
            return case_0([l[0],l[1],l[2]])
        elif (c[0] == 0 and c[1] == 1) or (c[0] == 1 and c[1] == 0):
            return case_1([l[0],l[1],l[2]])
        elif (c[0] == 1 and c[1] == 1):
            return case_6([l[0],l[1],l[2]])
        elif (c[0] == 2 and c[1] == 0) or (c[0] == 0 and c[1] == 2):
            return case_2([l[0],l[1],l[2]])
        elif (c[0] == 3 and c[1] == 0) or (c[0] == 0 and c[1] == 3):
            return case_3([l[0],l[1],l[2]])

def makeRule(c,d):
    rule = "^^^^^"
    for i in range(len(c)):
        print(c[i],d[i])
        rule = rule+CondInicial(c[i],d[i])
        print(rule)
    return rule

def polaca(a):
    p1 = ""
    p1 += a.label
    if a.right != None and a.left != None:
        p1 += polaca(a.left)
        p1 += polaca(a.right)
    elif a.right != None and a.left == None:
        p1 += polaca(a.right)
    return p1

def inversa(a):
    return a[::-1]

def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "~" in A:
        q = A[-1]
        # print('q', q)
        B = "~"+p+"°~"+q+"^"+p+"°"+q
    elif "^" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"°~"+p+"^"+r+"°~"+p+"^~"+q+"°~"+r+"°"+p
    elif "°" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = "~"+q+"°"+p+"^~"+r+"°"+p+"^"+q+"°"+r+"°~"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"°"+p+"^~"+r+"°"+p+"^~"+q+"°"+r+"°~"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 3000)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    L = []
    Pila = []
    I = -1
    S = A[0]
    while len(A) > 0:
        if (S in letrasProposicionalesA) and (Pila[-1] == "~"):
            I += 1
            Atomo = letrasProposicionalesB[I]
            Pila = Pila[:-1]
            Pila.append(Atomo)
            L.append(Atomo+"="+"~"+S)
            A = A[1:]
            if len(A) > 0:
                S = A[0]
        elif S == ')':
            W = Pila[-1]
            O = Pila[-2]
            V = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            I += 1
            Atomo = letrasProposicionalesB[I]
            L.append(Atomo+"="+"("+V+O+W+")")
            S = Atomo
        else:
            Pila.append(S)
            A = A[1:]
            if len(A) > 0:
                S = A[0]
    B = ""
    if I < 0:
        Atomo = Pila[-1]
    else:
        Atomo = letrasProposicionalesB[I]

    for X in L:
        Y = enFNC(X)
        B += "^"+Y

    B = Atomo + B

    return B

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales

def Clausula(C):
    L=[]
    while len(C)>0:
        s=C[0]
        if s=="^" or s=="°":
            C=C[1:]
        elif s=="~":
            literal=s+C[1]
            L.append(literal)
            C=C[2:]
        else:
            L.append(s)
            C=C[1:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    L=[]
    i=0
    while len(A)>0:
        if i==len(A)-1:
            L.append(Clausula(A))
            A=''
        else:
            if A[i]=="^":
                L.append(Clausula(A[:i]))
                A=A[i+1:]
                i=0
            else:
                i+=1
    return L

def clausulas(formula):
    clausulasFinales=[]
    tmp=[]
    string=""
    idx=formula.find("^")
    clausulasFinales.append([formula[1:idx]])
    for i in formula[idx+1:]:
        if(i=="+"):
            tmp.append(string)
            string=""
        elif(i=="^" or i=="]"):
            tmp.append(string)
            clausulasFinales.append(tmp)
            string=""
            tmp=[]
        elif(i!="(" and i!=")"):
            string += i
    return clausulasFinales

def clausulaUnitaria(lista) :
    for i in lista:
        if (len(i)==1):
            return i
        elif (len(i)==2 and i[0]=="-"):
            return i
    return None

def clausulaVacia(lista):
    for i in lista:
        if(i==''):
            return(True)
    return False



def unitPropagate(S, I):
    bool = True
    while bool:
        for k in S:
            if len(k) == 0:
                #return "Insatisfacible", {}
                break

        cont = 0
        for i in S:
            if len(i) == 1:
                cont += 1
                lit = i[0]
                if len(lit) == 1:
                    pp = lit
                    compl = "~" + lit
                    valor = 1

                elif(len(lit) == 2):
                    pp = lit[1]
                    compl = lit[1]
                    valor = 0

                for j in S:
                    if j != i:
                        if lit in j:
                            S.remove(j)
                I[pp] = valor
                S.remove(i)
                #print(i)


        if cont == 0:
            bool = False
        else:
            for k in S:
                if compl in k:
                    k.remove(compl)
    return S, I

def literal_complemento(lit):
    if lit[0] == "~":
        return lit[1]
    else:
        lit = "~" + lit
        return lit

def DPLL(lista, interps):
    lista, interps = unitPropagate(lista,interps)
    if(len(lista)==0):
        return(lista,interps)
    elif("" in lista):
        return (lista,{})
    else:
        listaTemp = [x for x in lista]
        for l in listaTemp[0]:
            if (len(listaTemp)==0):
                return (listaTemp, interps)
            if (l not in interps.keys() and l!='~'):
                break
        listaTemp.insert(0,l)
        lista2, inter2 = DPLL(listaTemp, interps)
        if inter2 == {}:
            listaTemp = [x for x in lista]
            a =literal_complemento(l)
            listaTemp.insert(0,a)
            lista2, inter2 = DPLL(listaTemp, interps)
        return lista2, inter2


def DPLLResultado(lista):
    lista, inter = DPLL(lista,{})
    return inter

def numero(c,dict):
    print(c)
    if c[0][0] == 0 and c[0][1] == 0:
        dict["â"] = 1
        dict["ã"] = 1
    elif c[0][0] == 0 and c[0][1] == 1:
        dict["â"] = 1
        dict["Q"] = 1
    elif c[0][0] == 1 and c[0][1] == 0:
        dict["P"] = 1
        dict["ã"] = 1
    elif c[0][0] == 1 and c[0][1] == 1:
        dict["P"] = 1
        dict["Q"] = 1
    elif c[0][0] == 2 and c[0][1] == 0:
        dict["b"] = 1
        dict["ã"] = 1
    elif c[0][0] == 0 and c[0][1] == 2:
        dict["â"] = 1
        dict["c"] = 1
    elif c[0][0] == 3 and c[0][1] == 0:
        dict["n"] = 1
        dict["ã"] = 1
    elif c[0][0] == 0 and c[0][1] == 3:
        dict["â"] = 1
        dict["o"] = 1
    #Fila_2
    if c[1][0] == 0 and c[1][1] == 0:
        dict["ä"] = 1
        dict["å"] = 1
    elif c[1][0] == 0 and c[1][1] == 1:
        dict["ä"] = 1
        dict["S"] = 1
    elif c[1][0] == 1 and c[1][1] == 0:
        dict["R"] = 1
        dict["å"] = 1
    elif c[1][0] == 1 and c[1][1] == 1:
        dict["R"] = 1
        dict["S"] = 1
    elif c[1][0] == 2 and c[1][1] == 0:
        dict["d"] = 1
        dict["å"] = 1
    elif c[1][0] == 0 and c[1][1] == 2:
        dict["ä"] = 1
        dict["e"] = 1
    elif c[1][0] == 3 and c[1][1] == 0:
        dict["p"] = 1
        dict["å"] = 1
    elif c[1][0] == 0 and c[1][1] == 3:
        dict["ä"] = 1
        dict["q"] = 1
    #Fila_3
    if c[2][0] == 0 and c[2][1] == 0:
        dict["æ"] = 1
        dict["ç"] = 1
    elif c[2][0] == 0 and c[2][1] == 1:
        dict["æ"] = 1
        dict["U"] = 1
    elif c[2][0] == 1 and c[2][1] == 0:
        dict["T"] = 1
        dict["ç"] = 1
    elif c[2][0] == 1 and c[2][1] == 1:
        dict["T"] = 1
        dict["U"] = 1
    elif c[2][0] == 2 and c[2][1] == 0:
        dict["f"] = 1
        dict["ç"] = 1
    elif c[2][0] == 0 and c[2][1] == 2:
        dict["æ"] = 1
        dict["g"] = 1
    elif c[2][0] == 3 and c[2][1] == 0:
        dict["r"] = 1
        dict["ç"] = 1
    elif c[2][0] == 0 and c[2][1] == 3:
        dict["æ"] = 1
        dict["s"] = 1
    #Columna_1
    if c[3][0] == 0 and c[3][1] == 0:
        dict["t"] = 1
        dict["u"] = 1
    elif c[3][0] == 0 and c[3][1] == 1:
        dict["t"] = 1
        dict["J"] = 1
    elif c[3][0] == 1 and c[3][1] == 0:
        dict["t"] = 1
        dict["K"] = 1
    elif c[3][0] == 1 and c[3][1] == 1:
        dict["J"] = 1
        dict["K"] = 1
    elif c[3][0] == 2 and c[3][1] == 0:
        dict["V"] = 1
        dict["u"] = 1
    elif c[3][0] == 0 and c[3][1] == 2:
        dict["t"] = 1
        dict["W"] = 1
    elif c[3][0] == 3 and c[3][1] == 0:
        dict["h"] = 1
        dict["u"] = 1
    elif c[3][0] == 0 and c[3][1] == 3:
        dict["t"] = 1
        dict["i"] = 1
    #Columna_2
    if c[4][0] == 0 and c[4][1] == 0:
        dict["v"] = 1
        dict["w"] = 1
    elif c[4][0] == 0 and c[4][1] == 1:
        dict["v"] = 1
        dict["M"] = 1
    elif c[4][0] == 1 and c[4][1] == 0:
        dict["L"] = 1
        dict["w"] = 1
    elif c[4][0] == 1 and c[4][1] == 1:
        dict["L"] = 1
        dict["M"] = 1
    elif c[4][0] == 2 and c[4][1] == 0:
        dict["X"] = 1
        dict["w"] = 1
    elif c[4][0] == 0 and c[4][1] == 2:
        dict["v"] = 1
        dict["Y"] = 1
    elif c[4][0] == 3 and c[4][1] == 0:
        dict["j"] = 1
        dict["w"] = 1
    elif c[4][0] == 0 and c[4][1] == 3:
        dict["v"] = 1
        dict["k"] = 1
    #Columna_3
    if c[5][0] == 0 and c[5][1] == 0:
        dict["à"] = 1
        dict["á"] = 1
    elif c[5][0] == 0 and c[5][1] == 1:
        dict["à"] = 1
        dict["O"] = 1
    elif c[5][0] == 1 and c[5][1] == 0:
        dict["N"] = 1
        dict["á"] = 1
    elif c[5][0] == 1 and c[5][1] == 1:
        dict["N"] = 1
        dict["O"] = 1
    elif c[5][0] == 2 and c[5][1] == 0:
        dict["Z"] = 1
        dict["á"] = 1
    elif c[5][0] == 0 and c[5][1] == 2:
        dict["à"] = 1
        dict["a"] = 1
    elif c[5][0] == 3 and c[5][1] == 0:
        dict["l"] = 1
        dict["á"] = 1
    elif c[5][0] == 0 and c[5][1] == 3:
        dict["à"] = 1
        dict["m"] = 1




def main(condiciones, cuadros, interp,letrasProp):
    r = inversa(makeRule(condiciones,cuadros))
    arbol = arboles.StringtoTree(r,letrasProp)
    Regla = arboles.Inorder(arbol)
    T = Tseitin(Regla, letrasProp)
    Clau = formaClausal(T)
    S, U =DPLL(Clau, interp)

    for k in U.keys():
        if k in letrasProp:
            interp[k] = U[k]

            










#m=arboles.StringtoTree(regla_1,letrasProp)
#print(m)
#cadenita= inversa(arboles.Inorder(m))
