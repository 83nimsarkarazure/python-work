from pdf2image import convert_from_path

# Specify the PDF file path
pdf_file = 'casteform.pdf'

# Convert each page to an image (TIFF format)
images = convert_from_path(pdf_file)

# Save the images
for i, image in enumerate(images):
    image.save(f'page_{i}.tiff')
