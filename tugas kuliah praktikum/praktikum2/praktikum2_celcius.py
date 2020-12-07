#judul : Konversi celcius       konv(c,n)

#Nama file : praktikum2_celcius.py
#Pembuat : Benhard simanullang
#tanggal : 30 september 2020
#Deskripsi : mengkonversi kan suhu celcius ke reamur,kelvin,dan fahrenheit

#Definisi dan spesifikasi
#konv : integer,string ---> integer
#konv(c,n) mengkonversi kan input c yang merupakan celcius ke unit lain berdasarkan input string pada
#n yang di masukkan "k" untuk kelvin,"r" untuk reamur, dan "f" untuk fahrenheit


#realisasi
def konv(c,n):
    if(n == "k"):
        return print(c+273)
    elif(n == "r"):
        return print(0.8*c)
    elif(n == "f"):
        return print(1.8*c + 32)

#aplikasi
konv(10,"k")
konv(10,"r")
konv(10,"f")
