import glob

files = glob.glob("/Users/alessiomariani/siti_web/mister_up_new_v2/*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # fix the malformed class
    new_content = content.replace('" d-none d-md-block data-wow-delay=".1s">', ' d-none d-md-block" data-wow-delay=".1s">')
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

