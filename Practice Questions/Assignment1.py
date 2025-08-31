#Load an image, change it to gray scale, display it and save it to disk.
import cv2
img= cv2.imread('Resources/Photos/cat.jpg')
if img is not None:
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts to gray scale
    cv2.imshow("New gray image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save=cv2.imwrite("GrayCat.jpg",gray)
    if save:
        print("Image saved")
    else:
        print("Error saving image")
else:
    print("Error: Could not read image.")