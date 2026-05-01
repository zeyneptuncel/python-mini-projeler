while True:

    def not_gir():
        isim=input("Öğrenci ismi giriniz: ")
        not1=int(input("1. sınav notunuzu giriniz: "))
        not2=int(input("2. sınav notunuzu giriniz: "))
        with open("ders_notlari.txt","a", encoding="utf8") as dosya :
            dosya.write(f"{isim}:{not1},{not2}\n")
        print("Not girişi başarıyla tamamlandı")
                
    def not_oku():
        kisi=input("Notlarını görüntülümek istediğiniz öğrenci adını giriniz: ")
        with open("ders_notlari.txt","r", encoding="utf8") as dosya:
            satirlar = dosya.readlines()
            bulundu_mu=False
            for satir in satirlar:
                if kisi.lower() in satir.lower():
                    bilgiler=satir.split(":")
                    isim=bilgiler[0]
                    notlar =bilgiler[1].split(",")
                    print(f"\nÖğrenci Adı: {isim}\nNot1: {notlar[0]}\nNot2: {notlar[1]}")
                    bulundu_mu=True
                    break
            if bulundu_mu==False:
                print("Bu öğrencinin bilgileri kayıtlı değil! ")

  
    def ort_hesapla():
        print("Şuan yapım aşamasında")

    secim=input("\n-----Öğrenci Bilgi Sistemi-----\n"
    "1-Not Gir\n" \
    "2-Not Oku\n" \
    "3-Ortalama_hesapla\n" \
    "q-Çıkış Yap\n" \
    "Yapmak istediğiniz işlemi seçiniz: ")
    if secim=="1":
        not_gir()
    elif secim=="2":
        not_oku()
    elif secim=="3":
        ort_hesapla()
    elif secim=="q" or secim=="Q":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Yanlış bir değer girdiniz")
