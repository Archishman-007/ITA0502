import cv2
import numpy as np

IMAGE_PATH = r"C:\Users\sunny\Downloads\EXP14.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.magnitude(sobel_x, sobel_y)

gradient = cv2.convertScaleAbs(gradient)

gradient_color = cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR)

sharpened = cv2.addWeighted(image, 1.0, gradient_color, 0.5, 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Gradient Mask Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
