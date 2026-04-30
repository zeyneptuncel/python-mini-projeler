print("----------KAYIT OL----------")

kullanici_adi=input("Kullanıcı adı oluşturun: ")
sifre=input("Şifre oluşturun: ")

with open("kullanicilar.txt","a", encoding="utf8") as dosya:
 dosya.write(f"{kullanici_adi}:{sifre}")
print("Kayıt başarıyla tamamlandı.")