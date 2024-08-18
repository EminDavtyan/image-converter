import os
import sys
from PIL import Image

format_to = sys.argv[1]
source_dir = sys.argv[2]
output_dir = sys.argv[3]

formats = ["JPEG", "PNG", "GIF", "TIFF", "BMP", "PPM", "PPG", "PBM", "PGM", "WebP", "ICO", "DDS", "PCX", "PDF", "EPS", "IM", "MSP", "TGA", "XBM"]

assert os.path.exists(source_dir), 'Source directory not found'
assert format_to in formats, 'No matching format'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for filename in os.listdir(source_dir):
    img = Image.open(f'{source_dir}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_dir}{clean_name}.{format_to.lower()}', f'{format_to.lower()}')
