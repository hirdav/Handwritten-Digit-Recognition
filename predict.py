import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import logging
from datetime import datetime

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename='logs/predict.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Load trained model
model = keras.models.load_model("mnist_model.h5")

def predict_digit(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28)) / 255.0
    img = img.reshape(1, 28, 28)
    prediction = model.predict(img)
    digit = np.argmax(prediction)
    return digit

def predict_folder(folder_path):
    results = {}
    for file in os.listdir(folder_path):
        if file.endswith(".png"):
            image_path = os.path.join(folder_path, file)
            digit = predict_digit(image_path)
            results[file] = digit
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"{timestamp} - Predicted {digit} for {file}")
            print(f"{file}: {digit}")
    return results



# Example usage
folder_path = "handwritten_images"  # Ensure this folder exists in your project
predict_folder(folder_path)