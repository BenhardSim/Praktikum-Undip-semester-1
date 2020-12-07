# Judul : penanggalan                

# nama file : praktikum3_penanggalan.py
# pembuat : Benhard simanullang
# tanggal : 6 oktober 2020
# deskripsi : membuat tipe bentukan date besarta konstruktur dan selektornya

# definisi dan spesifikasi


# REALISASI KONSTRUKTOR DAN SELEKTOR
# CONSTRUCTOR
#######################################################
#######################################################
# DEFINISI TYPE
# type hari : <d:integer>
# <d> adalah sebuah hari/day, dengan d menyatakan tanggal

# DEFINISI DAN SPEIFIKASI KONSTRUKTOR
# hari: integer[1..31] --> hari
# hari(d) definisi ini digunakan untuk menanamkan type integer dengan daerah nilai tertentu supaya mewakili tanggal
class hari:
    def __init__(self,a):
        self.d = a

# DEFINISI TYPE
# type bulan : <m:integer>
# <m> adalah sebuah bulan/month , dengan m menyatakan bulan ke berapa

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# bulan: integer[1..12] --> bulan
# bulan(m) definisi ini digunakan untuk menanamkan type integer dengan daerah nilai tertentu supaya mewakili bulan

class bulan:
    def __init__(self,b):
        self.m = b

# DEFINISI TYPE
# type tahun : <y:integer>
# <y> adalah sebuah tahun/year, dengan y menyatakan tahun keberapa

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# tahun: integer > 0 --> tahun
# tahun(y) definisi ini digunakan untuk menanamkan type integer dengan daerah nilai tertentu supaya mewakili tahun

class tahun:
    def __init__(self,c):
        self.y = c

# DEFINISI TYPE
# type makeadate : <d:hari,m:bulan,y:tahun>
# <d,m,y> merupakan sebuah waktu tanggal,bulan,dan tahun dengan d menyatakan tanggal m menyatakan bulan dan y menyatakan tahun

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeadate : hari,bulan,tahun --> date
# makeadate(d,m,y) menggunakan type bentukan lain yaitu hari,bulan,dan tahun sebagai perantara
# dan tiap hari,bulan,dan tahun itu di tanamkan pada d,m,y pada type bentukan makeadate

class makeadate:
    def __init__(self,day,month,year):
        self.d = day
        self.m = month
        self.y = year
#########################################################
#########################################################

# SELECTOR
#########################################################
#########################################################
# DEFINISI DAN SPESIFIKASI SELEKTOR
# day: hari --> integer[1..31]
# day(a) memberikan hari dari a

def day(a):
    return a.d

# DEFINISI DAN SPESIFIKASI SELEKTOR
# month: bulan --> integer[1..12]
# month(b) memberikan bulan dari b

def month(b):
    return b.m

# DEFINISI DAN SPESIFIKASI SELEKTOR
# year: tahun --> integer > 0
# year(c) memberikan tahun dari c

def year(c):
    return c.y

# DEFINISI DAN SPESIFIKASI SELEKTOR
# date : makeadate --> hari,bulan,tahun
# date(k) memberikan keluaran hari,bulan,tahun dari k

def date(k):
    return k.d,k.m,k.y
########################################################
########################################################

# DEFINISI DAN SPESIFIKASI FUNGSI LAIN
# ------------------------------------
# dpm : integer[1..12] ---> integer[1..365]
# dpm(a) memberikan total hari yang telah di tempuh sebagai output
# yang berdasar dari input a sebagai bulan yang telah di tempuh 

# harike1900 : makeadate ---> integer[1..366]
# harike1900(n) menghitung jumlah hari yang telah di lewati di hitung dari awal tahun
# dengan n merupakan type bentukan makeadate , fungsi dapat berjalan dengan memanggil komponen komponen dari makeadate
# menggunakan fungsi selektor sebagai perantara
# dan sudah memperhitungkan tahun kabisat serta menggunakan fungsi antara dpm(a) dan kabisat(y)

# nextday : makeadate --> makeadate
# nextday(m) merupakan fungsi yang memberitahukan tgl,bulan,dan tahun untuk hari selanjutnya dari date m 
# dengan cara memanggil komponen-komponen dari m
# dengan cara menggunakan fungsi selektor sebagai perantara

# yesterday : makeadate --> makeadate
# yesterday(m) merupakan fungsi yang memberitahukan tgl,bulan,dan tahun untuk hari sebelum nya dari date m
# dengan cara memanggil komponen-komponen dari m
# dengan menggunakan fungsi selektor sebagai perantara

# DEEFINISI DAN SPESIFIKASI PREDIKAT
# -----------------------------------
# iseqd : 2 makeadate --> boolean
# iseqd(a,b) merupakan fungsi yang mengecek apakah jumlah hari dari date a sama dengan date b
# menggunakan fungsi harike1900(n) sebagai perantara  , bila benar memberi keluaran true bila tidak false

# isbefore : 2 makeadate --> boolean
# isbefore(a,b) merupakan fungsi yang mengecek apakah date a itu sebelum date b dengan mengambil komponen komponen pada date
# lalu membandingkan nya

# isafter : 2 makeadate --> boolean
# isafter(a,b) merupakan fungsi yang mengecek apakah date a itu adalah sesudah date b dengan mengambil komponen komponen pada date
# lalu membandingkan nya

# iskabisat : makeadate --> boolean
# iskabisat(a) merupakan fungsi yang mengecek apakah date a merupakan tahun kabisat atau tidak 
# fungsi bekerja dengan cara mengambil komponen tahun dari date tersebut

# REALISASI FUNGSI
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

def harike1900(n):
    if(month(n) > 2 and kabisat(year(n))):
        return dpm(month(n))+day(n)
    else:
        return dpm(month(n))+day(n)-1

def kabisat(y):
    return ((y%4 == 0) and (y%100 != 100)) or (y//400 == 0)
# fungsi mencari tgl untuk hari selanjutnya
def nextday(m):
    # bulan dengan 31 hari kecuali bulan 12
    if(month(m) == 1 or month(m) == 3 or month(m) == 5 or month(m) == 7 or month(m) == 8 or month(m) == 10 ):
        if(day(m) < 31):
            return makeadate(day(m) + 1, month(m), year(m))
        else:
            return makeadate(1, month(m) + 1, year(m))
    # logika untuk bulan 2
    elif(month(m) == 2):
        # untuk bukan tahun kabisat saat di bawah tgl 28
        if(day(m) < 28):
            return makeadate(day(m) + 1, month(m), year(m))
        # untuk tahun kabisat
        elif(kabisat(year(m))):
            # kalau tanggal 28 pada saat tahun kabisat
            if(day(m) <= 28):
                return makeadate(day(m) + 1, month(m), year(m))
            # kalau bukan tanggal 28 pada saat tahun kabisat
            else:
                return makeadate(1, month(m) + 1, year(m))
        # untuk bukan tahun kabisat pada saat tanggal 28
        else:
            return makeadate(1, month(m) + 1, year(m))
    # untuk bulan dengan 30 hari
    elif(month(m) == 4 or month(m) == 6 or month(m) == 9 or month(m) == 11):
        # untuk tanggal kurang dari 30
        if(day(m) < 30):
            return makeadate(day(m) + 1, month(m), year(m))
        # untuk pada saat tepat tanggal 30
        else:
            return makeadate(1, month(m) + 1, year(m))
    # logika untuk bulan 12
    elif(month(m) == 12):
        # untuk tanggal kurang dari 31 pada saat desember
        if(day(m) < 31):
            return makeadate(day(m) + 1, month(m), year(m))
        # untuk tanggal tepat tangga 31
        else:
            return makeadate(1,1,year(m)+1) 

def iseqd(a,b):
    return (harike1900(a) == harike1900(b) and year(a) == year(b))

def isbefore(a,b):
    if(year(a) < year(b)):
        return True
    elif(month(a) < month(b) and year(a) == year(b)):
        return True
    elif(day(a) < day(b) and month(a) == month(b) and year(a) == year(b)):
        return True
    else:
        return False

def isafter(a,b):
    if(year(a) > year(b)):
        return True
    elif(month(a) > month(b) and year(a) == year(b)):
        return True
    elif(day(a) > day(b) and month(a) == month(b) and year(a) == year(b)):
        return True
    else:
        return False

def iskabisat(a):
    return (year(a) % 4 == 0 and year(a) % 100 != 0) or year(a)//400 == 0

def yesterday(m):
    # untuk tgl satu pada bulan apapun
    if(day(m) == 1):
        # untuk bulan dengan jumlah tanggal 31 kecuali tgl 3 dan 1
        if(month(m) == 12  or month(m) == 5 or month(m) == 7 or month(m) == 8 or month(m) == 10):
            return makeadate(30,month(m)-1,year(m))
        # untuk khusus bulan 3 karena 1 hari sebelum nya adalah bulan 2
        elif(month(m) == 3):
            # satu hari sebelum satu maret untuk tahun kabiat
            if(kabisat(year(m))):
                return makeadate(29,2,year(m))
            # satu hari sebelum satu maret(3) untuk bukan tahun kabisat
            else:
                return makeadate(28,2,year(m))
        # untuk bulan dengan jumlah tanggal 30/28/29
        elif(month(m) == 4 or month(m) == 6 or month(m) == 9 or month(m) == 11 or month(m) == 2):
            return makeadate(31,month(m) - 1,year(m))
        # khusus untuk pada bulan januari
        elif(month(m) == 1):
            return makeadate(31,12,year(m)-1)
    # untuk bukan tgl satu pada bulan apapun
    else:
        return makeadate(day(m) - 1,month(m),year(m))

# APLIKASI
# membuat variable dengan type bentukan
h1 = hari(28)
b1 = bulan(2)
t1 = tahun(1980)
d1 = makeadate(h1.d,b1.m,t1.y)

h2 = hari(31)
b2 = bulan(12)
t2 = tahun(1920)
d2 = makeadate(h2.d,b2.m,t2.y)

h3 = hari(1)
b3 = bulan(3)
t3 = tahun(1980)
d3 = makeadate(h3.d,b3.m,t3.y)

print(date(d1))
print(date(d2))
print(date(d3))

# mencari tanggal untuk hari selanjutnya d1 dan d2
m1 = nextday(d1)
print(date(m1))

m2 = nextday(d2)
print(date(m2))

m3 = nextday(d3)
print(date(m3))

# mencari tanggal untuk hari sebelum d3
y1 = yesterday(d1)
print(date(y1))

y2 = yesterday(d2)
print(date(y2))

y3 = yesterday(d3)
print(date(y3))

# mencari apakah kedua tanggal sama dan apakah merupakan tahun kabisat
print(iseqd(d1,d2))
print(iskabisat(d1))
print(iskabisat(d2))
print(iskabisat(d3))

# mengecek apakah d1 merupakan taggal sebelum d2
print(isbefore(d1,d2))

# mengecek apakah d1 merupakan tanggal setelah d2
print(isafter(d1,d2))











