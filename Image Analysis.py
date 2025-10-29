
import cv2 
import numpy as np
import os
import matplotlib.pyplot as plt

def divide_into_blocks(image, block_size=5):
    h, w = image.shape
    blocks = []
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = image[y:y+block_size, x:x+block_size]
            if block.shape == (block_size, block_size):
                blocks.append(block)
    return blocks

def calculate_mean_variance(blocks):
    mean_variances = []
    for block in blocks:
        mean = np.mean(block)
        variance = np.var(block)
        mean_variances.append((mean, variance))
    return mean_variances

def process_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error loading image {image_path}")
        return None
    blocks = divide_into_blocks(image)
    mean_variances = calculate_mean_variance(blocks)
    
    sorted_blocks = sorted(mean_variances, key=lambda x: x[1])
    top_10_percent_index = int(len(sorted_blocks) * 0.1)
    top_10_percent_blocks = sorted_blocks[-top_10_percent_index:]
    
    average_variance = np.mean([block[1] for block in top_10_percent_blocks])
    return average_variance

def process_images_in_directory(directory_path):
    variances = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            image_path = os.path.join(directory_path, filename)
            variance = process_image(image_path)
            if variance is not None:
                variances.append(variance)
                print(f"Processed {filename}: Average variance of top 10% blocks: {variance}")
    return variances

directory_path = r"C:\Users\Fredrich Bernard\Desktop\Online Writing\Pullman\New folder (2)\Photos"
variances = process_images_in_directory(directory_path)

print(f"Variances for all images: {variances}")













