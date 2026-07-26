import os
import re
import json

SITE_ROOT = r"C:\Users\Erdem\.gemini\antigravity\scratch\bricdersi-net"
REBUILD_ROOT = r"C:\Users\Erdem\.gemini\antigravity\scratch\bricdersi-seo-rebuild"

# Page Metadata Definitions
PAGES_META = {
    "anasayfa": {
        "slug": "",
        "dir": "",
        "title": "Briç Dersi & Online Briç Kursları | Türkiye Briç Okulu (bricdersi.net)",
        "description": "Türkiye'nin lider briç dersi ve online briç kursu platformu! Milli Takım Antrenörü Erdem Öztürk ve Milli Takım Oyuncusu Erdinç Erbil ile yüz yüze ve BBO özel briç dersleri.",
        "type": "home"
    },
    "bric-nedir": {
        "slug": "bric-nedir",
        "dir": "bric-nedir",
        "title": "Briç Nedir? Akıl Sporu ve Oyun Kuralları Rehberi | bricdersi.net",
        "description": "Briç nedir, nasıl bir akıl sporudur? Briç oyununun tarihi, kuralları, zihinsel faydaları ve başlama rehberi.",
        "type": "article"
    },
    "bric-nasil-oynanir": {
        "slug": "bric-nasil-oynanir",
        "dir": "bric-nasil-oynanir",
        "title": "Briç Nasıl Oynanır? Adım Adım Başlangıç Rehberi | bricdersi.net",
        "description": "Briç nasıl oynanır? Kart dağıtımı, ihale (konuşma), el oynama ve defans kurallarının detaylı açıklaması.",
        "type": "article"
    },
    "bric-dersleri": {
        "slug": "bric-dersleri",
        "dir": "bric-dersleri",
        "title": "Özel Briç Dersleri & Online Eğitim Programı | Erdem Öztürk",
        "description": "Milli Takım Antrenörü Erdem Öztürk'ten yüz yüze ve online (BBO) özel briç dersleri. Başlangıçtan ileri seviyeye.",
        "type": "course"
    },
    "bric-kursu": {
        "slug": "bric-kursu",
        "dir": "bric-kursu",
        "title": "Online Briç Kursu & Grup Eğitimleri | bricdersi.net",
        "description": "İnteraktif online briç kursu ile evinizden briç öğrenin. Esnek ders saatleri ve BBO pratik masaları.",
        "type": "course"
    },
    "bric-konvansiyonlari": {
        "slug": "bric-konvansiyonlari",
        "dir": "bric-konvansiyonlari",
        "title": "Tam Briç Konvansiyon Rehberi & Konuşma Sistemleri | bricdersi.net",
        "description": "Briçte en çok kullanılan konvansiyonlar: Stayman, Jacoby Transfer, Blackwood, Drury, Lebensohl ve fazlası.",
        "type": "article"
    },
    "bridge-base-online-turkce": {
        "slug": "bridge-base-online-turkce",
        "dir": "bridge-base-online-turkce",
        "title": "Bridge Base Online (BBO) Türkçe Kullanım Rehberi | bricdersi.net",
        "description": "BBO Türkçe giriş, masa açma, turnuva kaydı ve robotlarla ücretsiz briç oynama rehberi.",
        "type": "article"
    },
    "bric-spor-mu-kumar-mi": {
        "slug": "bric-spor-mu-kumar-mi",
        "dir": "bric-spor-mu-kumar-mi",
        "title": "Briç Spor mu Kumar mı? IOC ve TBF Yasal Statüsü | bricdersi.net",
        "description": "Briç kumar mıdır? Uluslararası Olimpiyat Komitesi (IOC) ve Gençlik ve Spor Bakanlığı onaylı zihin sporu briç hakkında gerçekler.",
        "type": "article"
    },
    "bric-ile-batak-farki": {
        "slug": "bric-ile-batak-farki",
        "dir": "bric-ile-batak-farki",
        "title": "Briç ile Batak Arasındaki 7 Temel Fark | bricdersi.net",
        "description": "Briç ve batak arasındaki farklar nelerdir? İhale, partner iletişimi, koz mantığı ve strateji karşılaştırması.",
        "type": "article"
    },
    "bric-kac-kisiyle-oynanir": {
        "slug": "bric-kac-kisiyle-oynanir",
        "dir": "bric-kac-kisiyle-oynanir",
        "title": "Briç Kaç Kişiyle Oynanır? Masa Düzeni ve Takımlar | bricdersi.net",
        "description": "Briç oyunu kaç kişiyle oynanır? 4 kişilik masa düzeni, Kuzey-Güney / Doğu-Batı ortaklıkları ve oyuncu rolleri.",
        "type": "article"
    },
    "bric-el-degerlendirme": {
        "slug": "bric-el-degerlendirme",
        "dir": "bric-el-degerlendirme",
        "title": "Briçte El Değerlendirme & Onör Puanı Hesabı | bricdersi.net",
        "description": "Briç el değerlendirme teknikleri: Onör puanı (HCP), uzunluk puanı, fit puanı ve dağılım hesabı.",
        "type": "article"
    },
    "bric-ihale-sistemi": {
        "slug": "bric-ihale-sistemi",
        "dir": "bric-ihale-sistemi",
        "title": "Briç İhale Sistemi & Deklarasyon Kuralları | bricdersi.net",
        "description": "Briçte açılış konuşmaları, kontrat belirleme, pas, kontr ve sürkontr mekaniklerinin kapsamlı anlatımı.",
        "type": "article"
    },
    "bric-deklare-oyunu": {
        "slug": "bric-deklare-oyunu",
        "dir": "bric-deklare-oyunu",
        "title": "Briç Deklare Oyunu & Konuşma Basamakları | bricdersi.net",
        "description": "Deklare konuşma basamakları, koz ve sanzatu kontratları, majör ve minör açışlarına yanıtlar.",
        "type": "article"
    },
    "bric-savunma-oyunu": {
        "slug": "bric-savunma-oyunu",
        "dir": "bric-savunma-oyunu",
        "title": "Briçte Savunma Oyunu & Atak Sinyalleri | bricdersi.net",
        "description": "Defansta atak seçimi, marka/sayı sinyalleri, ortağa sinyal verme ve koz kontratlarında defans teknikleri.",
        "type": "article"
    },
    "bric-puan-hesaplama": {
        "slug": "bric-puan-hesaplama",
        "dir": "bric-puan-hesaplama",
        "title": "Briç Puan Hesaplama, Kontrat & Skor Tablosu | bricdersi.net",
        "description": "Briç puan hesaplama nasıl yapılır? Zone (zon) bonusları, şlem skorları, ceza puanları ve tam skor tablosu.",
        "type": "article"
    },
    "bric-baslangic-rehberi": {
        "slug": "bric-baslangic-rehberi",
        "dir": "bric-baslangic-rehberi",
        "title": "Sıfırdan Briç Başlangıç Rehberi & Temel Kavramlar | bricdersi.net",
        "description": "Briç öğrenmeye yeni başlayanlar için adım adım başlangıç rehberi. Kart değerleri, löve toplama ve temel terimler.",
        "type": "article"
    },
    "bric-ders-notlari-pdf": {
        "slug": "bric-ders-notlari-pdf",
        "dir": "bric-ders-notlari-pdf",
        "title": "Briç Ders Notları & Özet Konvansiyon Tablosu | bricdersi.net",
        "description": "Ücretsiz briç ders notları, özet konu anlatımları ve indirilebilir PDF materyalleri.",
        "type": "article"
    },
    "stayman-konvansiyonu": {
        "slug": "stayman-konvansiyonu",
        "dir": "stayman-konvansiyonu",
        "title": "Stayman Konvansiyonu Rehberi & Örnek Eller | bricdersi.net",
        "description": "1NT açışına Stayman konvansiyonu nasıl yapılır? 2♣ cevabı, majör arama soruları ve örnek el çözümleri.",
        "type": "article"
    },
    "jacoby-transfer": {
        "slug": "jacoby-transfer",
        "dir": "jacoby-transfer",
        "title": "Jacoby Transfer Konvansiyonu & Majör Transferleri | bricdersi.net",
        "description": "1NT açışına Jacoby Transfer konuşmaları: 2♦ ve 2♥ transfer yanıtları, süper kabul ve şlem davetleri.",
        "type": "article"
    },
    "blackwood-rkcb-4nt": {
        "slug": "blackwood-rkcb-4nt",
        "dir": "blackwood-rkcb-4nt",
        "title": "Blackwood & RKCB 4NT Konvansiyonu Rehberi | bricdersi.net",
        "description": "4NT Roman Keycard Blackwood (RKCB) as sorma konvansiyonu: Koz damı sorma ve şlem ihaleleri.",
        "type": "article"
    },
    "drury-2c": {
        "slug": "drury-2c",
        "dir": "drury-2c",
        "title": "Ters Drury (2♣) Konvansiyonu & Örnek Eller | bricdersi.net",
        "description": "Pas geçmiş el ile majör açışına destek: Ters Drury 2♣ konvansiyonu, yanıtlar ve uygulama örnekleri.",
        "type": "article"
    },
    "sanzatu-oyun-plani": {
        "slug": "sanzatu-oyun-plani",
        "dir": "sanzatu-oyun-plani",
        "title": "Sanzatu (NT) Kontratlarında Oyun Planı & Löve Sağlama | bricdersi.net",
        "description": "Sanzatu kontratlarında yer oyunu teknikleri: Uzun renk kurma, empas ve löve sayımı.",
        "type": "article"
    },
    "bric-atak-ve-defans-sinyalleri": {
        "slug": "bric-atak-ve-defans-sinyalleri",
        "dir": "bric-atak-ve-defans-sinyalleri",
        "title": "Defansta Atak Seçimi & Sinyal Verme Rehberi | bricdersi.net",
        "description": "Doğru atak seçimi: Uzun renkten 4., bitşik onörden büyük kart çıkışı ve Lavinthal sinyalleri.",
        "type": "article"
    },
    "bric-empas-teknikleri": {
        "slug": "bric-empas-teknikleri",
        "dir": "bric-empas-teknikleri",
        "title": "Briçte Empas Teknikleri: Direkt & Çifte Empas | bricdersi.net",
        "description": "Briçte empas nasıl atılır? Direkt empas, empas tipleri ve ekstra löve kazanma teknikleri.",
        "type": "article"
    },
    "bric-sozlugu": {
        "slug": "bric-sozlugu",
        "dir": "bric-sozlugu",
        "title": "A’dan Z’ye Briç Terimleri Sözlüğü | bricdersi.net",
        "description": "Briç terimleri ve anlamları: Deklaran, dummy, empas, fit, koz, löve, zon, şlem ve daha fazlası.",
        "type": "dictionary"
    },
    "ozel-bric-dersleri": {
        "slug": "ozel-bric-dersleri",
        "dir": "ozel-bric-dersleri",
        "title": "Birebir Özel Briç Dersleri | Erdem Öztürk",
        "description": "Milli Takım Antrenöründen kişiselleştirilmiş birebir özel briç dersleri. Yüz yüze veya BBO üzerinden.",
        "type": "course"
    },
    "hakkimda": {
        "slug": "hakkimda",
        "dir": "hakkimda",
        "title": "Erdem Öztürk | Türkiye Briç Milli Takım Antrenörü | bricdersi.net",
        "description": "Erdem Öztürk'ün biyografisi, antrenörlük kariyeri, Milli Takım başarıları ve briç felsefesi.",
        "type": "profile"
    },
    "iletisim": {
        "slug": "iletisim",
        "dir": "iletisim",
        "title": "İletişim & Özel Ders Talebi | bricdersi.net",
        "description": "Erdem Öztürk ile iletişime geçin. Özel ve grup briç dersi başvuruları, konum ve WhatsApp hattı.",
        "type": "contact"
    },
    "sss": {
        "slug": "sss",
        "dir": "sss",
        "title": "Briç Hakkında Sıkça Sorulan Sorular (SSS) | bricdersi.net",
        "description": "Briç eğitimi, ders ücretleri, BBO pratikleri ve öğrenme süreci hakkında tüm merak edilen sorular ve cevaplar.",
        "type": "faq"
    }
}

def clean_html_template(content):
    # 1. Replace all erdembridge.com references with bricdersi.net
    content = content.replace("https://www.erdembridge.com/", "https://www.bricdersi.net/")
    content = content.replace("https://www.erdembridge.com", "https://www.bricdersi.net")
    content = content.replace("https://erdembridge.com", "https://www.bricdersi.net")
    content = content.replace("www.erdembridge.com", "www.bricdersi.net")

    # 2. Clean up duplicated initialRouteTab script lines in head
    content = re.sub(r'(\s*<script>window\.initialRouteTab\s*=\s*"[^"]*";</script>)+', '\n    <script>window.initialRouteTab = "__ROUTE__";</script>', content)
    
    return content

def build_schema_json(slug, page_meta):
    url = f"https://www.bricdersi.net/{slug}" if slug else "https://www.bricdersi.net/"
    
    graph = [
        {
            "@type": "Person",
            "@id": "https://www.bricdersi.net/#person",
            "name": "Erdem Öztürk",
            "jobTitle": "TBF 3. Kademe Lisanslı Briç Antrenörü & Milli Takım Antrenörü",
            "description": "2002'den bu yana aktif briç sporcusu, 2009'dan bu yana profesyonel briç eğitmeni. Türkiye Briç Milli Takım Antrenörü. ODTÜ mezunu.",
            "url": "https://www.bricdersi.net",
            "image": "https://www.bricdersi.net/favicon-32x32.png",
            "telephone": "+905368533284",
            "email": "bricogren@gmail.com",
            "sameAs": [
                "https://www.bricdersi.net",
                "https://www.instagram.com/bric.dersi",
                "https://www.youtube.com/channel/UCPvnp7T9eOpixvbIA4olNYQ"
            ],
            "knowsAbout": ["Briç", "Briç Eğitimi", "Briç Konvansiyonları", "Turnuva Briçi"],
            "alumniOf": {
                "@type": "CollegeOrUniversity",
                "name": "ODTÜ"
            },
            "award": "TBF 3. Kademe Antrenör"
        },
        {
            "@type": "EducationalOrganization",
            "@id": "https://www.bricdersi.net/#organization",
            "name": "bricdersi.net - Türkiye Briç Okulu",
            "url": "https://www.bricdersi.net",
            "logo": "https://www.bricdersi.net/favicon-32x32.png",
            "founder": {"@id": "https://www.bricdersi.net/#person"},
            "sameAs": [
                "https://www.instagram.com/bric.dersi",
                "https://www.youtube.com/channel/UCPvnp7T9eOpixvbIA4olNYQ"
            ]
        },
        {
            "@type": "WebSite",
            "@id": "https://www.bricdersi.net/#website",
            "url": "https://www.bricdersi.net/",
            "name": "bricdersi.net",
            "description": "Türkiye'nin Otorite Briç Eğitimi ve Rehber Platformu",
            "publisher": {"@id": "https://www.bricdersi.net/#organization"}
        }
    ]

    if slug:
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Ana Sayfa",
                    "item": "https://www.bricdersi.net/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": page_meta["title"].split("|")[0].strip(),
                    "item": url
                }
            ]
        })

    if page_meta["type"] == "article":
        graph.append({
            "@type": "Article",
            "@id": f"{url}#article",
            "isPartOf": {"@id": "https://www.bricdersi.net/#website"},
            "author": {"@id": "https://www.bricdersi.net/#person"},
            "headline": page_meta["title"],
            "description": page_meta["description"],
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "publisher": {"@id": "https://www.bricdersi.net/#organization"},
            "inLanguage": "tr",
            "datePublished": "2024-01-01",
            "dateModified": "2026-07-26"
        })
    elif page_meta["type"] == "course":
        graph.append({
            "@type": "Course",
            "@id": f"{url}#course",
            "name": page_meta["title"],
            "description": page_meta["description"],
            "url": url,
            "provider": {"@id": "https://www.bricdersi.net/#organization"},
            "instructor": {"@id": "https://www.bricdersi.net/#person"},
            "inLanguage": "tr"
        })

    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

def main():
    print("Building master bricdersi.net platform...")

    # Read base index.html
    base_index_path = os.path.join(SITE_ROOT, "index.html")
    with open(base_index_path, "r", encoding="utf-8") as f:
        base_html = f.read()

    base_html = clean_html_template(base_html)

    # Write cleaned root index.html
    root_html = base_html.replace('__ROUTE__', 'anasayfa')
    with open(base_index_path, "w", encoding="utf-8") as f:
        f.write(root_html)

    print("Root index.html cleaned and updated.")

    # Generate each subfolder page
    for key, meta in PAGES_META.items():
        if key == "anasayfa":
            continue

        slug = meta["slug"]
        dir_name = meta["dir"]
        page_dir = os.path.join(SITE_ROOT, dir_name)
        os.makedirs(page_dir, exist_ok=True)

        target_file = os.path.join(page_dir, "index.html")

        page_html = base_html.replace('__ROUTE__', slug)

        # Update page specific meta tags
        # Replace title tag
        page_html = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', page_html, flags=re.DOTALL)
        
        # Replace meta description
        page_html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        # Replace canonical link
        canonical_url = f"https://www.bricdersi.net/{slug}"
        page_html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical_url}">', page_html, flags=re.DOTALL)

        # Replace og:url, og:title, og:description
        page_html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical_url}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{meta["title"]}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        # Replace twitter tags
        page_html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{meta["title"]}">', page_html, flags=re.DOTALL)
        page_html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{meta["description"]}">', page_html, flags=re.DOTALL)

        # Inject page-specific JSON-LD Schema
        schema_json = build_schema_json(slug, meta)
        schema_script = f'<script type="application/ld+json">\n{schema_json}\n</script>'
        
        # Replace existing ld+json script
        page_html = re.sub(r'<script type="application/ld\+json">.*?</script>', schema_script, page_html, flags=re.DOTALL)

        with open(target_file, "w", encoding="utf-8") as f:
            f.write(page_html)

        print(f"Generated physical SEO page: /{slug}")

    # Generate sitemap.xml
    sitemap_entries = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for key, meta in PAGES_META.items():
        slug = meta["slug"]
        url = f"https://www.bricdersi.net/{slug}" if slug else "https://www.bricdersi.net/"
        priority = "1.0" if not slug else ("0.9" if "dersleri" in slug or "konvansiyon" in slug else "0.8")
        sitemap_entries.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-07-26</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{priority}</priority>\n  </url>")

    sitemap_entries.append('</urlset>')
    sitemap_path = os.path.join(SITE_ROOT, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_entries))

    print("sitemap.xml updated with all 28 canonical URLs.")

    # Generate robots.txt
    robots_content = "User-agent: *\nAllow: /\n\nSitemap: https://www.bricdersi.net/sitemap.xml\n"
    robots_path = os.path.join(SITE_ROOT, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)

    print("robots.txt updated.")

    # Update firebase.json
    firebase_config = {
        "hosting": {
            "site": "bricdersi-net",
            "public": ".",
            "ignore": [
                "firebase.json",
                "**/.*",
                "**/node_modules/**"
            ],
            "redirects": [
                {"source": "/sozluk", "destination": "/bric-sozlugu", "type": 301},
                {"source": "/notlar", "destination": "/bric-ders-notlari-pdf", "type": 301},
                {"source": "/malzemeler", "destination": "/bric-baslangic-rehberi", "type": 301},
                {"source": "/bric-konvansiyonlari-listesi", "destination": "/bric-konvansiyonlari", "type": 301},
                {"source": "/bric-bbo-online-oyun-rehberi", "destination": "/bridge-base-online-turkce", "type": 301},
                {"source": "/bric-el-degerlendirme-alistirmalari", "destination": "/bric-el-degerlendirme", "type": 301},
                {"source": "/bric-oyun-kurallari-ve-deklarasyon", "destination": "/bric-ihale-sistemi", "type": 301},
                {"source": "/bric-kart-oyunu-ve-love-saglama", "destination": "/sanzatu-oyun-plani", "type": 301},
                {"source": "/bric-puan-hesaplama-ve-skor", "destination": "/bric-puan-hesaplama", "type": 301},
                {"source": "/1nt-acisina-yanitlar", "destination": "/stayman-konvansiyonu", "type": 301},
                {"source": "/anasayfa", "destination": "/", "type": 301}
            ],
            "cleanUrls": True,
            "trailingSlash": False
        }
    }

    firebase_path = os.path.join(SITE_ROOT, "firebase.json")
    with open(firebase_path, "w", encoding="utf-8") as f:
        json.dump(firebase_config, f, indent=2, ensure_ascii=False)

    print("firebase.json updated with 301 redirects and clean URL settings.")

if __name__ == "__main__":
    main()
