import glob
import re

files = glob.glob("/Users/alessiomariani/siti_web/mister_up_new_v2/*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for Richiedi Informazioni su Mister<span class="logo-up">Up</span>
    # and replace with Richiedi Informazioni su MisterUp
    # Use regex to catch all variations (Up, POS, Self, ecc)
    new_content = re.sub(
        r'(Richiedi Informazioni su Mister)<span class="logo-up">([^<]+)</span>',
        r'\1\2',
        content,
        flags=re.IGNORECASE
    )
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")

