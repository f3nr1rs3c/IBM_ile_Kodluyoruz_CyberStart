# ! For
# * "for" döngüsü "in"'den sonra yazdığımız yapının bütün değerleri üzerinde dolanıp, eleman sayısı kadar içindeki kodu çalıştıracak x "in <obje>" yapısı
# * - ile tanımladığında x döngünün her adımında "in"'den sonra tanımlanan yapının elemanlarının değerleri alacak

# ! for <degısken> in <obje>
# * "for" döngüsünün en başında "<degisken> <obje>'nin ilk elemanının değerini alıyor. İÇindeki kod 1 kere çalışıp bittikten sonra ikinci kere çalıştırıyor ve <değişken>, <obje>"'nin ikinci elemanının değerini alıyor. Bu <obje>'nin tüm elemanları bitene kadar devam ediyor.

for c in "hey":
 print(c)


toplam = 0

for x in range(101):
 toplam += x 
print(toplam)


for x in range(5):
 print(x)


toplam = 1
for i in range(5):
 toplam *=5
print(toplam)

toplam = 1

# ! For vs While
# * "while" yapısında kaç kere iterasyon yapacağımızı bilmiyoruz, "for"'da eleman sayısı kadar iterasyon var ("break" veya "continue" ile bölünmezse)
# * Aslında "for" döngüsünü "while" döngüsünü kullanarak yazabiliriz, ama "while" döngüsünü "for" kullanarak yazamayız, çünkü "for"'da test mekanizması yok.

s = "hey"

for c in s:
    print(c)

n = len(s)
index = 0

while index < n:
      print(s[index])
      index += 1
