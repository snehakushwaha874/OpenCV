import cv2
img = cv2.imread('Resources/Photos/cat.jpg')
if img is not None:
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts to gray scale
    cv2.imshow("Gray Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read image.")
