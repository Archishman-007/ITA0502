import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\sunny\Downloads\images.jpg")

if img is None:
    print("ERROR: Image not found!")
    exit()

# Get image size
rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1]
])

# Destination points
pts2 = np.float32([
    [50, 100],
    [cols - 100, 50],
    [100, rows - 50]
])

# Calculate Affine Transformation Matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply transformation
result = cv2.warpAffine(img, M, (cols, rows))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transform", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
