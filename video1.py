import cv2
a = cv2.VideoCapture("C:/Users/hp/Downloads/mixkit-baby-on-the-belly-of-his-mother-plays-and-smiles-4042.mp4")
while True:
    ret,frame = a.read()
    frame = cv2.resize(frame,(200,200))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break
a.release()
cv2.destroyAllWindows()


