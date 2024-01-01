import pytesseract
from PIL import Image

# Open an image using PIL (Python Imaging Library)
image = Image.open('image.png')

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print or process the extracted text
print(text)
