import numpy as np
from PIL import Image
from scipy.fft import fft2, ifft2

def jpeg_compress(image_path, quality_factor):
    """
    Perform JPEG compression on an image using the Fourier Transform.

    Parameters:
        image_path (str): The path of the image to be compressed.
        quality_factor (int): The quality factor, between 1 and 100.

    Returns:
        compressed_image (numpy array): The compressed image.
    """
    # Open image
    image = Image.open(image_path)
    # Get image data in numpy array format
    image_data = np.array(image)
    # Perform 2D Fourier Transform on image data
    fft_image = fft2(image_data)
    # Get the center of the spectrum
    center_x, center_y = fft_image.shape[0]//2, fft_image.shape[1]//2
    # Generate mask
    mask = np.zeros(fft_image.shape)
    mask[center_x-quality_factor:center_x+quality_factor,
         center_y-quality_factor:center_y+quality_factor] = 1
    # Multiply the spectrum with the mask
    compressed_fft_image = fft_image * mask
    # Perform Inverse Fourier Transform to get the compressed image
    compressed_image = np.real(ifft2(compressed_fft_image))
    return compressed_image

# Example usage:
image_path = "image.jpg"
quality_factor = 10
compressed_image = jpeg_compress(image_path, quality_factor)
