# ! Expression (İfadeler)

# * Objeler(object) ve operatörlerin(operator) birleşimi expressionları oluşturur.
# * Expression'ların değeri (value)'ları vardır ve tabi ki de bunların tipleri vardır.
# * İfadeler şöyler oluşturulur: (object) (operator) (object)
# * Expression'ların tiplerini operator'ın uygulandığı objelerin tipleri belirler

# ! Operator
# * İki tane integer'ın toplamı integer verir.
2 + 2 # 4
type(2+2) # int

# * İki tane float'un toplamı float verir.
2.4 + 2.5 # 4.9
type(2.4 + 2.5) # float

# * Eğer objelerden biri bile float ise toplama işleminde expression'ın tipi float olur.

2.4 + 3 # 5.4

type(2.4 + 3) # float

# * İki tane integer'ın farkı integer verir.
type(3-2)

# * İki tane float'un farkı float verir.
2.6 - 2.1
type(2.6 + 2.1)

# * Eğer objelerden biri bile float ise çıkarma işleminde expression'ın tipi float olur.
2.4 + 3 # 5.4
type(2.4 + 3) # flaot

# ! Operator
# * İki tane integer'ın farkı ınteger verir.
3 - 2 # 1
type(3-2) # int

# * İki tane float'un farkı float verir.
2.6 - 2.1
type(2.6 + 2.1)

# * Eğer objelerden biri bile float ise çıkarma işleminde expression'ın tipi float olur.
2.5 - 3 # 7.5
type(2.5 - 3) # float

# ! Operator
3 * 2 # 6
type(3*2) # int

# * İki tane float'un çarpımı float verir.
2.6 * 2.4 # 6.24
type() # float

# ? İşleme giren objelerin tipi ne olursa olsun cevap float olur.

3 / 2 # 1.5
3 / 1.5 # 2.0
2.4 / 0.6 # 4.0

# ! // operator (int division)
# * Eğer işleme girenlerden biri bile float ise cevap float olur

5 // 2 # 2
5 // 2.5 # 2.0
4.2 // 5 # 0.0
8.2 // 5 # 1.0

# ! % operator (mod)
# * Eğer kalan float ise cevap float olur yoksa integer olur

5 % 2 # 1
10 % 3 # 1
2.5 % 2 # 0.5

# ! ** operator
# * Üst alma işlemi yapar

2 ** 3 # 8
3 ** 2 # 9
2.4 ** 2 # 5.76
5 ** -1 # 0.2

# ! print()
# * Bazen sadece bazı değerleri bastırmak isteriz, bunun için print()
print(5) # 5 