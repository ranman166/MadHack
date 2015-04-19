import cv2
import numpy as np
import thread
import time
import winsound
cap = cv2.VideoCapture(0)
oldx = 0
oldy = 0
oldx2 = 0
oldy2 = 0
xlist = 0
ylist = 0
xlist2 = 0
ylist2 = 0
hit = "none"
drums = ("kick", "high", "snare", "tom", "bass")
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    #define range of blue color in HSV
    

    lower_blue = np.array([50, 50, 50], dtype=np.uint8)
    upper_blue = np.array([70,255,255], dtype=np.uint8)
    lower_orange = np.array([80, 100, 50], dtype=np.uint8)
    upper_orange = np.array([110,255,255], dtype=np.uint8)
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res2 = cv2.bitwise_and(frame,frame, mask= mask2)
    height, width, depth = res.shape
    res = cv2.blur(res,(5,5))          
    res2 = cv2.blur(res2,(5,5))     
    
                                                                                                
    cv2.imshow('res',res)
    cv2.imshow('res2',res2)                   
    
    xnum = 1
    ynum = 1
    for x in range(0,height,15):
        for y in range(0,width,15):
            if res[x][y][0] > 50:
                if res[x][y][0] < 70:
                                
                    xlist += x
                    ylist += y
                    xnum += 1
                    ynum += 1

    xlist = xlist/xnum
    ylist = ylist/ynum
    print ylist
    if oldx-xlist<-70:
        ##print ("1 hit at ", drums[ylist/(width/4)])
        sound = str(drums[ylist/(width/4)])+".wav"
        print sound
        winsound.PlaySound(sound, winsound.SND_FILENAME)
    oldx = xlist
                       
    xnum2 = 1
    ynum2 = 1
    for x in range(0,height,15):
        for y in range(0,width,15):
            if res2[x][y][0] > 80:
                if res2[x][y][0] < 110:
                                
                    xlist2 += x
                    ylist2 += y
                    xnum2 += 1
                    ynum2 += 1

    xlist2 = xlist2/xnum2
    ylist2 = ylist2/ynum2
    if oldx2-xlist2<-60:
        #print ("2 hit at ", drums[ylist2/(width/4)])
        sound = str(drums[ylist2/(width/4)])+".wav"
        print sound
        winsound.PlaySound(sound, winsound.SND_FILENAME)
        del sound
    oldx2 = xlist2  


        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
