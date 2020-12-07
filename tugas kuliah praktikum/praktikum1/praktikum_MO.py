#Judul : Mean Olympic(MO)       MO(k,l,m,n)

#Nama file : praktikum_MO.py
#pembuat : Benhard Simanullang
#Deskripsi : menghitung nilai rata rata 2 integer
#           dari 4 integer kecuali integer max dan min
#Tanggal : 21 september 2020


#Definisi dan Spesifikasi

#MO :4 integer >= 0 ----> real
    #MO(k,l,m,n)menghitung rata rata 2 integer kecuali bilangan max dan min
    #menghasilkan bilangan real
    #menggunakan fungsi antara min4(a,b,c,d)dan
    #menggunakan fungsi antara max4(a,b,c,d)

#max4 :4 integer > 0 ----> integer
    #max4(a,b,c,d)memberi keluaran nilai terbesar antara 4 integer a,b,c,d
    #menghasilkan tipe data integer
    #menggunakan fungsi antara max2(x,y)

#min4 :4 integer > 0 ----> integer
    #min4(a,b,c,d)memberikan keluaran nilai terkecil antara 4 integer a,b,c,d
    #menghasilkan tipe data integer
    #menggunakan fungsi antara min2(x,y)

#max2 :2 integer > 0 ----> integer
    #max2(x,y)memberikan keluaran nilai terbesar antara 2 integer x,y
    #menghasilkan tipe data integer

#min2 :2 integer > 0 ----> integer
    #min2(x,y)memberikan keluaran nilai terkecil antara 2 integer x,y


#Realisasi
def max2(x,y):return (x+y+abs(x-y))//2
def min2(x,y):return (x+y-abs(x-y))//2
def max4(a,b,c,d):return max2(max2(a,b),max2(c,d))
def min4(a,b,c,d):return min2(min2(a,b),min2(c,d))

def MO(k,l,m,n):return (k+l+m+n-max4(k,l,m,n)-min4(k,l,m,n))/2


#Aplikasi

print(MO(8,12,10,20))
