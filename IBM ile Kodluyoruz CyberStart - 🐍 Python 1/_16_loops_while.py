# Döngüler (loops)
# * "if-else-elif" mantığı ile programımızı dallandırmayı öğrendik. Ama kod akışı hala lineer. Bu işlemi birden çok kere yapmak istiyorsam bunu kolayştırıacak bir yapım yok

# * Bir şeyi defalarca yapmak istediğimizde kullanacğım bir yapıya ihtiyacım var. Bu sadece kodumu defalarca yazmamak için işimi kolaylaştırsın diye değil, kodun o parçacasının

# * kaç kere çalışacağını önceden bilmediğim için de olabilir (100) kere çalışacak kod parçasını 100 kere ard arda yazmak da zaman için iyi bir pratik değil, sadece böyle şeyler için de kullanmak isteyebiliriz).

# * Mesela bir siteye girmek için şifreniiz girdiğinizi düşünün. Site siz şifrenizi yanlış girdikçe şifrenizi yanlış girdikçe şifrenizi bir daha girin diyor.

# * Siteyi kodlayan kişinin önceden sizin kaç kere şifrenizi yanlış gireceğinizi bilmesinin bir yolu yok. Bu yüzden kodun o parçasının doğru şifre sağlanmadıkça çalışacağı bir yapıya ihtiyacım var.


# ! While
# * while döngüsünün içine yazdığım yapı belirttiğim ifade doğru olduğu sürece çalışacak
# * "while"'da da "if"'te olduğu gibi bir test mantığı var aslında. "Testimizin doğru çıktığı sürece 'while' bloğunun içindeki kodları tekrarlıyorum"
# * "while"'ın içindeki kodu ğython anlasın diye "if" ile yaptığımız gibi iç kısmına boşluk bırakarak yazacağız.
# * Örnek olarak kullanıcdan pozitif bir sayı bekleyen, negatif sayı girildikçe bir daha soran bir yapıyı düşünelim. Burada bir döngü mantığına ihtiyacımız var.
# * - çünkü kullanıcının kaç defa negatif sayi gireceğini önceden bilmiyoruz.

x = int(input("Bir sayı girin: "))

while x < 0:
 print("Sayı negatif, lütfen pozitif bir sayı girin:")
 x = int(input("Bir sayı girin: "))

print("Sayınız pozitif ve", x)

# * Diyelim ki 0'dan 100'e kadar olan sayıların toplamını bulmakk istiyorum ve o kadar sayısı elle yazmak istemiyorum.

toplam = 0
x = 0

while x <=100:
 toplam += x
 x += 1
print(toplam)

# * Döngümün içinde kontrol ettiğim yapıya güncelleyecek bir ifadenin olması lazım yoksa sonsuz döngüye girerim.

toplam = 0
x = 0

while x <=100:
 toplam += x
 print(x)

print(toplam)
