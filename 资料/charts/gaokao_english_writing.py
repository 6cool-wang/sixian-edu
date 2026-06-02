import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 新高考英语作文评分维度雷达图 ───
categories = ['内容要点\nContent', '语言准确\nAccuracy', '词汇语法\nRange', '篇章结构\nCoherence', '书写规范\nHandwriting']
N = len(categories)
values = [9, 8, 7, 6, 5]
values += values[:1]
angles = [n/float(N)*2*np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(30)
ax.plot(angles, values, 'o-', linewidth=2, color='#2980b9', markersize=6)
ax.fill(angles, values, alpha=0.15, color='#2980b9')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([2,4,6,8,10])
ax.set_yticklabels(['2','4','6','8','10'], fontsize=9, color='#888')
ax.set_title('New Gaokao English Essay Scoring Dimensions', fontsize=15, fontweight='bold', pad=20, color='#2c3e50')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_radar.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_radar.svg")

# ─── Chart 2: 读后续写情节发展曲线图 ───
fig, ax = plt.subplots(figsize=(8,4.5))
x = [0, 1, 2, 3, 4, 5, 6]
y = [2, 3, 5, 8, 7, 9, 10]
ax.plot(x, y, 'o-', color='#e74c3c', linewidth=2.5, markersize=8, zorder=3)
ax.fill_between(x, y, alpha=0.1, color='#e74c3c')
labels = ['Read original\nunderstand the plot', 'Set the tone\natmosphere', 'Find conflict\nkey points', 'Build climax\nturning point', 'Emotion flow\ndetailed description', 'Natural ending\nconnect back', 'Theme elevation\nmeaning']
for i, (xi, yi) in enumerate(zip(x, y)):
    ax.annotate(labels[i], (xi, yi), textcoords="offset points", xytext=(0, 18 if i!=2 else -25),
                ha='center', fontsize=8.5, color='#2c3e50', fontweight='bold')
ax.set_xlim(-0.3, 6.3)
ax.set_ylim(0, 11)
ax.set_xticks([])
ax.set_ylabel('Plot Tension', fontsize=11, color='#555')
ax.set_title('Continuation Writing - Plot Development Curve', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_alpha(0.3)
ax.spines['bottom'].set_alpha(0.3)
ax.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_plot_curve.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_plot_curve.svg")

# ─── Chart 3: 应用文体裁分类统计（高考频率） ───
fig, ax = plt.subplots(figsize=(6,4))
genres = ['Letter/Email', 'Notice', 'Speech', 'Report', 'Proposal', 'Invitation', 'Thanks', 'Application']
freq = [28, 12, 18, 8, 14, 10, 5, 5]
colors = ['#2980b9','#3498db','#5dade2','#85c1e9','#aed6f1','#1a5276','#2e86c1','#7fb3d8']
bars = ax.barh(genres, freq, color=colors, edgecolor='white', height=0.65)
for bar, val in zip(bars, freq):
    ax.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2, f'{val}%', va='center', fontsize=10, fontweight='bold', color='#2c3e50')
ax.set_xlim(0, 35)
ax.set_xlabel('Test Frequency (%)', fontsize=11, color='#555')
ax.set_title('Gaokao Practical Writing: Genre Distribution', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_alpha(0.3)
ax.spines['bottom'].set_alpha(0.3)
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_genre_freq.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_genre_freq.svg")

# ─── Chart 4: 读后续写四步法流程图 ───
fig, ax = plt.subplots(figsize=(8, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')
steps = [
    ('Step 1\nRead & Understand', '#2980b9', 0.5),
    ('Step 2\nPlan the Plot', '#3498db', 2.5),
    ('Step 3\nWrite with Detail', '#5dade2', 4.5),
    ('Step 4\nPolish & Check', '#85c1e9', 6.5),
]
for text, color, x in steps:
    rect = FancyBboxPatch((x, 0.5), 1.8, 2, boxstyle="round,pad=0.15",
                          facecolor=color, edgecolor='white', linewidth=0, alpha=0.9)
    ax.add_patch(rect)
    ax.text(x+0.9, 1.5, text, ha='center', va='center', fontsize=10, fontweight='bold', color='white',
            linespacing=1.5)
for i in range(3):
    arrow_x = steps[i][2] + 1.8
    ax.annotate('', xy=(arrow_x+0.4, 1.5), xytext=(arrow_x, 1.5),
                arrowprops=dict(arrowstyle='->', color='#2980b9', lw=2.5))
plt.savefig('charts/gaokao_eng_4step.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_4step.svg")

# ─── Chart 5: 高考英语作文高频话题分布 ───
fig, ax = plt.subplots(figsize=(7, 4))
topics = ['Growth & Dream', 'Social Issues', 'Campus Life', 'Environment',
          'Tech & Life', 'Health & Sports', 'Culture', 'Relationships']
counts = [95, 88, 82, 78, 72, 68, 65, 60]
colors_bar = ['#e74c3c','#e67e22','#f1c40f','#2ecc71','#3498db','#9b59b6','#1abc9c','#34495e']
bars = ax.barh(topics, counts, color=colors_bar, edgecolor='white', height=0.6)
for bar, val in zip(bars, counts):
    ax.text(bar.get_width()+1, bar.get_y()+bar.get_height()/2, str(val), va='center', fontsize=10, fontweight='bold', color='#2c3e50')
ax.set_xlim(0, 110)
ax.set_xlabel('Frequency (Last 5 Years)', fontsize=11, color='#555')
ax.set_title('Gaokao Essay: High-Frequency Topics', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='y', labelsize=9)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_topic_dist.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_topic_dist.svg")
