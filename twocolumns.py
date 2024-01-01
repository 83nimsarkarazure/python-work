import cv2
import numpy as np

# Load the image with the table
image = cv2.imread("twocolumns.png")

# Define the coordinates and dimensions of the empty column
x1, y1, x2, y2 = 490, 30, 740, 90

# Define the text to fill the empty column
fill_value = "New Value"

# Crop the empty column
empty_column = image[y1:y2, x1:x2]

# Get the size of the empty column
height, width, _ = empty_column.shape

# Create a new image with the fill value
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 2
font_color = (0, 0, 0)  # Black
cv2.putText(
    empty_column,
    fill_value,
    (10, height // 2),
    font,
    font_scale,
    font_color,
    font_thickness,
)

# Update the original image with the filled column
image[y1:y2, x1:x2] = empty_column

# Save the result
cv2.imwrite("table_image_with_filled_column.png", image)

# Display the result (optional)
cv2.imshow("Filled Table Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
