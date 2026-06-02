import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

# ─── Chart 1: 高考阅读理解题型分布饼图 ───
fig, ax = plt.subplots(figsize=(6.5, 4.5))
types = ['Detail\nComprehension', 'Inference\nJudgment', 'Main\nIdea', 'Word\nGuessing', 'Attitude\nTone']
sizes = [35, 28, 18, 12, 7]
colors = ['#2980b9','#e74c3c','#27ae60','#f39c12','#9b59b6']
explode = (0.03, 0.03, 0.03, 0.03, 0.03)
wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=types, colors=colors,
                                   autopct='%1.0f%%', startangle=140, pctdistance=0.55,
                                   textprops={'fontsize': 9, 'fontweight': 'bold'})
for t in autotexts:
    t.set_color('white')
    t.set_fontsize(10)
ax.set_title('Gaokao Reading Comprehension: Question Type Distribution', fontsize=15, fontweight='bold', color='#2c3e50', pad=15)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_reading_types.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_reading_types.svg")

# ─── Chart 2: 阅读速度与理解率关系曲线 ───
fig, ax = plt.subplots(figsize=(7, 4.5))
speed = np.array([40, 60, 80, 100, 120, 140, 160, 180, 200, 220])
comprehension = np.array([98, 96, 92, 88, 82, 74, 62, 48, 32, 18])
ax.plot(speed, comprehension, 'o-', color='#2980b9', linewidth=2.5, markersize=7, zorder=3)
ax.fill_between(speed, comprehension, 0, alpha=0.08, color='#2980b9')
ax.axvspan(70, 110, alpha=0.12, color='#27ae60')
ax.annotate('Recommended Zone\n= 80-100 wpm\nComprehension >= 85%', xy=(90, 62), fontsize=10,
            fontweight='bold', color='#27ae60', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#e6f7e6', edgecolor='#27ae60', alpha=0.9))
ax.set_xlabel('Reading Speed (words/min)', fontsize=11, color='#555')
ax.set_ylabel('Comprehension Rate (%)', fontsize=11, color='#555')
ax.set_title('Reading Speed vs Comprehension Rate', fontsize=14, fontweight='bold', color='#2c3e50', pad=10)
ax.set_ylim(0, 105)
ax.set_xlim(30, 230)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(alpha=0.15)
plt.tight_layout()
plt.savefig('charts/gaokao_eng_speed_vs_comp.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_speed_vs_comp.svg")

# ─── Chart 3: 七选五解题策略流程图 ───
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')

steps = [
    ('Step 1\nRead whole text\nget the gist', '#2980b9'),
    ('Step 2\nAnalyze options\nfind keywords', '#3498db'),
    ('Step 3\nLocate gaps\ncheck logic', '#5dade2'),
    ('Step 4\nVerify & eliminate\noptions', '#85c1e9'),
]
for i, (text, color) in enumerate(steps):
    x = i * 2.8 + 0.3
    rect = FancyBboxPatch((x, 2.2), 2.2, 1.5, boxstyle="round,pad=0.12",
                          facecolor=color, edgecolor='white', alpha=0.9)
    ax.add_patch(rect)
    ax.text(x+1.1, 2.95, text, ha='center', va='center', fontsize=9, fontweight='bold', color='white',
            linespacing=1.4)
    if i < len(steps)-1:
        ax.annotate('', xy=(x+2.5, 2.95), xytext=(x+2.2, 2.95),
                    arrowprops=dict(arrowstyle='->', color='#2980b9', lw=2))

tips = [
    ('KEY: Transition words', 'but, however,\nthough, yet', 0.5),
    ('KEY: Cause-effect', 'because, so,\ntherefore, thus', 3.3),
    ('KEY: Addition', 'besides, moreover,\nfurthermore', 6.1),
    ('KEY: Pronouns', 'it, they, this,\nsuch, one', 8.9),
]
for label, detail, x in tips:
    ax.text(x+0.1, 0.6, label, fontsize=9, fontweight='bold', color='#e74c3c')
    ax.text(x+0.1, 0.2, detail, fontsize=7.5, color='#666')
    ax.plot([x+0.8, x+0.8], [1.0, 2.2], ':', color='#2980b9', alpha=0.4, lw=1)

ax.text(5.5, 3.75, '7-choose-5: Four-Step Strategy', fontsize=14, fontweight='bold', color='#2c3e50',
        ha='center', va='bottom')
plt.savefig('charts/gaokao_eng_7choose5_flow.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_7choose5_flow.svg")

# ─── Chart 4: 长难句分析结构分解 ───
fig, ax = plt.subplots(figsize=(8, 2.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

ax.text(5, 2.6, 'The research, which has been conducted over the past decade,', fontsize=12,
        color='#2c3e50', ha='center', fontweight='bold')
ax.text(5, 2.2, 'suggests that the key to success lies not in talent alone', fontsize=12,
        color='#2c3e50', ha='center', fontweight='bold')
ax.text(5, 1.8, 'but in persistent effort and effective strategies.', fontsize=12,
        color='#2c3e50', ha='center', fontweight='bold')

parts = [
    ('The research', 'Subject (S)', 1.0, '#e74c3c'),
    ('which has been conducted...', 'Attributive clause', 3.2, '#2980b9'),
    ('suggests', 'Predicate (V)', 6.5, '#27ae60'),
    ('that the key lies...', 'Object clause (O)', 8.0, '#f39c12'),
]
for text, label, x, color in parts:
    ax.plot([x, x], [0.3, 1.5], ':', color=color, alpha=0.5, lw=1.5)
    ax.text(x, 1.2, text, ha='center', fontsize=8.5, fontweight='bold', color=color,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.8))
    ax.text(x, 0.4, label, ha='center', fontsize=7.5, color=color, fontweight='bold')

ax.text(5, 0.05, 'Sentence core: The research + suggests + that... (SVO structure with attributive clause inserted)',
        fontsize=9, color='#888', ha='center', style='italic')
plt.savefig('charts/gaokao_eng_sentence_analysis.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_sentence_analysis.svg")

# ─── Chart 5: 推理判断题解题框架 ───
fig, ax = plt.subplots(figsize=(7, 4))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')

types_data = [
    ('Explicit Inference\nSurface level', '#2980b9', 0.3, 3.5),
    ('Implicit Inference\nDeep meaning', '#e74c3c', 2.8, 3.5),
    ('Prediction\nNext step', '#27ae60', 5.3, 3.5),
]
for text, color, x, y in types_data:
    rect = FancyBboxPatch((x, y), 2.2, 0.9, boxstyle="round,pad=0.12",
                          facecolor=color, edgecolor='white', alpha=0.85)
    ax.add_patch(rect)
    ax.text(x+1.1, y+0.45, text, ha='center', va='center', fontsize=9, fontweight='bold', color='white',
            linespacing=1.3)

methods = [
    ('Locate Evidence', 'Find relevant\nsentences in text', 0.5, 1.8),
    ('Read Between Lines', 'Understand author\ntrue intention', 3.0, 1.8),
    ('Eliminate', 'Remove absolute/unrelated\n/reversed options', 5.5, 1.8),
]
for text, desc, x, y in methods:
    ax.text(x+0.1, y+0.6, '* '+text, fontsize=9, fontweight='bold', color='#2c3e50')
    ax.text(x+0.1, y+0.1, desc, fontsize=8, color='#666')
    ax.plot([x+1.0, x+1.0], [y+1.2, y+1.7], ':', color='#888', alpha=0.4)

for x_mid in [1.4, 3.9, 6.4]:
    ax.plot([x_mid, x_mid], [2.9, 3.5], '-', color='#ccc', lw=1)

ax.text(4, 4.7, 'Inference Questions: Problem-Solving Framework', fontsize=14, fontweight='bold', color='#2c3e50', ha='center')

ax.text(4, 0.3, 'Correct inference answer = reasonable deduction from text, NOT word-for-word from original', fontsize=9, color='#e74c3c', ha='center',
        fontweight='bold')
plt.savefig('charts/gaokao_eng_inference.svg', bbox_inches='tight', dpi=150)
plt.close()
print("OK gaokao_eng_inference.svg")
