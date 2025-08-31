import cv2
img = cv2.imread('Resources/Photos/cat.jpg')

if img is None:
    print("Error loading image")
else:
    cv2.putText(img, "This is a cat",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,255),2) #(img, text, org, font, fontScale, color, thickness)
    cv2.imshow("Image with text",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()