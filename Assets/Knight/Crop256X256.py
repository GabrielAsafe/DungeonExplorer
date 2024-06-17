"""
Este script corta uma imagem em várias sprites de 256x256.

Para usar, execute-o na raiz da pasta onde deseja cortar as imagens.
"""

import os
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
    num_cols = img_width // 255
    num_rows = img_height // 255
    
    
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

def main():
    # Create the output directory if it doesn't exist
    output_dir = 'cropped'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all the file names in the current directory
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        # Process only image files (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            input_path = os.path.join(current_dir, filename)
            crop_image(input_path, output_dir, 256)  # Define o tamanho de corte como 256x256

if __name__ == "__main__":
    main()