"""
Este script corta uma imagem em várias sprites de 256x256.

Escanear todas as subpastas na pasta atual.
Apagar todos os arquivos cujo nome termina com "import".
Apagar a pasta "cropped", se existir.
Criar a pasta "cropped" e realizar o corte das imagens como já está no código.
"""

import os
import shutil
from PIL import Image

def crop_image(input_path, output_path, crop_size):
    img = Image.open(input_path)
    img_width, img_height = img.size
    basename = os.path.splitext(os.path.basename(input_path))[0]
 
    # Create a subfolder inside the output directory with the name of the image
    subfolder_path = os.path.join(output_path, basename)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    # Calculate number of rows and columns of crops
    num_cols = img_width // crop_size
    num_rows = img_height // crop_size
    
    for j in range(num_rows):
        for i in range(num_cols):
            # Calculate crop box coordinates
            left = i * crop_size
            upper = j * crop_size
            right = left + crop_size
            lower = upper + crop_size
            box = (left, upper, right, lower)
            # Crop the image
            img_crop = img.crop(box)
            
            # Generate crop name based on crop position
            crop_name = f"{basename}_crop_{j}_{i}.png"
            
            # Save the cropped image
            img_crop.save(os.path.join(subfolder_path, crop_name))

def process_directory(directory, crop_size=256):
    # Delete all files ending with "import"
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('import'):
                os.remove(os.path.join(root, file))
    
    # Delete the "cropped" folder if it exists
    cropped_path = os.path.join(directory, 'cropped')
    if os.path.exists(cropped_path):
        shutil.rmtree(cropped_path)
    
    # Create the "cropped" folder
    os.makedirs(cropped_path)
    
    # Process images in the current directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            input_path = os.path.join(directory, filename)
            crop_image(input_path, cropped_path, crop_size)

def main():
    current_dir = os.getcwd()
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(current_dir):
        for directory in dirs:
            process_directory(os.path.join(root, directory))

if __name__ == "__main__":
    main()
