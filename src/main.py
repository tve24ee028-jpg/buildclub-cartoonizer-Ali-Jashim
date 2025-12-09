import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg") 

if img is None:
    print("Error: input.jpg not found in assets/")
    exit()


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting BGR to RGB 

img_rgb_blur = cv2.medianBlur(img_rgb, 3)   # median blur to remove small noise

#To display blurred image
plt.figure(figsize=(12,6))  
plt.subplot(1,2,1)
plt.imshow(img_rgb); plt.title("Original")
plt.subplot(1,2,2)
plt.imshow(img_rgb_blur); plt.title("Blurred")
plt.show()

n = 6  
step = 255 // (n - 1) 
lut = np.array([ (i // step) * step for i in range(256) ], dtype=np.uint8)
posterized = cv2.LUT(img_rgb_blur, lut)

''' 
# To save output:
posterized_bgr = cv2.cvtColor(posterized, cv2.COLOR_RGB2BGR) # converting back to BGR for saving with OpenCV
cv2.imwrite("posterized_output.jpg", posterized_bgr)
'''
#To display posterized image
plt.figure(figsize=(12,6))
plt.subplot(1,2,1); plt.title("Original"); plt.imshow(img_rgb)
plt.subplot(1,2,2); plt.title(f"Posterized (n={n})"); plt.imshow(posterized)
plt.show()
