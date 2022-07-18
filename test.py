#from curses import window
#import tkinter as tk
from gettext import find
import re
from asyncore import read
from traceback import print_tb
from tabulate import tabulate



print("Silahkan Pilih Menu : ")
menu_options = {
    1: 'Menambahkan Data', 
    2: 'Melihat Data',
    3: 'Mencari Data',
    4: 'Keluar',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def menambahkan_data():
     print('Menu \'Menambah Data\'')

def melihat_data():
     
     print('Menu \'Melihat Data\'')      
     
def mencari_data():
     print('Menu \'Mencari Data\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Silahkan Memilih Menu '))
        except:
            print('Menu Yang Anda Pilih Tidak Tersedia, Silahkan Coba Lagi')
        #Check what choice was entered and act accordingly
        if option == 1: #MENAMBAHKAN DATA
           menambahkan_data()
           A = input("Masukkan Nama Anda = ")
           B = int(input("Masukkan NIK Anda =  "))
           C = input("Masukkan Tanggal Lahir Anda(Tahun-Bulan-Tanggal) = ")
           D = input("Masukkan Agama Anda = ")
           E = input("Masukkan Pekerjaan Anda = ")
           F = input("Masukkan Pendidikan Terakhir Anda = ")

           f = open("data.txt", "a")
           f.writelines(A+"*"+str(B)+"*"+C+"*"+D+"*"+E+"*"+F+"*"+"\n3")

           f.close
           
        elif option == 2: # MELIHAT DATA
            f = open("data.txt", "r")
            melihat_data()
            tampilkan = f.readlines()
            for item in tampilkan:
                #print(item)
                isi = item.split("*")
                oke = [[isi[0],isi[1],isi[2],isi[3],isi[4],isi[5]]]
                head = ["Nama", "NIK","TTL","Agama","Pekerjaan","Pendidikan"]
                print(tabulate(oke, headers=head, tablefmt="grid"))

                #print

           # str = tampilkan
            #print(tampilkan[0].split("*"))


        elif option == 3: # CARI DATA
            f = open("data.txt", "r")
            #kata_kata = input("Masukkan Kata Yang Dicari = ")
            #mencari_data()
            dicari = f.readlines()
            #print(kata_kata)
            #if kata_kata in dicari:
            #    print("Ditemukan")
            #else :
            #    print("Data Tidak Ditemukan")
            katanya = input("Masukkan Kata - Kata yang Dicari = ")
            x = dicari.find(katanya)
            print(x)

        elif option == 4:
            print('Terima Kasih')
            exit()
        else:
            print('Menu yang Anda pilih tidak ada, silahkan coba lagi')

#window = tk.Tk()
