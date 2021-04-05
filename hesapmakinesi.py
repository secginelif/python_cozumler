def topla(sayi1,sayi2):
    return sayi1 + sayi2
def cıkar(sayi1,sayi2):
    return sayi1 - sayi2
def carp(sayi1,sayi2):
    return sayi1 * sayi2  
def bol(sayi1,sayi2):
    return sayi1 / sayi2 



print("Operasyon?")
print("1 : Topla")
print("2 : Cıkar")
print("3 : Carp")
print("4 : Böl")


secenek = input("Operasyon:")
sayi1 = input("sayi1: ")
sayi2 = input("sayi2: ")

if secenek == '1':
    print("Toplam: " + str(topla(sayi1,sayi2)))