# Judul : Least Square          jarak(x1,y1,x2,y2)

# Nama File : praktikum_LeastSquare.py
# Pembuat : Benhard Simanullang
# Tanggal : 21 September 2020
# Deskripsi : digunakan untuk mencari jarak antara titik

# Definisi dan Spesifikasi
# jarak : 4 integer ----> real
# jarak(x1,y1,x2,y2) fungsi ini di gunakan untuk mencari jarak antara x1,y1 dengan x2,y2

import math
#realisasi
def jarak(x1,y1,x2,y2):return print (math.sqrt((x1-x2)**2 + (y1-y2)**2))

#aplikasi
jarak(2,0,4,0)
jarak(2,2,3,3)
jarak(3,3,4,4)
jarak(3,3,6,6)
