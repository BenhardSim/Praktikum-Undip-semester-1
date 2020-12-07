"""
NIM         : 24060120140136
Nama        : Benhard Simanullang
Deskripsi   : Tugas praktikum Daspro
Tanggal     : 7 Desember 2020
"""

class PohonBiner:
      def __init__(self,A,L,R):
            self.A = A
            self.L = L
            self.R = R

def MakePB(A,L,R):
      return PohonBiner(A,L,R)

def Akar(P):
      return P.A

def Left(P):
      return P.L

def Right(P):
      return P.R

def AkarList(P):
    return P[0]

def LeftList(P):
    return P[1]

def RightList(P):
    return P[2]

def MakePBList(A,L,R):
    return  [A,L,R]

def IsTreeEmpty(P):
      if P == None:
            return True
      else:
            return False

def IsOneElmtPB(P):
      if not(IsTreeEmpty(P)) and IsTreeEmpty(Right(P)) and IsTreeEmpty(Left(P)):
            return True
      else:
            return False

def is_empty(L):
    return L == []

def tail(L):
    if not(is_empty(L)):
        return L[1:]

def first_element(n):
    return n[0]

def IsExistRight(P):
      if not(IsTreeEmpty(P)) and not(IsTreeEmpty(Right(P))):
            return True
      else:
            return False

def IsExistLeft(P):
      if not(IsTreeEmpty(P)) and IsTreeEmpty(Left(P)):
            return True
      else:
            return False

def maybiner(P):
    if(not(IsTreeEmpty(P)) and (IsUnerLeftPb(P) or IsUnerRightPB(P))):
        return True
    else:
        return False

def IsBiner(P):
      if not(IsTreeEmpty(P)) and not(IsTreeEmpty(Right(P))) and not(IsTreeEmpty(Left(P))):
            return True
      else:
            return False

def IsBinerList(P):
    if not(is_empty(P)):
        return True
    else: 
        return False

def konso(x,L):
    return [x]+L

def Head(L):
    if not L==[]:
        return L[:-1]

# punya cabang kiri
def IsUnerLeftPb(P):
      if not(IsTreeEmpty(P)) and IsTreeEmpty(Right(P)) and not(IsTreeEmpty(Left(P))):
            return True
      else:
            return False

# punya cabang kanan
def IsUnerRightPB(P):
      if not(IsTreeEmpty(P)) and not(IsTreeEmpty(Right(P))) and IsTreeEmpty(Left(P)):
            return True
      else:
            return False

def BsearchX(P,X):
    if(IsTreeEmpty(P)):
        return False
    else:
        if AkarList(P) == X:
            return True
        elif AkarList(P) < X:
            return BsearchX(RightList(P),X)
        else:
            return BsearchX(LeftList(P),X)

def rember(e,L):
    if(is_empty(L)):
        return []
    elif(first_element(L) == e):
        return rember(e,tail(L))
    else:
        return konso(first_element(L) ,rember(e,tail(L)))

def convertTree(P):
    if(IsOneElmtPB(P)):
        return [P.A,None,None]
        # biner dan anak kiri dan kanan tak bercabang
    elif(IsBiner(P) and not maybiner(Left(P)) and not maybiner(Right(P))):
        return [P.A,[P.L.A,None,None],[P.R.A,None,None]]
        # biner anak kiri dan kanan bercabang
    elif(IsBiner(P)):
        return [P.A,convertTree(P.L),convertTree(P.R)]
        # biner anak kiri bercabang
    elif(IsBiner(P) and maybiner(Left(P)) and not maybiner(Right(P))):
        return [P.A,convertTree(P.L),P.R]
        # biner anak kanan bercabang
    elif(IsBiner(P) and not maybiner(Left(P)) and maybiner(Right(P))):
        return [P.A,P.L,convertTree(P.R)]
        # hanyan bercabang kiri
    elif(IsUnerLeftPb(P)):
        return [P.A,convertTree(P.L),None]
        # hanya bercabang kanan
    elif(IsUnerRightPB(P)):
        return [P.A,None,convertTree(P.R)]

def addXList(P,x):
    if IsTreeEmpty(P):
        return MakePBList(x,None,None)
    elif x > AkarList(P): # bermasalah
        return MakePBList(AkarList(P),LeftList(P),addXList(RightList(P),x))
    elif x < AkarList(P):
        return MakePBList(AkarList(P) , addXList(LeftList(P),x) , RightList(P))

# print(addXList(t1,5))

def BinSearchTree(L,P):
    if(is_empty(L)):
        return P
    else:
        return BinSearchTree(tail(L), addXList(P, first_element(L)))

# NO.1
# DEFINISI DAN SPESIFIKASI
# MakeBinSearchTree : list --> tree dalam bentuk list of list
# MakeBinSearchTree(L) merupakan fungsi yang memberikan keluaran tree dalam bentuk reprefix dari masukkan list
# REALISASI
def MakeBinSearchTree(L):
    return BinSearchTree(L,None)
# APLIKASI
l1 = [3,1,5,7,9,4]
t1 = MakePBList(10,None,None)
print("\n--BinSearchTree-- :")
print(BinSearchTree(l1,t1))
print("\nNO.1 --MakeBinSearchTree-- :")
print(MakeBinSearchTree(l1))

# NO.2
# DEFINISI DAN SPESIFIKASI
# DekBTree : tree tak kosong , integer node --> tree tak kosong
# DelBTree(P,X) merupakan fungsi yang memberikan keluaran tree dalam bentuk list of list tanpa node X di dalam nya
# REALISAI
def DelBtree(P,X):
    if(IsTreeEmpty(P)):
        return []
    elif(BsearchX(P,X)):
        if(X == AkarList(P)):
            return None
        elif(X > AkarList(P)):
            return MakePBList(AkarList(P),LeftList(P),DelBtree(RightList(P),X))
        elif(X < AkarList(P)):
            return MakePBList(AkarList(P),DelBtree(LeftList(P),X),RightList(P))
    else:
        return P
# APLIKASI
t2 = MakePBList(6,MakePBList(3,MakePBList(2,None,None),MakePBList(4,None,None)),MakePBList(8,None,None))
print("\nNO.2 --DelBTree-- :")
print(DelBtree(t2,2))

# NO.3
# DEFINSI DAN SPESIFIKASI
# BuildBallanceTree : List of node , integer --> BinBallTree
# BuildBallanceTree(L,X) merupakan fungsi yang memberikan keluaran tree yang sudah ballance dengan n node
# REALISASI
import math
def BuildBalanceTree(L,n):
    Akar = [L[0]]
    b = sorted(L[1:])
    Kiri = []
    Kanan = []
    e = int(math.log(n,2))
    x = 0
    for n in range (e):
        j = 2**n
        for x in range (j):
                [Kiri.append(b[x])]
                x = x+1
        for x in range (j) :  
                [Kanan.append(b[x])]
                x = x+1
    return print ([Akar]+[Kiri]+[Kanan])

L1 = [4,1,6,3,9,7,2]
print("\nNO.3 --BuildBallanceTree-- : ")
print(BuildBalanceTree(L1,7))

        



