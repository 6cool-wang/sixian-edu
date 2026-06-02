import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Arc, Circle
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 平面图形面积公式对比 ───
fig, ax = plt.subplots(figsize=(7, 4))
shapes = ['Triangle\n(1/2)ah', 'Rectangle\nab', 'Square\na^2', 'Parallelogram\nah', 'Trapezoid\n(1/2)(a+b)h', 'Circle\npir^2']
formulas = ['S = ½ah', 'S = ab', 'S = a²', 'S = ah', 'S = ½(a+b)h', 'S = πr²']
colors = ['#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6','#1abc9c']
y_pos = np.arange(len(shapes))
bars = ax.barh(y_pos, [8,8,8,8,8,8], color=colors, alpha=0.15, edgecolor='none')
for i, (shape, formula, color) in enumerate(zip(shapes, formulas, colors)):
    ax.text(4, i, shape, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
    ax.text(7.5, i, formula, ha='center', va='center', fontsize=11, fontweight='bold', color='#2c3e50',
            fontfamily='serif')
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 5.5)
ax.axis('off')
ax.set_title('Common Plane Figure Area Formulas', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
plt.tight_layout()
plt.savefig('charts/formula_geometry_areas.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_geometry_areas.svg")

# ─── Chart 2: 立体图形体积关系 ───
fig, ax = plt.subplots(figsize=(7, 4.5))
solids = ['Cube\na^3', 'Cuboid\nabc', 'Cylinder\npir^2h', 'Cone\n(1/3)pir^2h', 'Sphere\n(4/3)pir^3', 'Prism\nSh', 'Pyramid\n(1/3)Sh']
volumes = [1.0, 1.2, 1.5, 0.5, 2.0, 1.3, 0.6]
colors = ['#e74c3c','#3498db','#2ecc71','#f39c12','#9b59b6','#1abc9c','#e67e22']
bars = ax.bar(range(len(solids)), volumes, color=colors, alpha=0.8, width=0.55, edgecolor='white', linewidth=0.5)
for i, (v, bar) in enumerate(zip(volumes, bars)):
    ax.text(i, v+0.05, f'V = {v:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold', color=colors[i])
ax.set_xticks(range(len(solids)))
ax.set_xticklabels(solids, fontsize=8.5)
ax.set_ylabel('Relative Volume', fontsize=11, color='#555')
ax.set_title('Solid Volume Comparison (Relative to Same Base Size)', fontsize=13, fontweight='bold', color='#2c3e50', pad=10)
ax.set_ylim(0, 2.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig('charts/formula_geometry_volumes.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_geometry_volumes.svg")

# ─── Chart 3: 三角形分类关系图 ───
fig, ax = plt.subplots(figsize=(7, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Root
ax.text(5, 5.3, 'Triangles (by Angle)', fontsize=13, fontweight='bold', color='#2c3e50', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8e8e8', edgecolor='#888'))

# Level 1
ax.annotate('', xy=(2, 4.2), xytext=(5, 4.8), arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))
ax.annotate('', xy=(8, 4.2), xytext=(5, 4.8), arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))

ax.text(2, 3.8, 'Acute Triangle\nAll angles < 90°', fontsize=9, fontweight='bold', color='#27ae60', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e6f7e6', edgecolor='#27ae60'))
ax.text(8, 3.8, 'Obtuse Triangle\nOne angle > 90°', fontsize=9, fontweight='bold', color='#e74c3c', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fde8e8', edgecolor='#e74c3c'))

# Level 1 right - right triangle
ax.annotate('', xy=(5, 4.2), xytext=(5, 4.8), arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))
ax.text(5, 3.8, 'Right Triangle\nOne angle = 90°', fontsize=9, fontweight='bold', color='#2980b9', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#e3f2fd', edgecolor='#2980b9'))

# Level 2
for start, label, x, y, color, bg in [(2, 'Equilateral\nAll sides equal\nAll angles 60°', 0.5, 2, '#e67e22','#fff3e0'),
                                        (2, 'Isosceles\nTwo sides equal\nBase angles equal', 3.5, 2, '#9b59b6','#f3e8ff'),
                                        (8, 'Isosceles\n(Two sides equal)', 6.5, 2, '#9b59b6','#f3e8ff'),
                                        (8, 'Scalene\nNo sides equal\nAll angles differ', 9.5, 2, '#e74c3c','#fde8e8'),
                                        (5, 'Isosceles Right\n45°-45°-90°', 5, 2, '#1abc9c','#e6f7e6')]:
    ax.annotate('', xy=(x, 2.4), xytext=(start, 3.4), arrowprops=dict(arrowstyle='->', color='#ccc', lw=1))
    ax.text(x, y, label, fontsize=8, fontweight='bold', color=color, ha='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor=bg, edgecolor=color, alpha=0.9))

# Bottom note
ax.text(5, 0.5, 'Tip: Triangle angles sum = 180°  |  Side-angle relation: larger side opposite larger angle',
        fontsize=9, color='#888', ha='center', style='italic')
plt.savefig('charts/formula_geometry_triangles.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_geometry_triangles.svg")

# ─── Chart 4: 圆的性质示意图 ───
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

circle = Circle((0, 0), 2, fill=False, edgecolor='#2980b9', linewidth=2.5)
ax.add_patch(circle)
ax.plot([0, 2], [0, 0], 'r-', linewidth=2, zorder=3)
ax.plot([0, 0], [0, 2], 'orange', linewidth=2, zorder=3)
ax.plot([0, -2*np.cos(np.pi/6)], [0, 2*np.sin(np.pi/6)], 'green', linewidth=2, zorder=3)
ax.plot([0, -2*np.cos(np.pi/3)], [0, -2*np.sin(np.pi/3)], 'purple', linewidth=2, zorder=3)
# angles
theta = np.linspace(0, np.pi/6, 30)
ax.plot(0.3*np.cos(theta), 0.3*np.sin(theta), 'k-', lw=1)
ax.text(0.45, 0.15, 'θ', fontsize=11, fontweight='bold')
# Labels
ax.text(1.0, -0.15, 'radius r', fontsize=10, color='red', fontweight='bold')
ax.text(0.1, 1.1, 'diameter d=2r', fontsize=10, color='orange', fontweight='bold')
ax.text(-1.5, 0.8, 'chord', fontsize=10, color='green', fontweight='bold')
ax.text(-1.8, -0.8, 'arc', fontsize=10, color='purple', fontweight='bold')
# center point
ax.plot(0, 0, 'ko', markersize=5)
ax.text(0.05, -0.25, 'O', fontsize=10, fontweight='bold')
ax.set_title('Circle Properties', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
plt.tight_layout()
plt.savefig('charts/formula_geometry_circle.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_geometry_circle.svg")

# ─── Chart 5: 勾股定理可视化 ───
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

# Right triangle
tri = Polygon([[1, 1], [4, 1], [1, 4]], closed=True, fill=False, edgecolor='#e74c3c', linewidth=2.5, zorder=3)
ax.add_patch(tri)
ax.text(1, 1, 'A', fontsize=12, fontweight='bold', ha='right', va='top')
ax.text(4, 1, 'B', fontsize=12, fontweight='bold', ha='left', va='top')
ax.text(1, 4, 'C', fontsize=12, fontweight='bold', ha='right', va='bottom')

# Right angle marker
ax.plot([1, 1.3], [1, 1], 'k-', lw=1)
ax.plot([1, 1], [1, 1.3], 'k-', lw=1)

# Squares on each side
# Bottom square (a^2)
sq_a = Polygon([[1, 1], [4, 1], [4, -2], [1, -2]], closed=True, fill=True, facecolor='#3498db', alpha=0.15, edgecolor='#3498db', linewidth=1.5)
ax.add_patch(sq_a)
ax.text(2.5, -0.5, 'a² = 9', fontsize=11, fontweight='bold', color='#3498db', ha='center')

# Left square (b^2)
sq_b = Polygon([[1, 1], [-2, 1], [-2, 4], [1, 4]], closed=True, fill=True, facecolor='#2ecc71', alpha=0.15, edgecolor='#2ecc71', linewidth=1.5)
ax.add_patch(sq_b)
ax.text(-0.5, 2.5, 'b² = 9', fontsize=11, fontweight='bold', color='#27ae60', ha='center', rotation=90)

# Top-right square (c^2)
sq_c = Polygon([[4, 1], [4+3, 1+3], [1+3, 4+3], [1, 4]], closed=True, fill=True, facecolor='#e74c3c', alpha=0.1, edgecolor='#e74c3c', linewidth=1.5)
ax.add_patch(sq_c)
ax.text(4.5, 4.5, 'c² = 18', fontsize=11, fontweight='bold', color='#e74c3c', ha='center')

# Pythagoras theorem
ax.text(3, 0.2, 'a = 3, b = 3', fontsize=10, color='#555', ha='center')
ax.text(3, 5.5, 'a² + b² = c²  →  9 + 9 = 18',
        fontsize=14, fontweight='bold', color='#1a1a2e', ha='center',
        fontfamily='serif')

# Side labels on triangle
ax.text(2.5, 0.8, 'a=3', fontsize=11, fontweight='bold', color='#3498db', ha='center')
ax.text(0.8, 2.5, 'b=3', fontsize=11, fontweight='bold', color='#27ae60', ha='center', rotation=90)
ax.text(2.8, 2.8, 'c=?', fontsize=11, fontweight='bold', color='#e74c3c', ha='center')

ax.set_title('Pythagorean Theorem: a² + b² = c²', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
plt.tight_layout()
plt.savefig('charts/formula_geometry_pythagoras.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_geometry_pythagoras.svg")
