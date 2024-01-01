import cv2

# Load the preprocessed image
image = cv2.imread("C:\\Users\\hitesh\\Documents\\gptAi\\python\\frauddetection\\image.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Connected component analysis
_, labels, stats, centroids = cv2.connectedComponentsWithStats(gray_image, connectivity=4)

# Define lists to store bounding boxes
bounding_boxes = []

# Iterate through the connected components
min_width=40
min_height=40
for label in range(1, len(stats)):
    x, y, w, h = stats[label][:4]  # Get the position and size of the component
    if w > min_width and h > min_height:  # Filter based on size criteria
        bounding_boxes.append((x, y, x + w, y + h))  # Store the bounding box

# Visualize the bounding boxes (optional)
for (x_min, y_min, x_max, y_max) in bounding_boxes:
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

# Display the image with bounding boxes (optional)
cv2.imshow("Bounding Box Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
