import math

# Noktaların Tanımlanmasını sağladım.
points = [(1, 2), (4, 6), (7, 8), (3, 9)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazdım.
def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid uzaklığını hesaplar.
    
    Parametreler:
    point1 (tuple): Birinci nokta
    point2 (tuple): İkinci nokta
    
    Döndürülen değer:
    float: İki nokta arasındaki Öklid uzaklığı
    """
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    return distance

# Mesafelerin Hesaplanmasını gerçekleştirdim.
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafenin Bulunmasını da sağladım.
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance:.2f}")
