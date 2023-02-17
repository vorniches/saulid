from PIL import Image
import os


def reduce_image_quality(image_path):
    """
    Reduces the quality of the given image, resizes it to be 2x wider with a maximum
    width of 500 pixels, and saves it with a new name for fun.

    Args:
        image_path (str): The path to the image file.
    """

    # Open the image file
    img = Image.open(image_path)

    # Reduce the image quality
    img = img.convert('RGB')

    # Construct the new file name
    base_path, extension = os.path.splitext(image_path)
    original_name = os.path.basename(base_path)
    new_name = f"saulid-{original_name}{extension}"
    new_path = os.path.join(os.path.dirname(base_path), new_name)

    # Resize the image to be 50% wider
    width, height = img.size
    new_width = int(width * 3)
    img = img.resize((new_width, height))

    # Resize the image to have a maximum width of 500 pixels
    if new_width > 500:
        new_width = 500
        new_height = 230
        img = img.resize((new_width, new_height))

    # Reduce the image quality
    img.save(new_path, quality=10)

    print(f"New image saved at {new_path}")


# Ask the user to input the path to the image file
image_path = input("Please enter the path to the image file: ")

# Call the reduce_image_quality function with the user-specified parameters
reduce_image_quality(image_path)
