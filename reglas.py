import arboles
import re

#Los numeros en P(i) suman 0
def case_0(letras):
    regla = "(~{0}^~{1}^~{2})".format(letras[0],letras[1],letras[2])
    return regla

#Los numeros en P(i) suman 1
def case_1(letras):
    regla = "((({0}^~{1}^~{2})°(~{0}^{1}^~{2}))°(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla

#Los numeros en P(i) suman 2
def case_2(letras):
    regla = "(({0}^{1}^~{2})°(~{0}^{1}^{2})°({0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla
        
#Los numeros en P(i) suman 3
def case_3(letras):
    regla = "({0}^{1}^{2})".format(letras[0],letras[1],letras[2])
    return regla

#Hay una casila rellenada en p(i) con el 1
def case_4(letras):
    regla = "((({0}^~{1}^~{2})°(~{0}^{1}^~{2}))°(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla

#Hay una casila rellenada en p(i) con el 2
def case_5(letras):
    regla = "(({0}^{1}^~{2})°(~{0}^{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla
        
#Hay dos casilas rellenadas en p(i)
def case_6(letras):
    regla = "({0}^~{1}^{2})".format(letras[0],letras[1],letras[2])
    return regla

#No hay casilas rellenadas en p(i)
def case_7(letras):
    regla = "(~{0}^~{1}^~{2})".format(letras[0],letras[1],letras[2])
    return regla

def case_p(letras):
    regla = "(((({0}^~{1}^~{2}^~{3})°(~{0}^~{1}^~{2}^{3}))°(~{0}^~{1}^{2}^~{3}))°(~{0}^{1}^~{2}^~{3}))".format(letras[0],letras[1],letras[2],letras[3])
    return regla

#regla 1
r1 = "(((i^t)°(h^u))^"+case_3(["A","D","G"])+")"
r2 = "(((j^w)°(v^k))^"+case_3(["B","E","H"])+")"
r3 = "(((l^á)°(à^m))^"+case_3(["C","F","I"])+")"
r4 = "(((n^ã)°(â^o))^"+case_3(["A","B","C"])+")"
r5 = "(((p^å)°(ä^q))^"+case_3(["D","E","F"])+")"
r6 = "(((r^ç)°(æ^s))^"+case_3(["G","H","I"])+")"

r7 = "((((J^K)°(V^U))°(t^W))^"+case_2(["A","D","G"]) +")"
r8 = "((((L^M)°(X^W))°(v^Y))^"+case_2(["B","E","H"])+")"
r9 = "((((N^O)°(Z^á))°(à^a))^"+case_2(["C","F","I"])+")"
r10 = "((((P^Q)°(b^ã))°(â^c))^"+case_2(["A","B","C"])+")"
r11 = "((((R^S)°(d^å))°(ä^e))^"+case_2(["D","E","F"])+")"
r12 = "((((T^U)°(F^ç))°(æ^g))^"+case_2(["G","H","I"])+")"

r13 = "((((v^t)°(v^J))°(t^k))^"+case_1(["A","D","G"])+")"
r14 = "((((w^v)°(w^L))°(v^M))^"+case_1(["B","E","H"])+")"
r15 = "((((á^à)°(á^N))°(à^O))^"+case_1(["C","F","I"])+")"
r16 = "((((â^ã)°(â^Q))°(P^ã))^"+case_1(["A","B","C"])+")"
r17 = "((((ä^å)°(ä^S))°(R^å))^"+case_1(["D","E","F"])+")"
r18 = "((((æ^f)°(æ^U))°(T^ç))^"+case_1(["G","H","I"])+")"

r19 = "((u^t)^"+case_0(["A","D","G"])+")"
r20 = "((v^w)^"+case_0(["B","E","H"])+")"
r21 = "((à^á)^"+case_0(["C","F","I"])+")"
r22 = "((â^ã)^"+case_0(["A","B","C"])+")"
r23 = "((ä^å)^"+case_0(["D","E","F"])+")"
r24 = "((æ^ç)^"+case_0(["G","H","I"])+")"

regla_1="((((((((((((((((((((((("+r1+"^"+r2+")^"+r3+")^"+r4+")^"+r5+")^"+r6+")^"+r7+")^"+r8+")^"+r9+")^"+r10+")^"+r11+")^"+r12+")^"+r13+")^"+r14+")^"+r15+")^"+r16+")^"+r17+")^"+r18+")^"+r19+")^"+r20+")^"+r21+")^"+r22+")^"+r23+")^"+r24+")"

#regla p

p1= case_p(["W","K","i","u"])
p2= case_p(["V","J","h","t"])
p3= case_p(["M","Y","w","k"])
p4= case_p(["L","X","v","j"])
p5= case_p(["Z","N","l","à"])
p6= case_p(["a","O","m","á"])
p7= case_p(["n","b","P","â"])
p8= case_p(["c","Q","o","ã"])
p9= case_p(["d","p","R","ä"])
p10= case_p(["e","S","q","å"])
p11= case_p(["f","r","T","æ"])
p12= case_p(["g","s","U","ç"])

regla_p="((((((((((("+p1+"^"+p2+")"+"^"+p3+")"+"^"+p4+")"+"^"+p5+")"+"^"+p6+")"+"^"+p7+")"+"^"+p8+")"+"^"+p9+")"+"^"+p10+")"+"^"+p11+")"+"^"+p12+")"
#{'à': 0, 'á': 0, 'â': 0, 'ã': 0, 'ä': 0, 'å': 0, 'æ': 0, 'ç': 0, 'è': 0}
dic = {}
for i in range(224,233):
    dic[chr(i)] = 0
    
letrasProp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç']

m=arboles.StringtoTree(regla_1,letrasProp)
print(m)
#cadenita=arboles.Inorder(m)
#
#print(cadenita)

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
    x3 = polaca(a)
    return x3[::-1]

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
        B = q+"O°"+p+"^~"+r+"°"+p+"^"+q+"°"+r+"°~"+p
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
    letrasProposicionalesB = [chr(x) for x in range(256, 300)]
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
            S = A[0]
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

def unitPropagate(lista,interps):
    x = clausulaUnitaria(lista)
    while(x!= None and clausulaVacia(lista)!=True):
        if (len(x)==1):
            interps[str(x)]=1
            j = 0
            for i in range(0,len(lista)):
                lista[i]=re.sub('~'+x,'',lista[i])
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
        else:
            interps[str(x[1])]=0
            j = 0
            for i in range(0,len(lista)):
                if(x in lista[i-j]):
                    lista.remove(lista[i-j])
                    j+=1
            for i in range(0,len(lista)):
                lista[i]=re.sub(x[1],'',lista[i])
        x = clausulaUnitaria(lista)
    return(lista, interps)

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