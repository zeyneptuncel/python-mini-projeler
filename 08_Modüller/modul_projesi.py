import time
import os
import pygame
from termcolor import colored
import random

os.system("cls")
pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

def metinyaz(metin, sure):
    colors=["yellow","green","blue","magenta","cyan"]
    renk=random.choice(colors)
    if metin=="Sana kırmızı çok yakışıyooor":
        metin=metin.upper()
        for harf in metin:
            print(colored(harf,"red"),end="",flush=True)
            time.sleep(0.1)
        return
    for harf in metin:
        print(colored(harf,renk),end="",flush=True)
        time.sleep(0.1)
    print()
    time.sleep(sure)


# Şarkının introsuna göre ilk giriş beklemesi
time.sleep(2) 

metinyaz("Hatayı ben en başında yaptım", 1)
metinyaz("Aynı evi senle paylaşarak", 1)
metinyaz("Kendimi çok takdir edeceğim", 1)
metinyaz("Ayrılığı kutlayarak", 1.5)
print()
metinyaz("Vedalaşırken üzülmüş gibi", 1)
metinyaz("Tutma ellerimi acıyarak", 1)
metinyaz("Kendine dev aynasında değil", 1)
metinyaz("Boy aynasında bir bak", 2.3)
print()
metinyaz("Acım taze kurtulamazsın", 1.3)
metinyaz("Gözlerini kaçırarak", 2)
print()
metinyaz("Belki birazcık bozuldun", 1)
metinyaz("Ruhun belki can çekişiyor", 1)
metinyaz("Belki biraz da kızardın ama", 1.3)
metinyaz("Sana kırmızı çok yakışıyooor", 2)
time.sleep(3)

