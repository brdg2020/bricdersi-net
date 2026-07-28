import os
import json
import re

local_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(local_path, "seo_metadata.json")
template_path = os.path.join(local_path, "index.html")

routes = [
  "",
  "hakkimda",
  "dersler",
  "rehber",
  "sss",
  "iletisim",
  "bric-baslangic-rehberi",
  "bric-puan-hesaplama-ve-skor",
  "bric-el-degerlendirme-alistirmalari",
  "bric-oyun-kurallari-ve-deklarasyon",
  "bric-kart-oyunu-ve-love-saglama",
  "bric-bbo-online-oyun-rehberi",
  "ozel-bric-dersleri",
  "stayman-konvansiyonu",
  "jacoby-transfer",
  "blackwood-rkcb-4nt",
  "drury-2c",
  "sanzatu-oyun-plani",
  "bric-sozlugu",
  "bric-konvansiyonlari-listesi",
  "1nt-acisina-yanitlar",
  "bric-empas-teknikleri",
  "bric-atak-ve-defans-sinyalleri"
]

def build():
    if not os.path.exists(config_path) or not os.path.exists(template_path):
        print("Error: Config or template file missing.")
        return False

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    base_url = "https://www.bricdersi.net"
    pages = config.get("pages", [])

    for r in routes:
        if r == "":
            target_file = os.path.join(local_path, "index.html")
            page_url = base_url + "/"
        else:
            target_dir = os.path.join(local_path, r)
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, "index.html")
            page_url = f"{base_url}/{r}"

        page_html = template
        page_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{page_url}">', page_html)
        page_html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{page_url}">', page_html)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)

    print("SSG Build finished successfully for bricdersi.net!")
    return True

if __name__ == "__main__":
    build()
