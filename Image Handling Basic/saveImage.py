import cv2
img = cv2.imread('Resources/Photos/cat.jpg') #flag=0 for grey, 1 for color, -1 for unchanged
if img is not None:
    save= cv2.imwrite('output.jpg', img) #file name, image variable
    if save:
        print("Image saved successfully")
    else:
        print("Could not save image")
else:
    print("Could not read image.")
