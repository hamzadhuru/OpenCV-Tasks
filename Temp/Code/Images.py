import cv2
import numpy as np

# Read image 

img = cv2.imread("Images/Dog.png")
im1 = cv2.imread("Images/Lambo.png")
im2 = cv2.imread("Images/Tree.png")
im3 = cv2.imread("Images/Group.jpg")

# Show image 

cv2.imshow("Dog", img)
cv2.imshow("Lamborghini", im1)
cv2.imshow("Tree", im2)
cv2.imshow("Group", im3)

# Convert image into Gray, Blur, Canny, Dialation & Eroded image 

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilate = cv2.dilate(imgCanny, kernel, iterations = 1)
imgErode = cv2.erode(imgDilate, kernel, iterations = 1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDilate)
cv2.imshow("Eroded Image", imgErode)

# Resize image into: (i) Smaller than original & (ii) Upto to screen size 

imgShrink = cv2.resize(img, (150,150))
imgEnlarge = cv2.resize(img, (1550,800))

cv2.imshow("Shrunken Image", imgShrink)
cv2.imshow("Enlarged Image", imgEnlarge)

# Cropping of image 

imgCropped = img[10:170, 100:260]

cv2.imshow("Cropped Image", imgCropped)

# Insertion of shapes (rectangle & circle) in the given image 

cv2.rectangle(img, (20,50), (100,150), (0,255,255), 0)
cv2.circle(img, (60,100), 40, (0,255,0), 1)

cv2.imshow("Image", img)

# Join two different images 
# We are using resize to get the dimensions same for both in order to join 

im1resize = cv2.resize(im1, (200,300))
im2resize = cv2.resize(im2, (200,300))

imstack = np.hstack((im1resize,im2resize))

cv2.imshow("Joined Images", imstack)

# Face detection on the given image of group (im3) as we have performed read function above

im3Gray = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)
faceCassade = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")
faces = faceCassade.detectMultiScale(im3Gray, 1.1 ,4)

for (x,y,w,h) in faces:
    cv2.rectangle(im3, (x,y), (x+w,y+h), (0,0,255), 3)
    cv2.imshow("Result", im3)
    
cv2.waitKey(0)
