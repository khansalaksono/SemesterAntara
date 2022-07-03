# Apabila diberikan matriks 3x3, buat kode Python untuk menghitung baris ke-2 dikurangi baris ke-1 dan baris ke-3 dikurangi baris ke-2, dst. 
# Buat program yang berlaku untuk nxn dan nxm, TIDAK hanya 3x3 

import numpy as np
array = [] # membuat array kosong
baris = int(input("Jumlah baris: ")) # input jumlah baris
kolom = int(input("Jumlah kolom: ")) # input jumlah kolom

elemen = baris * kolom # Jumlah elemen
for i in range(0, elemen): 
    print("Angka", i+1, ":")
    angka = int(input())
    array.append(angka) # Menambahkan elemen ke array

array = np.array(array) # Membuat array numpy dari list array
array = array.reshape(baris, kolom) # Membuat array dengan bentuk baris dan kolom

print("\nMatriks:")
print(array)
print()

for i in range(0, baris):
    try:
        a = array[i, 0:kolom] # i menyatakan baris, 0:kolom menyatakan kolom dari index 0 hingga kolom terakhir
        b = array[i+1, 0:kolom] # i+1 menyatakan baris setelah baris i, 0:kolom menyatakan kolom dari index 0 hingga kolom terakhir
        hasil = b - a 
        print("Hasil pengurangan baris", i+2, "dengan baris", i+1, ":")
        print(hasil), print()
        
    except IndexError: # Jika baris yang dijumlahkan dengan baris sebelumnya melebihi jumlah baris
        break  # Berhenti
