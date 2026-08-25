import cv2

img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
faces=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1.2,50,param1=100,param2=50,minRadius=20,maxRadius=200)

if faces is not None:
    faces=faces[0]
    for x,y,r in faces:
        x=int(x)
        y=int(y)
        r=int(r)
        cv2.rectangle(img,(x-r,y-r),(x+r,y+r),(0,255,0),2)

cv2.imshow("Face Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
