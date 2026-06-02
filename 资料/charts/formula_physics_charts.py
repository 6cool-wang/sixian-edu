import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arc
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 运动学公式关系图 ───
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# v-t graph
x_vt = np.array([0, 4, 6, 10])
y_vt = np.array([2, 6, 6, 10])
ax.plot([0, 10], [0, 0], 'k-', lw=0.8)
ax.plot([0, 0], [0, 10], 'k-', lw=0.8)
ax.plot(x_vt, y_vt, 'b-', linewidth=2.5, zorder=3)

# Fill area
ax.fill_between(x_vt, 0, y_vt, alpha=0.1, color='#3498db')
ax.text(5, 1.5, 'Area = displacement s', fontsize=9, color='#3498db', fontweight='bold', ha='center',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#3498db', alpha=0.8))

# labels
ax.text(9.5, -0.3, 't', fontsize=12, fontweight='bold')
ax.text(-0.3, 9.5, 'v', fontsize=12, fontweight='bold')
ax.text(0.5, 8.5, 'v = v₀ + at', fontsize=10, fontweight='bold', color='#e74c3c')
ax.text(0.5, 7.5, 's = v₀t + ½at²', fontsize=10, fontweight='bold', color='#e74c3c')
ax.text(0.5, 6.5, 'v² - v₀² = 2as', fontsize=10, fontweight='bold', color='#e74c3c')
ax.text(0.5, 5.5, 's = (v₀+v)t/2', fontsize=10, fontweight='bold', color='#e74c3c')

# velocity markers
ax.plot([0, 4], [2, 6], 'b-', lw=2)
ax.plot([4, 6], [6, 6], 'b-', lw=2)
ax.plot([6, 10], [6, 10], 'b-', lw=2)
ax.text(0.2, 2, 'v₀', fontsize=9, fontweight='bold')
ax.text(3.8, 6.2, 'v', fontsize=9, fontweight='bold')
ax.set_title('Kinematics: v-t Graph & Key Formulas', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
plt.savefig('charts/formula_physics_kinematics.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_physics_kinematics.svg")

# ─── Chart 2: 受力分析图 ───
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Block (box on a surface)
box = plt.Rectangle((-0.8, 0), 1.6, 1.2, facecolor='#3498db', alpha=0.3, edgecolor='#3498db', linewidth=2, zorder=2)
ax.add_patch(box)
ax.text(0, 0.6, 'Block\nm', ha='center', va='center', fontsize=10, fontweight='bold', color='#2c3e50')

# Forces
# Gravity (down)
ax.arrow(0, 0, 0, -1.8, head_width=0.15, head_length=0.15, fc='#e74c3c', ec='#e74c3c', linewidth=2.5, zorder=3)
ax.text(0.3, -1.2, 'G = mg', fontsize=10, fontweight='bold', color='#e74c3c')

# Normal force (up)
ax.arrow(0, 1.2, 0, 1.5, head_width=0.15, head_length=0.15, fc='#27ae60', ec='#27ae60', linewidth=2.5, zorder=3)
ax.text(0.3, 2.0, 'N (normal)', fontsize=10, fontweight='bold', color='#27ae60')

# Friction (left)
ax.arrow(0.8, 0.6, 1.2, 0, head_width=0.15, head_length=0.15, fc='#e67e22', ec='#e67e22', linewidth=2.5, zorder=3)
ax.text(1.8, 0.75, 'f =μN', fontsize=10, fontweight='bold', color='#e67e22')

# Applied force (right, at angle)
fx, fy = 1.5, 1.0
ax.arrow(-0.8, 0.6, -1.2, 0.8, head_width=0.15, head_length=0.15, fc='#9b59b6', ec='#9b59b6', linewidth=2.5, zorder=3)
ax.text(-2.2, 1.5, 'F (applied)', fontsize=10, fontweight='bold', color='#9b59b6')

# Surface line
ax.plot([-2.5, 2.5], [0, 0], 'k-', linewidth=2, zorder=1)
ax.text(2.2, -0.2, 'Surface', fontsize=9, color='#888', fontstyle='italic')

# Force balance equation
ax.text(0, -2.5, 'Newton: F_net = ma  |  Equilibrium: F_net = 0',
        fontsize=10, fontweight='bold', color='#2c3e50', ha='center')

ax.set_title('Force Analysis on a Horizontal Surface', fontsize=13, fontweight='bold', color='#2c3e50', pad=10)
plt.savefig('charts/formula_physics_forces.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_physics_forces.svg")

# ─── Chart 3: 浮力三种状态对比 ───
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

states = [
    ('Floating', 'ρ_obj < ρ_liq', 'V_displaced < V_obj\nF_float = G = mg', '#3498db'),
    ('Suspending', 'ρ_obj = ρ_liq', 'V_displaced = V_obj\nF_float = G = mg', '#27ae60'),
    ('Sinking', 'ρ_obj > ρ_liq', 'V_displaced = V_obj\nF_float < G, sinks', '#e74c3c'),
]

for i, (name, condition, desc, color) in enumerate(states):
    x = i * 3.3 + 0.5
    # Water container
    rect = FancyBboxPatch((x, 0.8), 2.8, 3, boxstyle="round,pad=0.08",
                          facecolor=color, alpha=0.08, edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    # Water line
    ax.plot([x, x+2.8], [2.2, 2.2], '--', color=color, alpha=0.5, lw=1)

    # Object (circle)
    if i == 0:  # floating - above water
        circle = plt.Circle((x+1.4, 2.5), 0.5, facecolor=color, alpha=0.4, edgecolor=color, linewidth=2)
    elif i == 1:  # suspending - at water line
        circle = plt.Circle((x+1.4, 2.2), 0.5, facecolor=color, alpha=0.4, edgecolor=color, linewidth=2)
    else:  # sinking - below water
        circle = plt.Circle((x+1.4, 1.5), 0.5, facecolor=color, alpha=0.4, edgecolor=color, linewidth=2)
    ax.add_patch(circle)

    ax.text(x+1.4, 3.6, name, ha='center', fontsize=11, fontweight='bold', color=color)
    ax.text(x+1.4, 3.2, condition, ha='center', fontsize=9, fontweight='bold', color='#555',
            bbox=dict(boxstyle='round,pad=0.1', facecolor='#fffbe6', edgecolor='none'))
    ax.text(x+1.4, 0.4, desc, ha='center', fontsize=8, color='#666')

ax.set_title('Buoyancy: Three States Compared', fontsize=14, fontweight='bold', color='#2c3e50', pad=5)
plt.savefig('charts/formula_physics_buoyancy.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_physics_buoyancy.svg")

# ─── Chart 4: 电路对比图（串联 vs 并联）───
fig, axes = plt.subplots(1, 2, figsize=(8, 3.5))

# Series circuit
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 4)
ax1.axis('off')

# Battery
ax1.plot([1, 1], [2.5, 3.5], 'k-', lw=2)
ax1.plot([0.5, 1.5], [3.5, 3.5], 'k-', lw=2)
ax1.plot([0.5, 0.5, 1.5, 1.5], [3.5, 3.8, 3.8, 3.5], 'k-', lw=2)
ax1.plot([0.5, 1.5], [2.5, 2.5], 'k-', lw=2)
ax1.plot([0.7, 1.3], [2.2, 2.2], 'k-', lw=2)
ax1.plot([0.7, 0.7, 1.3, 1.3], [2.2, 2.5, 2.5, 2.2], 'k-', lw=2)

# Wire to R1
ax1.plot([1, 1], [2.5, 2], 'k-', lw=1.5)
ax1.plot([1, 3.5], [2, 2], 'k-', lw=1.5)

# R1
rect1 = FancyBboxPatch((3.5, 1.5), 1.2, 1, boxstyle="round,pad=0.05",
                        facecolor='#e74c3c', alpha=0.25, edgecolor='#e74c3c', linewidth=1.5)
ax1.add_patch(rect1)
ax1.text(4.1, 2, 'R₁', ha='center', va='center', fontsize=10, fontweight='bold', color='#e74c3c')

# Wire to R2
ax1.plot([4.7, 7], [2, 2], 'k-', lw=1.5)
rect2 = FancyBboxPatch((7, 1.5), 1.2, 1, boxstyle="round,pad=0.05",
                        facecolor='#e74c3c', alpha=0.25, edgecolor='#e74c3c', linewidth=1.5)
ax1.add_patch(rect2)
ax1.text(7.6, 2, 'R₂', ha='center', va='center', fontsize=10, fontweight='bold', color='#e74c3c')

# Wire back to battery
ax1.plot([8.2, 9], [2, 2], 'k-', lw=1.5)
ax1.plot([9, 9], [2, 2.5], 'k-', lw=1.5)

# Formula
ax1.text(5, 0.5, 'R_total = R₁ + R₂\nI = U / R_total\nU = U₁ + U₂\nI₁ = I₂ = I',
        fontsize=9, fontweight='bold', color='#2c3e50', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fc', edgecolor='#ccc'))
ax1.set_title('Series Circuit (串联)', fontsize=12, fontweight='bold', color='#e74c3c')

# Parallel circuit
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 4)
ax2.axis('off')

# Battery
ax2.plot([1, 1], [2.5, 3.5], 'k-', lw=2)
ax2.plot([0.5, 1.5], [3.5, 3.5], 'k-', lw=2)
ax2.plot([0.5, 0.5, 1.5, 1.5], [3.5, 3.8, 3.8, 3.5], 'k-', lw=2)
ax2.plot([0.5, 1.5], [2.5, 2.5], 'k-', lw=2)
ax2.plot([0.7, 1.3], [2.2, 2.2], 'k-', lw=2)
ax2.plot([0.7, 0.7, 1.3, 1.3], [2.2, 2.5, 2.5, 2.2], 'k-', lw=2)

# Main wire
ax2.plot([1, 1], [2.5, 1.5], 'k-', lw=1.5)
ax2.plot([1, 9], [1.5, 1.5], 'k-', lw=1.5)

# Split 1 - R1
ax2.plot([3, 3], [1.5, 3], 'k-', lw=1.5)
ax2.plot([3, 5], [3, 3], 'k-', lw=1.5)
rect3 = FancyBboxPatch((5, 2.5), 1.2, 1, boxstyle="round,pad=0.05",
                        facecolor='#27ae60', alpha=0.25, edgecolor='#27ae60', linewidth=1.5)
ax2.add_patch(rect3)
ax2.text(5.6, 3, 'R₁', ha='center', va='center', fontsize=10, fontweight='bold', color='#27ae60')
ax2.plot([6.2, 7], [3, 3], 'k-', lw=1.5)
ax2.plot([7, 7], [3, 1.5], 'k-', lw=1.5)

# Split 2 - R2
ax2.plot([3.5, 3.5], [1.5, 0.5], 'k-', lw=1.5)
ax2.plot([3.5, 5], [0.5, 0.5], 'k-', lw=1.5)
rect4 = FancyBboxPatch((5, 0), 1.2, 1, boxstyle="round,pad=0.05",
                        facecolor='#27ae60', alpha=0.25, edgecolor='#27ae60', linewidth=1.5)
ax2.add_patch(rect4)
ax2.text(5.6, 0.5, 'R₂', ha='center', va='center', fontsize=10, fontweight='bold', color='#27ae60')
ax2.plot([6.2, 7], [0.5, 0.5], 'k-', lw=1.5)
ax2.plot([7, 7], [0.5, 1.5], 'k-', lw=1.5)

# Back to battery
ax2.plot([9, 9], [1.5, 2.5], 'k-', lw=1.5)

# Formula
ax2.text(5, 3.5, '1/R_total = 1/R₁ + 1/R₂\nU = U₁ = U₂\nI = I₁ + I₂\nI₁/I₂ = R₂/R₁',
        fontsize=9, fontweight='bold', color='#2c3e50', ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fc', edgecolor='#ccc'))

ax2.set_title('Parallel Circuit (并联)', fontsize=12, fontweight='bold', color='#27ae60')
plt.suptitle('Series vs Parallel Circuits', fontsize=13, fontweight='bold', color='#2c3e50')
plt.tight_layout()
plt.savefig('charts/formula_physics_circuits.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_physics_circuits.svg")

# ─── Chart 5: 能量转化关系图 ───
fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Central hub
ax.text(5, 2.5, 'Energy\nConservation\nE_total = const.', fontsize=12, fontweight='bold', color='#fff', ha='center', va='center',
        bbox=dict(boxstyle='circle', facecolor='#2c3e50', edgecolor='#1a1a2e', pad=0.5))

# Energy types around
types = [
    ('Kinetic\nE_k = 1/2 mv²', 5, 4.5, '#3498db'),
    ('Potential (Gravity)\nE_p = mgh', 8.5, 3.8, '#27ae60'),
    ('Elastic\nE_e = 1/2 kx²', 9, 1.2, '#e67e22'),
    ('Internal (Heat)\nQ = cmΔT', 6, 0.5, '#e74c3c'),
    ('Electrical\nW = UIt', 1.5, 1.5, '#9b59b6'),
]
for text, x, y, color in types:
    ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, alpha=0.9))
    ax.plot([x, 5+2*(x-5)/6], [y, 2.5+2*(y-2.5)/6], '-', color=color, alpha=0.3, lw=1.5)

# Conversion arrows
ax.annotate('', xy=(6.8, 4), xytext=(6, 4.2), arrowprops=dict(arrowstyle='<->', color='#ccc', lw=1))
ax.annotate('', xy=(7, 1.5), xytext=(7.5, 2.8), arrowprops=dict(arrowstyle='<->', color='#ccc', lw=1))

# Formulas at bottom
ax.text(5, 0.1, 'Work-Energy Theorem: W = ΔE_k  |  Conservation: E_initial = E_final (no friction)',
        fontsize=10, fontweight='bold', color='#2c3e50', ha='center')

ax.set_title('Energy Forms & Conservation', fontsize=14, fontweight='bold', color='#2c3e50', pad=5)
plt.savefig('charts/formula_physics_energy.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK formula_physics_energy.svg")
