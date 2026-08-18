import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\sunny\Downloads\EXP14.jpg")

# Check image
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
    [80, 60],
    [cols - 80, 30],
    [40, rows - 60],
    [cols - 40, rows - 30]
])

# Calculate Homography matrix
H, status = cv2.findHomography(src_points, dst_points)

# Apply Homography transformation
result = cv2.warpPerspective(img, H, (cols, rows))

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Homography Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
