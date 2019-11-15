#Los numeros en P(i) suman 0
def case_0(letras):
    regla = "(~{0}^~{1}^~{2})".format(letras[0],letras[1],letras[2])
    return regla

#Los numeros en P(i) suman 1
def case_1(letras):
    regla = "((({0}^~{1}^~{2})0(~{0}^{1}^~{2}))0(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla

#Los numeros en P(i) suman 2
def case_2(letras):
    regla = "(({0}^{1}^~{2})0(~{0}^{1}^{2})0({0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla
        
#Los numeros en P(i) suman 3
def case_3(letras):
    regla = "({0}^{1}^{2})".format(letras[0],letras[1],letras[2])
    return regla

#Hay una casila rellenada en p(i) con el 1
def case_4(letras):
    regla = "((({0}^~{1}^~{2})0(~{0}^{1}^~{2}))0(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla

#Hay una casila rellenada en p(i) con el 2
def case_5(letras):
    regla = "(({0}^{1}^~{2})0(~{0}^{1}^{2}))".format(letras[0],letras[1],letras[2])
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
    regla = "({0}^~{1}^~{2}^~{3})0(~{0}^~{1}^~{2}^{3})0(~{0}^~{1}^{2}^~{3})0(~{0}^{1}^~{2}^~{3})".format(letras[0],letras[1],letras[2],letras[3])
    return regla

#regla 1
r1 = "((i^t)0(h^u))^"+case_3(["A","D","G"])
r2 = "((j^w)0(v^k))^"+case_3(["B","E","H"])
r3 = "((l^á)0(à^m))^"+case_3(["C","F","I"])
r4 = "((n^ã)0(â^o))^"+case_3(["A","B","C"])
r5 = "((p^å)0(ä^q))^"+case_3(["D","E","F"])
r6 = "((r^ç)0(æ^s))^"+case_3(["G","H","I"])

r7 = "(((J^K)0(V^U))0(t^W))^"+case_2(["A","D","G"])
r8 = "(((L^M)0(X^W))0(v^Y))^"+case_2(["B","E","H"])
r9 = "(((N^O)0(Z^á))0(à^a))^"+case_2(["C","F","I"])
r10 = "(((P^Q)0(b^ã))0(â^c))^"+case_2(["A","B","C"])
r11 = "(((R^S)0(d^å))0(ä^e))^"+case_2(["D","E","F"])
r12 = "(((T^U)0(F^ç))0(æ^g))^"+case_2(["G","H","I"])

r13 = "(((v^t)0(v^J))0(t^k))^"+case_1(["A","D","G"])
r14 = "(((w^v)0(w^L))0(v^M))^"+case_1(["B","E","H"])
r15 = "(((á^à)0(á^N))0(à^O))^"+case_1(["C","F","I"])
r16 = "(((â^ã)0(â^Q))0(P^ã))^"+case_1(["A","B","C"])
r17 = "(((ä^å)0(ä^S))0(R^å))^"+case_1(["D","E","F"])
r18 = "(((æ^f)0(æ^U))0(T^ç))^"+case_1(["G","H","I"])

r19 = "(u^t)^"+case_0(["A","D","G"])
r20 = "(v^w)^"+case_0(["B","E","H"])
r21 = "(à^á)^"+case_0(["C","F","I"])
r22 = "(â^ã)^"+case_0(["A","B","C"])
r23 = "(ä^å)^"+case_0(["D","E","F"])
r24 = "(æ^ç)^"+case_0(["G","H","I"])

regla_1=r1+"^"+r2+"^"+r3+"^"+r4+"^"+r5+"^"+r6+"^"+r7+"^"+r8+"^"+r9+"^"+r10+"^"+r11+"^"+r12+"^"+r13+"^"+r14+"^"+r15+"^"+r16+"^"+r17+"^"+r18+"^"+r19+"^"+r20+"^"+r21+"^"+r22+"^"+r23+"^"+r24

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

regla_p=p1+"^"+p2+"^"+p3+"^"+p4+"^"+p5+"^"+p6+"^"+p7+"^"+p8+"^"+p9+"^"+p10+"^"+p11+"^"+p12+"^"
#{'à': 0, 'á': 0, 'â': 0, 'ã': 0, 'ä': 0, 'å': 0, 'æ': 0, 'ç': 0, 'è': 0}
dic = {}
for i in range(224,233):
    dic[chr(i)] = 0
    
print(dic)