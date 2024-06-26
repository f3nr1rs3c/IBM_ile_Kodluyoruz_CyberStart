# Numerik Veri Tiplerinde Karşılaştırma:

# * Bir programın farklı durumlar olduğunda başka davranışlar göstermesini isteyebiliriz. Bunun için belirli testler yapmam lazım ve bu testler sonuca göre
# * farklı davranışlar tasarlamam lazım

# * Bu testler için verilerimizi birbirleri ile karşılaştırabilir olmamız lazım. Bunları Comparison Operator'lar (karşılaştırma operatörleri) ile yapacağız. 
# * Cevabın True veya False olmasına göre, farklı durumlarda farklı davranacak program tasarlayabiliriz. Bu karşılaştırmalar o programların temelini oluşturacak.

# * Numerik veri tiplerinde karşılaştırma deyince aklımıza bir kaç şey gelebilir:

# * " i=j " eşitlik testi (equality test.) i ve j birbirlerine eşitse bu ifadenin değeri "boolean" veri objesi "True", eşit değilse "False" olacak. "=" değişken atama
# * operatörü olarak tanımlandığı için eşitlik test ederken onu kullanırsak "="'in sağındaki değere solundaki adı vermiş oluruz.

# * i!=j eşitsizlik testi (inequality test). i ve j birbirlerine eşit değilse bu ifadenin değeri "boolean" veri objesi "True", eşitse "False" olacak
# * i>j i,j'den büyükse bu ifadenin değeri "boolean" veri objesi "True", eşit veya az ise "False" olacak.
# * i>=j i,j'den büyükse "veya" eşitse bu ifadenin değeri "boolean" veri objesi "True", az ise "False" olacak.
# * i<j i,j'den küçükse bu ifadenin değeri "boolean" veri objesi "True", eşit veya büyük ise "False" olacak.
# * i<=j i,j'den küçükse "veya" eşitse bu ifadenin değeri "boolean" veri objesi "True", büyük ise "False" olacak.

# ! Operator

5 == 4 # False, 5 ile 4 eşit değil diye bize bu sonucu verdi
5 == 5 # True, 5 ile 5 eşit diye bize bu sonucu verdi

i = 10
j = 20
i == j # False, ikisi de farklı 10 ile 20 eşit değil.

j = 10
i = 10 
j = i # True, bu sefer eşit aynı sayıda çünkü

# * Adlarının i ve j olması lazım değil, sadece o adları vermiştik önceki örneklerde
a = 10
b = 20
a == b # False, eşit değil.

# * Float ver tipleri için eşitlik karşılaştırması yaparken "==" kullanılması çok mantıklı değil, bunun nedenini ilerki derslerde göreceğiz.

5.3 == 5.4 # False, çünkü eşit değil.
5.4 == 5.4 # True, çünkü ikiside aynı eşit.

x = (0.3 * 3) + 0.1 
y = 1.0
x == y # False çıkıyor, ama True olmasını bekleriz.


# ! "!=" Operator
5 != 4 # False, çünkü != eşit değilleri, eşit olmicaklarını tanımlarken kullanıyoruz.
5 != 5 # True,  eşitler bunlar diyoruz çünkü eşit yapıyoruz.

i = 10
j = 20

i != j # True, biri büyük biri küçük sayı çünkü

# ! ">" Operator 
5 > 4 # True, ">" büyüktür işareti "<" küçüktür işareti
5 > 5 # False,

i = 10
j = 20
i > j # False, çünkü i j'den büyük değil!

j = 5
i > j # False

j = 5
i > j # True

5.3 > 5.4 # False
5.4 > 5.3 # True

# ! "<" Operator
5 < 4 # False
5 < 5 # False

i = 10
j = 20
i < j # True

5.3 < 5.4 # True

# * Floatlar için, değerler eşit ama ifadeleri farklıysa (bunun ne olduğunu göreceğiz) > ve < de hatalı olabilir

# ! >= Operator
5 >= 4 # True
5 >= 5 # True

5 >= 7 # False

i = 10
j = 20
i >= j # True

5.3 >= 5.4 # False
5.4 >= 5.3 # True
5.4 >= 5.4 # True, Yine eşitlik içerdiği için sorun olabilir 

# ! "<=" Operator
5 <= 4 # False
5 <= 5 # True

i = 10
j = 20
i <= j # True

j = 10
i <= j # True
