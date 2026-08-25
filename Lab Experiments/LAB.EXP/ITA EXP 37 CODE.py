import cv2

cap=cv2.VideoCapture(r"C:\Users\Maruthi\Downloads\www.5MovieRulz.software - Love Oh Love (2026) 1080p TRUE WEB-DL - AVC - (DD+5.1 - 192Kbps) [Tel + Mal + Kan] - 2.6GB - ESub.mkv")

frames=[]

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

for i in range(len(frames)-1,-1,-1):
    cv2.imshow("Reverse Video",frames[i])
    if cv2.waitKey(30)&0xFF==27:
        break

cv2.destroyAllWindows()
