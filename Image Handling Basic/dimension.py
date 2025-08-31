import cv2
img = cv2.imread('Resources/Photos/cat.jpg')
if img is not None:
    h, w, c= img.shape
    print(f"Image Loaded:\nHeight: {h}\n Width {w}\nChannels: {c}")
else:
    print("Error: Could not read image.")