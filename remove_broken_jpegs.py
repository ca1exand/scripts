import argparse
import os
import glob
import PIL
from PIL import Image

def is_img_ok(fn):
  try:
    Image.open(fn)
    return True
  except:
    return False

def main():
    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
    file_list = []
    print("Looking for images in '" + FLAGS.image_dir + "'")
    c = 0
    for extension in extensions:
        for filename in glob.iglob(FLAGS.image_dir + '*.' + extension):
            c += 1
            if not is_img_ok(filename):
                print("Broken image discovered: " + filename)
                os.rename(filename, FLAGS.broken_dir + c + ".JPG")
                print("broken image moved to " + FLAGS.broken_dir)
    print(c + " images found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image_dir',
        type=str,
        default='',
        help='Path to folder of images.'
    )

    parser.add_argument(
        '--broken_dir',
        type=str,
        default='',
        help='Path to folder of broken images.'
    )

    FLAGS, unparsed = parser.parse_known_args()
    main()
