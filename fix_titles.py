import os

replacements = {
    'm4.html': 'MisterUp M4',
    'm6.html': 'MisterUp M6',
    'm8.html': 'MisterUp M8',
    'm9.html': 'MisterUp M9',
    'm11.html': 'MisterUp M11',
    'misterPos.html': 'Mister POS',
    'totem.html': 'Totem'
}

for file, correct_title in replacements.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the title inside <title>
        import re
        content = re.sub(r'<title>.*?</title>', f'<title>{correct_title}</title>', content)
        # Replace the mobile-section-title
        content = re.sub(r'<span class="mobile-section-title">.*?</span>', f'<span class="mobile-section-title">{correct_title}</span>', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
