import glob
import re

files = glob.glob("/Users/alessiomariani/siti_web/mister_up_new_v2/*.html")

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for the section that has the second owl-carousel next to "Dimensioni e peso"
    # Actually, we can find the section by checking for "Dimensioni e peso" and finding the previous column.
    
    # Let's find <div class="col-md-10 col-lg-6 wow slideInUp" data-wow-delay=".1s"> which is the wrapper of the carousel
    # right before <div class="col-md-10 col-lg-5 wow-outer"> that contains "Dimensioni e peso" or the form.
    
    # We can just look for the row:
    # <div class="col-md-10 col-lg-6 wow slideInUp" data-wow-delay=".1s">
    #   <!-- il tuo owl resta -->
    
    # Or more generally: find the owl carousel inside a col-lg-6 that is inside the section bg-dark-3 pd50
    # Let's use regex to find the column before "Dimensioni e peso"
    
    # Let's find the section that contains "Dimensioni e peso"
    if "Dimensioni e peso" in content:
        # replace the specific col-md-10 col-lg-6 that contains the carousel.
        # it usually looks like: <div class="col-md-10 col-lg-6 wow slideInUp" data-wow-delay=".1s">
        content = re.sub(
            r'(<div class="col-md-10 col-lg-6[^"]*")([^>]*>\s*<!-- il tuo owl resta -->)',
            r'\1 d-none d-md-block\2',
            content
        )
        content = re.sub(
            r'(<div class="col-md-10 col-lg-6[^"]*")([^>]*>\s*<div class="owl-carousel"[^>]*data-items="1"[^>]*>\s*<img)',
            r'\1 d-none d-md-block\2',
            content
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")

