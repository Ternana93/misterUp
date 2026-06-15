import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # M6
    old_m6 = '<a class="rd-nav-link" href="m6.html"><i class="linearicons-wallet nav-icon"></i>M6</a>'
    new_m6 = '<a class="rd-nav-link" href="#" style="opacity: 0.4; pointer-events: none;"><i class="linearicons-wallet nav-icon"></i>M6 <i class="mdi mdi-lock-outline nav-icon" style="margin-left: 5px;"></i></a>'
    
    # Totem
    old_totem = '<a class="rd-nav-link" href="totem.html"><i class="linearicons-tablet nav-icon"></i>Totem</a>'
    new_totem = '<a class="rd-nav-link" href="#" style="opacity: 0.4; pointer-events: none;"><i class="linearicons-tablet nav-icon"></i>Totem <i class="mdi mdi-lock-outline nav-icon" style="margin-left: 5px;"></i></a>'

    if old_m6 in content or old_totem in content:
        content = content.replace(old_m6, new_m6)
        content = content.replace(old_totem, new_totem)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
