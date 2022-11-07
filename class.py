class mobil(): 
    def __init__(self, merk, price):
        #atribut
        self.merk = merk
        self.price = price

    
        honda = mobil("honda", 600000000)
        mitsubishi = mobil ("mitsubishi", 50000000)
        toyota = mobil ("toyota", 30000000)
        daihatsu = mobil ("daihatsu", 25000000)

        #print(honda.__dict__)
        print("Mobil ini bermerk: " + toyota.merk + "dengan harga Rp." + str(toyota.price))
        print("Mobil ini bermerk: " + mitsubishi.merk + "dengan harga Rp." + str(toyota.price))
        print("Mobil ini bermerk: " + honda.merk + "dengan harga Rp." + str(toyota.price))
        print("Mobil ini bermerk: " + daihatsu.merk + "dengan harga Rp." + str(toyota.price))


def penjumlahan():

    a=int(input("masukkan angka pertama pembelian : "))
    b=int(input("masukkan angka kedua pembelian : "))
    c=a+b
    print("Total Penjumlahan Mobil yang akan di beli ", c)

while True:
    print("MENU")
    print("1. Data mobil yang akan di beli")
    print("2.  Exit")
    choice = int(input("pilihanmu : "))
    if choice == 1:
        penjumlahan()
    elif choice == 2:
        break
    else:
        print("pilihan salah")