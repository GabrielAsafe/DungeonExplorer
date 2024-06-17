"""
Essa imagem corta as imagens com várias sprites em várias de 256X256

Para usar basta executar ela na raiz da pasta que quer croppar
"""

import os
from PIL import Image

def crop_image(input_path, output_path, crop_width, crop_height):
    img = Image.open(input_path)
    img_width, img_height = img.size
    basename = os.path.splitext(os.path.basename(input_path))[0]
    
    # Create a subfolder inside the output directory with the name of the image
    subfolder_path = os.path.join(output_path, basename)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    for i in range(0, img_width, crop_width):
        for j in range(0, img_height, crop_height):
            box = (i, j, i + crop_width, j + crop_height)
            img_crop = img.crop(box)
            crop_name = f"{basename}_crop_{i}_{j}.png"
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
            crop_image(input_path, output_dir, 256, 256)

if __name__ == "__main__":
    main()
