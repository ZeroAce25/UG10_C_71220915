datamenu = str(input("Masukkan daftar pesanan : "))
firstmenu = [datamenu]
print("Daftar pesanan : ",firstmenu)
newmenu = str(input("Masukkan pesanan yang ingin ditambahkan : "))
if newmenu in datamenu:
    print(newmenu.upper(), "sudah berada dalam daftar pesanan")
else:
    secondmenu = [datamenu, newmenu]
    print(secondmenu)
