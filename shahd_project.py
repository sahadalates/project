import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("bars")
cv2.createTrackbar("L - H", "bars", 0, 179, nothing)
cv2.createTrackbar("L - S", "bars", 0, 255, nothing)
cv2.createTrackbar("L - V", "bars", 0, 255, nothing)
cv2.createTrackbar("U - H", "bars", 179, 179, nothing)
cv2.createTrackbar("U - S", "bars", 255, 255, nothing)
cv2.createTrackbar("U - V", "bars", 255, 255, nothing)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "bars")
    l_s = cv2.getTrackbarPos("L - S", "bars")
    l_v = cv2.getTrackbarPos("L - V", "bars")
    u_h = cv2.getTrackbarPos("U - H", "bars")
    u_s = cv2.getTrackbarPos("U - S", "bars")
    u_v = cv2.getTrackbarPos("U - V", "bars")
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])
    maskB = cv2.inRange(hsv, lower_blue, upper_blue)
    maskG = cv2.inRange(hsv, lower_green, upper_green)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    
    resultB = cv2.bitwise_and(frame, frame, mask=maskB)
    resultG = cv2.bitwise_and(frame, frame, mask=maskG)
    resultR = cv2.bitwise_and(frame, frame, mask=maskR)
    result = cv2.bitwise_and(resultB , resultG , resultR )
    
    cv2.imshow("frame", frame)
  
    cv2.imshow("result", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()