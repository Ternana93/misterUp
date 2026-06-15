import sys
from PIL import Image, ImageFilter

def create_full_bg():
    img_path = 'images/chisiamo_hero_bg.png'
    img = Image.open(img_path).convert('RGB')
    w, h = img.size # 1024x1024

    # We want to fill the left side (0 to ~600px) with tech patterns.
    # The right side (500 to 1024) has the cash register and nice lines.
    # Let's take a slice of the top-right which is just lines
    # Let's say x=600 to 1024, y=0 to 400
    slice1 = img.crop((600, 0, 1024, 424)) # 424x424
    
    # We can paste it in a loop or strategically
    # Top Left
    p1 = slice1.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(p1, (0, 0))
    
    # Middle Left
    p2 = slice1.transpose(Image.FLIP_TOP_BOTTOM)
    img.paste(p2, (0, 424))
    
    # Bottom Left
    p3 = slice1.transpose(Image.ROTATE_180)
    img.paste(p3, (0, 848))
    
    p4 = slice1.transpose(Image.ROTATE_90)
    img.paste(p4, (176, 0)) # filling the gap
    
    # To make it blend better and not distract too much from the text,
    # let's blur the left side heavily or darken it? No, user explicitly asked for no black part.
    
    img.save('images/chisiamo_hero_bg_full.png')
    print("Full background image created.")

if __name__ == '__main__':
    create_full_bg()
