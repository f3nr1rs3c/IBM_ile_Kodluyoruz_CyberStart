# Stringlerde Karşılaştırma

"Elma" == "Elma" # False
"Elma" != "elma" # True
"elma" == "elma" # True

a = "elma"
b = "elma"
a == b # True

"a" < "b" # True
"ab" < "b" # True
"ab" < "basşdlad" # True, fazla karakterden fazlaysa  doğru
"ab" < "ac" # True
"abc" < "abb" # False
