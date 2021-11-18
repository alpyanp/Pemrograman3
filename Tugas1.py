# Program Python Kalender

import calendar
nama = "Alpyan Padjar Rizki"
nim = "3220609"

def menu():
    print("1. Untuk melihat kalender perbulan")
    print("2. Untuk melihat kalender pertahun")
    print("3. Untuk menentukan hari dari pencarian tanggal")
    print("4. Untuk menentukan tahun kabisat atau bukan")


def bulanan():
    # Untuk melihat kalender perbulan
    tahun = int(input("Masukkan Tahun : "))
    bulan = int(input("Masukkan Bulan : "))
    print (" ") 
    print ("======== {} ========".format(nama))
    print ("Kalender Pada Bulan ke {} Tahun {} :".format(bulan,tahun))
    print ("============== {} ==============".format(nim))
    print (" ")
    print(calendar.month(tahun,bulan))

def tahunan():
    # Untuk melihat kalender pertahun
    tahun1 = int (input ("Masukkan Tahun : "))
    print(calendar.calendar(tahun1))
    
def kabisat():
    yy = int (input ("Masukkan Tahun : "))
    print ("Apakah Tahun {} Merupakan Tahun Kabisat : ".format(yy))
    print (calendar.isleap(yy))
    
def harian():
    print ("Program Menentukan Hari")
    print (" ")
    thn= int(input("Masukkan Tahun : "))
    bln= int (input("Masukkan Bulan : "))
    tgl= int(input("Masukkan Tanggal : "))
    day_week_day= calendar.weekday(thn,bln,tgl)
    print (" ")
    if day_week_day == 0:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Senin".format(tgl,bln,thn))
    if day_week_day == 1:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Selesa".format(tgl,bln,thn))
    if day_week_day == 2:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Rabu".format(tgl,bln,thn))
    if day_week_day == 3:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Kamis".format(tgl,bln,thn))
    if day_week_day == 4:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Jumat".format(tgl,bln,thn))
    if day_week_day == 5:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Sabtu".format(tgl,bln,thn))
    if day_week_day == 6:
        print ("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Minggu".format(tgl,bln,thn))
        
print ("======== {} ========".format(nama))
menu()
opsi = input("Masukan Pilihan : ")
if opsi == 1:
    bulanan()
elif opsi == 2:
    tahunan()
elif opsi == 3:
    harian()
elif opsi == 4:
    kabisat()
else :
    print("Menu tidak ditemukan!")
print ("============== {} ==============".format(nim))
