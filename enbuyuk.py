sayi1 = int(input("Sayi1:"))
sayi2 = int(input("Sayi2:"))
sayi3 = int(input("Sayi3:"))

if (sayi1>=sayi2) and (sayi1>=sayi3) :
    enBuyuk = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3) :
    enBuyuk = sayi2

else:
    enBuyuk = sayi3
print("en buyuk sayı: ",enBuyuk)
