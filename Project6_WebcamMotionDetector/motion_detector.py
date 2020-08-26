import cv2, time

video=cv2.VideoCapture(0)

first_frame=None
while True:
    check, frame = video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    
    delta_frame=cv2.absdiff(first_frame,gray2)

    thresh_delta=cv2.threshold(delta_frame,30, 255, cv2.THRESH_BINARY)[1]

    
    cv2.imshow("Color", frame)
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_delta)


    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()