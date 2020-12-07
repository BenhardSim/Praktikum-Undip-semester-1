#Judul : jenis segitiga            setiga(a,b,c)

#Nama file : praktikum2_cekSegitiga.py
#Pembuat : Benhard simanullang
#Tanggal : 30 september 2020
#Deskripsi : memberitahu jenis segitiga berdasarkan panjang sisi nya

#Definisi dan spesifikasi
#segitiga : 3 integer > 0 ---> string
#segitiga(a,b,c) memberitahu jenis segitiga berdasar nilai a,b,dan c sebagai sisi-sisi nya


#realisasi
def segitiga(a,b,c):
    if(a==b==c):
        return print("segitiga sama sisi")
    elif((a==b and a!=c) or (b==c and a!=c) or (c==a and a!=b)):
        return print("segitiga sama kaki")
    elif(a!=b and b!=c and c!=a):
        return print("segitiga sembarang")

#aplikasi
segitiga(2,2,2)
segitiga(2,2,1)
segitiga(1,2,3)
