#Judul : APAKAH VALID           isValid(x)

#Nama file : praktikum_VALID.py
#Pembuat : Benhard Simanullang
#Tanggal : 21 September 2020
#Deskripsi : mengecek apakah input yang di masukkan sudah seseuai batas nilai yang di atur

# Definisi dan Spesifikasi
# IsValid : integer ----> boolen
# Fungsi ini mengecek apakah nilai integer yang di input berada di bawah 5 dan di atas 500

#Realisasi
def IsValid(x):return x<5 or x>500


#Aplikasi
print(IsValid(5))
print(IsValid(0))
print(IsValid(25))
print(IsValid(100))
