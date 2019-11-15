def case_1(letras):
    regla = "((({0}^~{1}^~{2})0(~{0}^{1}^~{2}))0(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla


def case_2(letras):
    regla = "(({0}^{1}^~{2})0(~{0}^{1}^{2})0({0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla
        

def case_3(letras):
    regla = "({0}^{1}^{2})".format(letras[0],letras[1],letras[2])
    return regla

def case_4(letras):
    regla = "((({0}^~{1}^~{2})0(~{0}^{1}^~{2}))0(~{0}^~{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla


def case_5(letras):
    regla = "(({0}^{1}^~{2})0(~{0}^{1}^{2}))".format(letras[0],letras[1],letras[2])
    return regla
        

def case_6(letras):
    regla = "({0}^~{1}^{2})".format(letras[0],letras[1],letras[2])
    return regla

def case_p(letras):
    regla = "({0}^~{1}^~{2}^~{3})0(~{0}^~{1}^~{2}^{3})0(~{0}^~{1}^{2}^~{3})0(~{0}^{1}^~{2}^~{3})".format(letras[0],letras[1],letras[2],letras[3])
    return regla


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

print(r1)

dic = {}
for i in range(224,233):
    dic[chr(i)] = 0
    
print(dic)