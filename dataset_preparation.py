from datasets import load_dataset
ds = load_dataset("lansinuote/diffusion.8.instruct_pix2pix")

import os
from PIL import Image

# Define directories
input_folder = 'dataset/input_images'
output_folder = 'dataset/output_images'
text_folder = 'dataset/prompts'

# Create directories if they do not exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

for i in range(len(ds['train'])):
    input_image_path = os.path.join(input_folder, f'{i+1}.jpg')
    output_image_path = os.path.join(output_folder, f'{i+1}.jpg')
    text_file_path = os.path.join(text_folder, f'{i+1}.txt')

    # Save the input image as JPEG
    ds['train']['input'][i].convert("RGB").save(input_image_path, 'JPEG')

    # Save the output image as JPEG
    ds['train']['output'][i].convert("RGB").save(output_image_path, 'JPEG')

    # Save the prompt text in a file
    with open(text_file_path, 'w') as f:
        f.write(ds['train']['text'][i])