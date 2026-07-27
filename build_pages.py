import os
import json
import re
import shutil

local_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(local_path, "seo_metadata.json")
template_path = os.path.join(local_path, "index.html")

def extract_json_ld(html):
    match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1).strip()), match.group(0)
        except Exception as e:
            print(f"Warning parsing JSON-LD from template: {e}")
    return None, None

def build():
    if not os.path.exists(config_path):
        print("Error: seo_metadata.json config file not found.")
        return False
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    if not os.path.exists(template_path):
        print("Error: index.html template file not found.")
        return False
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    base_url = config.get("site_base_url", "https://www.bricdersi.net")
    default_og_image = config.get("default_og_image", f"{base_url}/logo.png")
    pages = config.get("pages", [])
    original_schema, original_script_tag = extract_json_ld(template)
    
    for page in pages:
        route = page.get("route", "")
        if route == "":
            target_file = os.path.join(local_path, "index.html")
        else:
            target_dir = os.path.join(local_path, route)
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, "index.html")
            
        page_url = base_url if route == "" else f"{base_url}/{route}"
        
        # Replace title, description, canonical
        page_html = template
        if page.get("title"):
            page_html = re.sub(r'<title>.*?</title>', f'<title>{page["title"]}</title>', page_html)
        if page.get("description"):
            page_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{page["description"]}">', page_html)
        page_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{page_url}">', page_html)
        
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)

    print("SSG Build completed for workspace:", local_path)
    return True

if __name__ == "__main__":
    build()
