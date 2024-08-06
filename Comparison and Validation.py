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

def plot_histogram(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error loading image {image_path}")
        return None
    plt.hist(image.ravel(), bins=256, range=[0, 256], density=True)
    plt.title('Histogram of Pixel Values')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

def calculate_noise_variance(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Error loading image {image_path}")
        return None
    noise_variance = np.var(image)
    return noise_variance

def compare_variances(image_variances, homogeneous_image_variances):
    differences = []
    for i, (img_var, homo_var) in enumerate(zip(image_variances, homogeneous_image_variances)):
        print(f"Image {i+1} - Top 10% Blocks Variance: {img_var}, Homogeneous Surface Variance: {homo_var}")
        difference = abs(img_var - homo_var)
        differences.append(difference)
        print(f"Difference: {difference}")
    return differences

# Directory paths
image_directory = r"C:\Users\Fredrich Bernard\Desktop\Online Writing\Pullman\New folder (2)\Photos"
homogeneous_image_directory = r"C:\Users\Fredrich Bernard\Desktop\Online Writing\Pullman\New folder (2)\Photos\Homogeneous"

# Process images and homogeneous images
image_variances = process_images_in_directory(image_directory)
homogeneous_image_variances = process_images_in_directory(homogeneous_image_directory)

# Plot histograms for homogeneous images
for filename in os.listdir(homogeneous_image_directory):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        image_path = os.path.join(homogeneous_image_directory, filename)
        plot_histogram(image_path)

# Calculate noise variances for homogeneous images
homogeneous_noise_variances = []
for filename in os.listdir(homogeneous_image_directory):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        image_path = os.path.join(homogeneous_image_directory, filename)
        noise_variance = calculate_noise_variance(image_path)
        if noise_variance is not None:
            homogeneous_noise_variances.append(noise_variance)
            print(f"Processed homogeneous {filename}: Noise variance: {noise_variance}")

# Compare variances
differences = compare_variances(image_variances, homogeneous_noise_variances)

# Plotting variances and differences
x = np.arange(1, len(image_variances) + 1)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, image_variances, 'r', label='Top 10% Blocks Variance')
plt.plot(x, homogeneous_noise_variances, 'b', label='Homogeneous Surface Variance')
plt.xlabel('Image Index')
plt.ylabel('Variance')
plt.title('Variance Comparison')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, differences, 'g', label='Difference')
plt.xlabel('Image Index')
plt.ylabel('Difference')
plt.title('Variance Differences')
plt.legend()

plt.tight_layout()
plt.show()
