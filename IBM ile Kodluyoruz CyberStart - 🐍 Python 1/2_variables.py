# Variables (değişkenler)
# * Bazı değerleri bilgisayarın hafızasında tutmak ve daha sonra bunlara verdiğimiz adlarla erişmek isteyebiliriz. Bunu variable'lar ile gerçekleştireceğiz.
# * İlk olarak yapacağımız şey variable'a vereceğimiz ismi yazmak. Bu isim "penguen", "uzunluk", "maaş" gibi istediğiniz bir isim olabilir 
# * - (burada dikkat edilmesi gereken yer, verilecek ismin daha önceden python'ın default olarak kullanmadığı isimler olması. Mesela "if", "continue", "for" gibi keyword'ler
# * daha önceden ayrıldığı için bunları variable ismi olarak kullanmayız.)

# * Python'ın daha çnceden kendisine ayrıdığı isimler (reserved words)
# ! and, del, from, not, while
# ! as, elif, global, or, with
# ! assert, else, if, pass, yield
# ! break, except, import, print, True
# ! class, exec, in, raise, False
# ! continue, finally, is, return
# ! def, for, lambda, try

# * Variable ismini seçtikten sonr abu ismin değerinin ne oalcağını söylemeliyiz. Bu aşamadan sonra
# * python verdiğimiz ismi gördüğünde aslında verdiğimiz değeri çağırıyor olacak.

# * Bu beğeri atama işlemini "=" sembolü ile yapacağız. Normalde bilgiğimiz anlamında farklı bu "=" işareti.
# * 

a = 2 # A harfine 2 isimli değeri veriyoruz.

a + 5 # A harfine 5 isimli değer

y = 2 + 4 # Sonuç bize 6 olarak çıkar çünkü b karşısındaki 2 ve 4 topla çıkan sonucu yaz.

a = 2
print(a)

x = a + 5
print(x)

z = a + 3

limon_fiyat = 10 # Buradda neyi değiştirirsek sonuç da değişir alt taraftan sıfırdan yazmaya gerek kalmaz.
s1 = limon_fiyat * 100
s2 = limon_fiyat * 70
s3 = limon_fiyat * 30
print(s1) # 1000 çıktısı alıcaz


s1 = 15 * 100 # Tek tek 15 yaparakta elbette aynı sonucu alırız.
s2 = 15 * 70
s3 = 15 * 30
print(s1) # 1500
print(s2) # 1050
print(s3) # 450

# * Container kavramını kavramak için şöyle düşünüyoruz; " bir değer var ve bu değer bir kutunun içerisinde."