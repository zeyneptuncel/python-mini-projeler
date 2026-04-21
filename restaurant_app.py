# ["ürün ismi", "ürün fiyatı", "ürün stoku"]
menu_info = [
    ["Hamburger", 300, 30],
    ["Pizza", 250, 20],
    ["Salad", 160, 5],
    ["Soup", 90, 7],
    ["Coffee", 150, 25],
    ["Tea", 50, 20]
]

print("\nHoşgeldiniz")
price = 0
siparis = [] 

while True:
    choice = input("\n1-Menüye ekle\n" 
                   "2-Menüden çıkar\n" 
                   "3-Siparişi Tamamla\n" 
                   "4-Çıkış\n" 
                   "Yapmak istediğiniz işlemi seçiniz: ")

    if choice == "4":
        print("Bizi tercih ettiğiniz için teşekkür ederiz")
        break
        
    elif choice == "1":
        # MENÜ GÖSTERİMİ
        s = 1 
        print("\n--- MENÜ ---")
        for i in menu_info:
            print(f"{s}: {i[0]} - {i[1]} TL (Stok: {i[2]})")
            s += 1
            
        while True: 
            item = int(input("\nİstediğiniz ürünün numarasını giriniz (Daha fazla ürün eklemek istemiyorsanız 0'a basınız): "))

            if item == 0: 
                break
            elif 1 <= item <= len(menu_info): 
                if menu_info[item-1][2] == 0:
                    print(f"Maalesef {menu_info[item-1][0]} stoklarda yoktur!\n")
                else:
                    siparis.append(menu_info[item-1][0])
                    price = price + menu_info[item-1][1]
                    menu_info[item-1][2] -= 1 # Sepete ekleyince stoktan 1 düşürdük.
                    print(f"Başarılı! {menu_info[item-1][0]} sepete eklendi. Güncel Tutar: {price} TL")
            else:
                print("Geçersiz bir ürün numarası girdiniz.")

    elif choice == "2":
        if len(siparis) == 0:
            print("\nSepetiniz zaten boş!\n")
        else:
            while True:
                print("\n--- SEPETİNİZ ---")
                s = 1
                for urun in siparis:
                    print(f"{s}: {urun}")
                    s += 1
                
                print(f"Toplam Tutar: {price} TL")
                
                sil_secim = input("\nSepetten silmek istediğiniz ürünün numarasını giriniz (İşlemi bitirmek için 0'a basınız): ")
                
                if sil_secim == "0":
                    break
                
                # Kullanıcının harf veya boşluk girip programı çökertmesini engellemek için isdigit() kullanıyoruz
                if sil_secim.isdigit():
                    sil_secim = int(sil_secim)
                    
                    # Girilen numara sepetteki ürün sayısıyla eşleşiyor mu kontrolü
                    if 1 <= sil_secim <= len(siparis):
                        # 1. Adım: Ürünü sepetten çıkar (pop komutu indeks ile siler, o yüzden 1 çıkarıyoruz)
                        silinen_urun = siparis.pop(sil_secim - 1)
                        
                        # 2. Adım: Çıkarılan ürünün fiyatını toplamdan düş ve stoklara geri ekle
                        for i in menu_info:
                            if i[0] == silinen_urun:
                                price -= i[1] # Fiyatı ana toplamdan düşürüyoruz
                                i[2] += 1     # Sepetten çıktığı için stoku 1 artırıp geri rafa koyuyoruz
                                break
                                
                        print(f"\nBaşarılı! {silinen_urun} sepetten silindi.")
                    else:
                        print("\nSepette böyle bir numara yok, tekrar deneyiniz.")
                else:
                    print("\nLütfen geçerli bir sayı giriniz!")

    elif choice == "3":
        print("\n--- SİPARİŞ ÖZETİ ---")
        # Sepeti gösteren döngü
        if len(siparis) > 0:
            print("Siparişleriniz:", ", ".join(siparis))
        print("Toplam Sipariş Tutarınız: ", price, "TL\n")
        
    else:
        print("Hatalı tuşlama yaptınız.")




