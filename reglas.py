import arboles

#Los numeros en P(i) suman 0
def case_0(letras):
    regla = "^^~{0}~{1}~{2}".format(letras[0],letras[1],letras[2])
    return regla
#Los numeros en P(i) suman 1
def case_1(letras):
    regla = "°°^^^^{0}~{1}~{2}°°{0}~{1}{2}°°{0}{1}~{2}^^^^~{0}{1}~{2}°°~{0}{1}{2}°°~{0}{1}~{2}^^^^~{0}~{1}{2}°°~{0}{1}{2}°°{0}~{1}{2}".format(letras[0],letras[1],letras[2])
    return regla
#Los numeros en P(i) suman 2
def case_2(letras):
    regla = "°°^^^^{0}{1}~{2}°°{0}~{1}~{2}°°~{0}{1}~{2}^^^^~{0}{1}{2}°°~{0}~{1}{2}°°~{0}{1}~{2}^^^^{0}~{1}{2}°°~{0}~{1}{2}°°{0}~{1}~{2}".format(letras[0],letras[1],letras[2]) 
    return regla
        
#Los numeros en P(i) suman 3
def case_3(letras):
    regla = "^^{0}{1}{2}".format(letras[0],letras[1],letras[2])
    return regla
#Hay una casila rellenada en p(i) con el 1
def case_4(letras):
    regla = "°°^^^^{0}~{1}~{2}°°{0}~{1}{2}°°{0}{1}~{2}^^^^~{0}{1}~{2}°°~{0}{1}{2}°°{0}{1}~{2}^^^^~{0}~{1}{2}°°~{0}{1}{2}°°{0}~{1}{2}".format(letras[0],letras[1],letras[2]) 
    return regla
#Hay una casila rellenada en p(i) con el 2
def case_5(letras):
    regla = "°^^^{0}{1}~{2}°°{0}~{1}~{2}^^^~{0}{1}{2}°°~{0}~{1}{2}".format(letras[0],letras[1],letras[2]) 
    return regla
        
#Hay dos casilas rellenadas en p(i)
def case_6(letras):
    regla = "^^{0}~{1}{2}".format(letras[0],letras[1],letras[2])
    return regla
#No hay casilas rellenadas en p(i)
def case_7(letras):
    regla = "^^~{0}~{1}~{2}".format(letras[0],letras[1],letras[2])
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
            return case_5([l[0],l[1],l[2]])
        elif (c[0] == 3 and c[1] == 0) or (c[0] == 0 and c[1] == 3):
            return case_3([l[0],l[1],l[2]])

def makeRule(c,d):
    rule = "^^^^^"
    rule6=CondInicial(c[0],d[0])
    rule1=CondInicial(c[1],d[1])
    rule2=CondInicial(c[2],d[2])
    rule3=CondInicial(c[3],d[3])
    rule4=CondInicial(c[4],d[4])
    rule5=CondInicial(c[5],d[5])
    rule = rule+rule1+rule2+rule3+rule4+rule5+rule6
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
    if "~" in A:
        q = A[-1]
        B = "~"+p+"°~"+q+"^"+p+"°"+q
    elif "^" in A:
        q = A[3]
        r = A[5]
        B = q+"°~"+p+"^"+r+"°~"+p+"^~"+q+"°~"+r+"°"+p
    elif "°" in A:
        q = A[3]
        r = A[5]
        B = "~"+q+"°"+p+"^~"+r+"°"+p+"^"+q+"°"+r+"°~"+p
    elif ">" in A:
        q = A[3]
        r = A[5]
        B = q+"°"+p+"^~"+r+"°"+p+"^~"+q+"°"+r+"°~"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

#regla 1
r1 = "^°^it^hu"+case_3(["A","D","G"])
r2 = "^°^jw^vk"+case_3(["B","E","H"])
r3 = "^°^lá^àm"+case_3(["C","F","I"])
r4 = "^°^nã^âo"+case_3(["A","B","C"])
r5 = "^°^på^äq"+case_3(["D","E","F"])
r6 = "^°^rç^æs"+case_3(["G","H","I"])

r7 = "^°°^JK^VU^tW"+case_2(["A","D","G"]) 
r8 = "^°°^LM^XW^vY"+case_2(["B","E","H"])
r9 = "^°°^NO^Zá^àa"+case_2(["C","F","I"])
r10 = "^°°^PQ^bã^âc"+case_2(["A","B","C"])
r11 = "^°°^RS^då^äe"+case_2(["D","E","F"])
r12 = "^°°^TU^Fç^æg"+case_2(["G","H","I"])

r13 = "^°°^vt^vJ^tk"+case_1(["A","D","G"])   
r14 = "^°°^wv^wL^vM"+case_1(["B","E","H"])
r15 = "^°°^áà^áN^àO"+case_1(["C","F","I"])
r16 = "^°°^âã^âQ^Pã"+case_1(["A","B","C"])
r17 = "^°°^äå^äS^Rå"+case_1(["D","E","F"])
r18 = "^°°^æf^æU^Tç"+case_1(["G","H","I"])

r19 = "^^ut"+case_0(["A","D","G"]) 
r20 = "^^vw"+case_0(["B","E","H"])
r21 = "^^àá"+case_0(["C","F","I"])
r22 = "^^âã"+case_0(["A","B","C"])
r23 = "^^äå"+case_0(["D","E","F"])
r24 = "^^æç"+case_0(["G","H","I"])

regla_1="^^^^^^^^^^^^^^^^^^^^^^^"+r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16+r17+r18+r19+r20+r21+r22+r23+r24

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

regla_p="^^^^^^^^^^^"+p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12

#regla 2
r2_1 = "^°^kt^Ju"+case_4(["A","D","G"])
r2_2 = "^°^Lw^vM"+case_4(["B","E","H"])
r2_3 = "^°^Ná^àO"+case_4(["C","F","I"])
r2_4 = "^°^Pã^âQ"+case_4(["A","B","C"])
r2_5 = "^°^Rå^sä"+case_4(["D","E","F"])
r2_6 = "^°^Tç^Uæ"+case_4(["G","H","I"])

r2_7 = "^°^Vu^tW"+case_5(["A","D","G"])
r2_8 = "^°^Xw^vY"+case_5(["B","E","H"])
r2_9 = "^°^Zá^aà"+case_5(["C","F","I"])
r2_10 = "^°^bã^âc"+case_5(["A","B","C"])
r2_11 = "^°^då^äe"+case_5(["D","E","F"])
r2_12 = "^°^fç^æg"+case_5(["G","H","I"])

r2_13 = "^^JK"+case_6(["A","D","G"])
r2_14 = "^^LM"+case_6(["B","E","H"])
r2_15 = "^^NO"+case_6(["C","F","I"])
r2_16 = "^^PQ"+case_6(["A","B","C"])
r2_17 = "^^RS"+case_6(["D","E","F"])
r2_18 = "^^TU"+case_6(["G","H","I"])

r2_19 = "^^ut"+case_7(["A","D","G"]) 
r2_20 = "^^vw"+case_7(["B","E","H"])
r2_21 = "^^àá"+case_7(["C","F","I"])
r2_22 = "^^âã"+case_7(["A","B","C"])
r2_23 = "^^äå"+case_7(["D","E","F"])
r2_24 = "^^æç"+case_7(["G","H","I"])

regla_2 = "^^^^^^^^^^^^^^^^^^^^^^^"+r2_1+r2_2+r2_3+r2_4+r2_5+r2_6+r2_7+r2_8+r2_9+r2_10+r2_11+r2_12+r2_13+r2_14+r2_15+r2_16+r2_17+r2_18+r2_19+r2_20+r2_21+r2_22+r2_23+r2_24
regla_tot ="^"+regla_p+regla_2


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
    

def neg(a):
    if len(a) == 1:
        l = "~" + a
    else:
        l = a[-1]
    return l

#def DPLL(s, i):
#    void = []
#    s, i = unitPropagate(s,i)
#    if void in s:
#        return "Insatisfacible", {}
#    elif len(s) == 0:
#        return "Satisfacible", i
#    l = ""
#    for y in s:
#        for x in y:
#            if x not in i.keys():
#                l = x
#    l_comp = neg(l)
#    if l == "":
#        return None
#    Sp = copy.deepcopy(s)
#    Sp = [n for n in Sp if l not in n]
#    for q in Sp:
#        if l_comp in q:
#            q.remove(neg(l))
#    Ip = copy.deepcopy(i)
#    if l[0] == "~":
#        Ip[l[1]] = 0
#    else:
#        Ip[l] = 1
#    S1, I1 = DPLL(Sp, Ip)
#    if S1 == "Satisfacible":
#        return S1, I1
#    else:
#        Spp = copy.deepcopy(s)
#        Spp = [q for q in Spp if neg(l) not in q]
#        for h in Spp:
#            if l in h:
#                h.remove(l)
#        Ipp = copy.deepcopy(i)
#        if l[0] == "~":
#            Ipp[l[1]] = 0
#        else:
#            Ipp[l] = 1
#        return DPLL(Spp, Ipp)

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


def numero(c,dict):
    reglaa="^^^^^"
    if c[0][0] == 0 and c[0][1] == 0:
        dict["â"] = 1
        dict["ã"] = 1
        reglaa=reglaa+"^âã"
    elif c[0][0] == 0 and c[0][1] == 1:
        dict["â"] = 1
        dict["Q"] = 1
        reglaa=reglaa+"^âQ"
    elif c[0][0] == 1 and c[0][1] == 0:
        dict["P"] = 1
        dict["ã"] = 1
        reglaa=reglaa+"^Pã"
    elif c[0][0] == 1 and c[0][1] == 1:
        dict["P"] = 1
        dict["Q"] = 1
        reglaa=reglaa+"^PQ"
    elif c[0][0] == 2 and c[0][1] == 0:
        dict["b"] = 1
        dict["ã"] = 1
        reglaa=reglaa+"^bã"
    elif c[0][0] == 0 and c[0][1] == 2:
        dict["â"] = 1
        dict["c"] = 1
        reglaa=reglaa+"^âc"
    elif c[0][0] == 3 and c[0][1] == 0:
        dict["n"] = 1
        dict["ã"] = 1
        reglaa=reglaa+"^nã"
    elif c[0][0] == 0 and c[0][1] == 3:
        dict["â"] = 1
        dict["o"] = 1
        reglaa=reglaa+"^âo"
    #Fila_2
    if c[1][0] == 0 and c[1][1] == 0:
        dict["ä"] = 1
        dict["å"] = 1
        reglaa=reglaa+"^äå"
    elif c[1][0] == 0 and c[1][1] == 1:
        dict["ä"] = 1
        dict["S"] = 1
        reglaa=reglaa+"^äS"
    elif c[1][0] == 1 and c[1][1] == 0:
        dict["R"] = 1
        dict["å"] = 1
        reglaa=reglaa+"^Rå"
    elif c[1][0] == 1 and c[1][1] == 1:
        dict["R"] = 1
        dict["S"] = 1
        reglaa=reglaa+"^RS"
    elif c[1][0] == 2 and c[1][1] == 0:
        dict["d"] = 1
        dict["å"] = 1
        reglaa=reglaa+"^då"
    elif c[1][0] == 0 and c[1][1] == 2:
        dict["ä"] = 1
        dict["e"] = 1
        reglaa=reglaa+"^äe"
    elif c[1][0] == 3 and c[1][1] == 0:
        dict["p"] = 1
        dict["å"] = 1
        reglaa=reglaa+"^på"
    elif c[1][0] == 0 and c[1][1] == 3:
        dict["ä"] = 1
        dict["q"] = 1
        reglaa=reglaa+"^äq"
    #Fila_3
    if c[2][0] == 0 and c[2][1] == 0:
        dict["æ"] = 1
        dict["ç"] = 1
        reglaa=reglaa+"^æç"
    elif c[2][0] == 0 and c[2][1] == 1:
        dict["æ"] = 1
        dict["U"] = 1
        reglaa=reglaa+"^æU"
    elif c[2][0] == 1 and c[2][1] == 0:
        dict["T"] = 1
        dict["ç"] = 1
        reglaa=reglaa+"^Tç"
    elif c[2][0] == 1 and c[2][1] == 1:
        dict["T"] = 1
        dict["U"] = 1
        reglaa=reglaa+"^TU"
    elif c[2][0] == 2 and c[2][1] == 0:
        dict["f"] = 1
        dict["ç"] = 1
        reglaa=reglaa+"^fç"
    elif c[2][0] == 0 and c[2][1] == 2:
        dict["æ"] = 1
        dict["g"] = 1
        reglaa=reglaa+"^æg"
    elif c[2][0] == 3 and c[2][1] == 0:
        dict["r"] = 1
        dict["ç"] = 1
        reglaa=reglaa+"^rç"
    elif c[2][0] == 0 and c[2][1] == 3:
        dict["æ"] = 1
        dict["s"] = 1
        reglaa=reglaa+"^æs"
    #Columna_1
    if c[3][0] == 0 and c[3][1] == 0:
        dict["t"] = 1
        dict["u"] = 1
        reglaa=reglaa+"^tu"
    elif c[3][0] == 0 and c[3][1] == 1:
        dict["t"] = 1
        dict["J"] = 1
        reglaa=reglaa+"^tJ"
    elif c[3][0] == 1 and c[3][1] == 0:
        dict["t"] = 1
        dict["K"] = 1
        reglaa=reglaa+"^tK"
    elif c[3][0] == 1 and c[3][1] == 1:
        dict["J"] = 1
        dict["K"] = 1
        reglaa=reglaa+"^JK"
    elif c[3][0] == 2 and c[3][1] == 0:
        dict["V"] = 1
        dict["u"] = 1
        reglaa=reglaa+"^Vu"
    elif c[3][0] == 0 and c[3][1] == 2:
        dict["t"] = 1
        dict["W"] = 1
        reglaa=reglaa+"^tW"
    elif c[3][0] == 3 and c[3][1] == 0:
        dict["h"] = 1
        dict["u"] = 1
        reglaa=reglaa+"^hu"
    elif c[3][0] == 0 and c[3][1] == 3:
        dict["t"] = 1
        dict["i"] = 1
        reglaa=reglaa+"^ti"
    #Columna_2
    if c[4][0] == 0 and c[4][1] == 0:
        dict["v"] = 1
        dict["w"] = 1
        reglaa=reglaa+"^vw"
    elif c[4][0] == 0 and c[4][1] == 1:
        dict["v"] = 1
        dict["M"] = 1
        reglaa=reglaa+"^vM"
    elif c[4][0] == 1 and c[4][1] == 0:
        dict["L"] = 1
        dict["w"] = 1
        reglaa=reglaa+"^Lw"
    elif c[4][0] == 1 and c[4][1] == 1:
        dict["L"] = 1
        dict["M"] = 1
        reglaa=reglaa+"^LM"
    elif c[4][0] == 2 and c[4][1] == 0:
        dict["X"] = 1
        dict["w"] = 1
        reglaa=reglaa+"^Xw"
    elif c[4][0] == 0 and c[4][1] == 2:
        dict["v"] = 1
        dict["Y"] = 1
        reglaa=reglaa+"^vY"
    elif c[4][0] == 3 and c[4][1] == 0:
        dict["j"] = 1
        dict["w"] = 1
        reglaa=reglaa+"^jw"
    elif c[4][0] == 0 and c[4][1] == 3:
        dict["v"] = 1
        dict["k"] = 1
        reglaa=reglaa+"^vk"
    #Columna_3
    if c[5][0] == 0 and c[5][1] == 0:
        dict["à"] = 1
        dict["á"] = 1
        reglaa=reglaa+"^àá"
    elif c[5][0] == 0 and c[5][1] == 1:
        dict["à"] = 1
        dict["O"] = 1
        reglaa=reglaa+"^àO"
    elif c[5][0] == 1 and c[5][1] == 0:
        dict["N"] = 1
        dict["á"] = 1
        reglaa=reglaa+"^Ná"
    elif c[5][0] == 1 and c[5][1] == 1:
        dict["N"] = 1
        dict["O"] = 1
        reglaa=reglaa+"^NO"
    elif c[5][0] == 2 and c[5][1] == 0:
        dict["Z"] = 1
        dict["á"] = 1
        reglaa=reglaa+"^Zá"
    elif c[5][0] == 0 and c[5][1] == 2:
        dict["à"] = 1
        dict["a"] = 1
        reglaa=reglaa+"^àa"
    elif c[5][0] == 3 and c[5][1] == 0:
        dict["l"] = 1
        dict["á"] = 1
        reglaa=reglaa+"^lá"
    elif c[5][0] == 0 and c[5][1] == 3:
        dict["à"] = 1
        dict["m"] = 1
        reglaa=reglaa+"^àm"
    return reglaa

letrasProp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç']



def main(interp,letrasProp,je):
    d = {}
    r = inversa(je)
    arbol = arboles.StringtoTree(r,letrasProp)
    Regla = arboles.Inorder(arbol)
    T = Tseitin(Regla, letrasProp)
    Clau = formaClausal(T)
    S, U =DPLL(Clau, interp)

    for k in U.keys():
        if k in letrasProp:
            d[k] = U[k]
    print(d)
    return(d)

            


#m=arboles.StringtoTree(regla_1,letrasProp)
#print(m)
#cadenita= inversa(arboles.Inorder(m))
