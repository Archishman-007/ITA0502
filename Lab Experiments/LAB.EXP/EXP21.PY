import cv2
import numpy as np

IMAGE_PATH = r"C:\Users\sunny\Downloads\images (5).jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

kernel = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
], dtype=np.float32)

laplacian = cv2.filter2D(image, cv2.CV_32F, kernel)

sharpened = image.astype(np.float32) - laplacian

sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Laplacian Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
