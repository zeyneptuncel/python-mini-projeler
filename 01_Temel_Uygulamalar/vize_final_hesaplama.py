islem = (input("Hoş geldiniz," \
"\n 1- Vize ve final notları girip no öğrenme" \
"\n 2- Vize notu girip finalden kaç alman gerektiğini öğren " \
"\n Yapmak istediginiz işlemin rakamını giriniz: "))

if islem=="1":
    not1= float(input("\nVize notunuzu giriniz: "))
    not2 = float(input("Final notunuzu giriniz: "))
    ort = (not1*0.30) + (not2*0.70)
    if ort>=35:
        print("\n Tebrikler, Dersi geçtiniz. Dönem sonu notunuz: ",ort)
    else:
        print("\n Maalesef, Dersten kaldınız. Dönem sonu notunuz: ", ort)
elif islem=="2":
    vizeNot= float(input("\nVize notunuzu giriniz: "))
    x = 35-(vizeNot*0.30)   # x finalde gelmesi gereken puan 
    finalnot=(x*100)/70     # hangi sayının yüzde 70i x tir 
    print("Final için alman gereken min not: ",finalnot)
else:
    print("\nclearHATA \n Lütfen yazılı işlemlerden birini seçiniz")





