with open("notlar.txt","r") as nots:
 butun_yazilar=nots.read()
 print(butun_yazilar)

print("------Dosya Değişti------")

with open("notlar.txt","a") as nots:
 nots.write("\nYazilimi cok seviyorum")

with open("notlar.txt","r") as nots:
 butun_yazilar=nots.read()
 print(butun_yazilar)


