import keras
import matplotlib.pyplot as plt
import tqdm
import numpy as np

def ShowImage(image):
	plt.imshow(image, cmap='gray')
	plt.show()

def ProcessImagesWithDense(images):
	images = images//255
	images = images.reshape((images.shape[0], images.shape[1]*images.shape[2]))
	return images

def ProcessImagesWithConv2D(images):
	images = images//255
	images = images.reshape((images.shape[0], images.shape[1], images.shape[2], 1))
	return images

def ProcessLabel(labels):
	return keras.utils.to_categorical(labels, len(np.unique(labels)))




