# Nama file : Praktikum4_rekursif
# Pembuat : Benhard simanullang
# tanggal : 27 Oktober 2020
# Deskripsi : beberapa aplikasi dari metode rekursif

# pengurangan no 1
# DEFINISI DAN SPESIFIKASI
# kurang : 2 integer --> integer
# mengembalikan nilai hasil dari pengurangan x dengan y
# REALISASI
def kurang(x,y):
    if(y==0):
        return x
    elif(x<0 or y<0):
        return 1 + kurang(x,y+1)
    else:
        return kurang(x,y-1)-1
# APLIKASI
print(kurang(20,13))

# perkalian no 2
# DEFINISI DAN SPESIFIKASI
# kali : 2 integer --> integer
# mengembalikan nilai hasil perkalian x dengan y
# REALISASI
def kali(x,y):
    if(y==0 or x==0):
        return 0
    elif(y<0):
        return (x + kali(x,-(y)-1))*-1
    else:
         return (x + kali(x,y-1))
# APLIKASI
print(kali(2,4)) 

# pembagian no 3
# DEFINISI DAN SPESIFIKASI
# bagi : 2 integer --> integer
# mengembalikan nilai hasil dari pembagian x dengan y
# REALISASI
def bagi(x,y):
    if (x <= 0):
        return 0
    else:
        return 1 + bagi(x-y, y)
# APLIKASI
print(bagi(4,2))

# pangkat no 5
# DEFINISI DAN SPESIFIKASI
# pangkat : 2 integer --> integer
# mengembalikan nilai dari a pangkat b
# REALISASI
def pangkat(a,b):
    if(b==0):
        return 1
    else:
        return a*pangkat(a,b-1)
# APLIKASI
print(pangkat(3,2))

# kelipatan 3 no 6
# DEFINISI DAN SPESIFIKASI
# kel3 : integer --> integer
# mengembalikan nilai kelipatan 3 ke n
# REALISASI
def kel3(n):
    if(n==0):
        return 0
    else:
        return 3 + kel3(n-1)
# APLIKASI
print(kel3(5))

# deret bilangan no 7
# DEFINISI DAN SPESIFIKASI
# total : integer --> integer
# mengembalikan nilai jumlah bil bulat positif sampai n
# REALISASI
def total(n):
    if(n==0):
        return 0
    else:
        return total(n-1) + n
# APLIKASI
print(total(5))

# deret aritmatika no 8
# DEFINISI DAN SPESIFIKASI
# arit_kel3 : integer --> integer
# mengembalikan nilai deret aritmatika sampai n dengan beda 3 
# REALISASI
def arit_kel3(n):
    if(n==0):
        return 0
    else:
        return 3*n + arit_kel3(n-1)
# APLIKASI
print(arit_kel3(4))

# deret geometri no 9
# DEFIINISI DAN SPESFIFIKASI
# geo_kel3 : integer --> integer
# mengembalikan nilai deret geometri sampai n dengan rasio 3
# REALISASI
def geo_kel3(n):
    if(n==0):
        return 0
    else:
        return 1 + 3*geo_kel3(n-1)
# APLIKASI
print(geo_kel3(3))

# menghitung deret no 10
# DEFINSI DAN SPESIFIKASI
# kuadratan : integer --> integer
# mengembalikan nilai deret kuadrat untuk setiap n
# REALISASI
def kuadratan(x):
    if x == 0:
        return 0
    else:
        return kuadratan(x-1) + x*x
# APLIKASI
print(kuadratan(4))

