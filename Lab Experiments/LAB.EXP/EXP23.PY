import cv2
import numpy as np

IMAGE_PATH = r"C:\Users\sunny\Downloads\images.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

# Create blurred image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Create unsharp mask
mask = cv2.subtract(image, blurred)

# Sharpen the image
sharpened = cv2.add(image, mask)

sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Unsharp Masked Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
