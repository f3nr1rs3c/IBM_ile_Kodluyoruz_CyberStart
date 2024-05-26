# ! Break
# * Belki bir şart sağlandığı zaman döngüden aniden çıkmak istiyorum, bunu "break" ile sağlıyoruz.
# * "break" komutunu gördüğümüz yerde döngüden çıkıyoruz.

for i in range(10):
    if i == 3:
         break
    print(i) # 0 1 2
    
x = 0 

while x < 10:
   print(x) # yukarıda ike aynı işlem yapmak için
   x += 1
    
   if x == 3:
      break
     
# ! continue
# * Bazen döngülerde bir şart sağlandığında bir sonraki iterasyondan devam etmek isteyebilirim. Bunu "continue" ile sağlayacağız.
# * "continue" komutu ile karşılaşıldığı zaman, döngünün bir sonraki iterasyonuna geçilir.

for i in range(10):
    if i == 3:
     print(i)
    print("merhaba") 
