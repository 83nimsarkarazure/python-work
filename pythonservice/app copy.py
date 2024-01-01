from flask import Flask, request
from flask_cors import CORS
import pytesseract
from PIL import Image
from flask import Flask
from OpenSSL import SSL
import datetime
import os

app = Flask(__name__)
passphrase = 'password'
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('./certs/key.pem', passphrase=passphrase)
context.use_certificate_file('./certs/cert.pem')
CORS(app)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\hitesh\\Documents\\gptAi\python\\frauddetection\\pythonservice\\uploads'  # Create a 'uploads' folder in the same directory as your app

@app.route('/upload', methods=['POST'])
def upload_image():
    img_data = request.data
    if img_data:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{formatted_datetime}.png"

        # Save the image data to a file in the 'uploads' directory
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
            f.write(img_data)
            image = Image.open(f"{app.config['UPLOAD_FOLDER']}/"+filename)
            text = pytesseract.image_to_string(image)
            print(text)

        return text, 200
    else:
        return "error", 400
    


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=443, ssl_context=context)