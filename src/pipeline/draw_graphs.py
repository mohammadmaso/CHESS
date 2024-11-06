from langchain_core.runnables.graph import MermaidDrawMethod
from PIL import Image
import io
import os


def save_image_from_bytes(image_bytes, folder_path, file_name):
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    # Create a full file path
    file_path = os.path.join(folder_path, file_name)
    
    # Open the image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Save the image as PNG
    image.save(file_path, 'PNG')
    
    print(f"Image saved successfully at {file_path}")

