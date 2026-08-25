import cv2

video_path=r"C:\Users\Maruthi\Downloads\www.5MovieRulz.software - Love Oh Love (2026) 1080p TRUE WEB-DL - AVC - (DD+5.1 - 192Kbps) [Tel + Mal + Kan] - 2.6GB - ESub.mkv"
cap=cv2.VideoCapture(video_path)

ret,frame=cap.read()

if ret:
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(blur,50,150)
    contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour)
        if w>50 and h>30:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Vehicle Detection",frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
