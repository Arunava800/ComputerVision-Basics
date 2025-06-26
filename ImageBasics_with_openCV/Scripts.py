import cv2

img = cv2.imread('00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)
    cv2.waitKey(1)&0xff ==27:
        break
        
cv2.destroyAllWindows()