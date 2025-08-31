import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is None:
    print("Error loading image")
else:
    print("Image loaded successfully")
    pt1=(50,100) #(x,y), how much right to go, how much down to go
    pt2=(300,100) 
    color=(255,0,0) #BGR
    thickness=4
    cv2.line(img, pt1, pt2, color, thickness) #(src, start point, end point, color, thickness)
    cv2.imshow("Line Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
