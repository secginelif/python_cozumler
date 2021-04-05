class Matematik :
    def Topla(self,sayi1,sayi2):
        return sayi1 + sayi2

    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2

    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2

    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2           
mat = Matematik()

print(mat.carp(4,6))