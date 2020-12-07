#judul : pembagian akar             pembagian_akar(a,b,c)

#Nama file : praktikum2_pembagianakar.py
#Pembuat : Benhard simanullang
#Tanggal : 30 september 2020
#Deskripsi : menghitung pembagian antara akar terbesar dan terkecil
#dari suatu persamaan kuadrat

#Definsi dan spesifikasi
#min2 : 2 integer ---> integer
#min2(x,y) mengembalikan nilai terkecil antara nilai x dan y

#max2 : 2 integer ---> integer
#max2(x,y) mengembalikan nilai terbesar antara nilai x dan y

#pembagian_akar : integer != 0 , integer , integer ---> real
#pembagian_akar(a,b,c) mengembalikan hasil pembagian antara akar terbesar dan akar terkecil
#dari persamaan kuadrat dengan koofisien a,b,c dan menggunakan min2(x,y) dan max2(x,y) 
#sebagai fungsi perantara


#realisasi
import math
def max2(x,y):
    if(x>y):return x
    else:return y

def min2(x,y):
    if(x<y):return x
    else:return y


def pembagian_akar(a,b,c):
    k = (-b + math.sqrt(b*b-4*a*c))/2*a
    l = (-b - math.sqrt(b*b-4*a*c))/2*a
    return max2(k,l)/min2(k,l)

#aplikasi
print(pembagian_akar(1,-6,8))
    
