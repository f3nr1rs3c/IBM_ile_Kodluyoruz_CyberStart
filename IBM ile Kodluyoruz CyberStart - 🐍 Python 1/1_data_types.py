# ! Temel Veri Yapıları

# * Programlar veri objelerini (data object) manipüle ederek istediklerimizi yaparlar.

# * Programa istediğimizi yaptırmamız için girdiklerimizi ve programın içerisinde kullanılacak verileri ifade edebilmemiz lazım.

# ! Veri Objeleri ikiye ayrılır.

# * 1) Scalar: Daha alt parçalara bölünemeyen yapılar (sayılar vs gibi)
# * 2) Non-scalar: Daha alt parçalar abölünebilen, içsel yapısına erişebilen (sayıları ard arda koyduğumuz bir yapı buna bir örnek olabilir.)

# * Her objenin bir tipi vardır, program bu tiplere göre onlarla nasıl işlem yapabileceğine karar verir. Mesela iki tane sayıyı toplamak; iki tane yazıyı birleştirmek...

# ! Integers (tam sayılar)

2
3

# ! Floats (kesirli sayılar)

2.3
2.5
2.0
3. # * sayı ve nokta yapsak bile float olarak tanımlıyor python.

# ! Boolean
# * Daha ilerki konularda if-else mantığını gördüğümüzde daha iyi oturtacak bir veri tipi. Özetle bir şeyin doğru (True) veya yanlış (False) olduğunu belirten bir yapı.
# * Bir önermenin doğru veya yanlış olduğunu söyler bize.

True
False
2 > 3 # < > bu işaretler de true ve false da aynı anlamda karşılar.
2 < 3

# ! type()
# * Objelerin tiplerine type() ile bakabiliriz

type(2) # * int tipini kullandığımızı belirtir.
type(2.0) # * float tipini kullandığımızı belirtir.
type(True) # * bool tipini kullandığımızı belirtir.

# ! Type Casting (Tip Dönüştürmesi)
# * Data objelerinin tipini değiştrebiliyoruz, buna "casting" deniyor.

int(2.4) # * Çıktı olarak 2 verir sadece.

# * Sayıları yuvarlamaz, sadece tam olan kısmını alır.
int(2.9) # * 2 Çıktısı olarak verir sadece.

float(4) # * 4.0 çıktısı olarak vericek, çünkü float bir işlem yapıldı.


