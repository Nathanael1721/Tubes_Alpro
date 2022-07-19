from traceback import print_tb


def menu():
    import os
    os.system("cls")
    print("===================================")
    print(" DATA KEPENDUDUKAN ")
    print("===================================")
    print("1. Melihat Data")
    print("2. Menambah Data")
    print("3. Mencari Data")
    print("4. Mengubah Data")
    print("5. Menghapus Data")
    print("6. Urutkan Data")    
    print("7. Keluar")
    print("===================================")
    
    no = int(input("\nMasukan Menu Yang Anda Inginkan : "))
    no_menu(no)
    
def no_menu(a):
    if a == 1:
        lihat_data()
    elif a == 2:
        tambahkan_data()
    elif a == 3:
        cari_data()
    elif a == 4:
        update_data()
    elif a == 5:
        hapus_data()
    elif a == 6:
        urutkan_data()
    elif a == 7:
        keluar_program()    
#================================================#
def lihat_data():
    print("\n================================")
    print("Anda Berada Pada Menu Menampilkan Data ")
    print("================================")
    f = open("data.txt")
    isi = f.readlines()
    isi.sort
    if len(isi) == 0 :
        print("Data Masih Kosong")
    else :
        i = 1
        for x in isi:
            pisah = x.split(",")
            print("Data", str(i))
            print("Nama                : "+pisah[0])
            print("Umur                : "+pisah[1],"Tahun")
            print("Asal                : "+pisah[2])
            print("Agama               : "+pisah[3])
            print("Pendidikan Terakhir : "+pisah[4])

            i +=1
    print("Tekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#=================================================#
def tambahkan_data():
    print("\n===============================")
    print("Anda Berada Pada Menu Menambahkan Data")
    print("===============================")
    print("\nMasukkan Data Anda : ")
    print("_______________________")
    n = input("Nama                : ")
    u = input("Umur                : ")
    a = input("Asal                : ")
    b = input("Agama               : ")
    c = input("Pendidikan Terakhir : ")
    f = open("data.txt", "a")
    f.writelines([n+","+u+","+a+","+b+","+c+"\n"])
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#==================================================#
def cari_data():
    print("\n==================================")
    print("Anda Berada Pada Menu Mencari Data")
    print("==================================")
    f = open("data.txt")
    nc = input("Masukkan Nama Yang Ingin Anda Cari : ")
    isi = f.readlines()
    
    idx = 0
    #urut = 12
    for a in isi:
#        print(a)
        x = a.split(",")
        if nc in x :
            print("Data Ditemukan !!!")
            print("Nama                : "+x[0])
            print("Usia                : "+x[1])
            print("Asal                : "+x[2])
            print("Agama               : "+x[3])
            print("Pendidikan Terakhir : "+x[4])
        idx += 1
        # if x[0] == nc:
        #     print("\nData Ditemukan, Data Ke : ", urut)
        #     print("----------------------------")
        #     print("Nama : "+x[0])
        #     print("Usia : "+x[1])
        #     print("Asal : "+x[2])
        #     urut += 1
        #     continue
        #     breakasd asdas asd
        # idx += 1
        # if idx == len(isi):
        #     print("DATA TIDAK DITEMUKAN !!!")
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#===================================================#
def update_data():
    print("\n==============================")
    print("Anda Berada Pada Menu Update Data")
    print("==============================")
    upnama = input("Masukkan Nama Data Yang Ingin Diubah : ")
    print("\nMasukkan Data Baru !!")
    print("_______________________")
    nb = input("Masukkan Nama Baru             : ")
    ub = input("Masukkan Umur Baru             : ")
    ab = input("Masukkan Asal Baru             : ")
    bb = input("Masukkan Agama Baru            : ")
    cb = input("Masukkan Pendidikan Akhir Baru : ")
    
    f = open("data.txt")
    isi = f.readlines()
    idx = 0
    for x in isi :
        data = x.split(",")
        if data[0] == upnama:
            data[0] = nb
            data[1] = ub
            data[2] = ab 
            data[3] = bb
            data[4] = cb + "\n"
            datax = ",".join(data)
            isi[idx] = datax
            break
        idx += 1
    f.close()
    
    f = open("data.txt","w")
    isi = f.writelines(isi)
    
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#=========================================================#
def hapus_data():
    print("\n=============================")
    print("Anda Berada Pada Menu Menghapus Data")
    print("=============================")
    
    hapus = input("Masukkan Nama Penduduk yang ingin dihapus : ")
    
    f = open("Tugas Akhir\data.txt")
    isi = f.readlines()
    isi.sort()
    
    idx = 0
    for i in isi:
        h = i.split(",")
        if h[0] == hapus :
            del(isi[idx])
            print("\nData Anda Berhasil Dihapus")
        idx += 1
    f.close()
    
    f = open("data.txt","w")
    isi = f.writelines(isi)
    
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()
#=======================================================#

def urutkan_data():
    f = open("data.txt","r")
    isi = f.readlines()
    isi.sort()
    for a in isi:
        x = a.split(",")
        print("Nama                : "+x[0])
        print("Usia                : "+x[1])
        print("Asal                : "+x[2])
        print("Agama               : "+x[3])
        print("Pendidikan Terakhir : "+x[4])
    print("\nTekan [Enter] Untuk Melanjutkan")
    f.close()
    input()
    menu()

def keluar_program():
    print("\nTekan [Enter] Untuk Melanjutkan")

menu()
