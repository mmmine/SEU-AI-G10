import pickle as pk

def load(fname):
	timage = None
	tlabel = None

	with open(fname + 'image.pk', 'rb') as f:
		timage = pk.load(f)

	with open(fname + 'label.pk', 'rb') as f:
		tlabel = pk.load(f)

	return (timage, tlabel)


def load_train():
	return load('train')

def load_test():
	return load('test')
