def kayıt_ol(): 
    print("\n----------KAYIT OL----------") 
    kullanici_adi=input("Kullanıcı adı oluşturun: ") 
    sifre=input("Şifre oluşturun: ") 
    with open("kullanicilar.txt","a", encoding="utf8") as dosya: 
        dosya.write(f"{kullanici_adi}:{sifre}\n")  
    print("Kayıt başarıyla tamamlandı.") 

def giris_yap(): 
    print("\n----------GİRİŞ YAP----------") 
    kullanici_adi=input("Kullanıcı adınızı giriniz: ") 
    sifre=input("Şifrenizi girinz: ") 
    aranan_kelime= f"{kullanici_adi}:{sifre}"
    giris_basarili_mi=False
    with open("kullanicilar.txt", "r",encoding="utf8") as dosya:
        for i in dosya:
            if aranan_kelime in i:
                giris_basarili_mi = True
                break
    if giris_basarili_mi==True:
        print(f"Giriş Başarılı\nHoş Geldiniz {kullanici_adi}")
    else:
        print("Kullanıcı adı veya şifre hatalı")
    

secim=input("1-Kayıt ol\n" \
"2-Giriş yap\n" \
"İstediğiniz işlemi seçiniz: ")
if secim=="1":
    kayıt_ol()
elif secim=="2":
    giris_yap()
else:
    print("Hatalı giriş yaptınız")