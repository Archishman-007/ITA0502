import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\sunny\Downloads\EXP15.jpg")

# Check if image is loaded
if img is None:
    print("ERROR: Image not found!")
    exit()

# Get image dimensions
rows, cols = img.shape[:2]

# Source points
src_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

# Destination points
dst_points = np.float32([
    [100, 50],
    [cols - 100, 20],
    [50, rows - 50],
    [cols - 50, rows - 100]
])

# Direct Linear Transformation
H = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply transformation
result = cv2.warpPerspective(img, H, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Direct Linear Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
