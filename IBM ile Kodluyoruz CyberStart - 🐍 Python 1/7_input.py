# Input
# * Bazen kullanacağımız değeri kullanıcıdan almak isteyebiliriz. Bunu "input" metodu ile yapacağız
# * "input" uniçinde yazacağımız bize kullanıcıya gösterilecek yazıyı verecek, kullanıcıdan girdi bekleyip enter'a basmasını bekleyecek, ve girdiyi "string"
# * olarak döndürecek

x = input("Bir sayı giriniz: ")
# Çıktı: Bir sayı giriniz: 5

x + 10 # çıktı 15 olur x soruluyor verdiğimiz sayıyı alıyor 10 ile topluyor işlemi yapıyor.

type(x) # str veriyor çünkü başta tanımlanan string değeri

int(x) + 10 # 15 ile 10 topluyor çıktı => 20  veriyor çünkü. Başta 5 verdik sonrasında 10 ile topladık 15 oldu, şimdide 10 ile tekrar topluyoruz çıktı 20 veriyor

x = int(input("Bir sayı giriniz: ")) # sadece sayısal veri al diyoruz çünkü 'int' verilmiş

x + 10 # 15

mesaj = input("Mesajı girin: ") # 5 veriyoruz
isim = input("İsim girin: ") # Ahmet

mesaj = str(input("Mesajı girin: ")) # sadece yazı verisi al diyoruz çünkü "string" verilmiş. String olarak tutuyoruz
sayı = int(input("Bir sayı girin: ")) # sadece sayısal veri al diyoruz çünkü "integer" verilmiş. İnteger olarak tutuyoruz.

mesaj + " " + sayı
