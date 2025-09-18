import cv2 # type: ignore

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0

while True:
    ret,frame = cam.read()
    
    if not ret:
        print("failed to Grab frame")
        break
    cv2.imshow("Test",frame)
    
    k = cv2.waitKet(1)

    if k%256 == 27:
        print("Escape hit, Closing the app")
        break
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("Screenshot taken")
        img_counter+=1

cam.release()
cam.destroyAllWindows()
    