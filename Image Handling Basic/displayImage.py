import cv2 
img = cv2.imread('Resources/Photos/cat.jpg') #flag=0 for grey, 1 for color, -1 for unchanged
if img is not None:
    cv2.imshow("My image", img) #window name, image variable
    cv2.waitKey(0) #waits for a key to be pressed
    cv2.destroyAllWindows() #closes the window
else:
    print("Error: Could not read image.")
