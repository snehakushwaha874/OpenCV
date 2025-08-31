import cv2
img=cv2.imread('Resources/Photos/cat.jpg')

if img is None:
    print("Could not read the image.")
else:
    print("Image Loaded Successfully")
    pt1= (50,50) #top-left corner point
    pt2= (300,150)#bottom-right corner point
    color= (255,255,0) #BGR color
    thickness= -1 #thickness of the line (-1 for filled rectangle)
    rectangle=cv2.rectangle(img,pt1,pt2,color,thickness) #(src, top-left point, bottom-right point, color, thickness)
    cv2.imshow("Rectangle Image", rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()