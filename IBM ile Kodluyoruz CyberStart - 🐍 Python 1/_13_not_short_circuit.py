# "&"'dan "and" yaptığını yapar ama short-circuit davranışı göstermez.

(2 == 2) & (3 == 3) # True
(5 < 3) & print("hey") 

# * "5 < 3 and print("hey")" karşılaştırması yaptığımızda hata almıyorken "5 < 3 & print("hey")"'de hata alıyoruz."and" boolean NoneType karşılaştırırken hata vermezk "&" hata veriyor.

# * "|"'dan "or"'un yaptığını yapar ama short-circuit davranışı göstermez.

(2 == 2) | (3 < 3) # True
(5 > 3) | print("hey") # hey

