# https://pytorch.org/vision/stable/datasets.html

import argparse
import os

import numpy as np
import cv2

from torchvision.transforms import ToTensor
import torchvision

def to_np_image(tensor_image):
    np_image = tensor_image.numpy()
    return np.transpose(np_image, (1, 2, 0))

def parser_opt():
    parser = argparse.ArgumentParser()
    opt = parser.parse_args()
    return opt

def main(opt):
    mnist_dataset = torchvision.datasets.MNIST('/datasets/', train=True, download=True, transform=ToTensor())
    
    # print(mnist_dataset.classes)
    for idx, (image, label) in enumerate(mnist_dataset):
        # print(label)
        # print(image.shape)

        uint8_image = to_np_image(image)*255
        cv2.imwrite(f'{idx}.jpg', uint8_image)
        if idx >= 5:
            break
    # data_loader = torch.utils.data.DataLoader(imagenet_data,
    #                                           batch_size=4,
    #                                           shuffle=True,
    #                                            num_workers=args.nThreads)
    

if __name__ == '__main__':
    opt = parser_opt()
    main(opt)