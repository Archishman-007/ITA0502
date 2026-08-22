import cv2

IMAGE_PATH = r"C:\Users\sunny\Downloads\EXP12.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Error: Image not found!")
    exit()

watermark = "A. ARCHISHMAN"

position = (20, image.shape[0] - 30)

cv2.putText(
    image,
    watermark,
    position,
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imshow("Watermarked Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
