# import necessary dependencies
import cv2, os
import numpy as np

# define path
input_dir = 'SfM_seafloor_benchmark_v4'
output_dir = 'SfM_seafloor_benchmark_v4_optimized'
os.makedirs('SfM_seafloor_benchmark_v4_optimized', exist_ok=True)

# adjust the figures 
alpha = 1.2 # contrast control (1.0-3.0)
beta = 10 # brightness control (0-100)
blue = 1.2 # increase the blue channel 
green = 0.85 # # reduce the green channel 

for filename in os.listdir(input_dir):

    if filename.endswith('.png'):
        im_path = os.path.join(input_dir, filename)
        im = cv2.imread(im_path)

        if im is not None:
            # adjust contrast and brightness
            adjusted_im = cv2.convertScaleAbs(im, alpha=alpha, beta=beta)

            # adjust colors BGR
            adjusted_im[:, :, 0] = np.clip(adjusted_im[:, :, 0] * blue, 0, 255)
            adjusted_im[:, :, 1] = np.clip(adjusted_im[:, :, 1] * green, 0, 255)
            adjusted_im = adjusted_im.astype(np.uint8) # 8-bit integer required for OpenCV

            # apply Gaussian filter to remove noise
            # reduced_noise_im = cv2.GaussianBlur(adjusted_im, (3, 3), 0) # kernel size and sigma (SD); 0 allows OpenCV to automatically calculate SD based on the kernel size

            # save image
            output_filename = f'{os.path.splitext(filename)[0]}_optimized.png'
            output_path = os.path.join(output_dir, output_filename)
            cv2.imwrite(output_path, adjusted_im)

            print(f'Processed and saved: {output_filename}')

        else:
            print(f'Failed to load: {output_filename}')

# visualization
# cv2.imshow('Adjusted Image', adjusted_im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()