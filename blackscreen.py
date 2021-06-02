import cv2
import time 
import numpy as np
import keyboard


fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

cap = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

for i in range(60):
    ret,bg = cap.read()
#Flipping the background
bg = np.flip(bg,axis = 1)

while(cap.isOpened()):
    ret,img = cap.read()
    if not ret :
        break
    #Flipping the image for consistency
    img = np.flip(img,axis = 1)

    image = cv2.resize(img,(640,480))
    frame = cv2.resize(bg,(640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask = cv2.inRange(frame,u_black,l_black)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    

    f = frame-res
    f = np.where(f == 0,image,f)

    final_output = cv2.addWeighted(res, 1, image, 1, 0)
    output_file.write(final_output)
    #Displaying the output to the user
    cv2.imshow("magic", final_output)
    cv2.waitKey(45)

     
    if keyboard.is_pressed('Esc'):
        break

cap.release()
out.release()
cv2.destroyAllWindows() 