import cv2 as cv
import numpy as np
from PIL import Image, ImageEnhance, ImageOps
import os #for saving files in directory

def convert_to_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# blur
def apply_blur(image, kernel_size=(15, 15)):
    return cv.GaussianBlur(image, kernel_size, 0)

# rotate hue
def rotate_hue(image, angle):
    pillow_image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    hsv_image = pillow_image.convert('HSV')
    h, s, v = hsv_image.split()
    np_h = np.array(h, dtype=int)
    np_h = (np_h + angle) % 256
    np_h = np_h.astype(np.uint8)
    h = Image.fromarray(np_h, mode='L')
    rotated_hue_image = Image.merge('HSV', (h, s, v)).convert('RGB')
    return cv.cvtColor(np.array(rotated_hue_image), cv.COLOR_RGB2BGR)

# Gaussian noise
def add_gaussian_noise(image, mean=0, sigma=25):
    gauss = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv.add(image, gauss)
    return noisy_image

# contrast
def adjust_contrast(image, factor=1.5):
    pillow_image = Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    enhancer = ImageEnhance.Contrast(pillow_image)
    contrasted_image = enhancer.enhance(factor)
    return cv.cvtColor(np.array(contrasted_image), cv.COLOR_RGB2BGR)

# invert colors
def invert_colors(image):
    return cv.bitwise_not(image)

# Load and resize image
image_path = 'D:/python/week2/image/5.png'
output_dir = 'D:/python/week2/image'

Img = cv.imread(image_path)

resized = cv.resize(Img, (500, 500), interpolation=cv.INTER_AREA)
    
grayscale_image = convert_to_grayscale(resized)
cv.imwrite(os.path.join(output_dir, 'grayscale_image.png'), grayscale_image)
    
blurred_image = apply_blur(resized)
cv.imwrite(os.path.join(output_dir, 'blurred_image.png'), blurred_image)


hue_rotated_image = rotate_hue(resized, 90)
cv.imwrite(os.path.join(output_dir, 'hue_rotated_image.png'), hue_rotated_image)

noisy_image = add_gaussian_noise(resized)
cv.imwrite(os.path.join(output_dir, 'noisy_image.png'), noisy_image)

contrasted_image = adjust_contrast(resized)
cv.imwrite(os.path.join(output_dir, 'contrasted_image.png'), contrasted_image)

inverted_image = invert_colors(resized)
cv.imwrite(os.path.join(output_dir, 'inverted_image.png'), inverted_image)

print('done')



