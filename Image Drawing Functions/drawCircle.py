import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is None:
    print("Could not read the image.")
else:
    print("Image Loaded Successfully")
    cv2.circle(img,(150,150),50,(0,0,255),thickness=-1) #(src, center, radius, color, thickness)
    cv2.imshow("Circle Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

