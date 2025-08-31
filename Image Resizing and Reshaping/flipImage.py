import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is not None:
    flipped=cv2.flip(img,1)#(src, flipCode : 0=vertical, 1=horizontal, -1=both)
    cv2.imshow("Original Image",img)
    cv2.imshow("Flipped Image", flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error could not load image")