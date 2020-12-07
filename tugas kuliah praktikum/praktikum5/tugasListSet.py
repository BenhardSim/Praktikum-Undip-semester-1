"""
NIM         : 24060120140136
Nama        : Benhard Simanullang
Deskripsi   : 
Tanggal     : 12,November 2020
"""

# FUNGSI PERANTARA
#is_empty: List-->Boolean
#is_empty(L)bernilai benar(true) jika list kosong
#Realisasi
def is_empty(L):
    return L == []

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

#IsOneElement : list tidak kosong --> boolean
#IsOneElement(L) menghasil kan nilai boolean true bila jumlah elemend dalam list sama dengan 1
#Realisasi
def IsOneElement(L):
    if not(is_empty(L)):
        return tail(L) == []

#konso : integer,list tidak kosong --> list
#konso(e,L) menambahkan integer e sebagai elemen baru di depan list L
#Realisasi
def konso(e,L):
    return [e] + L

#list_is_member: element,List--> boolean
#Is_Member(X,L) bernilai true jika x adalah elemen list L
#realisasi
def list_is_member(x,L):
    if(is_empty(L)):
        return False
    else:
        if(x == first_element(L)):
            return True
        else:
            return list_is_member(x,tail(L))

#is_set : set --> boolean
#is_set(L) memberi keluaran true bila merupakan himpunan dan false bila bukan himpunan
#Realisasi
def is_set(L):
    if(is_empty(L)):
        return True
    elif(list_is_member(first_element(L),tail(L))):
        return False
    else:
        return is_set(tail(L))

#rember : integer,list tak kosong --> list
#rember(e,L) menghapus elemen e dalam list L sehingga dihasilkan list baru tanpa elemen e
#realisasi
def rember(e,L):
    if(is_empty(L)):
        return []
    elif(first_element(L) == e):
        return rember(e,tail(L))
    else:
        return konso(first_element(L) ,rember(e,tail(L)))

# ------------------------------------------------------------

#0
#DefSpek
#NbVokal : list of char --> integer
#NbVokal(l) menghitung banyak elemen vokal dalam list
# Realisasi
def NbVokal(L):
    if(is_empty(L)):
        return 0
    elif(first_element(L) == 'a' or first_element(L) == 'i' or first_element(L) == 'u' or first_element(L) == 'e' or first_element(L) == 'o' or first_element(L) == 'A' or first_element(L) == 'I' or first_element(L) == 'U' or first_element(L) == 'E' or first_element(L) == 'O'):
        return 1 + NbVokal(tail(L))
    else:
        return NbVokal(tail(L))
# aplikasi
l1 = ['w','k','a','a','b','e','A','o']
l2 = ['w','z','k','l']
print("\njawaban no.0 fungsi NbVokal :")
print(NbVokal(l1))
print(NbVokal(l2))

#1
#SumElmt : list of integer --> integer
#SumElmt(L) menghasilkan jumlah semua elemen dalam list
# Realisasi
def SumElmt(L):
    if(is_empty(L)):
        return 0
    else:
        return first_element(L) + SumElmt(tail(L))
# aplikasi
l3 = [3,1,5,6,2]
print("\njawaban no.1 fungsi SubElmt :")
print(SumElmt(l3))

#2
#max : list of integer --> integer
#max(Li) menghasilkan nilai maksimum dari elemen suatu list integer Li
# reaisasi
def Max(Li):
    if IsOneElement(Li):
        return first_element(Li)
    else:
        if(first_element(Li) > Max(tail(Li))):
            return first_element(Li)
        else:
            return Max(tail(Li))
# aplikasi
l6 = [1,3,3,2,1,3,3]
print("\njawaban no 2.1 fungsi max :")
print(Max(l6))

#NbOcc : integer, list of integer --> integer > 0
#NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
# Realisasi
def NbOcc(X,Li):
    if IsOneElement(Li):
        if X == first_element(Li):
            return 1
        else:
            return 0
    else:
        if X == first_element(Li):
            return 1+NbOcc(X,tail(Li))
        else:
            return NbOcc(X,tail(Li))
# Aplikasi
print("\njawaban no 2.3 dengan fungsi NbOcc :")
print(NbOcc(1,l6))

#Vmax : list of integer --> integer
#Vmax(Li) adalah NbOcc(max(Li),Li) yaitu banyaknya kemunculan nilai maksimum dari
#         Li, dengan aplikasi terhadap NbOcc(max(Li),Li)
# Realisasi
def Vmax(Li):
    return NbOcc(Max(Li),Li)
# aplikasi
print("\njawaban no 2.2 fungsi Vmax :")
print(Vmax(l6))

#KEMUNCULAN MAKSIMUM versi-2
#maxNb : list of integer --> <integer, integer>
#maxNb(Li) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer Li; <m,n> = m adalah maks x dari n
#          occurence m dalam list
# Realisasi
def maxNb(Li):
    m = Max(Li)
    n = Vmax(Li)
    return m,n
# Apliasi
print("\njawaban no 2.4 dengan fungsi maxNb : ")
print(maxNb(l6))

#3
#LPrime(L) : list of integer --> list
#LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima
# program bawaan
# -------------------------------------
def faktor(n,count):
    if(n == count):
        return 1
    elif(n % count == 0):
        return 1 + faktor(n,count+1)
    else:
        return faktor(n,count+1)

def IsPrime(n):
    if(faktor(n,1) == 2):
        return True
    else:
        return False
# ------------------------------------
def LPrime(L):
    if is_empty(L):
        return L 
    else:
        if IsPrime(first_element(L)):
            return konso(first_element(L),LPrime(tail(L)))
        else:
            return LPrime(tail(L))
# Aplikasi
l7 = [2,3,4,5,6,7,8,9,1,21,33,11,56,13,2,2]
print("\njawaban no 3 dari fungsi LPrime :")
print(LPrime(l7))
# print(konso(first_element(l6),l7))

#4
#InsertAfter: list --> list
#InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e
def InsertAfter(L,x,e):
    if(is_empty(L)):
        return L
    elif(first_element(L) == e):
        return konso(first_element(L),konso(x,InsertAfter(tail(L),x,e)))
    else:
        return konso(first_element(L),InsertAfter(tail(L),x,e))
l10 = [0,1,2,3,4,5,3,6,7,8]
print("\njawaban no 4 dari fungsi InsertAfter :")
print(InsertAfter(l10,21,3))
# print(is_set(l6))

#5
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2
def MakeMinus(H1,H2):
    if(is_set(H1) and is_set(H2)):
        if(is_empty(H1) or is_empty(H2)):
            return H1
        elif(list_is_member(first_element(H1),H2)):
            return MakeMinus(tail(H1),H2)
        else:
            return konso(first_element(H1),MakeMinus(tail(H1),H2))
    else:
        return "bukan set"

H1 = [1,2,3,4,5,6,7,100]
H2 = [5,6,7,8,9,10,11]
print("\njawaban no 5 dari fungsi MakeMinus :")
print(MakeMinus(H1,H2))

#6
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya

def MakeKomplemen(H1,H2):
    if(is_set(H1) and is_set(H2)):
        if(is_empty(H1)):
            return H2
        elif(is_empty(H2)):
            return H1
        elif(is_empty(H1) and is_empty(H2)):
            return []
        elif(list_is_member(first_element(H1),H2)):
            return MakeKomplemen(tail(H1),rember(first_element(H1),H2))
        elif(list_is_member(first_element(H2),H1)):
            return MakeKomplemen(tail(H2),rember(first_element(H2),H1))
        elif(not(list_is_member(first_element(H1),H2))):
            return konso(first_element(H1),MakeKomplemen(tail(H1),H2))
        elif(not(list_is_member(first_element(H2),H1))):
            return konso(first_element(H2),MakeKomplemen(H1,tail(H2)))
    else:
        return "bukan set"

H3 = [3,2,4,5,1,23,45,6,8,9,0]
H4 = [1,3,2,45,4,7,8,11,0]

H5 = [100,101,102,200]
H6 = [12,200,201,202]

H7 = [3,4,5]
H8 = [6,7,8]
print("\njawaban no 6 dari fungsi MakeKomplemen :")
print(MakeKomplemen(H3,H4))
print(MakeKomplemen(H5,H6))
print(MakeKomplemen(H7,H8))
print("\n")









    
