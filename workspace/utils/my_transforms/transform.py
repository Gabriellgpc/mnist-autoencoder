import numpy as np

def to_numpy(tensor_image):
    np_image = tensor_image.numpy()
    return np.transpose(np_image, (1, 2, 0))

