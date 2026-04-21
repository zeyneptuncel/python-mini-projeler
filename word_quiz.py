import random
from colorama import Fore, Style, init
init(autoreset=True) #her satırda otomatik rengi resetler

# quizde kullanılacak kelimelerin dizi hali
ingilizce = [
    "always", "never", "sometimes", "usually", "often",
    "beautiful", "ugly", "easy", "difficult", "important",
    "accept", "believe", "create", "decide", "explain",
    "forget", "guess", "happen", "improve", "listen",
    "morning", "afternoon", "evening", "night", "midnight",
    "water", "fire", "earth", "wind", "nature",
    "angry", "happy", "sad", "tired", "excited",
    "journey", "vacation", "ticket", "airport", "luggage",
    "friend", "family", "enemy", "stranger", "neighbor",
    "success", "failure", "mistake", "solution", "problem",
    "remember", "understand", "develop", "discover", "imagine"
]
turkce = [
    "her zaman", "asla", "bazen", "genellikle", "sık sık",
    "güzel", "çirkin", "kolay", "zor", "önemli",
    "kabul etmek", "inanmak", "yaratmak", "karar vermek", "açıklamak",
    "unutmak", "tahmin etmek", "olmak", "gelişmek", "dinlemek",
    "sabah", "öğleden sonra", "akşam", "gece", "gece yarısı",
    "su", "ateş", "toprak", "rüzgar", "doğa",
    "kızgın", "mutlu", "üzgün", "yorgun", "heyecanlı",
    "yolculuk", "tatil", "bilet", "havalimanı", "bagaj",
    "arkadaş", "aile", "düşman", "yabancı", "komşu",
    "başarı", "başarısızlık", "hata", "çözüm", "problem",
    "hatırlamak", "anlamak", "geliştirmek", "keşfetmek", "hayal etmek"
]


question=1
score=0
while question<=20:
    number=random.randint(0,len(ingilizce))
    print("\nQuestion ",question)
    answer = input(f"What does '{ingilizce[number]}' mean in Turkish?: ").strip().lower()
    if answer==turkce[number]:
        print(Fore.GREEN+"Correct answer")
        score+=5
    else:
        print(Fore.RED+"Wrong answer")
        print("The answer is: ",turkce[number])
    question=question+1
print("Your score is: ",score)

