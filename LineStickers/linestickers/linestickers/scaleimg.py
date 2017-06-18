#!/usr/bin/env python3

import os
import traceback
import PIL
from PIL import Image

def main():
    wd = os.getcwd()
    upscale_sz = (512, 512)
    upscale_dir = wd + '/scrapped/upscale'

    try:
        os.mkdir(upscale_dir)
    except OSError:
        print('upscale directory exist. Proceeding.')

    try:
        list_img_dir = wd + '/scrapped/full'
        list_img = os.listdir(list_img_dir)
        if (len(list_img) == 0):
            print('Empty directory')
            return
        img_count = 0
        for img in os.listdir(list_img_dir):
            try:
                orig_img = Image.open(list_img_dir + '/' + img)
                print(orig_img)
                scaled_img = orig_img.resize(upscale_sz, resample=PIL.Image.NEAREST)
                scaled_img.save(upscale_dir + '/' + img)
                img_count += 1
            except (IOError):
                print("Can't open " + img)
                traceback.print_exc()
                pass

    except (OSError):
        print('Something went wrong.')
        traceback.print_exc()

    print('Done.' + str(img_count) + ' images were upscaled to ' + str(upscale_sz))


if __name__ == '__main__':
    main()


