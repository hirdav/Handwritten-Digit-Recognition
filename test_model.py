import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
import os
import logging

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename='logs/test.log', level=logging.INFO)

# Load trained model
model = keras.models.load_model("mnist_model.h5")

# Load test dataset
(_, _), (X_test, y_test) = mnist.load_data()
X_test = X_test / 255.0

# Evaluate model
test_loss, test_acc = model.evaluate(X_test, y_test)
logging.info(f"Test accuracy: {test_acc:.4f}")
print(f"Test accuracy: {test_acc:.4f}")