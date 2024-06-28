# Kullanıcıdan girdi alma
text = input()

# Palindrome kontrolü ve debug çıktısı
if can_form_palindrome(text): # type: ignore
   print("True")
   print("Örnek Palindrome:", form_palindrome(text))
else:
    print("False")

def form_palindrome(text):
    """
    Verilen metinden palindrome oluşturur (eğer mümkünse).
    
    Args:
        text (str): Palindrome oluşturulacak metin.
    
    Returns:
        str: Oluşturulan palindrome veya "Palindrome oluşturulamaz" mesajı.
    """
    if not can_form_palindrome(text): # type: ignore # Eğer palindrome oluşturmuyorsa
       return "Palindrome oluşturulamaz"
    
    palindrome = [] # Palindrome'u tutacak liste
    char_counts = {} # Karakter sayılarını tutacak sözlük
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    middle = "" # Ortadaki tek karakter (varsa)
    for char, count in char_counts.items(): # Karakterler ve tekrar sayıları üzerinde dön
        if count % 2 != 0: # Eğer tekrar sayısı tek ise
            middle = char # Ortadaki karakter olarak ayır
        palindrome.extend([char] * (count // 2)) # Karakteri tekrar sayısının yarısı kadar ekle
    
    # Palindrome'u oluştur: sol kısım + orta karakter + sağ kısım (sol kısmın tersi)
    return "".join(palindrome + [middle] + palindrome[::-1])

def can_form_palindrome(text):
    """
    Verilen metinden palindrome oluşturulup oluşturulmayacağını kontrol eder.

    Args:
        text (str): Palindrome kontrolü yapılacak metin.
        
    Returns:
        bool: Palindrome oluşturulabiliyorsa True, aksi takdirde False.
    """
    char_counts = {} # Karakter sayılarını tutacak boş bir sözlük oluşturur.
    
    for char in text: # Metindeki her karakter için
        char_counts[char] = char_counts.get(char, 0) + 1
        # Karakter sözlükte yoksa 0'dan başlat, varsa değerini 1 artır.
    
    odd_count = 0 # Tekrar sayısı tek olan karakter sayacı
    for count in char_counts.values(): # Sözlükteki tekrar sayıları üzerinde dön
        if count % 2 != 0: # Eğer tekrar sayısı tek ise
            odd_count += 1 # Sayaç artır
    
    # Debug çıktısı: Karakter sayıları ve tek sayıda tekrar eden karakter sayısı
    print("Debug - Karakter sayıları:", char_counts file=sys.stderr, flush=True)
    print("Debug - Tek sayıda tekrar eden karakter sayısı:", odd_count, file=sys.stderr, flush=True)  # type: ignore
    
    # En fazla bir karakter tek sayıda tekrar edebilir (palindrom koşulu),
    return odd_count <= 1
