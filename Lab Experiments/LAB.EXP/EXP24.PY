import cv2
import numpy as np

IMAGE_PATH = r"C:\Users\sunny\Downloads\EXP15.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

A = 2.0

blurred = cv2.GaussianBlur(image, (5, 5), 0)

high_boost = (A * image.astype(np.float32)) - blurred.astype(np.float32)

high_boost = np.clip(high_boost, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("High-Boost Sharpened Image", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()
