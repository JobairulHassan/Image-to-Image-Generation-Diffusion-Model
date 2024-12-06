# Image-to-Image Generation with Fine-Tuned Stable Diffusion and LoRA

This project leverages a fine-tuned version of **Stable Diffusion** for **image-to-image generation** using text prompts. The model was trained using a dataset of images with corresponding prompts and target images. The goal is to take an input image and generate a modified version of it based on a given text prompt. The project uses **LoRA** (Low-Rank Adaptation) for efficient model fine-tuning, and **PyTorch** for training the model.

## Features

- **Image-to-Image Generation**: Generate new images from existing images using text-based prompts.
- **Fine-Tuning with Stable Diffusion**: Fine-tune a pre-trained Stable Diffusion model using Hugging Face `lansinuote/diffusion.8.instruct_pix2pix` dataset.
- **LoRA**: Efficient fine-tuning of the model using LoRA for reduced memory usage and faster convergence.
- **Integration with `diffusers`**: Uses Hugging Face's `diffusers` library for Stable Diffusion.

## Dataset

Original Dataset [Link](https://huggingface.co/datasets/lansinuote/diffusion.8.instruct_pix2pix). Modify dataset after download using `dataset_preparation.py`. Modified dataset structure:
```
/dataset
    /train
        /source        # Input images
        /target        # Target images
        /prompts       # Text prompts for training
    /test
        /source        # Input images for testing
        /target        # Target images for testing
        /prompts       # Text prompts for testing
```
## Model Training

The model(`CompVis/stable-diffusion-v1-1`) is fine-tuned on dataset using the following steps:

- **Prepare the Data:** Place training images, target images, and prompts in the appropriate directories.
- **Configure the Training:** Update the batch size, number of epochs, and other parameters.
- **Train the Model:** Run the script to fine-tune the model.
- **Save Model:** Saving the model in proper directory.

## Testing the Model

- Load the fine-tuned model.
- Process the test data (input images and corresponding prompts).
- Generate images based on the given prompts and save them to the output directory.

## Dependencies

To run the project, the following dependencies installed:

- Python
- PyTorch (with CUDA support for GPU acceleration)
- Hugging Face `diffusers`
- Other required libraries (can be installed using the provided `requirements.txt` file)
