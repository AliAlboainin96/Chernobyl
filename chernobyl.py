import numpy as np
import cv2 
import matplotlib.pyplot as plt


#  Loading the image to be tested
test_image = cv2.imread('boiis.jpg', cv2.IMREAD_COLOR)

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')


# Since we know that OpenCV loads an image in BGR format so we need to convert it into RBG format to be able to display its true colours. Let us write a small function for that.



def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

haar_cascade_face = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')

# Let us print the no. of faces found


def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors = 1)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    print('Faces found: ', len(faces_rect))
    
    return image_copy
    



#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image)

#convert to RGB and display image
plt.imshow(convertToRGB(faces))

cv2.imwrite('image1.png',faces)

final_image = cv2.imread('image1.png', cv2.IMREAD_COLOR)
cv2.imshow('Final', final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



def detectFace()

def detectMovement()

def processImage()
