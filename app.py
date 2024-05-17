from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io

app = Flask(__name__)

# Load model yang sudah disimpan
model = load_model('model-pistachio-3.h5')

# Definisikan kelas sesuai dengan urutan pelatihan
class_labels = ['Kirmizi_Pistachio', 'Siirt_Pistachio']

def prepare_image(image, target_size):
    # Preprocess the image
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image /= 255.0
    return image

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Read image file as BytesIO
    img_bytes = file.read()
    image = load_img(io.BytesIO(img_bytes), target_size=(128, 128))
    image = prepare_image(image, target_size=(128, 128))

    # Prediksi gambar
    preds = model.predict(image)
    pred_class = class_labels[np.argmax(preds)]

    return jsonify({'class': pred_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
