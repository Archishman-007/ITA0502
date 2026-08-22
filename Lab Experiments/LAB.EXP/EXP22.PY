import cv2
import numpy as np

IMAGE_PATH = r"C:\Users\sunny\Downloads\images (6).jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.float32)

laplacian = cv2.filter2D(image, cv2.CV_32F, kernel)

sharpened = image.astype(np.float32) + laplacian

sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Positive Center Laplacian", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
