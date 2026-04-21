metin=input("Metin giriniz: ").lower()

#kaç sesli harf olduğunu bul
def sesli_harf_say(metin):
    sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
    karakter_sayisi =len(sesli_harfler)
    i=0
    sonuc=0
    while i<karakter_sayisi:
        sesli_harf_sayisi= list(metin).count(sesli_harfler[i]) 
        sonuc= sonuc + sesli_harf_sayisi
        i+=1   
    return sonuc

cevap=sesli_harf_say(metin)
print(cevap)


