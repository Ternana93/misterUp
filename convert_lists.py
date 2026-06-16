import glob
import re

files = glob.glob("/Users/alessiomariani/siti_web/mister_up_new_v2/*.html")

def process_li_text(text):
    text = text.strip()
    # remove check-icon if it's there
    text = re.sub(r'<span class="check-icon[^>]*></span>', '', text).strip()
    
    if ':' in text:
        parts = text.split(':', 1)
        return f"<p>{parts[0].strip()}<br><small>{parts[1].strip()}</small></p>"
    elif '-' in text:
        parts = text.split('-', 1)
        return f"<p>{parts[0].strip()}<br><small>{parts[1].strip()}</small></p>"
    else:
        # just put the text
        return f"<p>{text}</p>"

for file_path in files:
    if "about-me.html" in file_path:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    matches = re.finditer(r'(<h4[^>]*>.*?Perché scegliere Mister.*?</h4>\s*)<ul>(.*?)</ul>', content, flags=re.IGNORECASE | re.DOTALL)
    
    new_content = content
    for match in matches:
        full_match = match.group(0)
        prefix = match.group(1)
        ul_content = match.group(2)
        
        li_matches = re.findall(r'<li[^>]*>(.*?)</li>', ul_content, flags=re.IGNORECASE | re.DOTALL)
        if not li_matches:
            continue
            
        grid_html = '<div class="m4-specs-grid">\n'
        for li in li_matches:
            processed = process_li_text(li)
            grid_html += f'  <div class="m4-spec-card">\n    <span class="check-icon linearicons-check"></span>\n    {processed}\n  </div>\n'
        grid_html += '</div>'
        
        new_content = new_content.replace(full_match, prefix + grid_html)
        
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")

