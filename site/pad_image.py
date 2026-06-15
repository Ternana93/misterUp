import sys
from PIL import Image

# Open the original image
img_path = 'images/chisiamo_hero_bg.png'
img = Image.open(img_path).convert('RGB')

# Original size: 1024x1024
# We want to add 1000px of padding to the LEFT, and maybe 200px to the TOP/BOTTOM to make it smaller overall.
pad_left = 1200
pad_top = 300
pad_bottom = 300
pad_right = 300

new_width = img.width + pad_left + pad_right
new_height = img.height + pad_top + pad_bottom

# Create a new image filled with the edge color (we'll sample a few and average, or just use 15,18,21)
bg_color = (13, 18, 21)
new_img = Image.new('RGB', (new_width, new_height), bg_color)

# Paste the original image
new_img.paste(img, (pad_left, pad_top))

# To avoid seams on top/bottom/right, we can optionally blur the edges, 
# but let's hope it's dark enough that it blends.
# Actually, let's just save it.
new_img.save('images/chisiamo_hero_bg_wide.png')
print("Image padded and saved as chisiamo_hero_bg_wide.png")
