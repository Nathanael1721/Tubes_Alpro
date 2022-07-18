
# import module
from tabulate import tabulate
 
# assign data
# mydata = [
#     ["Nikhil", "Delhi"],
#     ["Ravi", "Kanpur"],
#     ["Manish", "Ahmedabad"],
#       ["Prince", "Bangalore"]
# ]
 
mydata = [["Nathan","3507241711020004","17-11-2002","Kristen","Mahasiswa","SMK"]]
# create header
head = ["Nama", "NIK","TTL","Agama","Pekerjaan","Pendidikan"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))