import argparse
from PIL import Image

parser = argparse.ArgumentParser(
    prog='Image shrinker',
    description='Abizaidlab website tool')

parser.add_argument('input_file', type=str, help="The input filepath")
parser.add_argument('output_file', type=str, help="The output filepath")
parser.add_argument('scale', type=float, help="How much to shrink image, e.g. 0.2 is 2/10ths the width/height") 

args = parser.parse_args()

image = Image.open(args.input_file)
width, height = image.size
print(f"Original size: width={width}, height={height}")

new_width = int(width * args.scale)
new_height = int(height * args.scale)
new_image = image.resize((new_width, new_height))


new_image.save(args.output_file)
print(f"New size: width={new_width}, height={new_height}")