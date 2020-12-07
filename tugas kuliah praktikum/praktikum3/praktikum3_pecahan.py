# Judul : pecahan

# nama file : praktikum3_pecahan.py
# pembuat : Benhard simanullang
# tanggal : 7 Oktober 2020
# deskripsi : membuat tipe bentukan pecahan beserta konstruktor dan selektornya

# REALISAI KONSTRUKTOR DAN SELEKTOR
# KONSTRUKTOR
# --------------------------------
# DEFINISI TYPE
# type pecahan : <a:integer,b:integer>
# <a,b> a menyatakan pembilang pecahan dan b menyatakan penyebut pecahan

# DEFINISI DAN SPESIFIKASI DARI KONSTRUKTOR
# pecahan: 2 integer --> pecahan
# pecahan(n,d) definisi ini di gunakan untuk menanamkan type integer untuk mewakili nilai pembilang dan penyebut dari suatu pecahan
class pecahan:
    def __init__(self,n,d):
        self.a = n
        self.b = d

# SELEKTOR
# --------------------------------
# DEFINSI DAN SPESIFIKASI SELEKTOR
# pemb: pecahan --> integer
# pemb(p) memberikan pembilang dari pecahan p
def pemb(p):
    return p.a

# peny: pecahan --> integer
# peny(p) memberikan penyebut dari pecahan p
def peny(p):
    return p.b


# DEFINISI DAN SPEFIFIKASI FUNGSI
# -------------------------------
# addP : 2 pecahan --> pecahan
# addP(p1,p2) merupakan fungsi yang bertugas untuk menambahkan pembilang dan penyebut pecahan p1 
# dengan pecahan p2 , memiliki 2 keluran berupa pembilang dan penyebut nya

# subP : 2 pecahan --> pecahanr
# subP(p1,p2) merupakan fungsi yang bertugas untuk menguragi pembilang dan penyebut pecahan p1
# dengan pembilang dan penyebut pecahan p2 , memiliki 2 keluran berupa pembilang dan penyebut nya

# mulP : 2 pecahan --> pecahan
# mulP(p1,p2) merupakan fungsi yang bertugas untuk mengalikan pembilang dan penyebut pecahan p1
# dengan pembilang dan penyebut pecahan p2 , memiliki 2 keluran berupa pembilang dan penyebut nya

# divP : 2 pecahan --> pecahan
# divP(p1,p2) merupakan fungsi yang bertugas untuk membagi pembilang dan penyebut pecahan p1
# dengan pembilang dan penyebut pecahan p2 , memiliki 2 keluran berupa pembilang dan penyebut nya

# realP : 1 pecahan --> real
# realP(p1) merupakan fungsi yang di gunakan untuk merubah pecahan p1 ke dalam bentuk pecahan desimal
# dengan cara membagi pembilang dengan penyebut nya

# DEFINISI DAN SPESIFIKASI PREDIKAT
# ---------------------------------
# iseqp : 2 pecahaan --> boolean
# iseqp(p1,p2) merupakan fungsi yang mengecek apakah besar dari pecahan p1 
# sama dengan pecahan p2

# isltp : 2 pecahaan --> boolean
# isltp(p1,p2) merupakan fungsi yang mengcek apakah nilai dari pecahan p1 lebih sedikit
# dari pecahan p2 , fungsi ini menggunakan fungsi antara realP(p1) untuk menghasil kan nilai pecahan desimal

# isgtp : 2 pecahaan --> boolean 
# isgtp(p1,p2) merupakan fungsi yang mengcek apakah nilai dari pecahan p1 lebih besar
# dari pecahan p2 , fungsi ini menggunakan fungsi antara realP(p1) untuk menghasil kan nilai pecahan desimal


p1 = pecahan(2,5)
p2 = pecahan(3,7)

# REALISASI FUNGSI DAN PREDIKAT

def addP(p1,p2):
    return ((pemb(p1)*peny(p2)+pemb(p2)*peny(p1)),(peny(p1)*peny(p2)))

def subP(p1,p2):
    return ((pemb(p1)*peny(p2)-pemb(p2)*peny(p1)),(peny(p1)*peny(p2)))

def mulP(p1,p2):
    return (pemb(p1)*pemb(p2),peny(p1)*peny(p2))

def divP(p1,p2):
    return (pemb(p1)*peny(p2),peny(p1)*pemb(p1))

def realP(p1):
    return (pemb(p1)/peny(p1))

def iseqp(p1,p2):
    return (pemb(p1)*peny(p2) == pemb(p2)*peny(p1))

def isltp(p1,p2):
    if(realP(p1) < realP(p2)):
        return True
    else: return False 

def isgtp(p1,p2):
    if(realP(p1) > realP(p2)):
        return True
    else : return False


#aplikasi

print(addP(p1,p2))
print(subP(p1,p2))
print(mulP(p1,p2))
print(divP(p1,p2))
print(realP(p1))
print(iseqp(p1,p2))
print(isltp(p1,p2))
print(isgtp(p1,p2))

