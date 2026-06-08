"""Generate expanded charts for math/physics/chem/bio topic pages."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os, math

plt.rcParams['font.family'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 120

out = os.path.join(os.path.dirname(__file__), '资料', 'charts')
os.makedirs(out, exist_ok=True)

def save(name):
    plt.savefig(os.path.join(out, name), bbox_inches='tight', transparent=True)
    plt.close()
    print(f'  [OK] {name}')

# ────── 1. 圆 - 圆心角与圆周角 ──────
def fig_circle():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5); ax.set_aspect('equal')
    ax.axis('off')
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), 'k', lw=2)

    pts = [(0, 0), (1.5, 1.3), (-1.8, 0.6), (-0.5, -1.8)]
    labels = ['O', 'A', 'B', 'C']
    colors = ['#c0392b', '#3498db', '#2ecc71', '#e67e22']
    for (x, y), l, c in zip(pts, labels, colors):
        ax.plot(x, y, 'o', color=c, ms=6, zorder=5)
        ax.text(x*1.08, y*1.08, l, fontsize=12, fontweight='bold', color=c, ha='center')

    # Central angle ∠AOB
    ax.plot([0, 1.5], [0, 1.3], '#3498db', lw=1.5)
    ax.plot([0, -1.8], [0, 0.6], '#2ecc71', lw=1.5)

    # Inscribed angle ∠ACB
    ax.plot([1.5, -0.5], [1.3, -1.8], '#e67e22', lw=1.5)
    ax.plot([-1.8, -0.5], [0.6, -1.8], '#e67e22', lw=1.5)

    # Arc for central angle
    arc_theta = np.linspace(0.71, 2.8, 50)
    ax.plot(0.5*np.cos(arc_theta), 0.5*np.sin(arc_theta), '#c0392b', lw=2)
    ax.text(0.25, 0.4, 'α', fontsize=14, fontweight='bold', color='#c0392b')

    # Arc for inscribed angle
    ax.plot(0.9*np.cos(np.linspace(2.2, 2.8, 30)), 0.9*np.sin(np.linspace(2.2, 2.8, 30)), '#e67e22', lw=2)
    ax.text(-0.1, 0.55, 'β', fontsize=14, fontweight='bold', color='#e67e22')

    ax.set_title('圆心角 α = 2× 圆周角 β', fontsize=13, fontweight='bold', pad=10)
    plt.tight_layout()
    save('topic_math_circle.svg')

# ────── 2. 概率：树状图 ──────
def fig_prob():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_xlim(0, 6); ax.set_ylim(0, 4); ax.axis('off')

    # Root
    ax.plot(0.5, 3, 'o', color='#c0392b', ms=10)
    ax.text(0.5, 3.2, '开始', ha='center', fontsize=10, fontweight='bold', color='#c0392b')

    # Level 1: two branches
    for i, (lbl, col) in enumerate([('正面 ½', '#3498db'), ('反面 ½', '#2ecc71')]):
        x, y = 2, 2.5-i*1.0
        ax.plot([0.5, x], [3, y], 'k', lw=1.5)
        ax.plot(x, y, 'o', color=col, ms=8)
        ax.text(x, y+0.2, lbl, ha='center', fontsize=9, color=col, fontweight='bold')

        # Level 2: two more branches from each
        for j, (lbl2, col2) in enumerate([('正面', '#3498db'), ('反面', '#2ecc71')]):
            x2, y2 = 4, y+0.35-j*0.7
            ax.plot([x, x2], [y, y2], 'k', lw=1.2)
            ax.plot(x2, y2, 'o', color=col2, ms=6)
            ax.text(x2+0.3, y2, lbl2, fontsize=8, va='center')

            # Outcome probability
            prob = 0.25
            ax.text(x2, y2-0.2, 'P=¼', ha='center', fontsize=7, color='#888')

    ax.set_title('掷硬币两次的概率树状图', fontsize=12, fontweight='bold')
    plt.tight_layout()
    save('topic_math_prob.svg')

# ────── 3. 浮力 ──────
def fig_float():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

    # Left: Object submerged in water
    ax1.set_xlim(0, 5); ax1.set_ylim(0, 5); ax1.set_aspect('equal')
    ax1.axis('off')
    # Water container
    ax1.plot([0.5, 4.5], [1, 1], '#3498db', lw=2)
    ax1.plot([0.5, 0.5], [1, 4.5], '#3498db', lw=2)
    ax1.plot([4.5, 4.5], [1, 4.5], '#3498db', lw=2)
    ax1.plot([0.5, 4.5], [4.5, 4.5], '#3498db', lw=1)
    # Water fill
    ax1.fill([0.5, 4.5, 4.5, 0.5], [1, 1, 4.3, 4.3], '#3498db', alpha=0.15)

    # Block
    bx, by = 2.5, 2.5
    sz = 1.2
    rect = mpatches.FancyBboxPatch((bx-sz/2, by-sz/2), sz, sz, boxstyle="round,pad=0.1",
                                    fill=True, fc='#f0f0f0', ec='#333', lw=2)
    ax1.add_patch(rect)
    ax1.text(bx, by, '物体', ha='center', va='center', fontsize=10, fontweight='bold')

    # Forces
    ax1.arrow(bx, by-sz/2-0.1, 0, -0.9, head_width=0.15, head_length=0.15, fc='#c0392b', ec='#c0392b', lw=2)
    ax1.text(bx+0.2, by-sz/2-0.5, 'G', fontsize=11, fontweight='bold', color='#c0392b')
    ax1.arrow(bx, by+sz/2+0.1, 0, 0.9, head_width=0.15, head_length=0.15, fc='#3498db', ec='#3498db', lw=2)
    ax1.text(bx+0.2, by+sz/2+0.5, 'F浮', fontsize=11, fontweight='bold', color='#3498db')

    ax1.text(2.5, 0.5, 'F浮 = ρ液 g V排', ha='center', fontsize=12, fontweight='bold', color='#c0392b')
    ax1.set_title('物体在液体中的受力分析', fontsize=11, fontweight='bold')

    # Right: Relationship between ρ物 and ρ液
    states = ['ρ物 < ρ液\n(漂浮)', 'ρ物 = ρ液\n(悬浮)', 'ρ物 > ρ液\n(沉底)']
    colors_s = ['#2ecc71', '#f39c12', '#e74c3c']
    for i, (s, c) in enumerate(zip(states, colors_s)):
        y = 3.5 - i*1.2
        ax2.barh(y, 1, height=0.6, color=c, alpha=0.7)
        ax2.text(0.5, y, s, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # Density scale
    ax2.plot([0.5, 0.5], [0.5, 4.5], 'k', lw=1.5)
    ax2.text(0.5, 0.2, '密度增大→', ha='center', fontsize=9)

    # Arrow
    ax2.annotate('', xy=(0.5, 0.5), xytext=(0.5, 4.5),
                 arrowprops=dict(arrowstyle='->', lw=2, color='#888'))

    ax2.set_xlim(0, 1.5); ax2.set_ylim(0, 4.5)
    ax2.axis('off')
    ax2.set_title('浮沉条件与密度关系', fontsize=11, fontweight='bold')
    plt.tight_layout()
    save('topic_phy_float.svg')

# ────── 4. 功与能 ──────
def fig_work():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.2))

    # Left: Work = F × s
    ax1.set_xlim(0, 6); ax1.set_ylim(0, 3); ax1.set_aspect('equal')
    ax1.axis('off')

    # Block being pulled
    rect = mpatches.FancyBboxPatch((1.5, 1), 1.2, 0.8, boxstyle="round,pad=0",
                                    fill=True, fc='#f0f0f0', ec='#333', lw=2)
    ax1.add_patch(rect)
    ax1.text(2.1, 1.4, 'm', ha='center', fontsize=11, fontweight='bold')

    # Force arrow
    ax1.arrow(2.7, 1.4, 2.0, 0, head_width=0.15, head_length=0.2, fc='#c0392b', ec='#c0392b', lw=2.5)
    ax1.text(3.8, 1.7, 'F', fontsize=12, fontweight='bold', color='#c0392b')

    # Displacement
    ax1.plot([1.5, 4.5], [2.4, 2.4], 'k', lw=1.5)
    ax1.text(3, 2.6, 's（位移）', ha='center', fontsize=10, fontweight='bold')

    # Friction
    ax1.arrow(1.5, 1.4, -0.8, 0, head_width=0.12, head_length=0.15, fc='#e67e22', ec='#e67e22', lw=2)
    ax1.text(1.0, 1.2, 'f', fontsize=11, fontweight='bold', color='#e67e22')

    ax1.text(3, 0.4, 'W = Fs（恒力做功）', ha='center', fontsize=12, fontweight='bold', color='#c0392b')

    # Right: Energy conversion bar chart
    x = np.arange(3)
    labels = ['动能 Ek', '重力势能 Ep', '机械能 E']
    vals = [40, 60, 100]
    bars = ax2.bar(x, vals, width=0.4, color=['#3498db', '#2ecc71', '#e67e22'], alpha=0.8)
    for bar, v in zip(bars, vals):
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, str(v),
                 ha='center', fontsize=11, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontsize=10)
    ax2.set_ylim(0, 120)
    ax2.set_ylabel('能量 / J', fontsize=11)
    ax2.set_title('机械能 = 动能 + 势能', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    save('topic_phy_work.svg')

# ────── 5. 折射 ──────
def fig_refract():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect('equal')
    ax.axis('off')

    # Interface
    ax.plot([-3, 3], [0, 0], 'k', lw=2)
    ax.text(2.8, -0.3, '空气', fontsize=10, ha='right', color='#3498db')
    ax.text(2.8, 0.3, '水', fontsize=10, ha='right', color='#2ecc71')

    # Normal line
    ax.plot([0, 0], [-3, 3], '--', color='#999', lw=1.2)

    # Incident ray (air → water)
    theta1 = 50 * np.pi/180
    ax.arrow(-2.5*np.sin(theta1), 2.5*np.cos(theta1), 2.5*np.sin(theta1), -2.5*np.cos(theta1),
             head_width=0.12, head_length=0.15, fc='#c0392b', ec='#c0392b', lw=2)
    ax.text(-1.5*np.sin(theta1), 1.5*np.cos(theta1)+0.2, '入射光线', fontsize=9,
            rotation=-40, ha='center', color='#c0392b')

    # Refracted ray (bends toward normal)
    theta2 = 35 * np.pi/180
    ax.arrow(0, 0, 2.5*np.sin(theta2), -2.5*np.cos(theta2),
             head_width=0.12, head_length=0.15, fc='#3498db', ec='#3498db', lw=2)
    ax.text(1.8*np.sin(theta2), -1.8*np.cos(theta2)-0.3, '折射光线', fontsize=9,
            rotation=-35, ha='center', color='#3498db')

    # Reflected ray
    ax.arrow(0, 0, 2.5*np.sin(theta1), 2.5*np.cos(theta1),
             head_width=0.12, head_length=0.15, fc='#2ecc71', ec='#2ecc71', lw=2)
    ax.text(1.5*np.sin(theta1), 1.5*np.cos(theta1)+0.2, '反射光线', fontsize=9,
            rotation=40, ha='center', color='#2ecc71')

    # Angle markers
    arc1 = mpatches.Arc((0, 0), 1.2, 1.2, theta1=90-theta1*180/np.pi, theta2=90, ec='#c0392b', lw=1.5)
    ax.add_patch(arc1)
    ax.text(0.5*np.sin(theta1/2), 0.5*np.cos(theta1/2)+0.1, 'θ₁', fontsize=11, fontweight='bold', color='#c0392b')

    arc2 = mpatches.Arc((0, 0), 1.0, 1.0, theta1=270, theta2=270+theta2*180/np.pi, ec='#3498db', lw=1.5)
    ax.add_patch(arc2)
    ax.text(0.4*np.sin(theta2/2), -0.4*np.cos(theta2/2)-0.15, 'θ₂', fontsize=11, fontweight='bold', color='#3498db')

    ax.set_title('光的折射：光从空气斜射入水中', fontsize=12, fontweight='bold')
    plt.tight_layout()
    save('topic_phy_refract.svg')

# ────── 6. 生物细胞结构 ──────
def fig_cell():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

    # Left: Plant cell
    ax1.set_xlim(0, 5); ax1.set_ylim(0, 5); ax1.set_aspect('equal')
    ax1.axis('off')

    cell = mpatches.FancyBboxPatch((0.5, 0.5), 3.5, 3.5, boxstyle="round,pad=0.3",
                                    fill=True, fc='#e8f5e9', ec='#2e7d32', lw=2.5)
    ax1.add_patch(cell)
    # Cell wall (outer)
    cell_wall = mpatches.FancyBboxPatch((0.3, 0.3), 3.9, 3.9, boxstyle="round,pad=0.3",
                                         fill=False, ec='#555', lw=2, linestyle='-')
    ax1.add_patch(cell_wall)

    # Nucleus
    nuc = plt.Circle((2.5, 2.8), 0.6, fill=True, fc='#7b1fa2', alpha=0.3, ec='#7b1fa2', lw=1.5)
    ax1.add_patch(nuc)
    ax1.text(2.5, 2.8, '细胞核', ha='center', va='center', fontsize=8, fontweight='bold')

    # Vacuole (large central)
    vac = mpatches.FancyBboxPatch((1.2, 0.8), 2.0, 1.3, boxstyle="round,pad=0.2",
                                   fill=True, fc='#bbdefb', alpha=0.4, ec='#1976d2', lw=1.2)
    ax1.add_patch(vac)
    ax1.text(2.2, 1.5, '液泡', ha='center', fontsize=8, fontweight='bold', color='#1976d2')

    # Chloroplasts
    for (cx, cy) in [(1.0, 3.5), (3.5, 3.8), (3.2, 1.8)]:
        chl = plt.Circle((cx, cy), 0.25, fill=True, fc='#4caf50', alpha=0.6, ec='#2e7d32', lw=1)
        ax1.add_patch(chl)
    ax1.text(1.0, 4.0, '叶绿体', ha='center', fontsize=7.5, fontweight='bold', color='#2e7d32')

    ax1.set_title('植物细胞结构', fontsize=12, fontweight='bold')

    # Right: Animal cell
    ax2.set_xlim(0, 5); ax2.set_ylim(0, 5); ax2.set_aspect('equal')
    ax2.axis('off')

    cell2 = mpatches.FancyBboxPatch((0.8, 0.8), 3.0, 3.0, boxstyle="round,pad=0.4",
                                     fill=True, fc='#fce4ec', ec='#c62828', lw=2.5)
    ax2.add_patch(cell2)

    # Nucleus
    nuc2 = plt.Circle((2.3, 2.8), 0.55, fill=True, fc='#7b1fa2', alpha=0.3, ec='#7b1fa2', lw=1.5)
    ax2.add_patch(nuc2)
    ax2.text(2.3, 2.8, '细胞核', ha='center', va='center', fontsize=8, fontweight='bold')

    # Mitochondria
    for (mx, my) in [(1.5, 2.0), (3.2, 2.2)]:
        mit = mpatches.Ellipse((mx, my), 0.35, 0.2, fill=True, fc='#ff9800', alpha=0.6, ec='#e65100', lw=1)
        ax2.add_patch(mit)
    ax2.text(3.2, 2.5, '线粒体', ha='center', fontsize=7.5, fontweight='bold', color='#e65100')

    ax2.text(2.3, 1.3, '细胞膜', ha='center', fontsize=8, fontweight='bold', color='#c62828')

    # Labels for both
    ax2.plot([2.3, 4.0], [3.3, 4.0], 'k', lw=0.8)
    ax2.text(4.2, 4.0, '无细胞壁', fontsize=8, color='#555')

    ax2.set_title('动物细胞结构', fontsize=12, fontweight='bold')
    plt.tight_layout()
    save('topic_bio_cell.svg')

# ────── 7. 人体消化系统简图 ──────
def fig_digest():
    fig, ax = plt.subplots(figsize=(5, 6))
    ax.set_xlim(0, 5); ax.set_ylim(0, 6); ax.set_aspect('equal')
    ax.axis('off')

    # Mouth
    ax.fill([1.5, 3.5, 3.5, 1.5], [5.5, 5.5, 5.0, 5.0], '#fce4ec', ec='#c62828', lw=1.5)
    ax.text(2.5, 5.25, '口腔', ha='center', fontsize=10, fontweight='bold', color='#c62828')

    # Esophagus (tube)
    ax.plot([2.5, 2.5], [5.0, 4.0], 'k', lw=3)

    # Stomach
    stom = mpatches.FancyBboxPatch((1.5, 2.8), 2.0, 1.2, boxstyle="round,pad=0.15",
                                    fill=True, fc='#f3e5f5', ec='#7b1fa2', lw=1.5)
    ax.add_patch(stom)
    ax.text(2.5, 3.4, '胃', ha='center', fontsize=10, fontweight='bold', color='#7b1fa2')

    # Small intestine
    si = mpatches.FancyBboxPatch((1.8, 1.2), 1.4, 1.6, boxstyle="round,pad=0.1",
                                  fill=True, fc='#e8f5e9', ec='#2e7d32', lw=1.5)
    ax.add_patch(si)
    ax.text(2.5, 2.0, '小肠', ha='center', fontsize=10, fontweight='bold', color='#2e7d32')

    # Large intestine
    ax.plot([0.5, 0.5], [2.2, 1.2], 'k', lw=2)
    ax.plot([0.5, 4.0], [1.2, 1.2], 'k', lw=2)
    ax.plot([4.0, 4.0], [1.2, 2.2], 'k', lw=2)
    ax.text(0.5, 1.0, '大肠', ha='center', fontsize=8, color='#e65100')

    # Arrows showing path
    ax.annotate('', xy=(2.5, 4.0), xytext=(2.5, 4.0),  # already connected
               arrowprops=dict(arrowstyle='->', lw=0))

    ax.set_title('人体消化系统（示意）', fontsize=13, fontweight='bold')
    plt.tight_layout()
    save('topic_bio_digest.svg')

# ────── 8. 化学：空气成分 ──────
def fig_air():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))

    # Left: Pie chart of air composition
    labels = ['氮气 N₂\n78%', '氧气 O₂\n21%', '稀有气体\n0.94%', 'CO₂\n0.03%', '其他\n0.03%']
    sizes = [78, 21, 0.94, 0.03, 0.03]
    colors_p = ['#5c6bc0', '#42a5f5', '#66bb6a', '#ffa726', '#ef5350']
    ax1.pie(sizes, labels=labels, colors=colors_p, startangle=90,
            textprops={'fontsize': 9, 'fontweight': 'bold'})
    ax1.set_title('空气成分（体积分数）', fontsize=12, fontweight='bold')

    # Right: Simple experiment - O₂ supports combustion
    ax2.set_xlim(0, 4); ax2.set_ylim(0, 4); ax2.set_aspect('equal')
    ax2.axis('off')

    # Gas jar
    ax2.plot([0.8, 3.2], [3.5, 3.5], 'k', lw=2)
    ax2.plot([0.8, 0.8], [0.5, 3.5], 'k', lw=2)
    ax2.plot([3.2, 3.2], [0.5, 3.5], 'k', lw=2)
    ax2.plot([0.8, 3.2], [0.5, 0.5], 'k', lw=2)
    # Gas inside
    ax2.fill([0.9, 3.1, 3.1, 0.9], [0.6, 0.6, 3.4, 3.4], '#e3f2fd', alpha=0.4)
    ax2.text(2.0, 2.0, 'O₂', ha='center', fontsize=14, fontweight='bold', color='#1565c0')

    # Splint
    ax2.plot([2.0, 2.0], [0.5, 1.0], 'k', lw=2)
    ax2.plot([2.0, 2.0], [1.0, 2.0], 'sienna', lw=3)

    # Flame
    ax2.plot(2.0, 2.2, '*', color='orange', ms=15)
    ax2.plot(2.0, 2.5, '*', color='yellow', ms=10)

    ax2.text(2.0, 3.0, '带火星木条复燃', ha='center', fontsize=9, fontweight='bold', color='#e65100')
    ax2.set_title('O₂ 检验方法', fontsize=12, fontweight='bold')
    plt.tight_layout()
    save('topic_chem_air.svg')

# ────── 9. 化学：金属活动性柱状图 ──────
def fig_metal_activity():
    fig, ax = plt.subplots(figsize=(7, 4))
    metals = ['K', 'Ca', 'Na', 'Mg', 'Al', 'Zn', 'Fe', 'Sn', 'Pb', '(H)', 'Cu', 'Hg', 'Ag', 'Pt', 'Au']
    activity = [95, 92, 90, 80, 70, 55, 45, 35, 30, 25, 15, 10, 5, 2, 1]

    colors_m = ['#c0392b']*5 + ['#e67e22']*3 + ['#f1c40f']*2 + ['#3498db']*2 + ['#2ecc71']*3

    bars = ax.bar(range(len(metals)), activity, color=colors_m, alpha=0.8, width=0.6)
    ax.set_xticks(range(len(metals)))
    ax.set_xticklabels(metals, fontsize=10, fontweight='bold')
    ax.set_ylabel('活动性（相对值）', fontsize=11)
    ax.set_title('常见金属活动性顺序', fontsize=12, fontweight='bold')
    ax.set_xlim(-0.5, len(metals)-0.5)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    save('topic_chem_metal.svg')


if __name__ == '__main__':
    print('Generating expanded topic charts...')
    fig_circle()
    fig_prob()
    fig_float()
    fig_work()
    fig_refract()
    fig_cell()
    fig_digest()
    fig_air()
    fig_metal_activity()
    print('All expanded charts done.')
