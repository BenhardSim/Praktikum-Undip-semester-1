#Judul : wujud air              wujud_air(c)

#Nama file : praktikum2_wujudAir.py
#Pembuat : Benhard simanullang
#Tanggal : 30 september 2020
#Deskripsi : memberitahu wujud air dalam suhu tertentu

#Definsi dan spesifikasi
#wujud_air : integer ---> string
#wujud_air(c) memberikan keluaran wujud air berdasarkan input dari nilai c

#realisasi
def wujud_air(c):
    if(c>=100):
        return print("wujud gas/uap")
    elif(0<c<100):
        return print("wujud cair")
    elif(c<=0):
        return print("wujud solid/padat")

#aplikasi
wujud_air(120)
wujud_air(90)
wujud_air(-10)
