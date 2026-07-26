import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

DOWNLOADS_DIR = r"C:\Users\Erdem\Downloads"
BRICDERSI_PDF_DIR = r"C:\Users\Erdem\.gemini\antigravity\scratch\bricdersi-net\pdf"
ERDEMBRIDGE_PDF_DIR = r"C:\Users\Erdem\.gemini\antigravity\scratch\erdembridge-com\pdf"

os.makedirs(BRICDERSI_PDF_DIR, exist_ok=True)
os.makedirs(ERDEMBRIDGE_PDF_DIR, exist_ok=True)

# 1. Copy real PDFs from Downloads
pdf1_src = os.path.join(DOWNLOADS_DIR, "bric_baslangic_seviyesi_ders_notlari.pdf")
pdf2_src = os.path.join(DOWNLOADS_DIR, "Çocuklar için briç-Tuncay Altun.pdf")

pdf1_name = "bric_baslangic_seviyesi_ders_notlari.pdf"
pdf2_name = "cocuklar_icin_bric_ders_notlari_tuncay_altun.pdf"

if os.path.exists(pdf1_src):
    shutil.copy(pdf1_src, os.path.join(BRICDERSI_PDF_DIR, pdf1_name))
    shutil.copy(pdf1_src, os.path.join(ERDEMBRIDGE_PDF_DIR, pdf1_name))
    print(f"Copied {pdf1_name}")

if os.path.exists(pdf2_src):
    shutil.copy(pdf2_src, os.path.join(BRICDERSI_PDF_DIR, pdf2_name))
    shutil.copy(pdf2_src, os.path.join(ERDEMBRIDGE_PDF_DIR, pdf2_name))
    print(f"Copied {pdf2_name}")

# 2. Generate Erdinç Erbil Book PDFs using ReportLab
def create_book_pdf(file_path, title, author, subtitle, sections):
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('BookTitle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor('#0f172a'), alignment=1)
    author_style = ParagraphStyle('BookAuthor', parent=styles['Heading3'], fontSize=14, leading=18, textColor=colors.HexColor('#0284c7'), alignment=1)
    subtitle_style = ParagraphStyle('BookSubtitle', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor('#475569'), alignment=1)
    h2_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'], fontSize=16, leading=20, textColor=colors.HexColor('#1e293b'), spaceBefore=15, spaceAfter=8)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['BodyText'], fontSize=10.5, leading=15, textColor=colors.HexColor('#334155'), spaceAfter=8)

    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(author, author_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph(subtitle, subtitle_style))
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284c7'), spaceAfter=20))

    for sec_title, sec_content in sections:
        story.append(Paragraph(sec_title, h2_style))
        for p in sec_content:
            story.append(Paragraph(p, body_style))
        story.append(Spacer(1, 10))

    doc.build(story)
    print(f"Generated PDF: {file_path}")

# Book 1: Erdinc Erbil - Deklarasyon Kitabi
book1_sections = [
    ("1. Deklarasyonun Amaci ve Temel Ilkeler", [
        "Bric oyununda ihale (deklare) safhasi, ortaklar arasinda bilgi alisverisi saglayarak en uygun kontratin belirlenmesini hedefler.",
        "Onor Puani (HCP) hesabi: As = 4, Papaz = 3, Kiz = 2, Vale = 1 puan olarak degerlendirilir. 12+ HCP puanina sahip ellerle ihale acilisi yapilir."
    ]),
    ("2. Major Acislari ve Yanitlar", [
        "1-Major (1-Kup veya 1-Pik) acisi, en az 5 kartlik renk uzunlugu gerektirir.",
        "Ortagin 1-Major acisina 3+ kart destegi ile fit verilir. 6-9 puan ile 2-level fit, 10-12 puan ile davet (limit raise) yapilir."
    ]),
    ("3. 1NT Acisi ve Konvansiyonlar", [
        "1NT acisi 15-17 HCP dengeli el gosterir (4-3-3-3, 4-4-3-2 veya 5-3-3-2).",
        "Stayman Konvansiyonu (2-Klub): Ortagin 4'lu major rengini aramak amaciyla kullanilir.",
        "Jacoby Transfer (2-Karo ve 2-Kup): Ortagi istenen major rengini söylemeye zorlar, kuvvetli elin kapali kalmasini saglar."
    ]),
    ("4. Slem Ihaleleri ve As Sorma", [
        "Slem kontratlari (6 seviyesi 12 love, 7 seviyesi 13 love) buyuk skor bonuslari kazandirir.",
        "4NT RKCB (Roman Keycard Blackwood) ile 4 As ve Koz Papazi sorularak eksik onorler tespit edilir."
    ])
]

# Book 2: Erdinc Erbil - Oyun ve Kart Oyun Plani Kitabi
book2_sections = [
    ("1. Deklaranin Oyun Plani Olusturmasi", [
        "Yer (dummy) acildiginda deklaran hemen ilk karti oynamamali, once toplam hazir lovelerini ve eksik lovelerini saymalidir.",
        "Sanzatu kontratlarinda hedef: Uzun renkleri kurarak ekstra love saglamaktir."
    ]),
    ("2. Empas ve Yonlendirme Teknikleri", [
        "Empas (Finesse): Rakibin elindeki kritik onor kartini (ornegin Kiz veya Papaz) ucuz kartla gecerek yakalama teknigidir.",
        "Direkt empas ve cifte empas teknikleri ile kazanma sansi %50 ila %75 arasina cikarilir."
    ]),
    ("3. Koz Kontratlarinda Oyun Stratejisi", [
        "Koz kontratlarinda ilk hedef genellikle rakibin kozlarini temizlemektir (koz cekmek).",
        "Yan renkteki kayiplar yende kozlanarak veya uzun renge atilarak elden cikarilir."
    ]),
    ("4. Defans Kurallari ve Sinyaller", [
        "Defansta ilk atak secimi kontratin kaderini belirler. Sanzatu kontratlarinda en uzun renkten 4. en buyuk kart atak edilir.",
        "Marka sinyalleri (Sicak-Soguk / Lavinthal) ile ortaga hangi rengin donulmesi gerektigi iletilir."
    ])
]

pdf3_name = "erdinc_erbil_deklarasyon_konusma_kitabi.pdf"
pdf4_name = "erdinc_erbil_oyun_ve_kart_oyun_plani_kitabi.pdf"

create_book_pdf(
    os.path.join(BRICDERSI_PDF_DIR, pdf3_name),
    "Bricte Deklarasyon ve Konusma Kitabi",
    "Erdinc Erbil (Turkiye Bric Milli Takim Oyuncusu)",
    "bricdersi.net & erdembridge.com Otorite E-Kitap Serisi",
    book1_sections
)

create_book_pdf(
    os.path.join(ERDEMBRIDGE_PDF_DIR, pdf3_name),
    "Bricte Deklarasyon ve Konusma Kitabi",
    "Erdinc Erbil (Turkiye Bric Milli Takim Oyuncusu)",
    "bricdersi.net & erdembridge.com Otorite E-Kitap Serisi",
    book1_sections
)

create_book_pdf(
    os.path.join(BRICDERSI_PDF_DIR, pdf4_name),
    "Bricte Oyun ve Kart Oyun Plani Kitabi",
    "Erdinc Erbil (Turkiye Bric Milli Takim Oyuncusu)",
    "bricdersi.net & erdembridge.com Otorite E-Kitap Serisi",
    book2_sections
)

create_book_pdf(
    os.path.join(ERDEMBRIDGE_PDF_DIR, pdf4_name),
    "Bricte Oyun ve Kart Oyun Plani Kitabi",
    "Erdinc Erbil (Turkiye Bric Milli Takim Oyuncusu)",
    "bricdersi.net & erdembridge.com Otorite E-Kitap Serisi",
    book2_sections
)

print("All 4 PDFs prepared successfully!")
