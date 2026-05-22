class BankaHesabi:
    def __init__(self,hesapSahibi,bakiye):
        self.hesapSahibi=hesapSahibi
        self.bakiye=bakiye
        
    
    def paraCek(self,cekilecekTutar):
        self.bakiye-=cekilecekTutar
        return self.bakiye

    def paraYatir(self,yatirilacakTutar):
        self.bakiye+=yatirilacakTutar
        return self.bakiye

print("---------Banka Sistemine Hoşgeldiniz----------")
isim=input("İsim Soyisim Giriniz: ")
hesap=BankaHesabi(isim,1000) #Banka hesabında otomatik 1000 tl olucak
while True:
    secim=input(f"{hesap.hesapSahibi} hesap bakiyeniz {hesap.bakiye} tl\n1-Para Çek\n2-Para Yatır\n3-Çıkış\nSeçiminiz: ")
    if secim=="1":
        miktar=int(input("Çekmek istediğiniz para miktarını giriniz: "))
        if hesap.bakiye<miktar:
            print("HATA\nHesabınızda yeterli bakiye bulunmamaktadır.")
        else:
            hesap.paraCek(miktar)
    if secim=="2":
        miktar=int(input("Yatırmak istediğiniz para miktarını giriniz: "))
        hesap.paraYatir(miktar)
    if secim=="3":
        print("Bankamızı tercih ettiğiniz için teşekkürler, Görüşmek Üzere")
        break



    
