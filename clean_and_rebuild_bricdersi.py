import os
import shutil

SITE_ROOT = r"C:\Users\Erdem\.gemini\antigravity\scratch\bricdersi-net"

LEGACY_DIRS = [
    "rehber",
    "dersler",
    "1nt-acisina-yanitlar",
    "bric-bbo-online-oyun-rehberi",
    "bric-el-degerlendirme-alistirmalari",
    "bric-kart-oyunu-ve-love-saglama",
    "bric-konvansiyonlari-listesi",
    "bric-oyun-kurallari-ve-deklarasyon",
    "bric-puan-hesaplama-ve-skor"
]

for leg in LEGACY_DIRS:
    path = os.path.join(SITE_ROOT, leg)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Removed legacy directory: {leg}")

print("Legacy directory cleanup complete.")
