import cv2
import numpy as np

# Image path
image_path = r"C:\Users\sunny\Downloads\EXP14.jpg"

# Read image
img = cv2.imread(image_path)

# Check image
if img is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
height, width = img.shape[:2]

# Move image
x = 100
y = 50

# Translation matrix
matrix = np.float32([
    [1, 0, x],
    [0, 1, y]
])

# Apply translation
moved = cv2.warpAffine(
    img,
    matrix,
    (width, height)
)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved)

# Save output
output_path = r"C:\Users\sunny\Downloads\moved.jpg"
cv2.imwrite(output_path, moved)

print("Image moved successfully.")
print("Output saved at:", output_path)

# Press any key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
