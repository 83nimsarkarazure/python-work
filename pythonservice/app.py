from flask import Flask, request
from flask_cors import CORS
import pytesseract
from PIL import Image
from flask import Flask
from OpenSSL import SSL
import datetime
import os
import base64
from gtts import gTTS
from googletrans import Translator

app = Flask(__name__)

CORS(app)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] =  'C:\\Users\\hitesh\\Documents\\gptAi\python\\frauddetection\\pythonservice\\uploads'  # Create a 'uploads' folder in the same directory as your app

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.json.get('imgData')
    if data:
        try:
            # Decode the base64 image data
            image_data = base64.b64decode(data.split(",")[1])

            # Generate a unique filename or use a fixed one if needed
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{formatted_datetime}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the image to the server
            with open(filepath, 'wb') as file:
                file.write(image_data)
                image = Image.open(f"{app.config['UPLOAD_FOLDER']}\\"+filename)
                text = pytesseract.image_to_string(image)
                target_language = "mr"  # Change to your desired target language code (e.g., "fr" for French)
                # Translate the text to the target language
                translated_text = translate_text(text, target_language)
                tts = gTTS(translated_text,lang='mr')
                
                tts.save("output.mp3")
                os.system("start output.mp3") 
                print(text)

            return text, 200
        except Exception as e:
            print(e)
            return 'error', 500

    return 'error', 400



# def upload_image():
#     img_data = request.data
#     if img_data:
#         binary_data = base64.b64decode(img_data)
#         current_datetime = datetime.datetime.now()
#         formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
#         filename = f"{formatted_datetime}.png"

#         # Save the image data to a file in the 'uploads' directory
#         with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
#             f.write(binary_data)
#             image = Image.open(f"{app.config['UPLOAD_FOLDER']}"+filename)
#             text = pytesseract.image_to_string(image)
#             print(text)

#         return text, 200
#     else:
#         return "error", 400
    


if __name__ == '__main__':
    #app.run(debug=True) 
    app.run(debug=True, host='0.0.0.0', port=443, ssl_context='adhoc')