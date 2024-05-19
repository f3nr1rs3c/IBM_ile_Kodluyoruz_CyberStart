# Indexing (elemanlara erişme)

# * Stringlerin non-scalar veri tiplerine örnek olduğunu konuşmuştuk. Stringler elemanmları karakter olan, alt birim olarak karakterler içeren bir veri tipi

# * Stringler karakterler dizisi olduğu için, bu dizideki spesifik konumdaki elemanlara erişme aklımıza gelebilir. Mesela String'in ilk karakteri nedir gibi

# * Bir yapının alt elemanlarına erişmek için yapacağımız işleme "indexing" deniyor. Bunu köşeli parantez "[]" ile sağlayacağız.

# * İsim diye bir değişken oluşturup, 

isim = "Deniz"
isim[1] # Birinci elemanı getir yani Deniz'in "e" si "d" niye getirmedi çünkü 0dan başlıyor indexler
"Deniz"[1]

# * Python'da indexler "0"'dan başlıyor. Yani biz ilk elemana ulaşmak istiyorsak [0]  ile sorgulamamız lazım.
isim[0]

"Deniz"[0]
"Deniz"[1]

# * Son elemanı elde etmek için [-1] yazabiliriz

isim[len(isim)]
isim[-1]

# * Sondan ikinci için
isim[-2]

# * "Deniz" 5 karakterden oluşuyor, indedxleri 0,1,2,3,4,5. Eğer ben 5'ten büyük bir index verirsem o indexte bir eleman olmadığı için hata alırım.

isim = "deniz"
len(isim)
isim[5] #  
isim[4] # n
isim[3] # i
isim[2] # d
isim[1] #  e 
isim[0] # d

# ! Slicing (Dilimleme)
# * İndexing ile sonuç olarak sadece bir eleman elde ettik, ama bir kaç tanesini arka arkaya, bir öbek olarak istiyorsam ne yapardım?
# * Diyelim ki ilk elemandan başlayarak 3. elemana kadar olan karkaterleri elde etmek istiyorum (0. indexten 3.indexe kadar olanlara)

name = "deniz"

name[0:3] # 0'dan 3'e kadar olanı al dersek 'den' sadece bastır diyoruz.
name[:3] # Bitişi belirtmeksek python string'i sonuna kadar alıyor => deniz çıktısı veriyor.
name[1:] # 1den 4e kadar al diyor => eniz çıktısı veriyor.
name[0:] # tüm adı alıyor.
name[:] # Deniz direk alıyoruz
name[6] # farklı bir şeyi alırsak hata alırız
name[1:20] # tam eniz string alıyoruz 20 bir olayı olmuyor.
name[1:200] # yine aynı
name[0:10:2] # 'dnz' alıyor çünkü atlıyor aralarda 

# * 0. indexten 10. indexe 1 azaltarak gidemez o yüzden boş string döndürür
name[0:10:-1] # '' çıktısı verir
name[10:0:-1] # 'zine' çıktıısı verir
name[10::-1] # 'zined' çıktısı veriyor
