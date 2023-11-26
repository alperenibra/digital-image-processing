import cv2
import numpy as np

# Resmi yükle
image = cv2.imread('rice_photo.jpeg')  # Resminizin yolunu buraya girin

# Görüntüyü Gri Tonlamaya Dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Beyaz renk için bir eşik değeri belirleyin (örneğin, 200)
threshold_value = 200

# Beyaz pikselleri tespit etmek için eşikleme yapın
_, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Beyaz pikselleri içeren konturları bulun
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Her bir kontur için döngü
total_white_rice = 0
for contour in contours:
    area = cv2.contourArea(contour)
    # Belirli bir alandan daha büyükse, pirinç tanesi olarak kabul edin
    if area > 50:  # Bu değeri ihtiyaca göre ayarlayabilirsiniz
        total_white_rice += 1
        # Konturları çizin (opsiyonel)
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Pirinç tanelerini saydıktan sonra ekrana yazdırın
print(f"Beyaz pirinç taneleri sayısı: {total_white_rice}")

# Sonucu görselleştirin
cv2.imshow('Detected Rice Grains', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
