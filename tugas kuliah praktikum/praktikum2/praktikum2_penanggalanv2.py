#judul : penanggalan vers 2         harike1900(d,m,y)

#Nama file : praktikum2_penanggalanv2.py
#pembuat : Benhard simanullang
#tanggal : 30 september 2020
#deskripsi : menghitung jumlah hari yang sudah di lewati
#termasuk tahun kabisat

#Definisi dan spesifikasi
#dpm : integer[1..12] ---> integer[1..365]
#dpm(a) memberikan total hari yang telah di tempuh sebagai output
#yang berdasar dari input a sebagai bulan yang telah di tempuh 

#harike1900 : integer[1..31],integer[1..12],integer[1900..1999] ---> integer[1..366]
#harike1900(d,m,y) menghitung jumlah hari yang telah di lewati di hitung dari awal tahun
#dengan d sebagai hari m sebagai bulan dan y sebagai tahun
#dan sudah memperhitungkan tahun kabisat dan menggunakan fungsi antara dpm(a)

#realisasi
def dpm(a):
    if a == 1:return 1
    elif a == 2: return 32
    elif a == 3: return 60
    elif a == 4: return 91
    elif a == 5: return 121
    elif a == 6: return 152
    elif a == 7: return 182
    elif a == 8: return 213
    elif a == 9: return 244
    elif a == 10: return 274
    elif a == 11: return 305
    elif a == 12: return 335

def kabisat(y):
    return ((y%4 == 0) and (y%100 != 100)) or (y//400 == 0)

def harike1900(d,m,y):
    if(m > 2 and kabisat(y)):
        return print(dpm(m)+d)
    else:
        return print(dpm(m)+d-1)

#aplikasi
harike1900(1,3,1920)
harike1900(1,3,1929)
harike1900(20,5,1933)
harike1900(20,5,1980)
