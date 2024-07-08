# Programı Dallandırma (Branching)
# * İfadelerinin değerlerini True veya False olduklarını veren karşılaştırmalara ve mantıksal operaötlere bakmıştık
# * Şimdi bunların sonuçlarına göre programımızı dallandırmaya bakacağız.

# ! İf 
# * Eğer testimin değeri True ise "if" bloğunun içinde yazanı yapacağız.
# * Yapılacakların "if" bloğuna ait olduğunu anlatmak için kodu "if"'in içine yazarız. Pytrhon'ın o bloğun içinde olduğumuzu anlaması için boşluk bırakmamız gerekir:

x = int(input("Bir sayı girin: "))

if x % 2 == 0:
    print("Sayınız çift sayı")

print("Programınız sona ulaştı")
# Bir sayı girin: 3
# Programızın sona ulaştı

# ! Else
# * "if" ile kontolümüz (veya elseif-elif) "False" sonucu döndürülürse yapılacak blok

x = int(input("Bir sayı girin: "))

if x % 2 == 0:
    print("Sayı çift sayı ")
else:
    print("Sayınız tek sayı")
    
print("Programınız sona ulaştı")
# Bir sayı girin: 2
# Sayınız çift sayı
# Programınız sona ulaştı

# ? Elif ile sorgulama mantığı yapabiliriz, fakat else ile sorgulama mantığı yapamayız.

# ! Elif
# * "elif" "if" ile yaptığımız teste ek olarak başka testler yapmak istiyorsak kullanır.
x = int(input("Bir sayı girin: "))

if x < 10:
    print("Sayı 10'dan küçük")

elif x == 10:
    print("Sayı 10'a eşit")

else:
    print("Sayı 10'dan büyük")

print("Programınız sona ulaştı")
# Bir sayı girin: 12
# Sayı 10'dan büyük
# Programınız sona ulaştı


x = int(input("0 ile 100 arasında bir sayı girin: "))

if x == 100:
    print("Sayı 100")

elif x >= 90:
    print("Sayı 90 ile 100 arasında")

elif x >= 80:
    print("Sayı 80 ile 90 arasında")

else:
    print("Sayı 80'den küçük")

print("Programınız sona ulaştı.")


# ! Nested if
# * if, elif ve else bloğunun içine yazdığımız kod normal koddan farklı değil, o yüzden bunların içine de ayrıca "if" elif ve else yazabiliriz.

x = int(input("Bir sayı girin: "))

if x % 3 == 0:
    if x % 2 == 0:
        print("Bir hem 2'ye hem de 3'e bölünüyor")
    else:
        print("Sayı 3'e bölünüyor ama 2'ye bölünmüyor")
else:
    print("3'e bölünmüyor")

print("Programınız sona ulaştı")


# ! Test Olarak Mantıksal Operatörleri Kullanmak

x = int(input("Bir sayı girin: "))

if (x % 3 == 0) and (x % 2) == 0:
    print("Sayı hem 2'ye hem de 3'e bölünüyor.")

print("Programınız sona ulaştı")

x = int(input("Bir sayı girin: "))

if (x % 3 == 0) or (x % 2 == 0):
    print("Sayı 2 veya 3'den en az birine bölünüyor.")

print("Programınız sona ulaştı")
