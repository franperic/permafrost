import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Import helperfunctions
import sys
sys.path.append("./02_code")
import helperfunctions


image_folder = sorted(glob.glob("01_data/timelapse_images_fast/*"))
image_color = helperfunctions.load_images(image_folder, col=True)
image_gscale = helperfunctions.load_images(image_folder)

a = np.asarray(image_gscale[0:2])
b = np.asarray(image_gscale[1:3])
    
c = helperfunctions.subtract_images(a, b)

a_color = np.asarray(image_color[70:72])[:, :, :, [2, 1, 0]]
b_color = np.asarray(image_color[71:73])[:, :, :, [2, 1, 0]]
c_color = helperfunctions.subtract_c_images(a_color, b_color)


vector_set, mean_vec = helperfunctions.find_vector_set(c[1], [535, 355], 5)
pca = PCA()
pca.fit(vector_set)
EVS = pca.components_
FVS = helperfunctions.find_FVS(EVS, c[1], mean_vec, [535, 355])
a, change = helperfunctions.clustering(FVS, 2, [531, 351])

# figsize=(15,17), 
fig = plt.figure(frameon=False)
ax1 = fig.add_subplot(121, frameon=False)
ax1 = plt.axis("off")
ax1 = plt.title("Difference Image")
ax1 = plt.imshow(c[1], cmap="gray")
ax2 = fig.add_subplot(122, frameon=False)
ax2 = plt.axis("off")
ax2 = plt.title("Movement Detection")
ax2 = plt.imshow(change, cmap="gray")
#plt.savefig("change_map_exmpl2.png", bbox_inches="tight")
plt.show()



fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1 = plt.imshow(cv2.cvtColor(a_color[1], cv2.COLOR_BGR2RGB))
ax2 = fig.add_subplot(122)
ax2 = plt.imshow(cv2.cvtColor(a_color[1], cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(c[0], cmap="gray")
plt.show()