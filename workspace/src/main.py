# https://pytorch.org/vision/stable/datasets.html

import argparse
import os

import numpy as np
import cv2

from torchvision.transforms import ToTensor
import torchvision


def parser_opt():
    parser = argparse.ArgumentParser()
    opt = parser.parse_args()
    return opt

def main(opt):
    pass
    # data_loader = torch.utils.data.DataLoader(imagenet_data,
    #                                           batch_size=4,
    #                                           shuffle=True,
    #                                            num_workers=args.nThreads)
    

if __name__ == '__main__':
    opt = parser_opt()
    main(opt)