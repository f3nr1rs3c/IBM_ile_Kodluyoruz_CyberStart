# Casting in Strings

a = "5"
b = "5.3"

float(5) # 5.0
5.4 # 5.4
int(5.7)

int(a) # a içerisinde 5 sayısal değeri olduğundan 5 çıktısı verir
int(b) # float olduğundan dolayı olmuyor int oluyor sadece

int(float(b)) # 5 çıktısı alırız
