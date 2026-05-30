"""
Generate scientific charts for Baudrillard presentation
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
import os

os.makedirs('charts', exist_ok=True)

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ============ CHART 1: Simulyakrning to'rt bosqichi (Baudrillard's 4 stages) ============
fig, ax = plt.subplots(figsize=(11, 6.5))
stages = ['I bosqich\nHaqiqatning\naksi', 'II bosqich\nHaqiqatni\nbuzish', 'III bosqich\nHaqiqat\nyo\'qligini\nyashirish', 'IV bosqich\nSof\nsimulyakr']
descriptions = ['Tasvir haqiqatni\nsodda aks ettiradi', 'Tasvir haqiqatni\nniqoblaydi va\nbuzadi', 'Tasvir haqiqat\nyo\'qligini\nyashiradi', 'Tasvir hech\nqanday haqiqat\nbilan bog\'liq emas']
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
values = [25, 50, 75, 100]

x = np.arange(len(stages))
bars = ax.bar(x, values, color=colors, edgecolor='black', linewidth=1.5, width=0.65)

for i, (bar, desc) in enumerate(zip(bars, descriptions)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 3,
            desc, ha='center', va='bottom', fontsize=9, style='italic')

ax.set_xticks(x)
ax.set_xticklabels(stages, fontsize=10, fontweight='bold')
ax.set_ylabel('Haqiqatdan uzoqlashish darajasi (%)', fontsize=11, fontweight='bold')
ax.set_title('J. Bodriyar bo\'yicha simulyakrning rivojlanish bosqichlari',
             fontsize=13, fontweight='bold', pad=15)
ax.set_ylim(0, 140)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add arrow showing progression
ax.annotate('', xy=(3.4, 110), xytext=(-0.4, 110),
            arrowprops=dict(arrowstyle='->', color='darkred', lw=2.5))
ax.text(1.5, 118, 'GIPERREALLIK SARI', ha='center', fontsize=11,
        fontweight='bold', color='darkred')

plt.tight_layout()
plt.savefig('charts/chart1_simulacra_stages.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============ CHART 2: Virtual reallik foydalanuvchilari dinamikasi ============
fig, ax = plt.subplots(figsize=(11, 6))
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
vr_users = [171, 200, 254, 320, 421, 540, 698, 850]  # millions
metaverse = [10, 25, 60, 120, 240, 400, 600, 800]
social_media_hours = [2.4, 2.5, 2.6, 2.8, 3.0, 3.1, 3.2, 3.3]

ax2 = ax.twinx()
line1 = ax.plot(years, vr_users, 'o-', color='#2E86AB', linewidth=3, markersize=9, label='VR foydalanuvchilari (mln)')
line2 = ax.plot(years, metaverse, 's-', color='#C73E1D', linewidth=3, markersize=9, label='Metaverse iqtisodiyoti (mlrd $)')
line3 = ax2.plot(years, social_media_hours, '^--', color='#F18F01', linewidth=2.5, markersize=9, label='Ijtimoiy tarmoqlarda kunlik vaqt (soat)')

ax.fill_between(years, vr_users, alpha=0.15, color='#2E86AB')
ax.set_xlabel('Yillar', fontsize=11, fontweight='bold')
ax.set_ylabel('Foydalanuvchilar / Iqtisodiyot hajmi', fontsize=11, fontweight='bold', color='#2E86AB')
ax2.set_ylabel('Kunlik vaqt (soat)', fontsize=11, fontweight='bold', color='#F18F01')
ax.set_title('Virtual va raqamli giperreallikning o\'sish dinamikasi (2018-2025)',
             fontsize=13, fontweight='bold', pad=15)

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc='upper left', fontsize=10, framealpha=0.95)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('charts/chart2_vr_dynamics.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============ CHART 3: Axloqiy muammolar diagrammasi (pie chart) ============
fig, ax = plt.subplots(figsize=(10, 7))
problems = ['Identitet\nbuzilishi', 'Virtual\nzo\'ravonlik', 'Insoniy\nbegonalashuv',
            'Haqiqat va\nyolg\'on\nchegarasi', 'Manipulyatsiya\nva nazorat', 'Axloqiy\nrelyativizm']
sizes = [22, 18, 20, 16, 14, 10]
colors_pie = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#8E44AD']
explode = (0.05, 0.05, 0.08, 0.05, 0.05, 0.05)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=problems, colors=colors_pie,
                                     autopct='%1.1f%%', shadow=True, startangle=90,
                                     textprops={'fontsize': 10, 'fontweight': 'bold'})

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

ax.set_title('Virtual reallikdagi axloqiy muammolar tuzilmasi\n(Bodriyar konseptsiyasi asosida)',
             fontsize=13, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/chart3_ethical_problems.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============ CHART 4: Simulyatsiya - ijtimoiy-siyosiy ta'sir ============
fig, ax = plt.subplots(figsize=(11, 6.5))
spheres = ['Saylov\njarayonlari', 'Mediada\nyangiliklar', 'Reklama va\niste\'mol', 'Geosiyosat\nva urush', 'Ijtimoiy\ntarmoqlar', 'Ta\'lim\ntizimi']
real_influence = [45, 35, 30, 50, 25, 55]
simulated_influence = [55, 65, 70, 50, 75, 45]

x = np.arange(len(spheres))
width = 0.38

bars1 = ax.bar(x - width/2, real_influence, width, label='Haqiqiy ta\'sir (%)',
               color='#2A9D8F', edgecolor='black', linewidth=1.2)
bars2 = ax.bar(x + width/2, simulated_influence, width, label='Simulyatsion ta\'sir (%)',
               color='#E76F51', edgecolor='black', linewidth=1.2)

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(spheres, fontsize=10, fontweight='bold')
ax.set_ylabel('Ta\'sir darajasi (%)', fontsize=11, fontweight='bold')
ax.set_title('Bodriyar simulyatsiya nazariyasining zamonaviy sohalardagi namoyon bo\'lishi',
             fontsize=12.5, fontweight='bold', pad=15)
ax.legend(fontsize=11, loc='upper right', framealpha=0.95)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)
ax.set_ylim(0, 90)

plt.tight_layout()
plt.savefig('charts/chart4_simulation_spheres.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============ CHART 5: Insoniy begonalashuv darajasi ============
fig, ax = plt.subplots(figsize=(11, 6))
categories = ['O\'z-o\'zidan\nbegonalashuv', 'Boshqalardan\nbegonalashuv', 'Tabiatdan\nbegonalashuv',
              'Mehnatdan\nbegonalashuv', 'Madaniyatdan\nbegonalashuv', 'Haqiqatdan\nbegonalashuv']

# Marx vs Baudrillard comparison
marx_view = [70, 65, 60, 85, 55, 50]
baudrillard_view = [85, 80, 75, 70, 90, 95]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
marx_view += marx_view[:1]
baudrillard_view += baudrillard_view[:1]
angles += angles[:1]

ax = plt.subplot(111, projection='polar')
ax.plot(angles, marx_view, 'o-', linewidth=2.5, label='K. Marks (klassik begonalashuv)', color='#2E86AB')
ax.fill(angles, marx_view, alpha=0.25, color='#2E86AB')
ax.plot(angles, baudrillard_view, 's-', linewidth=2.5, label='J. Bodriyar (giperreal begonalashuv)', color='#C73E1D')
ax.fill(angles, baudrillard_view, alpha=0.25, color='#C73E1D')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=8)
ax.set_title('Insoniy begonalashuv darajasi: Marks va Bodriyar qarashlari qiyosiy tahlili\n',
             fontsize=12.5, fontweight='bold', pad=25)
ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.1), fontsize=10)
ax.grid(True, alpha=0.4)

plt.tight_layout()
plt.savefig('charts/chart5_alienation.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

# ============ CHART 6: Conceptual scheme - Real vs Hyperreal ============
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(6, 7.5, 'HAQIQAT — SIMULYAKR — GIPERREALLIK',
        ha='center', fontsize=15, fontweight='bold', color='#2C3E50')

# Three boxes
box1 = FancyBboxPatch((0.5, 3), 3, 3, boxstyle="round,pad=0.1",
                      linewidth=2, edgecolor='#2A9D8F', facecolor='#A8DADC')
box2 = FancyBboxPatch((4.5, 3), 3, 3, boxstyle="round,pad=0.1",
                      linewidth=2, edgecolor='#E76F51', facecolor='#F4A261')
box3 = FancyBboxPatch((8.5, 3), 3, 3, boxstyle="round,pad=0.1",
                      linewidth=2, edgecolor='#9B2226', facecolor='#E9C46A')

ax.add_patch(box1)
ax.add_patch(box2)
ax.add_patch(box3)

# Box texts
ax.text(2, 5.5, 'HAQIQAT', ha='center', fontsize=14, fontweight='bold', color='#1D3557')
ax.text(2, 4.7, 'Ontologik\nmavjudlik', ha='center', fontsize=10, style='italic')
ax.text(2, 3.7, '• Tabiat\n• Tana\n• Bevosita tajriba', ha='center', fontsize=9)

ax.text(6, 5.5, 'SIMULYAKR', ha='center', fontsize=14, fontweight='bold', color='#9B2226')
ax.text(6, 4.7, 'Belgilar va\nnusxalar', ha='center', fontsize=10, style='italic')
ax.text(6, 3.7, '• Tasvir\n• Reklama\n• Media-tasvirlar', ha='center', fontsize=9)

ax.text(10, 5.5, 'GIPERREALLIK', ha='center', fontsize=14, fontweight='bold', color='#6A040F')
ax.text(10, 4.7, 'Haqiqatdan\nhaqiqiyroq', ha='center', fontsize=10, style='italic')
ax.text(10, 3.7, '• Disneylend\n• VR olamlar\n• Ijtimoiy tarmoq', ha='center', fontsize=9)

# Arrows
arrow1 = FancyArrowPatch((3.5, 4.5), (4.5, 4.5), arrowstyle='->', mutation_scale=25,
                         linewidth=2.5, color='#264653')
arrow2 = FancyArrowPatch((7.5, 4.5), (8.5, 4.5), arrowstyle='->', mutation_scale=25,
                         linewidth=2.5, color='#264653')
ax.add_patch(arrow1)
ax.add_patch(arrow2)

ax.text(4, 4.8, 'aks ettirish', ha='center', fontsize=9, style='italic')
ax.text(8, 4.8, 'gipertrofiya', ha='center', fontsize=9, style='italic')

# Bottom note
ax.text(6, 2, '"Endi simulyakr haqiqatni emas, haqiqat simulyakrni aks ettiradi"',
        ha='center', fontsize=11, style='italic', color='#264653',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#F1FAEE', edgecolor='#457B9D'))
ax.text(6, 1.3, '— Jan Bodriyar, "Simulyakr va simulyatsiya" (1981)',
        ha='center', fontsize=10, color='#264653')

# Axis arrow at bottom
ax.annotate('', xy=(11.5, 0.5), xytext=(0.5, 0.5),
            arrowprops=dict(arrowstyle='->', color='darkred', lw=2))
ax.text(6, 0.15, 'HAQIQATDAN UZOQLASHISH VEKTORI',
        ha='center', fontsize=10, fontweight='bold', color='darkred')

plt.savefig('charts/chart6_conceptual_scheme.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()

print("Barcha grafiklar muvaffaqiyatli yaratildi!")
print(os.listdir('charts'))
