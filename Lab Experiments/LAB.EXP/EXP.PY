import cv2

IMAGE_PATH = r"C:\Users\sunny\Downloads\Fantasy-Butterfly-Jar-iphone.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
