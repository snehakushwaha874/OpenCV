import cv2 as cv
img = cv.imread('Resources/Photos/cat.jpg') #flag=0 for grey, 1 for color, -1 for unchanged
if img is None:
    print("Error: Could not read image.")
else:
    print("Image loaded successfully.")
