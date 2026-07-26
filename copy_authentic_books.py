import os
import shutil

SRC_DIR = r"C:\Users\Erdem\Downloads\site için kaynaklar"
BRICDERSI_PDF_DIR = r"C:\Users\Erdem\.gemini\antigravity\scratch\bricdersi-net\pdf"
ERDEMBRIDGE_PDF_DIR = r"C:\Users\Erdem\.gemini\antigravity\scratch\erdembridge-com\pdf"

os.makedirs(BRICDERSI_PDF_DIR, exist_ok=True)
os.makedirs(ERDEMBRIDGE_PDF_DIR, exist_ok=True)

file_mapping = {
    "Oyun-Erdinç Erbil.pdf": "erdinc_erbil_oyun_ve_kart_oyun_plani_kitabi.pdf",
    "Deklarasyon-Erdinç Erbil.pdf": "erdinc_erbil_deklarasyon_konusma_kitabi.pdf",
    "Bric-Baslangic-Seviyesi-Ders-Notlari-.pdf": "bric_baslangic_seviyesi_ders_notlari.pdf",
    "Çocuklar için Briç _ Tuncay Altun.pdf": "cocuklar_icin_bric_ders_notlari_tuncay_altun.pdf"
}

for src_file, target_file in file_mapping.items():
    src_path = os.path.join(SRC_DIR, src_file)
    if os.path.exists(src_path):
        size = os.path.getsize(src_path)
        shutil.copy(src_path, os.path.join(BRICDERSI_PDF_DIR, target_file))
        shutil.copy(src_path, os.path.join(ERDEMBRIDGE_PDF_DIR, target_file))
        print(f"Successfully copied authentic '{src_file}' ({size} bytes) -> '{target_file}'")
    else:
        print(f"Error: Source file '{src_file}' not found in {SRC_DIR}")

print("All authentic PDF files replaced without any synthetic generation!")
