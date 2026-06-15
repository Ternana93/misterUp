import os
import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    page_title = title_match.group(1).strip() if title_match else ""

    old_btn = '<button class="rd-navbar-toggle" data-rd-navbar-toggle="#rd-navbar-nav-wrap-1"><span></span></button>'
    
    if old_btn in content and 'rd-navbar-toggle-wrap' not in content:
        new_wrap = f'<div class="rd-navbar-toggle-wrap">\n                    <button class="rd-navbar-toggle" data-rd-navbar-toggle="#rd-navbar-nav-wrap-1"><span></span></button>\n                    <span class="mobile-section-title">{page_title}</span>\n                  </div>'
        content = content.replace(old_btn, new_wrap)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file} with title {page_title}")
