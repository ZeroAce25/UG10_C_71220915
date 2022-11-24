print("========== Pilih menu ==========")
print(' 1. Tambah ')
print(' 2. Kurang ')
print(' 3. Kali ')
print(' 4. Bagi ')
angka_1 = int(input("Masukkkan angka pertama: "))
angka_2 = int(input("Masukkkan angka kedua: "))
operasi = input("Pilihan Anda: ")
if operasi == '1':
    hasil = angka_1+angka_2
    print("hasil: ", hasil )
elif operasi == '2':
    hasil = angka_1-angka_2
    print("hasil: ", hasil )
elif operasi == '3':
    hasil = angka_1*angka_2
    print("hasil: ", hasil )
elif operasi == '4':
    hasil = angka_1%angka_2
    print("hasil: ", hasil )



