
# # Girilen iki sayının toplamının gösterildigi yanlış veri girilme durumundada hata mesajı gösteren console uygulaması
# try:
#     num1=int(input("Birinci sayıyı giriniz: "))
#     num2=int(input("İkinci sayıyı giriniz: "))
#     sonuc=num1+num2
#     print(sonuc)
# except ValueError:
#     print("HATA Lütfen sayı giriniz")
  

#ALMAN HESABI KİŞİ BASINA DÜŞEN HESAP HESAPLAMA
try:
    num1=int(input("Hesap tutarını giriniz: "))
    num2=int(input("Kişi sayısını giriniz: "))
    sonuc=num1/num2
    print(sonuc)
except ZeroDivisionError:
    print("Kişi sayısı 0 olamaz")
except ValueError:
    print("Lütfen sayı giriniz!")



