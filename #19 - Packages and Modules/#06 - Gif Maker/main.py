import contextlib
from PIL import Image
import glob

fp_input = "image_*.png"
fp_output = "awesome.gif"

def make_gif(fp_input):
    image_files = sorted(glob.glob(fp_input))

    if not image_files:
        print("No image files found in the specified directory.")
        return

    with contextlib.ExitStack() as stack:
        imgs = [stack.enter_context(Image.open(f)) for f in image_files]
        img = imgs[0]
        img.save(fp_output, format='GIF', append_images=imgs[1:], save_all=True, duration=200, loop=0)

if __name__ == '__main__':
    make_gif(fp_input)
