import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Load images
image1 = cv2.imread('./admin/pht1.jpg')
image2 = cv2.imread('./pht2.jpg')

# Convert to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the images
faces1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)

# Check if at least one face was detected in both images
if len(faces1) > 0 and len(faces2) > 0:
    # Assuming you want to compare the first detected face in each image (adjust if needed)
    x1, y1, w1, h1 = faces1[0]
    x2, y2, w2, h2 = faces2[0]
    
    # Crop the faces from the images
    face1 = gray1[y1:y1+h1, x1:x1+w1]
    face2 = gray2[y2:y2+h2, x2:x2+w2]
    
    # Resize the faces to the same size for comparison
    face1_resized = cv2.resize(face1, (face2.shape[1], face2.shape[0]))
    
    # Compare the faces using structural similarity index (SSI)
    score, _ = ssim(face1_resized, face2, full=True)
    
    print(f"Similarity score: {score}")
    
    # If similarity score is more than 0.4, print "Face match"
    if score > 0.4:
        print("Face match!")
    else:
        print("Faces do not match.")
else:
    print("No faces detected in one or both images.")