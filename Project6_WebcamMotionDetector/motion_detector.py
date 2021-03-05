import cv2, time
from datetime import datetime
import pandas

video=cv2.VideoCapture(0)

first_frame=None
status_list=[None, None]
times=[]

while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray2=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray2
        continue
    
    delta_frame=cv2.absdiff(first_frame,gray2)
    thresh_delta=cv2.threshold(delta_frame,30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_delta, None, iterations=2)
    
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    status_list.append(status)
    
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())


    # cv2.imshow("Color", frame)
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_delta)
    cv2.imshow("Color Frame", frame)


    key = cv2.waitKey(1)
    # print(gray)
    # print(delta_frame)

    if key==ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

# Save times data to .csv WITHOUT Pandas
f = open("times.csv", "w")
f.write("Enter, Exit\n")

for i in range(0,len(times),2):
    f.write(str(times[i])+", "+str(times[i+1])+"\n")

f.close()
f = open("times.csv", "r")
print(f.read())

# Save times data to .csv WITH Pandas


video.release()
cv2.destroyAllWindows()