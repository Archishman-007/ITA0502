import cv2

img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg")

if img is None:
    print("Image not found")
    exit()

x,y,w,h=50,50,200,200
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
object_img=img[y:y+h,x:x+w]

cv2.imshow("Original Image",img)
cv2.imshow("Extracted Object",object_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
