import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 幂运算层级关系图 ───
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Tree structure
nodes = [
    ('Exponent Rules\n指数运算法则', 5, 5.2, '#2c3e50', '#e8e8e8'),
]
children = [
    ('a^m x a^n \n= a^(m+n)', 1.5, 3.5, '#3498db'),
    ('a^m / a^n \n= a^(m-n)', 3.5, 3.5, '#2980b9'),
    ('(a^m)^n \n= a^(mn)', 5, 3.5, '#e74c3c'),
    ('(ab)^n \n= a^n b^n', 6.5, 3.5, '#27ae60'),
    ('a^0 = 1\na^(-n)=1/a^n', 8.5, 3.5, '#e67e22'),
]
grandchildren = [
    (1.5, 'Example:\n2^3 x 2^2 = 2^5 = 32', 1.5, 1.8, '#3498db'),
    (3.5, 'Example:\n2^5 / 2^3 = 2^2 = 4', 3.5, 1.8, '#2980b9'),
    (5, 'Example:\n(2^3)^2 = 2^6 = 64', 5, 1.8, '#e74c3c'),
    (6.5, 'Example:\n(2x3)^2 = 4 x 9 = 36', 6.5, 1.8, '#27ae60'),
    (8.5, 'Example:\n2^(-3) = 1/8 = 0.125', 8.5, 1.8, '#e67e22'),
]

for text, x, y, color, bg in nodes:
    ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=bg, edgecolor=color))

for text, x, y, color in children:
    ax.plot([x, nodes[0][1]], [y+0.3, nodes[0][2]-0.3], '-', color='#ccc', lw=1)
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.9))

for x, text, tx, ty, color in grandchildren:
    ax.plot([x, tx], [ty+0.3, y-0.3], ':', color='#ccc', lw=0.8)
    ax.text(tx, ty, text, ha='center', fontsize=8.5, color='#555',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#fffbe6', edgecolor='#fadb14', alpha=0.8))

plt.savefig('charts/formula_algebra_exponents.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_algebra_exponents.svg")

# ─── Chart 2: 二次函数图像特征 ───
fig, ax = plt.subplots(figsize=(6.5, 5))
x = np.linspace(-4, 4, 200)
# a > 0, opens up
y1 = 0.5 * (x - 0)**2 + 0
# a < 0, opens down
y2 = -0.4 * (x - 0)**2 + 3
# a > 0, shifted
y3 = 0.3 * (x - 1)**2 - 1
# Discriminant demo
y4 = x**2 - 3*x + 2

ax.plot(x, y1, 'b-', linewidth=2, label='y = 0.5x²  (Δ=0, vertex at origin)')
ax.plot(x, y2, 'r-', linewidth=2, label='y = -0.4x²+3  (a<0, opens down)')
ax.plot(x, y3, 'g-', linewidth=2, label='y = 0.3(x-1)²-1  (shifted)')
ax.plot(x, y4, 'orange', linewidth=2, label='y = x²-3x+2  (Δ=1>0, 2 roots)')

ax.axhline(y=0, color='#333', linewidth=0.8)
ax.axvline(x=0, color='#333', linewidth=0.8)
ax.grid(alpha=0.15)

# Mark the roots of y4
ax.plot(1, 0, 'o', color='orange', markersize=6)
ax.plot(2, 0, 'o', color='orange', markersize=6)
ax.text(1, -0.3, 'x=1', fontsize=8, color='orange', ha='center')
ax.text(2, -0.3, 'x=2', fontsize=8, color='orange', ha='center')

ax.set_xlim(-4, 4)
ax.set_ylim(-3, 5)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_title('Quadratic Functions: y = ax² + bx + c', fontsize=13, fontweight='bold', color='#2c3e50')
ax.legend(fontsize=8, loc='upper right', framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('charts/formula_algebra_quadratic.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_algebra_quadratic.svg")

# ─── Chart 3: 乘法公式几何意义 ───
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.axis('off')

# Large square (a+b)^2 = a^2 + 2ab + b^2
# a=3, b=2
# a^2 (bottom-left)
sq1 = plt.Rectangle((0, 0), 3, 3, facecolor='#3498db', alpha=0.2, edgecolor='#3498db', linewidth=2)
ax.add_patch(sq1)
ax.text(1.5, 1.5, 'a²', fontsize=20, fontweight='bold', color='#3498db', ha='center')

# ab (top-left)
sq2 = plt.Rectangle((0, 3), 3, 2, facecolor='#e74c3c', alpha=0.15, edgecolor='#e74c3c', linewidth=2)
ax.add_patch(sq2)
ax.text(1.5, 4, 'ab', fontsize=16, fontweight='bold', color='#e74c3c', ha='center')

# ab (bottom-right)
sq3 = plt.Rectangle((3, 0), 2, 3, facecolor='#e74c3c', alpha=0.15, edgecolor='#e74c3c', linewidth=2)
ax.add_patch(sq3)
ax.text(4, 1.5, 'ab', fontsize=16, fontweight='bold', color='#e74c3c', ha='center')

# b^2 (top-right)
sq4 = plt.Rectangle((3, 3), 2, 2, facecolor='#27ae60', alpha=0.2, edgecolor='#27ae60', linewidth=2)
ax.add_patch(sq4)
ax.text(4, 4, 'b²', fontsize=20, fontweight='bold', color='#27ae60', ha='center')

# Labels
ax.text(1.5, -0.3, 'a = 3', fontsize=10, color='#3498db', ha='center', fontweight='bold')
ax.text(4, -0.3, 'b = 2', fontsize=10, color='#27ae60', ha='center', fontweight='bold')
ax.text(-0.3, 1.5, 'a = 3', fontsize=10, color='#3498db', va='center', fontweight='bold', rotation=90)
ax.text(-0.3, 4, 'b = 2', fontsize=10, color='#e74c3c', va='center', fontweight='bold', rotation=90)

ax.set_title('(a+b)² = a² + 2ab + b²', fontsize=14, fontweight='bold', color='#2c3e50', fontfamily='serif', pad=10)
plt.savefig('charts/formula_algebra_square.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_algebra_square.svg")

# ─── Chart 4: 数列规律可视化 ───
fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))

# Arithmetic sequence
ax1 = axes[0]
n = np.arange(1, 9)
a1, d = 2, 3
arith = a1 + (n-1)*d
ax1.bar(n, arith, color='#3498db', alpha=0.7, width=0.5, edgecolor='white')
ax1.plot(n, arith, 'ro-', linewidth=2, markersize=6, zorder=3)
for i, val in enumerate(arith):
    ax1.text(i+1, val+0.3, str(val), ha='center', fontsize=9, fontweight='bold', color='#e74c3c')
ax1.set_xlabel('n (term)', fontsize=10)
ax1.set_ylabel('a_n', fontsize=10)
ax1.set_title('Arithmetic: a_n = 2 + (n-1)x3', fontsize=11, fontweight='bold', color='#2c3e50')
ax1.set_xticks(n)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', alpha=0.2)

# Geometric sequence
ax2 = axes[1]
n = np.arange(1, 7)
a1, r = 2, 2
geom = a1 * (r ** (n-1))
ax2.bar(n, geom, color='#e74c3c', alpha=0.7, width=0.4, edgecolor='white')
ax2.plot(n, geom, 'bo-', linewidth=2, markersize=6, zorder=3)
for i, val in enumerate(geom):
    ax2.text(i+1, val+0.3, str(val), ha='center', fontsize=9, fontweight='bold', color='#2980b9')
ax2.set_xlabel('n (term)', fontsize=10)
ax2.set_ylabel('a_n', fontsize=10)
ax2.set_title('Geometric: a_n = 2 x 2^(n-1)', fontsize=11, fontweight='bold', color='#2c3e50')
ax2.set_xticks(n)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='y', alpha=0.2)

plt.suptitle('Sequence Patterns Comparison', fontsize=14, fontweight='bold', color='#2c3e50')
plt.tight_layout()
plt.savefig('charts/formula_algebra_sequences.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_algebra_sequences.svg")

# ─── Chart 5: 数据分析——均值/方差/分布 ───
fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))

# Left: Box plot comparison of two datasets
ax1 = axes[0]
data1 = np.random.normal(75, 10, 100)
data2 = np.random.normal(75, 5, 100)
bp = ax1.boxplot([data1, data2], labels=['Class A\nStd=10', 'Class B\nStd=5'],
                 patch_artist=True, widths=0.4)
bp['boxes'][0].set_facecolor('#3498db')
bp['boxes'][0].set_alpha(0.5)
bp['boxes'][1].set_facecolor('#e74c3c')
bp['boxes'][1].set_alpha(0.5)
ax1.set_ylabel('Score', fontsize=10)
ax1.set_title('Variance Comparison\n(lower variance = more stable)', fontsize=10, fontweight='bold', color='#2c3e50')
ax1.grid(axis='y', alpha=0.2)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Right: 正态分布
ax2 = axes[1]
x = np.linspace(50, 100, 200)
y1 = (1/(10*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-75)/10)**2)
y2 = (1/(5*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-75)/5)**2)
ax2.plot(x, y1, 'b-', linewidth=2, label='σ=10 (wide)')
ax2.plot(x, y2, 'r-', linewidth=2, label='σ=5 (narrow)')
ax2.fill_between(x, y1, alpha=0.05, color='blue')
ax2.fill_between(x, y2, alpha=0.05, color='red')
ax2.set_xlabel('Score', fontsize=10)
ax2.set_ylabel('Density', fontsize=10)
ax2.set_title('Normal Distribution: same mean, different σ', fontsize=10, fontweight='bold', color='#2c3e50')
ax2.legend(fontsize=8)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(alpha=0.15)

plt.suptitle('Statistics: Mean, Variance & Distribution', fontsize=13, fontweight='bold', color='#2c3e50')
plt.tight_layout()
plt.savefig('charts/formula_algebra_statistics.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_algebra_statistics.svg")
