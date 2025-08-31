import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is not None:
    (h, w) = img.shape[:2]
    center=(w//2,h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)#(center, angle, scale)(scale :: 1.0= same size, 0.5 = half, 2.0 = double)
    rotated = cv2.warpAffine(img,M,(w,h))#(src, M, dsize)
    cv2.imshow("Original Image",img)
    cv2.imshow("Rotated Image",rotated)
    cv2.waitKey(0)
    cv2.destryAllWindows()
else:    
    print("Error: Could not read image.")