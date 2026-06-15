import sys
from PIL import Image

def crop_image():
    img_path = 'images/chisiamo_hero_bg.png'
    img = Image.open(img_path).convert('RGB')
    
    # Crop the left 400 pixels to remove the hard vertical line
    # The image is 1024x1024
    cropped = img.crop((400, 0, 1024, 1024))
    
    cropped.save('images/chisiamo_hero_bg_cropped.png')
    print("Cropped successfully.")

if __name__ == '__main__':
    crop_image()
