import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arc, Rectangle, Circle, FancyArrowPatch
import numpy as np
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 显微镜结构与成像原理 ───
fig, ax = plt.subplots(figsize=(6, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Draw microscope parts
# Eyepiece
ax.plot([4.8, 5.2], [9.2, 9.2], 'k-', lw=3)
ax.plot([4.8, 4.8], [9.2, 8.8], 'k-', lw=2)
ax.plot([5.2, 5.2], [9.2, 8.8], 'k-', lw=2)
ax.text(5, 9.5, '目镜', ha='center', fontsize=9, fontweight='bold', color='#2c3e50')

# Tube
ax.plot([4.8, 4.8], [8.8, 7.5], 'k-', lw=2)
ax.plot([5.2, 5.2], [8.8, 7.5], 'k-', lw=2)

# Coarse focus
ax.plot([5.5, 6.5], [8, 8], 'k-', lw=2.5)
ax.text(6.8, 7.9, '粗准焦螺旋', fontsize=8, color='#555')

# Fine focus
ax.plot([5.5, 6.5], [7.3, 7.3], 'k-', lw=2)
ax.text(6.8, 7.2, '细准焦螺旋', fontsize=8, color='#555')

# Arm
ax.plot([5.2, 5.2], [7.5, 5.5], 'k-', lw=2.5)
ax.plot([5.2, 4.2], [5.5, 5.5], 'k-', lw=2.5)

# Objective lenses (rotating)
ax.plot([4.2, 4.2], [5.5, 4.8], 'k-', lw=1.5)
ax.plot([3.7, 4.7], [4.8, 4.8], 'k-', lw=2)
ax.plot([3.7, 3.7], [4.8, 4.3], 'k-', lw=1.5)
ax.plot([4.7, 4.7], [4.8, 4.3], 'k-', lw=1.5)

# Lenses
ax.text(3.7, 4.1, '物镜', ha='center', fontsize=8, fontweight='bold', color='#e74c3c')
ax.text(4.7, 4.1, '物镜', ha='center', fontsize=8, fontweight='bold', color='#e74c3c')

# Stage
ax.plot([2.5, 6.5], [3.5, 3.5], 'k-', lw=2.5)
ax.text(5.5, 3.2, '载物台', fontsize=8, color='#555')

# Specimen (on stage)
circle = plt.Circle((4.5, 3.5), 0.08, color='#e74c3c', zorder=3)
ax.add_patch(circle)
ax.text(4.5, 3.8, '标本', ha='center', fontsize=7, color='#e74c3c')

# Light path (dotted)
ax.plot([4.5, 4.5], [3.5, 2.5], 'k--', lw=1, alpha=0.5)

# Mirror
ax.plot([3.8, 5.2], [1.8, 2.5], 'k-', lw=2)
ax.plot([3.8, 5.2], [1.8, 2.5], 'b-', lw=1, alpha=0.3)
ax.text(4.5, 1.5, '反光镜', ha='center', fontsize=8, color='#555')

# Base
ax.plot([2.5, 6.5], [1, 1], 'k-', lw=2.5)
ax.text(4.5, 0.7, '镜座', ha='center', fontsize=8, color='#555')

# Imaging principle on right
# Arrow showing inverted image
ax.annotate('', xy=(7.5, 7.5), xytext=(7.5, 6),
            arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
ax.text(7.5, 6.75, '成像', ha='center', fontsize=9, fontweight='bold', color='#3498db')

# Inverted image demo
ax.text(7.5, 5.5, '"b" 在显微镜下 → "q"', fontsize=10, fontweight='bold', color='#e74c3c', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbe6', edgecolor='#fadb14'))

# Key rules
rules = [
    '放大倍数 = 目镜 × 物镜',
    '目镜越长放大倍数越小',
    '物镜越长放大倍数越大',
    '低→高倍镜：视野变暗、细胞变少',
    '物像偏哪，玻片向哪移',
]
for i, r in enumerate(rules):
    ax.text(7.5, 4.5-i*0.4, f'• {r}', fontsize=8, color='#444', ha='center')

ax.set_title('Microscope: Structure & Imaging Principles', fontsize=13, fontweight='bold', color='#2c3e50', pad=5)
plt.tight_layout()
plt.savefig('./topic_bio_microscope.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK topic_bio_microscope.svg")

# ─── Chart 2: 细胞分裂（有丝分裂）过程对比 ───
fig, axes = plt.subplots(1, 4, figsize=(8, 2.8))

stages = [
    ('间期\nInterphase', 'DNA复制\n染色体复制', '#3498db'),
    ('前期\nProphase', '染色体出现\n核膜消失', '#e67e22'),
    ('中期\nMetaphase', '染色体排列\n在赤道板上', '#27ae60'),
    ('后期\nAnaphase', '着丝粒分裂\n染色体移向两极', '#e74c3c'),
]

for ax2, (name, desc, color) in zip(axes, stages):
    ax2.set_xlim(0, 3)
    ax2.set_ylim(0, 3)
    ax2.axis('off')

    # Cell (circle)
    cell = Circle((1.5, 1.5), 1.2, facecolor=color, alpha=0.08, edgecolor=color, linewidth=2)
    ax2.add_patch(cell)

    # Nucleus/chromosomes representation
    if '间期' in name:
        # Interphase - nucleus with DNA
        nuc = Circle((1.5, 1.5), 0.6, facecolor='none', edgecolor='#888', linewidth=1.5, linestyle='--')
        ax2.add_patch(nuc)
        # DNA threads
        for _ in range(6):
            x = np.random.uniform(1.2, 1.8)
            y = np.random.uniform(1.2, 1.8)
            dot = Circle((x, y), 0.04, color='#e74c3c', alpha=0.6)
            ax2.add_patch(dot)
        ax2.text(1.5, 0.3, 'DNA复制', ha='center', fontsize=7, color='#888')
    elif '前期' in name:
        # Prophase - chromosomes appearing
        for i in range(4):
            x = 1.5 + np.cos(i*np.pi/2)*0.4
            y = 1.5 + np.sin(i*np.pi/2)*0.4
            ax2.plot([x-0.15, x+0.15], [y, y], 'k-', lw=2)
        ax2.text(1.5, 0.3, '染色体出现', ha='center', fontsize=7, color='#888')
    elif '中期' in name:
        # Metaphase - aligned in center
        for i in range(4):
            x = 1.0 + i*0.33
            ax2.plot([x, x], [1.5, 1.5], 'k-', lw=2.5)
        ax2.text(1.5, 0.3, '排列在赤道板', ha='center', fontsize=7, color='#888')
    else:
        # Anaphase - splitting
        for i in range(4):
            x_L = 0.8 + i*0.15
            x_R = 2.2 - i*0.15
            ax2.plot([x_L, x_L], [1.5, 1.5], 'k-', lw=2.5)
            ax2.plot([x_R, x_R], [1.5, 1.5], 'k-', lw=2.5)
        # Arrows showing movement
        ax2.annotate('', xy=(0.5, 1.5), xytext=(0.8, 1.5), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1))
        ax2.annotate('', xy=(2.5, 1.5), xytext=(2.2, 1.5), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1))
        ax2.text(1.5, 0.3, '着丝粒分裂', ha='center', fontsize=7, color='#888')

    ax2.set_title(name, fontsize=9, fontweight='bold', color=color)

plt.suptitle('Cell Division: Mitosis Process (有丝分裂过程)', fontsize=12, fontweight='bold', color='#2c3e50', y=1.02)

# Key takeaway
fig.text(0.5, 0.01, '染色体先复制后均分 → 子细胞染色体数与母细胞相同',
         ha='center', fontsize=10, fontweight='bold', color='#e74c3c')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig('./topic_bio_mitosis.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK topic_bio_mitosis.svg")

# ─── Chart 3: 光合作用与呼吸作用对比 ───
fig, axes = plt.subplots(1, 2, figsize=(7.5, 4))

# Left: Photosynthesis
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)
ax1.axis('off')

# Leaf shape
leaf = plt.Polygon([[5, 0.5], [2, 1.5], [1.5, 2.5], [3, 3.5], [5, 4], [7, 3.5], [8.5, 2.5], [8, 1.5], [5, 0.5]],
                   facecolor='#27ae60', alpha=0.2, edgecolor='#27ae60', linewidth=2)
ax1.add_patch(leaf)

# Sun
sun = Circle((8.5, 4.2), 0.5, facecolor='#f1c40f', alpha=0.6, edgecolor='#f39c12', linewidth=1.5)
ax1.add_patch(sun)
ax1.text(8.5, 4.2, '☀', ha='center', va='center', fontsize=16)

# Arrow in
ax1.annotate('CO₂', xy=(2, 2), xytext=(-0.5, 1.5),
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax1.annotate('H₂O', xy=(3, 1.2), xytext=(-0.5, 0.3),
             arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))

# Arrow out
ax1.annotate('O₂', xy=(7.5, 3.5), xytext=(10, 3.8),
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax1.annotate('有机物', xy=(6.5, 1.5), xytext=(9.5, 1.2),
             arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2))

# Formula
ax1.text(5, 3.2, 'CO₂ + H₂O  → 有机物 + O₂', ha='center', fontsize=9, fontweight='bold', color='#2c3e50',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#27ae60'))
ax1.text(5, 2.5, '光 + 叶绿体', ha='center', fontsize=9, color='#888')
ax1.text(5, 1.8, '合成有机物，储存能量', ha='center', fontsize=9, color='#27ae60', fontweight='bold')

ax1.set_title('Photosynthesis 光合作用', fontsize=12, fontweight='bold', color='#27ae60')

# Right: Respiration
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5)
ax2.axis('off')

# Mitochondrion-like shape
mito = plt.Polygon([[5, 0.5], [1.5, 1], [1, 2.5], [3, 4], [5, 4.5], [7, 4], [9, 2.5], [8.5, 1], [5, 0.5]],
                   facecolor='#e74c3c', alpha=0.12, edgecolor='#e74c3c', linewidth=2)
ax2.add_patch(mito)

# Arrow in
ax2.annotate('有机物', xy=(3, 3), xytext=(-0.5, 3.5),
             arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2))
ax2.annotate('O₂', xy=(4, 2), xytext=(-0.5, 1.5),
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))

# Arrow out
ax2.annotate('CO₂', xy=(7, 3.5), xytext=(10, 3.5),
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax2.annotate('H₂O', xy=(7, 1.5), xytext=(10, 1.5),
             arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
ax2.annotate('Energy', xy=(6, 1), xytext=(10, 0.5),
             arrowprops=dict(arrowstyle='->', color='#f39c12', lw=2))

# Formula
ax2.text(5, 3.2, '有机物 + O₂  →  CO₂ + H₂O + 能量', ha='center', fontsize=9, fontweight='bold', color='#2c3e50',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#e74c3c'))
ax2.text(5, 2.5, '有光/无光均可（线粒体）', ha='center', fontsize=9, color='#888')
ax2.text(5, 1.8, '分解有机物，释放能量', ha='center', fontsize=9, color='#e74c3c', fontweight='bold')

ax2.set_title('Respiration 呼吸作用', fontsize=12, fontweight='bold', color='#e74c3c')

plt.suptitle('Photosynthesis vs Respiration (光合 vs 呼吸)', fontsize=13, fontweight='bold', color='#2c3e50')
plt.tight_layout()
plt.savefig('./topic_bio_photo_resp.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK topic_bio_photo_resp.svg")

# ─── Chart 4: 血液循环路径 ───
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Heart
# Right side (left side of diagram)
# Right atrium
ra = FancyBboxPatch((5.5, 5.5), 1.8, 1.5, boxstyle="round,pad=0.1",
                     facecolor='#e74c3c', alpha=0.2, edgecolor='#e74c3c', linewidth=2)
ax.add_patch(ra)
ax.text(6.4, 6.2, '右心房', ha='center', fontsize=8, color='#e74c3c', fontweight='bold')

# Right ventricle
rv = FancyBboxPatch((5.5, 3.2), 1.8, 1.5, boxstyle="round,pad=0.1",
                     facecolor='#e74c3c', alpha=0.15, edgecolor='#e74c3c', linewidth=2)
ax.add_patch(rv)
ax.text(6.4, 3.9, '右心室', ha='center', fontsize=8, color='#e74c3c', fontweight='bold')

# Left side of diagram (right side of heart)
la = FancyBboxPatch((2.5, 5.5), 1.8, 1.5, boxstyle="round,pad=0.1",
                     facecolor='#3498db', alpha=0.2, edgecolor='#3498db', linewidth=2)
ax.add_patch(la)
ax.text(3.4, 6.2, '左心房', ha='center', fontsize=8, color='#3498db', fontweight='bold')

lv = FancyBboxPatch((2.5, 3.2), 1.8, 1.5, boxstyle="round,pad=0.1",
                     facecolor='#3498db', alpha=0.15, edgecolor='#3498db', linewidth=2)
ax.add_patch(lv)
ax.text(3.4, 3.9, '左心室', ha='center', fontsize=8, color='#3498db', fontweight='bold')

# Heart label
ax.text(4.4, 8, 'Heart 心脏', ha='center', fontsize=11, fontweight='bold', color='#2c3e50')

# Pulmonary circulation (right side of diagram)
# Right ventricle → lungs
ax.annotate('', xy=(7.3, 4.8), xytext=(7.3, 8),
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))
# Lungs
lung = FancyBboxPatch((6.5, 8), 2, 1.5, boxstyle="round,pad=0.15",
                       facecolor='#e67e22', alpha=0.15, edgecolor='#e67e22', linewidth=2)
ax.add_patch(lung)
ax.text(7.5, 8.75, '肺（气体交换）', ha='center', fontsize=9, color='#e67e22', fontweight='bold')

# Lungs → left atrium
ax.annotate('', xy=(4.3, 8), xytext=(4.3, 7),
            arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))

# Pulmonary circulation label
ax.text(7.3, 7.3, '肺循环', ha='center', fontsize=8, color='#e74c3c', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#e74c3c', alpha=0.8))
ax.text(7.3, 6.8, 'CO₂排出·获得O₂', ha='center', fontsize=7, color='#888')

# Systemic circulation (left side of diagram)
# Left ventricle → body
ax.annotate('', xy=(2.5, 4.8), xytext=(2.5, 1),
            arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))

# Body
body = FancyBboxPatch((0.5, 0.5), 3, 1.2, boxstyle="round,pad=0.15",
                       facecolor='#9b59b6', alpha=0.1, edgecolor='#9b59b6', linewidth=2)
ax.add_patch(body)
ax.text(2, 1.1, '全身组织细胞\n（物质交换）', ha='center', fontsize=9, color='#9b59b6', fontweight='bold')

# Body → right atrium
ax.annotate('', xy=(5.5, 1.5), xytext=(5.5, 5.5),
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2.5))

# Systemic circulation label
ax.text(2, 0.3, '体循环', ha='center', fontsize=8, color='#3498db', fontweight='bold')
ax.text(2, -0.1, '供给O₂·带走CO₂', ha='center', fontsize=7, color='#888')

# Oxygenated/deoxygenated labels
ax.text(1.8, 4.5, '含氧多', fontsize=7, color='#3498db', rotation=90)
ax.text(8, 6.5, '含氧少', fontsize=7, color='#e74c3c', rotation=90)

# Legend
ax.plot([0.5], [9.5], 's', color='#e74c3c', markersize=8)
ax.text(0.9, 9.45, '含氧少的血液（静脉血）', fontsize=7, color='#555')
ax.plot([0.5], [9], 's', color='#3498db', markersize=8)
ax.text(0.9, 8.95, '含氧多的血液（动脉血）', fontsize=7, color='#555')

ax.set_title('Blood Circulation: Double Loop (血液循环)', fontsize=12, fontweight='bold', color='#2c3e50', pad=5)
plt.savefig('./topic_bio_circulation.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK topic_bio_circulation.svg")

# ─── Chart 5: 反射弧结构 ───
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')

# Spinal cord (central)
sc = FancyBboxPatch((5.5, 0.5), 1.2, 3, boxstyle="round,pad=0.08",
                     facecolor='#f5f0e8', alpha=0.3, edgecolor='#8B7355', linewidth=2)
ax.add_patch(sc)
ax.text(6.1, 2, '脊髓\n（神经中枢）', ha='center', va='center', fontsize=9, fontweight='bold', color='#8B7355')

# Receptor (left side)
receptor = Circle((0.5, 2), 0.4, facecolor='#e74c3c', alpha=0.3, edgecolor='#e74c3c', linewidth=2)
ax.add_patch(receptor)
ax.text(0.5, 2.7, '感受器', ha='center', fontsize=9, fontweight='bold', color='#e74c3c')

# Sensory neuron (receptor → spinal cord)
ax.annotate('', xy=(1.5, 2), xytext=(0.9, 2),
            arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))
ax.text(1, 1.5, '传入神经', ha='center', fontsize=8, color='#3498db', fontweight='bold')
ax.plot([1.5, 5.5], [2, 2.5], '-', color='#3498db', lw=2.5)

# Interneuron (in spinal cord)
ax.annotate('', xy=(6.1, 1.5), xytext=(6.1, 2.5),
            arrowprops=dict(arrowstyle='->', color='#8B7355', lw=1.5))

# Motor neuron (spinal cord → effector)
ax.plot([6.7, 10], [1.5, 2], '-', color='#27ae60', lw=2.5)
ax.annotate('', xy=(10, 2), xytext=(9.5, 2),
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2.5))
ax.text(8.5, 1.5, '传出神经', ha='center', fontsize=8, color='#27ae60', fontweight='bold')

# Effector (right side)
effector = Circle((11, 2), 0.4, facecolor='#e67e22', alpha=0.3, edgecolor='#e67e22', linewidth=2)
ax.add_patch(effector)
ax.text(11, 2.7, '效应器\n（肌肉/腺体）', ha='center', fontsize=9, fontweight='bold', color='#e67e22')

# Flow arrow labels
path_labels = [
    ('刺激', 0.5, 3.4),
    ('①', 0.9, 1.2),
    ('②', 3, 1.3),
    ('③', 6.5, 1),
    ('④', 8.5, 1.3),
    ('⑤', 11, 1.2),
    ('反应', 11.5, 3.4),
]
for text, x, y in path_labels:
    ax.text(x, y, text, ha='center', fontsize=9, fontweight='bold', color='#8B7355')

# Reflex arc formula
ax.text(6, 0.2, '反射弧：感受器 → 传入神经 → 神经中枢 → 传出神经 → 效应器',
        ha='center', fontsize=10, fontweight='bold', color='#2c3e50',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffbe6', edgecolor='#fadb14'))

ax.set_title('Reflex Arc Structure (反射弧结构)', fontsize=13, fontweight='bold', color='#2c3e50', pad=5)
plt.savefig('./topic_bio_reflex.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK topic_bio_reflex.svg")

print("\n=== All 5 charts generated ===")
