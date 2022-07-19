f = open("data.txt","r")
isi = f.readlines()
isi.sort()
#z = 0
#print(isi)
for a in isi:
    x = a.split(",")
    #y = print(x[1])
 #   z += 1
    #print(x[0])
    print(x[0])
#    z += 1
    f.close()
    # print("Nama                : "+x[0])
    # print("Usia                : "+x[1])
    # print("Asal                : "+x[2])
    # print("Agama               : "+x[3])
    # print("Pendidikan Terakhir : "+x[4])
    # data = y
    # data.sort()
    # print(data)

    # data = (x[4])
    # data.sort()
    # print(data)

    # print("Halo semuanya")
#     idx = 0
#     urut = 1
#     for a in isi:
# #        print(a)
#         x = a.split(",")
#         if nc in x :
#             print("Data Ditemukan !!!")
#             print("Nama                : "+x[0])
#             print("Usia                : "+x[1])
#             print("Asal                : "+x[2])
#             print("Agama               : "+x[3])
#             print("Pendidikan Terakhir : "+x[4])
#         idx += 1
#         # if x[0] == nc:
#         #     print("\nData Ditemukan, Data Ke : ", urut)
#         #     print("----------------------------")
#         #     print("Nama : "+x[0])
#         #     print("Usia : "+x[1])
#         #     print("Asal : "+x[2])
#         #     urut += 1
#         #     continue
#         #     breakasd asdas asd
#         # idx += 1
#         # if idx == len(isi):
#         #     print("DATA TIDAK DITEMUKAN !!!")
#     print("\nTekan [Enter] Untuk Melanjutkan")
#     f.close()
#     input()
