import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is not None:
    cropped = img[100:200,50:150] #img[start y: end y, start x: end x]
    cv2.imshow("Original Image",img)
    cv2.imshow("Cropped Image",cropped)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
else:
    print("Error: Could not read image.")