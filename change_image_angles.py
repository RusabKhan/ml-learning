from PIL import Image

def rotate_image(input_path, output_path, angle):
    # Open the image
    image = Image.open(input_path)

    # Rotate the image
    rotated_image = image.rotate(angle)

    # Save the rotated image
    rotated_image.save(output_path)

# Example usage
input_image_path = "_urdu.png"
output_image_path = "_urdu"

# Specify the angle by which you want to rotate the image
for i in range(0,10):
    input_image_path = "_urdu.png"
    output_image_path = "_urdu"
    
    input_image_path = f"img/urdu_numerals/{i}"+input_image_path
    output_image_path = f"img/urdu_numerals/{i}"+output_image_path
    
    for r in range(-40,40,10):
        rotation_angle = r
        rotate_image(input_image_path, output_image_path+f"{r}.png", rotation_angle)
