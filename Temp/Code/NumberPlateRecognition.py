from PIL import Image 
import pytesseract

# Read the images using pillow
img1 = Image.open("Number Plate Images/Try1.jpg")
img2 = Image.open("Number Plate Images/Try2.jpg")
img3 = Image.open("Number Plate Images/Try3.jpg")
img4 = Image.open("Number Plate Images/Try4.jpg")

# Rotate if necessary
ima4 = img4.rotate(350)

# Coordinates for the number plate
left1 = 675
top1 = 630
right1 = 1020
bottom1 = 734

left2 = 393
top2 = 347
right2 = 590
bottom2 = 395

left3 = 332
top3 = 300
right3 = 560
bottom3 = 370

left4 = 511
top4= 230
right4 = 1145
bottom4 = 440

# Crop the number plate
im1 = img1.crop((left1, top1, right1, bottom1)) 
im2 = img2.crop((left2, top2, right2, bottom2)) 
im3 = img3.crop((left3, top3, right3, bottom3)) 
im4 = ima4.crop((left4, top4, right4, bottom4)) 

# Save the number plates 
im1.save("Number Plate Images/Car1.jpg")
im2.save("Number Plate Images/Car2.jpg")
im3.save("Number Plate Images/Car3.jpg")
im4.save("Number Plate Images/Car4.jpg")

# Read the number plates
image1 = Image.open("Number Plate Images/Car1.jpg") 
image2 = Image.open("Number Plate Images/Car2.jpg") 
image3 = Image.open("Number Plate Images/Car3.jpg") 
image4 = Image.open("Number Plate Images/Car4.jpg") 

# Image to string function
def ocr_core(image1):
    text = pytesseract.image_to_string(Image.open(image1))
    return text
def ocr_core(image2):
    text = pytesseract.image_to_string(Image.open(image2))
    return text
def ocr_core(image3):
    text = pytesseract.image_to_string(Image.open(image3))
    return text
def ocr_core(image4):
    text = pytesseract.image_to_string(Image.open(image4))
    return text

# Print the output
print(ocr_core("Number Plate Images/Car1.jpg"))
print(ocr_core("Number Plate Images/Car2.jpg"))
print(ocr_core("Number Plate Images/Car3.jpg"))
print(ocr_core("Number Plate Images/Car4.jpg"))
