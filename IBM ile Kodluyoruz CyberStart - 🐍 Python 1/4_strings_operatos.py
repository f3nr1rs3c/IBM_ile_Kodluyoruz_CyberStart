# Stringler karakterlerden oluşan bir dizidir aslında. Stringlerin elemanları karakterlerdir.

# * Karakterler: (a, b, c, d...) gibi harfler, (*, ?, =, <, >, /...) gibi özel karakterler, (1, 2, 3...) gibi yazı biçiminde sayılar, boşluk(space) karakter olarak adlanabilir.
# * Stringler "Karakter"'lerden veya bunların kombinasyonlarından oluşabilirler.

# * Bir şeyin "String" olduğunu belirtmek için yazacaklarımızı ikili tırnak("") veya tekli tırnak('') içine yazarız.
# * Tırnak işaretlerinin yaptığı şey aslında: Bu tırnak işaretlerinin içinde verdiğimi diziye karakterler dizisi olarak davran, öyle algıla demek.

# * İki tırnak içine de yazsak, tekli tırnak içine de yazsak aynı şekilde algılanır. Önemli olan hangisiyle başladıysak onunla bitirmek.

# * Scalar ve Non-scalar objelerden bahsetmiştik. Non-scalar veri tiplerinin daha alt parçalara bölünebilen, elemanlar içeren yapılar olduğunu konuşmuştuk.
# * "String" non-scalar bir veri tipi. İçsel yapı olarak karakterlerden oluşuyorlar.

# * String "immutable" veri tipidir.

# ? Immutable: Elemanlarının değerleri değiştirilemez.

# ! Çift tırnak veya tek tırnakla bunlar olur fakat, tek tırnakla açtığımızı çift tırnakla kapatamayız.
"a"
'a'
"a"

"5"
'5'
# * Burada +'ya operator olarak davranılmıyor, yazı olarak davranılıyor.
"5 + 10"
"ab"
"hey"
"hey nasılsın"

"bugün 5 top dondurma yedim"
"Hmm o zmaan x = 5 diyebilir miyiz?"
'Hmm o zaman x = 5 diyebilir miyiz?'
type("Hmm o zaman x = 5 diyebilir miyiz?")
type('Hmm o zaman x = 5 diyebilir miyiz?')
type("5")
type("5 + 10")

"Bugün Kadıköy'e gidiyorum"
" 'Bugün Kadıköy'e gidiyorum' "# hata vermektedir

'Bana "Bugün ne yapıyorsun" dedi'

a = 3
b = 5 
a + b # gibi

# ! Stringlerde değeer atama (variable assignment)
# * Sayısal veri tiplerinde nasıl ki değer atayabiliyor, verilerin değerlerine isim verebiliyorsak, aynısını stringler için de yapabiliyoruz.

# ! Escape sequences
"Bana \"Bugün ne yapıyorsun\" dedi." # ' Bana "Bugün ne yapıyorsun" dedi'
'Bugün Kadıköy\'e gidiyorum' # "Bugün Kadıköy'e gidiyorum."

print("hey\nasılsın")
# hey
# nasılsın çıktısı veriyor.

merhaba = "Merhaba nasılsın bugün?"
print(merhaba)

# ! Stringlerde değer atama (variable assignment)
# * Sayısal veri tiplerinde nasıl ki değer atayabiliyor, verilerin değerlerine isim verebiliyorsak, aynısını stringler için de yapabiliyoruz

merhaba = "Merhaba nasılsın bugün?"
print(merhaba)

# ! String Concatenation
# * Operatörlerin uygulandıkları objelere göre değişik şeyler ifade edebilecğeini konuşmuştuk
# * "+" operatörü sayısal veri tipleri üzerine etki edince toplama işlemi yapıyor. Ama uyguladığı objeler "string" ise yapacağı işlem "concatenation" 
# * (birleştirme olacak), iki string'i ard arda birleştirecek

# * En çok karıştırılan durumlardan biri string olarak ifade edilen sayıları "+" operatörüne sokmak

"5" + "4"

# * Python tırnak işareti içinde verdiklerimize karakter olarak davrandığı için artık 4 ve 4 ü sayı olarak algılamıyor. "+" işlemi burada artık bu iki değeri yan yana koy demek, 
# * topla demek değil !

"hey" + "nasılsın?"

"* "+" operatörünün tek yaptığı birleştirmek, stringlerde boşluk (space) olmadığı için ifadenin sonucu boşluksuz çıktı "

"hey" + " " + "naber?"

# * Aynısını değer ataması yaparak da yapabilirdik

# * Diyleim ki karşılama mesajı yazdırmak istiyoruz. İsim ve karşılama kısmını ayrı tutacağız çünkü belki karşılacağımız kişinin ismi değişecek ve ben kodumda sadece o değeri değiştirerek
# * karşıalam mantığını korumaya devam edeyim istiyorum.

mesaj = "Merhaba"
isim = "Berkay"

human = mesaj + " " + isim
print(human) # gibi 

# ! Successive concatenation (Ardışık Birleştirme)
# * "*" opeartörü sayı objeleri için çarpım olarak tanımlanmışken, stringler için ard arda birleştirme işlemi yapıyor.

example1 = 4 * "hey"
example2 = "1" + "0"*10
total = example1 + example2
print(total)

# ! len()
# * Bu metod ile (metodları ileride ayrıntılı göreceğiz), elimizdeki string'in kaç karakterden oluştuğunu öğrenebiliriz (Boşluklarda sayılıyor.)

len("4")
len("42")
len("hey")
len("hey!")
len("hey nasılsın?")
len(" ")
len("  ")