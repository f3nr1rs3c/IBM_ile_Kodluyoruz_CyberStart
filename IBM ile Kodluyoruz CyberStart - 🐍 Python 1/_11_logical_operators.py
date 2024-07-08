# ! Mantıksal Operatörler (Logical Operators)

# * Verilerimizle nasıl karşılaştırma yapabileceğimizi gördük. Bunların cevaplarını birleştirmek isteyebiliriz. İki ifadenin sonucu da doğru olunca bir şey yapmak veya en az biri doğruyken
# * bir şey yapmak isteyebilirim.

# * Bunu sağlayabilmek için "boolean" veri tipleri üzerine uygulanabilecek mantıksal operatörlere bakacağız.
# * Göreceğimiz mantıksal operatörlerinin uyguladığı veri tipleri "boolean" olmalı.

# ! "Not" Bu cevapları değiştirmek istersek o yüzden kullanılır.
# ? Örnek vermek gerekirse; Bir test var diyelim 50 üzerinden 60 alırsa geçsin, 40 alırsa kalsın. Diyebiliriz.
# ? A ile B kişileri var Sinemaya gidelim diyor biri A: False derken. B: True diyor, doğru yada yanlış yani. Aynı şekilde. Okula gidelim dersekte A: True diyor bu sefer
# ? B: False diyor bu sefer.
 
not True # False
not False # True

not 5 < 6 # False
not 5 == 5 # False

a = 4
b = 10

not a < b # False
not (a > b) # True

# ! "And" 
# * Sadece iki ifade de "True" ise "True" sonucu verir, yoksa. "False" olur.

True and True # True
False and False # False
True and False # False

a = 4
b = 1
c = 10

(a > b) and (b < c) # True
(a > b) and (b > c) # False

# ! "or"
# * Sadece iki ifade de "False" ise "False" sonucu verir, yoksa "True" olur

True or True
False or False
False or True
True or False

a = 4
c = 1 
c = 10
(a > b) or (b < c) # True
(a > b) or (b > c) # True
(a < b) or (b > c) # False

