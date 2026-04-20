boycm = int(input("Boyunuzu Giriniz(cm) : "))
kilo= int(input("Kilonuzu Giriniz(kg) : "))
boy=boycm/100
bki=kilo/(boy*boy)
if bki<18.5:
    print("İdeal kilonun altındasın, biraz kilo alman sağlığın için iyi olabilir")
elif bki>=18.5 and bki<25:
    print("Harikasın! Tam ideal kilondasın, böyle devam et")
elif bki>=25 and bki<30:
    print("İdeal kilonun biraz üstündesin, porsiyonlara dikkat etmek iyi olabilir")
elif bki>=30 and bki<100:
    print("Obez kategorisindesiniz, sağlığınız için dikkat etmelisiniz.")
else:
    print("Hata, Verileri yanlış girilmiş olabilir")
