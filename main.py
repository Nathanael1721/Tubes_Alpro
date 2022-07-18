print("Pilihan Menu")
print("1. Tambahkan Data\n2. Lihat Data\n3. Cari Data")
menu = int(input("Silahkan Memilih Menu = "))

#if menu = 1
    

A = input("Masukkan Nama Anda = ")
B = int(input("Masukkan NIK Anda =  "))
C = input("Masukkan Tanggal Lahir Anda(Tahun-Bulan-Tanggal) = ")
D = input("Masukkan Agama Anda = ")
E = input("Masukkan Pekerjaan Anda = ")
F = input("Masukkan Pendidikan Terakhir Anda = ")

f = open("data.txt", "a")
f.write(A+"*"+str(B)+"*"+C+"*"+D+"*"+E+"*"+F+"*"+"\n")

f.close

f = open("data.txt", "r")
print(f.read())