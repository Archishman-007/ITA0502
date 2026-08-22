import cv2

IMAGE_PATH = r"C:\Users\sunny\Downloads\images (1).jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel X Edge Detection", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
