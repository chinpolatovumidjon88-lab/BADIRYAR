"""
Slaydlarni PNG rasm sifatida render qilish (Pillow yordamida).
Har bir slayd 1600x900 px (16:9) o'lchamda saqlanadi.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
OUT_DIR = "/projects/sandbox/BADIRYAR/slides"
os.makedirs(OUT_DIR, exist_ok=True)

# Ranglar
DARK_BLUE = (10, 42, 67)
DARK_BLUE_2 = (20, 61, 92)
ACCENT = (232, 181, 74)
LIGHT = (245, 245, 240)
GRAY = (176, 184, 193)
WHITE = (255, 255, 255)
DARK_TEXT = (26, 26, 26)
GREEN = (46, 125, 50)
ORANGE = (249, 168, 37)
RED_ORANGE = (230, 74, 25)
RED = (198, 40, 40)

FONT_PATH = "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"
FONT_PATH_IT = "/usr/share/fonts/google-noto-vf/NotoSans-Italic[wght].ttf"


def font(size, bold=False):
    f = ImageFont.truetype(FONT_PATH, size)
    if bold:
        try:
            f.set_variation_by_axes([700])
        except Exception:
            pass
    else:
        try:
            f.set_variation_by_axes([400])
        except Exception:
            pass
    return f


def new_slide(bg=DARK_BLUE):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def wrap_text(draw, text, fnt, max_width):
    """Matnni belgilangan kenglikka mos ravishda qatorlarga ajratish."""
    lines = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            lines.append("")
            continue
        words = paragraph.split(" ")
        current = ""
        for w in words:
            test = (current + " " + w).strip()
            bbox = draw.textbbox((0, 0), test, font=fnt)
            if bbox[2] - bbox[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = w
        if current:
            lines.append(current)
    return lines


def draw_text(draw, x, y, text, *, size=20, bold=False, color=LIGHT,
              max_width=None, line_spacing=1.35, align="left"):
    fnt = font(size, bold)
    if max_width:
        lines = wrap_text(draw, text, fnt, max_width)
    else:
        lines = text.split("\n")
    line_h = int(size * line_spacing)
    for i, line in enumerate(lines):
        if align == "center":
            bbox = draw.textbbox((0, 0), line, font=fnt)
            lx = x - (bbox[2] - bbox[0]) // 2
        elif align == "right":
            bbox = draw.textbbox((0, 0), line, font=fnt)
            lx = x - (bbox[2] - bbox[0])
        else:
            lx = x
        draw.text((lx, y + i * line_h), line, font=fnt, fill=color)
    return y + len(lines) * line_h


def rect(draw, xy, color, radius=0):
    if radius:
        draw.rounded_rectangle(xy, radius=radius, fill=color)
    else:
        draw.rectangle(xy, fill=color)


def header(draw, title, num, total, light=False):
    title_color = DARK_BLUE if light else WHITE
    sub_color = GRAY
    # Aksent chiziqcha
    rect(draw, (75, 60, 90, 130), ACCENT)
    draw_text(draw, 110, 50, title, size=38, bold=True, color=title_color)
    draw_text(draw, W - 80, 60, f"{num} / {total}", size=15, color=sub_color, align="right")
    # Pastdagi ingichka chiziq
    rect(draw, (75, 150, W - 75, 152), ACCENT)


# ============================================================
# SLAYD 1 — Sarlavha
# ============================================================
img, d = new_slide(DARK_BLUE)
# Dekor doiralar
d.ellipse((1250, -200, 1800, 350), fill=ACCENT)
d.ellipse((-150, 650, 250, 1050), fill=DARK_BLUE_2)
# Aksent chiziq
rect(d, (110, 280, 124, 540), ACCENT)
draw_text(d, 150, 270, "FALSAFIY TAHLIL", size=20, bold=True, color=ACCENT)
draw_text(d, 150, 320, "Jan Bodriyar g'oyalari asosida", size=52, bold=True, color=WHITE, max_width=1300)
draw_text(d, 150, 395, "virtual reallik va axloqiy", size=52, bold=True, color=WHITE, max_width=1300)
draw_text(d, 150, 470, "muammolar tahlili", size=52, bold=True, color=WHITE, max_width=1300)
draw_text(d, 150, 600, "Simulyakr  •  Giperreallik  •  Axloq  •  Raqamli davr",
          size=22, color=GRAY)
draw_text(d, 150, 820, "Prezentatsiya  |  2026", size=14, color=GRAY)
img.save(f"{OUT_DIR}/01-sarlavha.png")


# ============================================================
# SLAYD 2 — Reja
# ============================================================
img, d = new_slide(LIGHT)
rect(d, (75, 60, 90, 130), ACCENT)
draw_text(d, 110, 50, "Reja", size=38, bold=True, color=DARK_BLUE)
draw_text(d, W - 80, 60, "2 / 10", size=15, color=GRAY, align="right")
rect(d, (75, 150, W - 75, 152), ACCENT)

reja = [
    "Jan Bodriyar haqida qisqacha ma'lumot",
    "Asosiy tushunchalar: simulyakr va simulyatsiya",
    "Giperreallik nazariyasi",
    "Tasvirning to'rt bosqichi",
    "Virtual reallikning falsafiy tabiati",
    "Axloqiy muammolar: haqiqat va yolg'on chegarasi",
    "Zamonaviy raqamli olamga ta'siri",
    "Xulosa va munozara",
]
for i, item in enumerate(reja):
    col = i // 4
    row = i % 4
    x = 100 + col * 720
    y = 230 + row * 130
    color_bg = DARK_BLUE if col == 0 else ACCENT
    color_num = WHITE if col == 0 else DARK_BLUE
    d.ellipse((x, y, x + 80, y + 80), fill=color_bg)
    draw_text(d, x + 40, y + 22, f"{i+1:02d}", size=24, bold=True, color=color_num, align="center")
    draw_text(d, x + 110, y + 28, item, size=22, color=DARK_TEXT, max_width=580)

img.save(f"{OUT_DIR}/02-reja.png")


# ============================================================
# SLAYD 3 — Bodriyar haqida
# ============================================================
img, d = new_slide(DARK_BLUE)
header(d, "Jan Bodriyar (Jean Baudrillard) kim?", 3, 10)

draw_text(d, 110, 200, "Qisqacha ma'lumot", size=20, bold=True, color=ACCENT)
bio = [
    "1929–2007 — Frantsuz faylasufi va sotsiologi",
    "Postmodern falsafa va madaniyat tanqidchisi",
    "Sorbonna universitetida sotsiologiya bo'yicha tahsil olgan",
    "Iste'molchilik jamiyati va ommaviy axborot tahlili",
    "G'oyalari kino, san'at va texnologiyaga ta'sir ko'rsatgan",
]
y = 260
for b in bio:
    d.ellipse((110, y + 12, 124, y + 26), fill=ACCENT)
    draw_text(d, 145, y, b, size=20, color=LIGHT, max_width=720)
    y += 75

# O'ng kartochka
rect(d, (920, 195, 1525, 830), DARK_BLUE_2, radius=15)
draw_text(d, 950, 220, "Asosiy asarlari", size=24, bold=True, color=ACCENT)
asarlar = [
    ("1970", "Iste'molchilik jamiyati"),
    ("1981", "Simulyakr va simulyatsiya"),
    ("1991", "Fors ko'rfazi urushi bo'lmagan"),
    ("1995", "Mukammal jinoyat"),
    ("2000", "Yovuzlikning shaffofligi"),
]
y = 290
for year, name in asarlar:
    draw_text(d, 950, y, year, size=20, bold=True, color=ACCENT)
    draw_text(d, 1060, y, name, size=18, color=LIGHT, max_width=440)
    y += 100

img.save(f"{OUT_DIR}/03-bodriyar.png")


# ============================================================
# SLAYD 4 — Simulyakr va Simulyatsiya
# ============================================================
img, d = new_slide(LIGHT)
rect(d, (75, 60, 90, 130), ACCENT)
draw_text(d, 110, 50, "Simulyakr va Simulyatsiya", size=36, bold=True, color=DARK_BLUE)
draw_text(d, W - 80, 60, "4 / 10", size=15, color=GRAY, align="right")
rect(d, (75, 150, W - 75, 152), ACCENT)

# Chap kartochka
rect(d, (100, 200, 770, 830), DARK_BLUE, radius=15)
draw_text(d, 130, 230, "SIMULYAKR", size=20, bold=True, color=ACCENT)
draw_text(d, 130, 280, "Nusxasi bo'lmagan nusxa", size=28, bold=True, color=WHITE, max_width=620)
draw_text(d, 130, 380,
          "Bodriyar fikricha, simulyakr — bu asl narsani aks ettirmaydigan, "
          "balki o'zi mustaqil ravishda mavjud bo'lgan tasvir yoki belgidir.",
          size=18, color=LIGHT, max_width=620)
draw_text(d, 130, 580,
          "U haqiqatdan ajralib chiqib, o'zining alohida \"haqiqati\"ni "
          "yaratadi. Belgilar endi narsalarni emas, boshqa belgilarni ifodalaydi.",
          size=18, color=LIGHT, max_width=620)

# O'ng kartochka
rect(d, (830, 200, 1500, 830), ACCENT, radius=15)
draw_text(d, 860, 230, "SIMULYATSIYA", size=20, bold=True, color=DARK_BLUE)
draw_text(d, 860, 280, "Haqiqatni almashtirish jarayoni", size=28, bold=True, color=DARK_BLUE, max_width=620)
draw_text(d, 860, 400,
          "Simulyatsiya — bu shunday holatki, unda asl bilan nusxa, haqiqat bilan "
          "tasavvur o'rtasidagi farq yo'qoladi.",
          size=18, color=DARK_TEXT, max_width=620)
draw_text(d, 860, 580,
          "Natijada inson o'zi yashayotgan dunyoning haqiqiymi yoki yo'qligini "
          "aniqlay olmay qoladi. Bu — postmodern shart-sharoitning markaziy holatidir.",
          size=18, color=DARK_TEXT, max_width=620)

img.save(f"{OUT_DIR}/04-simulyakr.png")


# ============================================================
# SLAYD 5 — Giperreallik
# ============================================================
img, d = new_slide(DARK_BLUE)
header(d, "Giperreallik nazariyasi", 5, 10)

draw_text(d, 110, 190,
          "\"Giperreallik — bu haqiqatdan ham haqiqiyroq bo'lib tuyuladigan reallik.\"",
          size=24, bold=True, color=ACCENT, max_width=1450)
draw_text(d, 110, 290,
          "Bodriyar fikricha, zamonaviy jamiyatda ommaviy axborot vositalari, reklama va "
          "raqamli texnologiyalar shunday tasvirlar yaratadiki, ular asl voqelikdan kuchliroq, "
          "jonliroq va ishonchliroq ko'rinadi. Inson endi haqiqatga emas, uning tasviriga ishonadi.",
          size=18, color=LIGHT, max_width=1430)

# 3 kartochka
examples = [
    ("DISNEYLAND", "Sun'iy yaratilgan dunyo bo'lib, Amerika hayotini \"haqiqiyroq\" qilib ko'rsatadi."),
    ("REALITY-SHOULAR", "Tahrir qilingan, sahnalashtirilgan voqealar tomoshabin uchun haqiqat sifatida taqdim etiladi."),
    ("IJTIMOIY TARMOQLAR", "Foydalanuvchilar o'z hayotining \"yaxshilangan\" versiyasini ko'rsatadi va o'zlari ham unga ishonadi."),
]
for i, (title, desc) in enumerate(examples):
    x = 100 + i * 480
    rect(d, (x, 530, x + 460, 830), DARK_BLUE_2, radius=15)
    # Aksent chiziq
    rect(d, (x, 530, x + 460, 540), ACCENT, radius=0)
    draw_text(d, x + 25, 565, title, size=22, bold=True, color=ACCENT, max_width=420)
    draw_text(d, x + 25, 630, desc, size=17, color=LIGHT, max_width=420)

img.save(f"{OUT_DIR}/05-giperreallik.png")


# ============================================================
# SLAYD 6 — Tasvirning to'rt bosqichi
# ============================================================
img, d = new_slide(LIGHT)
rect(d, (75, 60, 90, 130), ACCENT)
draw_text(d, 110, 50, "Tasvirning to'rt bosqichi (Bodriyar)", size=36, bold=True, color=DARK_BLUE)
draw_text(d, W - 80, 60, "6 / 10", size=15, color=GRAY, align="right")
rect(d, (75, 150, W - 75, 152), ACCENT)

stages = [
    ("I", "Aks ettirish",
     "Tasvir chuqur haqiqatni aks ettiradi. Belgi va voqelik mos keladi.",
     GREEN),
    ("II", "Buzib ko'rsatish",
     "Tasvir haqiqatni yashiradi va buzadi. Belgi haqiqatni soxtalashtiradi.",
     ORANGE),
    ("III", "Yashirish",
     "Tasvir haqiqatning yo'qligini niqoblaydi. \"Bormi\" degan illyuziya yaratadi.",
     RED_ORANGE),
    ("IV", "Sof simulyakr",
     "Tasvir haqiqatga umuman bog'liq emas. U o'zining sof simulyakridir.",
     RED),
]

for i, (num, title, desc, color) in enumerate(stages):
    x = 90 + i * 360
    # Yuqori
    rect(d, (x, 200, x + 340, 380), color, radius=15)
    draw_text(d, x + 170, 225, num, size=64, bold=True, color=WHITE, align="center")
    draw_text(d, x + 170, 320, title, size=22, bold=True, color=WHITE, align="center", max_width=320)
    # Pastki
    rect(d, (x, 400, x + 340, 770), WHITE, radius=15)
    d.rounded_rectangle((x, 400, x + 340, 770), radius=15, outline=GRAY, width=1)
    draw_text(d, x + 25, 430, desc, size=17, color=DARK_TEXT, max_width=290)

draw_text(d, W // 2, 810, "Haqiqatdan uzoqlashish yo'nalishi  →  Sof simulyatsiyaga o'tish",
          size=18, bold=True, color=DARK_BLUE, align="center")

img.save(f"{OUT_DIR}/06-tort-bosqich.png")


# ============================================================
# SLAYD 7 — VR falsafiy tabiati
# ============================================================
img, d = new_slide(DARK_BLUE)
header(d, "Virtual reallikning falsafiy tabiati", 7, 10)

draw_text(d, 110, 195, "Bodriyar nuqtai nazaridan virtual reallik (VR)",
          size=24, bold=True, color=ACCENT)

points = [
    ("Haqiqatning oxiri",
     "VR — bu Bodriyar bashorat qilgan giperreallikning eng yuqori ko'rinishi. "
     "Foydalanuvchi tanasidan, makondan va hatto vaqtdan ajralib, sof simulyatsiyaga kiradi."),
    ("Tana va ong dixotomiyasi",
     "VR ongni jismoniy tanadan \"ajratadi\". Bu insonning o'zi haqidagi tushunchasini, "
     "identifikatsiyasini va mavjudligini qayta ko'rib chiqishga majbur qiladi."),
    ("Ramziy almashinuvning yo'qolishi",
     "An'anaviy madaniyatda belgilar haqiqiy munosabatlarni ifodalagan. VRda esa belgilar "
     "faqat boshqa belgilarga ishora qiladi — yopiq tizim paydo bo'ladi."),
    ("Yangi \"haqiqat\" turi",
     "VR — yolg'on emas, lekin haqiqat ham emas. U — uchinchi turdagi mavjudlik: "
     "texnologik vositachilik orqali yaratilgan giper-haqiqat."),
]
y = 270
for i, (title, desc) in enumerate(points):
    d.ellipse((110, y, 170, y + 60), fill=ACCENT)
    draw_text(d, 140, y + 12, str(i + 1), size=24, bold=True, color=DARK_BLUE, align="center")
    draw_text(d, 200, y, title, size=22, bold=True, color=ACCENT, max_width=1300)
    draw_text(d, 200, y + 40, desc, size=16, color=LIGHT, max_width=1300)
    y += 140

img.save(f"{OUT_DIR}/07-vr-falsafa.png")


# ============================================================
# SLAYD 8 — Axloqiy muammolar
# ============================================================
img, d = new_slide(LIGHT)
rect(d, (75, 60, 90, 130), ACCENT)
draw_text(d, 110, 50, "Axloqiy muammolar: haqiqat va yolg'on chegarasi",
          size=32, bold=True, color=DARK_BLUE)
draw_text(d, W - 80, 60, "8 / 10", size=15, color=GRAY, align="right")
rect(d, (75, 150, W - 75, 152), ACCENT)

problems = [
    ("Haqiqat tushunchasining yemirilishi",
     "Agar simulyatsiya haqiqatdan farq qilmasa, yolg'on va rost o'rtasidagi axloqiy "
     "chegara qaerda? Inson nimaga ishonishi kerak?"),
    ("Mas'uliyat masalasi",
     "Virtual makonda qilingan harakatlar (zo'ravonlik, aldash) uchun kim javob beradi? "
     "Ular axloqiy jihatdan haqiqiymi?"),
    ("Identifikatsiya va shaxs",
     "Avatarlar va raqamli ego — bu \"men\"ning haqiqiy ifodasimi yoki yana bir simulyakrmi?"),
    ("Empatiya va begonalashuv",
     "Ekran orqali muloqot insoniy hamdardlikni kamaytiradi. Ekrandagi azob — endi shunchaki tasvir."),
    ("Manipulyatsiya xavfi",
     "Hokimiyat va korporatsiyalar giperreallik orqali jamoatchilik fikrini boshqarishi mumkin "
     "(deepfake, soxta yangiliklar)."),
    ("Erkin iroda muammosi",
     "Algoritmlar va simulyatsiyalar bizning tanlovimizni shakllantirsa, biz haqiqatan ham erkinmizmi?"),
]

for i, (title, desc) in enumerate(problems):
    col = i % 3
    row = i // 3
    x = 90 + col * 480
    y = 200 + row * 320
    rect(d, (x, y, x + 460, y + 290), WHITE, radius=15)
    d.rounded_rectangle((x, y, x + 460, y + 290), radius=15, outline=ACCENT, width=2)
    rect(d, (x, y, x + 14, y + 290), DARK_BLUE)
    draw_text(d, x + 35, y + 30, title, size=20, bold=True, color=DARK_BLUE, max_width=410)
    draw_text(d, x + 35, y + 110, desc, size=15, color=DARK_TEXT, max_width=410)

img.save(f"{OUT_DIR}/08-axloqiy-muammolar.png")


# ============================================================
# SLAYD 9 — Zamonaviy ta'siri
# ============================================================
img, d = new_slide(DARK_BLUE)
header(d, "Zamonaviy raqamli olamga ta'siri", 9, 10)

draw_text(d, 110, 195, "Bodriyar g'oyalari bugun qanchalik dolzarb?",
          size=22, bold=True, color=ACCENT)

# Chap kartochka
rect(d, (100, 260, 780, 830), DARK_BLUE_2, radius=15)
draw_text(d, 130, 285, "RAQAMLI HAYOT", size=20, bold=True, color=ACCENT)
digital = [
    "Ijtimoiy tarmoqlardagi \"ideal hayot\" — sof simulyakr",
    "Deepfake va sun'iy intellekt — haqiqatni shubha ostiga oladi",
    "Metaverse — Bodriyar bashoratining moddiylashishi",
    "Onlayn shaxsiyatlar (avatar, profil) — yangi \"men\" turlari",
    "Algoritmik puzyrlar — har bir foydalanuvchi o'z giperrealligida",
]
y = 350
for item in digital:
    d.ellipse((130, y + 8, 144, y + 22), fill=ACCENT)
    draw_text(d, 165, y, "•  " + item, size=17, color=LIGHT, max_width=600)
    y += 90

# O'ng kartochka
rect(d, (820, 260, 1500, 830), ACCENT, radius=15)
draw_text(d, 850, 285, "MADANIYAT VA SIYOSAT", size=20, bold=True, color=DARK_BLUE)
culture = [
    "Soxta yangiliklar (fake news) — haqiqat siyosiy quroliga aylandi",
    "Reklama va brendlar — narsani emas, tasvirni sotadi",
    "Urush va inqirozlar — ekran orqali \"shou\"ga aylanadi",
    "Madaniyat takror ishlab chiqarish (remake, remix) ustida",
    "Tarixiy haqiqat — turli versiyalarda \"qayta yoziladi\"",
]
y = 350
for item in culture:
    draw_text(d, 850, y, "•  " + item, size=17, color=DARK_TEXT, max_width=620)
    y += 90

img.save(f"{OUT_DIR}/09-zamonaviy-tasir.png")


# ============================================================
# SLAYD 10 — Xulosa
# ============================================================
img, d = new_slide(DARK_BLUE)
# Dekor
d.ellipse((-200, -200, 500, 500), fill=DARK_BLUE_2)
d.ellipse((1300, 600, 1700, 1000), fill=ACCENT)

rect(d, (110, 90, 124, 180), ACCENT)
draw_text(d, 150, 80, "Xulosa", size=52, bold=True, color=WHITE)

draw_text(d, 150, 230, "Jan Bodriyar bizga muhim ogohlantirish qoldirdi:",
          size=22, bold=True, color=ACCENT)

conclusions = [
    "Virtual reallik shunchaki texnologiya emas — bu falsafiy va axloqiy hodisa.",
    "Haqiqat va simulyatsiya o'rtasidagi chegara yo'qolib borayotgan davrda inson "
    "tanqidiy fikrlashni saqlab qolishi kerak.",
    "Axloq endi nafaqat haqiqiy dunyoda, balki raqamli makonda ham qayta tiklanishi lozim.",
    "Bodriyar g'oyalari — bu pessimizm emas, balki ongli yashashga chaqiriqdir.",
]
y = 310
for c in conclusions:
    d.ellipse((150, y + 10, 175, y + 35), fill=ACCENT)
    draw_text(d, 200, y, c, size=19, color=LIGHT, max_width=1280)
    y += 100

# Sitata
draw_text(d, 150, 740,
          "\"Endi haqiqat yo'q — faqat uning simulyatsiyasi bor.\"  — J. Bodriyar",
          size=20, bold=True, color=ACCENT, max_width=1300)
draw_text(d, 150, 810, "E'tiboringiz uchun rahmat!", size=26, bold=True, color=WHITE)

img.save(f"{OUT_DIR}/10-xulosa.png")

print(f"\nTayyor! {OUT_DIR} papkasiga 10 ta PNG saqlandi.")
for f in sorted(os.listdir(OUT_DIR)):
    p = os.path.join(OUT_DIR, f)
    print(f"  {f:30s}  {os.path.getsize(p)//1024} KB")
