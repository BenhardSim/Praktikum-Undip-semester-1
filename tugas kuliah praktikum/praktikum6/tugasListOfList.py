"""
NIM         : 24060120140136
Nama        : Benhard Simanullang
Deskripsi   : Tugas praktikum Daspro
Tanggal     : 21 November 2020
"""
"""Ex:
Matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix1 = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
              ]
"""

#is_empty: List-->Boolean
#is_empty(L)bernilai benar(true) jika list kosong
#Realisasi
def is_empty(L):
    return L == []

#IsOneElement : list tidak kosong --> boolean
#IsOneElement(L) menghasil kan nilai boolean true bila jumlah elemend dalam list sama dengan 1
#Realisasi
def IsOneElement(L):
    if not(is_empty(L)):
        return tail(L) == []

#first_element : List tidak kosong--> elemen
#first_element(L)menghasilkan elemen pertama list L
#Realisasi
def first_element(L):
    if not(is_empty(L)):
        return L[0]

#tail : List tidak kosong--> List
#tail(L) menghasilkan list tanpa elemen pertama list L,mungkin kosong
#Realisasi
def tail(L):
    if not(is_empty(L)):
        return L[1:]

# konsLo : list,list of list --> list of list
# konsLo(E,L)  membentuk list baru dengan list yang di berikan sebagai elemen pertama
# realisasi
def konsLo(E,L):
    return [E]+L

# first_list : list of list tidak kosong --> list
# first_list(L) mengeluarkan elemen pertama list, mungkin sebuah list atau atom
# realisasi
def first_list(L):
    if(not(is_empty(L))):
        return L[0]

# is_atom : list of list --> boolean
# is_atom(S) mengeluarkan nilai boolean true bila S adalah atom
# realisasi
def is_atom(S):
    if type(S) != list:
        return True
    else :
        return False

# is_list : list of list --> boolean
# is_list(S) mengeluarkan nilai boolean true bila S adalah list
# realisasi
def is_list(L):
    if type(L) == list:
        return True
    else :
        return False

# taik_list : list of list tidak kosong --> list of list
# tail_list(L) mengeluarkan sisa list of list L tanpa element pertama list L
def tail_list(L):
    return L[1:]

#NbOcc : integer, list of integer --> integer > 0
#NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
# Realisasi
def NbOcc(X,Li):
    if(is_empty(Li)):
        return 0
    elif IsOneElement(Li):
        if X == first_element(Li):
            return 1
        else:
            return 0
    else:
        if X == first_element(Li):
            return 1+NbOcc(X,tail(Li))
        else:
            return NbOcc(X,tail(Li))
p =
# 1
# DefSpek
# NbEleX : elemen, list of list --> integer
# NbEleX (L,X) menentukan banyaknya X dalam list L
# Realisasi
def NbEleX(L,X):
    if is_empty(L):
        return 0 
    elif(is_list(first_list(L))):
        return NbOcc(X,first_list(L)) + NbEleX(tail_list(L),X) 
    elif(is_atom(first_list(L))):
        if(first_list(L) == X):
            return 1 + NbEleX(tail_list(L),X) 
        else:
            return 0 + NbEleX(tail_list(L),X)

L1 = [[4,1], 2, [3,4], 1, 4]
print("\nJawaban nomer 1 fungsi dari NbEleX : ")
print(NbEleX(L1,4))

# 2
# DefSpek
# KaliMatrix : Integer, list of list dalam bentuk matrix --> list
# KaliMatrix (k, L) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K
# Realisasi

# ------------------------------------------------------------------------------------------
# fungsi perantara
# kalilist : integer, list --> list
# kalilist(X,L) menghasilkan list baru yg dimana tiap tiap element nya telah di kalo dengan integer X
# realisasi
def kalilist(X,L):
    if is_empty(L):
        return []
    else:
        return konsLo(first_list(L)*X,kalilist(X,tail_list(L)))
# ----------------------------------------------------------------------------------------------

def KaliMatrix(k,L):
    if is_empty(L):
        return []
    else:
        return konsLo(kalilist(k,first_list(L)),KaliMatrix(k,tail_list(L)))

L = [[1,2,3], [4,5,6], [7,8,9]]
print("\nJawaban no 2 dengan fungsi KaliMatrix :")
print(KaliMatrix(2,L))

# 3
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L
L4 = [1, [2,3], [4]]
L3 = [[5], [6], [7]]
L2 = [8, 9, 10]
def NbList(L):
    if(is_empty(L)):
        return 0
    elif(is_list(first_list(L))):
        return 1 + NbList(tail_list(L))
    elif(is_atom(first_list(L))):
        return 0 + NbList(tail_list(L))
# Aplikasi
print("\nJawaban no 3 dengan fungsi NbList : ")
print(NbList(L4))
print(NbList(L3))
print(NbList(L2))
