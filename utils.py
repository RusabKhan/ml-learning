import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import tensorflow as tf
import os


def check(
    current_time,
    image_path,
    load_model="numerical_model_convolutional_2_fine_tuned_urdu_224.h5",
):
    model = tf.keras.models.load_model(
        f"{os.getcwd()}/models/{load_model}"
    )  # Replace with your model path # Replace with the path to your image
    image = Image.open(image_path)

    # Convert the image to grayscale (if needed) and resize it to 28x28 pixels
    image = image.convert("L")  # Convert to grayscale
    image = image.resize((224, 224))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize pixel values to be between 0 and 1
    # image_array = image_array / 255.0

    # Reshape the image to match the input shape expected by the model
    image_array = image_array.reshape((1, 224, 224))

    # Use the trained model to predict on the loaded image
    predictions = model.predict(image_array)

    # Get the predicted label (digit with highest probability)
    predicted_label = predictions.argmax()

    print(f"Predicted Label: {predicted_label}")
    return predicted_label


def add_noise():
    # Load the image from your local machine
    image_path = "img/drawing.png"  # Replace with the path to your image
    image = Image.open(image_path)

    # Resize the image to 28x28
    target_size = (28, 28)
    image = image.resize(target_size)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Add Gaussian noise
    mean = 0
    variance = 100
    sigma = np.sqrt(variance)
    noise = np.random.normal(mean, sigma, image_array.shape).astype("uint8")
    noisy_image_array = np.clip(image_array + noise, 0, 255).astype("uint8")

    # Convert the noisy array back to a PIL image
    noisy_image = Image.fromarray(noisy_image_array)

    # Display the original and noisy images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")  # Assuming it's a grayscale image
    plt.title("Original Image (28x28)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(noisy_image, cmap="gray")  # Assuming it's a grayscale image
    plt.title("Noisy Image (28x28)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
