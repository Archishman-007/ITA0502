import cv2
img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg")
cv2.putText(img,"Watch",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow("Object Recognition",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
