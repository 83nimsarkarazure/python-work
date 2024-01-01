import cv2
import pytesseract

image = cv2.imread("certificate.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR to get text and bounding box information
results = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

# Iterate through the detected text regions
for i in range(len(results["text"])):
    # Extract text, coordinates, and dimensions
    text = results["text"][i]
    x, y, w, h = results["left"][i], results["top"][i], results["width"][i], results["height"][i]

    # Filter out non-empty and non-whitespace text (customize as needed)
    if text.strip():
        print(f"Text: {text}")
        print(f"Coordinates (x, y): ({x}, {y})")
        print(f"Dimensions (width, height): ({w}, {h}")
        print("-" * 30)

        # Draw a bounding box around the detected text
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        
# Define the coordinates and dimensions of the empty column
x1, y1, x2, y2 = 493, 35, 350, 350

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

# Display the image with bounding boxes
cv2.imshow("Text Regions with Coordinates", image)
cv2.waitKey(0)
cv2.destroyAllWindows()