import os
import glob

html_files = glob.glob('*.html')
old_button = '<button class="button button-primary w-100" type="submit">Invia richiesta</button>'
new_button = '<button class="button button-primary w-100" type="button" disabled style="opacity: 0.5; cursor: not-allowed;">Invio temporaneamente disabilitato</button>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_button in content:
        content = content.replace(old_button, new_button)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
