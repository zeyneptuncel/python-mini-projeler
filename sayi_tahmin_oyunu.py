# 3 tahminle rakamı tahmin etme oyunu 
import random

while True:
    print("Hoşgeldiniz...")
    sayi=random.randint(0,10)
    hak=3
    while hak!=0:
        tahmin=int(input("Tahmininizi Giriniz: "))
        if sayi==tahmin:
          print("Doğru Bildiniz")
          hak=0
          son=input("\n Tekrar oynamak için: R oyundan çıkmak için: Q")
          if son.lower() == "r":
             print("\n")
             break
          if son.lower() == "q":
             print("Oyundan çıkılıyor....")
             break
          break
    
             
        else:
          print("Yanlış")
          hak=hak-1
    if hak==0:
       print("Maalesef hakkınız kalmadı Sayı: ",sayi)
       son=input("\n Tekrar oynamak için: R oyundan çıkmak için: Q")
       if son.lower() == "r":
        print("\n")
       if son.lower() == "q":
        print("Oyundan çıkılıyor....")
        break 

 

    

 