import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\sunny\Downloads\EXP13.jpg")

# Check if image is loaded
if img is None:
    print("ERROR: Image not found!")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Source points
pts1 = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

# Destination points
pts2 = np.float32([
    [100, 50],
    [cols - 100, 50],
    [50, rows - 50],
    [cols - 50, rows - 100]
])

# Calculate perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
result = cv2.warpPerspective(img, M, (cols, rows))

# Display original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transform", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
