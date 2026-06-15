from PIL import Image

bg = Image.open('site/images/home_new.png').convert('RGBA')
bg_w, bg_h = bg.size

# Load machine images
m4 = Image.open('site/images/m4/m4_0.png').convert('RGBA')
m8 = Image.open('site/images/m8/m8_1.png').convert('RGBA')
m9 = Image.open('site/images/m9/m9_1.png').convert('RGBA')
m11 = Image.open('site/images/m11/m11_1.png').convert('RGBA')

machines = [m4, m8, m9, m11]
target_height = int(bg_h * 0.5)

# Resize all machines to the same height (or keep aspect ratio)
resized_machines = []
for m in machines:
    ratio = target_height / m.height
    new_w = int(m.width * ratio)
    resized = m.resize((new_w, target_height), Image.Resampling.LANCZOS)
    resized_machines.append(resized)

# Calculate total width to center them
total_w = sum(m.width for m in resized_machines)
spacing = 50
total_w += spacing * (len(machines) - 1)

start_x = (bg_w - total_w) // 2
if start_x < 0:
    # If they are too wide, scale them down further
    scale = (bg_w - 100) / total_w
    target_height = int(target_height * scale)
    resized_machines = []
    for m in machines:
        ratio = target_height / m.height
        new_w = int(m.width * ratio)
        resized = m.resize((new_w, target_height), Image.Resampling.LANCZOS)
        resized_machines.append(resized)
    total_w = sum(m.width for m in resized_machines) + spacing * (len(machines) - 1)
    start_x = (bg_w - total_w) // 2

# Actually maybe place them on the right side if the text is on the left?
# Looking at index.html: <div class="col-lg-7"> has the text. So the text takes about 7/12 = 58% of the width.
# So we should put the machines on the right side.
start_x = int(bg_w * 0.5) # start at 50%
available_w = bg_w - start_x - 50

total_w = sum(m.width for m in resized_machines) + spacing * (len(machines) - 1)
if total_w > available_w:
    scale = available_w / total_w
    target_height = int(target_height * scale)
    resized_machines = []
    for m in machines:
        ratio = target_height / m.height
        new_w = int(m.width * ratio)
        resized = m.resize((new_w, target_height), Image.Resampling.LANCZOS)
        resized_machines.append(resized)
    total_w = sum(m.width for m in resized_machines) + spacing * (len(machines) - 1)

start_x = bg_w - total_w - 50
y_offset = (bg_h - target_height) // 2 + 50 # slightly lower

current_x = start_x
for m in resized_machines:
    bg.alpha_composite(m, (current_x, y_offset))
    current_x += m.width + spacing

bg.convert('RGB').save('site/images/home_machines.png')
print("Image saved to site/images/home_machines.png")
