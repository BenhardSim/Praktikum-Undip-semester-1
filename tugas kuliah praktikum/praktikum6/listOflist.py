def konsLo(E,L):
    return [E]+L

def is_empty(L):
    return L == []

def is_atom(S):
    if type(S) != list:
        return True
    else :
        return False

def is_list(L):
    if type(L) == list:
        return True
    else :
        return False

def first_list(L):
    return L[0]

def tail_list(L):
    return L[1:]

def IsOneElement(L):
    if not(is_empty(L)):
        return tail(L) == []

# def isMemberS(A,S):
#     if(is_empty(S)):
#         return False
#     elif(not(is_empty()))

def remberL(a,L):
    if(is_empty(L)):
        return L
    else:
        if is_list(first_list(L)):
            return konsLo(remberL(a,first_list(L)),remberL(a,tail_list(L)))
        elif(first_list(L) == a):
            return remberL(a,tail_list(L))
        else:
            return konsLo(first_list(L),remberL(a,tail_list(L)))

l1 = [[1,3],5,[6,7]]

print(remberL(3,l1))
print(tail_list(l1))

def max2(a,b):
    if a >= b:
        return a
    else:
        return b
def maks(S):
    if IsOneElement(S):
        if is_atom(first_list(S)):
            return first_list(S)
        else:
            return maks(first_list(S))
    else:
        if is