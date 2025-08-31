import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is None:
    print("Could not read the image.")
else:
    resized=cv2.resize(img,(300,300))#(src, dszie(width, height), fx, fy, interpolation))
    cv2.imshow("Original",img)
    cv2.imshow("Resized",resized)
    cv2.imwrite("Resized_cat.jpg",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
