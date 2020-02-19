import os
import pickle as pk
import numpy as np
import matplotlib.image as mpimg
import tqdm


def GetImageShape(fname):
	ti = mpimg.imread(fname)
	return ti.shape

def Save(fname, obj):
	with open(fname, 'wb') as f:
		pk.dump(obj, f, protocol = pk.HIGHEST_PROTOCOL)
	print('OK! Save in: ' + fname)


def SaveImageAsPk(fname, processor = None):
	path = 'set\\' + fname
	files = os.listdir(path)
	print('Save image from: ' + path)

	ims = GetImageShape(path + '\\' + files[0])
	timage = np.zeros((len(files), ) + ims)

	i = 0
	for f in tqdm.tqdm(files, ncols = 80):
		ti = mpimg.imread(path + '\\' + f)
		timage[i] = ti
		i += 1

	if processor:
		print('------- Process with', processor.__name__, '-------')
		timage = processor(timage)

	Save(fname + "image.pk", timage)


def SaveLabelAsPk(fname, processor = None):
	print('Save label from: ' + fname + 'label.txt')
	lab = np.loadtxt(fname + 'label.txt', dtype = int)

	if processor:
		print('------- Process with', processor.__name__, '-------')
		lab = processor(lab)

	Save(fname + "label.pk", lab)

