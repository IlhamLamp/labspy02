#program menampilkan angka terbesar dari 3 inputan

a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

if (a > b) and (a > c):
    print('Nilai a paling besar, yaitu', a)
elif (b > a) and (b > c):
    print('Nilai b paling besar, yaitu', b)
else:
    print('Nilai c paling besar, yaitu', c)
