# 5 soruluk rastgele carpma işlemleri sorulacaksonunda puan gösterilcek
import random

while True:
 puan = 0
 for i in range(10):
    print("\033[0m")
    a = random.randint(1,10)
    b = random.randint(1,10)
    cevap = a*b
    print("Soru: ", i+1)
    print(f"{a} x {b} = ?")
    tahmin= int(input("Cevabınız: "))
    if tahmin == cevap:  
        print("\033[92mTebrikler!\033[0m")
        puan += 10
    else:
        print("\033[91mYanlış Cevap!\033[0m")

 print(f"--------------\nToplam puan: {puan}")
 tekrar = input("\nTekrar oynamak için 'R' tuşuna, çıkmak için herhangi bir tuşa bas: ")
 if tekrar.lower() != 'r': 
        print("Görüşmek üzere!")
        break