import cv2
import numpy as np

def preprocess_image(image):
    # Preprocess the image (resize, thresholding, etc.)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresh

def compare_images(image1, image2):
    # Compare two preprocessed fingerprint images
    score = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)
    return score[0][0]

# Load reference and verification fingerprint images
ref_image = cv2.imread('ref_left2.jpg')
verification_image = cv2.imread('query_left.jpg')

# Preprocess the images
ref_fingerprint = preprocess_image(ref_image)
verification_fingerprint = preprocess_image(verification_image)

# Compare the two fingerprints
similarity_score = compare_images(ref_fingerprint, verification_fingerprint)

# Define a threshold for similarity
threshold = 0.7

# Perform verification
if similarity_score > threshold:
    print("Fingerprint Verified!")
else:
    print("Fingerprint Not Verified!")
