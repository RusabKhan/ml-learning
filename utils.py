import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import tensorflow as tf


def check(load_model="numerical_model.h5"):
    model = tf.keras.models.load_model(
        f"models/{load_model}"
    )  # Replace with your model path

    # Load the image from your local machine
    image_path = "img/drawing.png"  # Replace with the path to your image
    image = Image.open(image_path)

    # Convert the image to grayscale (if needed) and resize it to 28x28 pixels
    image = image.convert("RGB")  # Convert to grayscale
    image = image.resize((28, 28))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize pixel values to be between 0 and 1
    # image_array = image_array / 255.0

    # Reshape the image to match the input shape expected by the model
    image_array = image_array.reshape((1, 28, 28))

    # Use the trained model to predict on the loaded image
    predictions = model.predict(image_array)

    # Get the predicted label (digit with highest probability)
    predicted_label = predictions.argmax()

    print(f"Predicted Label: {predicted_label}")
    return predicted_label
