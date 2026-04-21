import sys
from colorama import Fore, Style, init

init(autoreset=True)

balance=1000 # bankadaki paramız
pin="1234"
attempts=3 #giris hakkı

while attempts>0:
    password=input("Please enter your PIN: ")
    if password==pin:
        print(Fore.GREEN +"Login successful!\n")
        break   #Şifre sorma ekranından çıkılsın
    else:
        print(Fore.LIGHTYELLOW_EX+"Incorrect PIN. Remaining attempts:\n")
        attempts=attempts-1

if attempts==0:
    print(Fore.RED+"Your card is blocked! \n")
    sys.exit()
       
while True:
    choice=input("\n1-Bakiye Sorgulama \n" 
    "2-Para Yatırma \n" 
    "3-Para Çekme \n" 
    "4-Çıkış \n" 
    "Yapmak istediğiniz işlemi seçiniz: ")

    if choice=="1":
        print(f"\nMevcut Bakiyeniz: {balance}")

    if choice=="2":
        amount = int(input("Yatırmak istediğiniz tutarı giriniz: "))
        balance=amount+balance
        print(Fore.GREEN+f"Yeni Bakiyeniz: {balance}")

    if choice=="3":
        amount = int(input("Çekmek istediğiniz tutarı giriniz: "))
        if amount>balance:
            print(Fore.RED + "Yetersiz Bakiye!")
        else:
         balance=balance-amount
         print(Fore.GREEN+f"Yeni Bakiyeniz: {balance}")
    
    if choice=="4":
        print(Fore.YELLOW+"Bizi Tercih Ettiğiniz İçin Teşekkürler.")
        break


    
        

    
    


