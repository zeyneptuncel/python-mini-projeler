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

def gizli_kod(metin):

    metin=metin.replace("e","3")
    metin=metin.replace("a","@")
    return(metin)


sesli_harf_sayisi=sesli_harf_say(metin)
gizli_kod=gizli_kod(metin)

print("Sesli harf sayısı: ",sesli_harf_sayisi)
print(f"Gizli Kod: {gizli_kod}")


