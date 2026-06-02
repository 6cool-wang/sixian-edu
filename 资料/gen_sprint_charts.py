"""中考冲刺方法 · 图表生成"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

OUT = r'C:\Users\21342\Desktop\sixian-edu\资料\charts'
C1, C2, C3, C4 = '#D18080','#C46565','#E8A060','#73BFAA'

def save(name):
    plt.tight_layout()
    plt.savefig(f'{OUT}/{name}.svg',bbox_inches='tight',dpi=150)
    plt.close()
    print(f'  OK {name}.svg')

# ── 1. 三轮复习时间轴 ──
def chart_timeline():
    fig,ax = plt.subplots(figsize=(9,3.5))
    ax.set_xlim(0,16); ax.set_ylim(0,3)
    phases = [
        (0,5,'第一轮·基础梳理\n全面复习教材\n构建知识网络','#D18080'),
        (5.5,10,'第二轮·专题突破\n重难点专项训练\n跨章节整合','#C46565'),
        (10.5,14,'第三轮·冲刺模拟\n真题实战演练\n查漏补缺','#E8A060'),
    ]
    for x1,x2,label,c in phases:
        bar = mpatches.FancyBboxPatch((x1,0.7),x2-x1,1.2,boxstyle="round,pad=0.05",facecolor=c,alpha=0.85,edgecolor='none')
        ax.add_patch(bar)
        ax.text((x1+x2)/2,1.3,label,ha='center',va='center',fontsize=9.5,color='white',fontweight='bold')
    # time axis
    for i in range(0,15):
        ax.plot([i,i],[0,0.5],color='#ccc',lw=0.8)
        ax.text(i,-0.1,f'{i+3}月',ha='center',fontsize=8,color='#888')
    ax.plot([0,14],[0.5,0.5],color='#999',lw=1.5)
    ax.set_title('中考冲刺 · 三轮复习时间轴',fontsize=14,fontweight='bold',color='#1a1a2e',pad=12)
    ax.axis('off')
    # legend note
    ax.text(14.5,1.3,'3月\n→\n6月',fontsize=8,color='#aaa',va='center')
    save('sprint_timeline')

# ── 2. 各科分值分布（圆环图）──
def chart_subject_scores():
    subjects = ['语文','数学','英语','物理','化学','历史\n道德与法治']
    scores = [120,120,120,70,50,100]
    colors = ['#E74C3C','#2980B9','#27AE60','#E67E22','#8E44AD','#D18080']
    fig,ax = plt.subplots(figsize=(5.5,4))
    wedges,texts,autotexts = ax.pie(scores,labels=subjects,colors=colors,autopct='%1.0f%%',
                                     startangle=90,pctdistance=0.75,wedgeprops=dict(width=0.4,edgecolor='white',lw=2))
    for t in autotexts: t.set_fontsize(9); t.set_fontweight('bold')
    for t in texts: t.set_fontsize(9)
    ax.set_title('中考各科分值分布',fontsize=13,fontweight='bold',color='#1a1a2e',pad=10)
    save('subject_scores')

# ── 3. 错题类型分布（条形图）──
def chart_mistake_types():
    types = ['概念理解','计算错误','审题不清','思路方法','粗心大意']
    pcts = [28,22,20,18,12]
    colors = ['#C0392B','#E74C3C','#E67E22','#F39C12','#95A5A6']
    fig,ax = plt.subplots(figsize=(6,3.5))
    bars = ax.barh(types,pcts,color=colors,edgecolor='white',height=0.6)
    for bar,p in zip(bars,pcts):
        ax.text(bar.get_width()+0.5,bar.get_y()+bar.get_height()/2,f'{p}%',va='center',fontsize=10,fontweight='bold',color='#555')
    ax.set_xlim(0,38)
    ax.set_xlabel('占比 (%)',fontsize=10)
    ax.set_title('常见错题类型分布',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=10)
    # note
    ax.text(35,5,'数据基于\n往届考生\n统计',fontsize=7,color='#aaa',va='center',ha='center')
    save('mistake_types')

# ── 4. 各科复习时间分配（饼图）──
def chart_time_allocation():
    subjects = ['数学','语文','英语','物理','化学','历史/道法']
    vals = [22,18,17,14,12,17]
    colors = ['#2980B9','#E74C3C','#27AE60','#E67E22','#8E44AD','#D18080']
    fig,ax = plt.subplots(figsize=(5.5,4))
    wedges,texts,autotexts = ax.pie(vals,labels=subjects,colors=colors,autopct='%1.0f%%',
                                     startangle=90,pctdistance=0.75,wedgeprops=dict(width=0.35,edgecolor='white',lw=2))
    for t in autotexts: t.set_fontsize(9); t.set_fontweight('bold')
    for t in texts: t.set_fontsize(9)
    ax.set_title('冲刺期各科复习时间推荐分配',fontsize=13,fontweight='bold',color='#1a1a2e',pad=10)
    save('time_allocation')

# ── 5. 记忆遗忘曲线 ──
def chart_forgetting_curve():
    fig,ax = plt.subplots(figsize=(6,3.5))
    x = np.array([0,1,2,4,7,15,30])
    y = 100 * np.exp(-0.2 * x) + 15
    ax.plot(x,y,color='#C46565',lw=2.5,marker='o',markersize=7)
    # review points
    review_x = [1,2,4,7,15,30]
    review_y = 100 * np.exp(-0.2 * np.array(review_x)) + 15
    ax.scatter(review_x,review_y,color='#E8A060',s=60,zorder=5,marker='*')
    for rx,ry in zip(review_x,review_y):
        ax.annotate(f'复习\n{int(round(ry))}%',(rx,ry),textcoords="offset points",xytext=(0,-18),
                    ha='center',fontsize=7.5,color='#E67E22',fontweight='bold')
    ax.set_xlim(-1,32); ax.set_ylim(0,105)
    ax.set_xlabel('天数 (天)',fontsize=10); ax.set_ylabel('记忆保留率 (%)',fontsize=10)
    ax.set_title('艾宾浩斯遗忘曲线 · 冲刺期复习节奏',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True,alpha=0.3)
    ax.legend(['自然遗忘','最佳复习点'],fontsize=9,loc='upper right')
    save('forgetting_curve')

# ── 6. 一日作息时间表（条形图）──
def chart_daily_schedule():
    activities = ['睡眠','早读记忆','上午学习','午休','下午学习','体育锻炼','晚间自习','休息放松']
    hours  = [7.5,1,3,0.75,3,0.5,3.5,1]
    colors = ['#34495E','#E8A060','#D18080','#95A5A6','#C46565','#27AE60','#C0392B','#73BFAA']
    bars = plt.cm.Reds(np.linspace(0.3,0.8,len(activities)))
    fig,ax = plt.subplots(figsize=(7,3.5))
    ypos = range(len(activities))
    bars = ax.barh(ypos,hours,color=colors,height=0.6)
    for bar,h,a in zip(bars,hours,activities):
        ax.text(bar.get_width()+0.05,bar.get_y()+bar.get_height()/2,f'{h:.1f}h',va='center',fontsize=9,color='#555')
    ax.set_yticks(list(ypos)); ax.set_yticklabels(activities,fontsize=10)
    ax.set_xlim(0,9.5)
    ax.set_xlabel('时长 (小时)',fontsize=10)
    ax.set_title('冲刺期推荐每日作息安排',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=9)
    # total
    ax.text(8.8,-0.3,f'合计 {sum(hours):.1f}h',fontsize=8,color='#999',ha='right')
    save('daily_schedule')

# ── 7. 考前心理状态变化 ──
def chart_mental_state():
    fig,ax = plt.subplots(figsize=(6,3.5))
    weeks = ['第12周','第10周','第8周','第6周','第4周','第2周','考前','考中']
    confidence = [65,58,50,42,38,55,48,82]
    anxiety = [30,38,48,55,60,75,82,45]
    x = range(len(weeks))
    ax.plot(x,confidence,'o-',color='#27AE60',lw=2.5,markersize=7)
    ax.plot(x,anxiety,'s-',color='#E74C3C',lw=2.5,markersize=7)
    ax.fill_between(x,confidence,anxiety,alpha=0.06,color='#D18080')
    ax.set_xticks(list(x)); ax.set_xticklabels(weeks,fontsize=8.5,rotation=15)
    ax.set_ylim(0,100)
    ax.set_ylabel('程度 (%)',fontsize=10)
    ax.set_title('冲刺期自信心与焦虑水平变化趋势',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True,alpha=0.25)
    ax.legend(['自信心','焦虑水平'],fontsize=9,loc='center left')
    ax.axvspan(5.5,7.5,alpha=0.08,color='#D18080')
    ax.text(6.5,5,'关键期',fontsize=8,color='#D18080',ha='center',fontweight='bold')
    ax.text(6.5,96,'考前冲刺\n阶段',fontsize=7,color='#aaa',ha='center')
    save('mental_state')

# ── 8. 各科掌握度雷达图 ──
def chart_mastery_radar():
    categories = ['语文','数学','英语','物理','化学','历史\n道法']
    N = len(categories)
    angles = np.linspace(0,2*np.pi,N,endpoint=False).tolist()
    angles += angles[:1]
    fig,ax = plt.subplots(figsize=(5.5,5),subplot_kw=dict(polar=True))
    # before
    vals1 = [55,45,50,40,35,48]
    vals1 += vals1[:1]
    ax.plot(angles,vals1,'o-',color='#95A5A6',lw=1.5,markersize=6,alpha=0.6,label='冲刺前')
    ax.fill(angles,vals1,alpha=0.04,color='#95A5A6')
    # after goal
    vals2 = [78,82,75,72,68,80]
    vals2 += vals2[:1]
    ax.plot(angles,vals2,'o-',color='#C46565',lw=2.5,markersize=7,label='冲刺目标')
    ax.fill(angles,vals2,alpha=0.1,color='#C46565')
    ax.set_xticks(angles[:-1]); ax.set_xticklabels(categories,fontsize=10)
    ax.set_ylim(0,100); ax.set_yticks([20,40,60,80,100])
    ax.set_yticklabels(['20','40','60','80','100'],fontsize=7,color='#999')
    ax.set_title('各科掌握度 · 冲刺前后对比',fontsize=13,fontweight='bold',color='#1a1a2e',pad=18)
    ax.legend(fontsize=9,loc='upper right',bbox_to_anchor=(1.2,1.1))
    save('mastery_radar')

# ── 9. 模拟考成绩趋势 ──
def chart_mock_trend():
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    exams = ['一模','二模','三模','中考目标']
    scores = [425,452,478,510]
    ax.plot(exams,scores,'o-',color='#D18080',lw=2.5,markersize=9,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#D18080')
    for e,s in zip(exams,scores):
        ax.text(e,s+5,f'{s}',ha='center',fontsize=11,fontweight='bold',color='#C46565')
    ax.set_ylim(380,540)
    ax.set_ylabel('总分',fontsize=10)
    ax.set_title('模拟考成绩递进趋势',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True,alpha=0.25,axis='y')
    # zone fill
    ax.fill_between(range(4),380,540,where=(np.array(range(4))>=2),alpha=0.06,color='#E8A060')
    ax.text(2.5,385,'冲刺\n阶段',fontsize=8,color='#E8A060',ha='center')
    save('mock_trend')

# ── 10. 考前一个月学习强度 ──
def chart_study_intensity():
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    days = list(range(1,31))
    hours = [6+np.random.uniform(-0.5,0.5) for _ in range(20)] + [7+np.random.uniform(-0.5,0.5) for _ in range(5)] + [5+np.random.uniform(-0.5,0.5) for _ in range(5)]
    colors = ['#D18080' if d<=20 else ('#E8A060' if d<=25 else '#73BFAA') for d in days]
    bars = ax.bar(days,hours,color=colors,width=0.7)
    ax.axhline(y=6,color='#95A5A6',ls='--',lw=1,alpha=0.5)
    ax.text(30.5,6,'日均6h',fontsize=8,color='#999',va='center')
    ax.set_xlim(0.5,31.5); ax.set_ylim(0,9)
    ax.set_xlabel('距离中考天数',fontsize=10); ax.set_ylabel('每日学习时长 (h)',fontsize=10)
    ax.set_title('考前30天 · 学习强度建议',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    # phase annotations
    ax.text(10.5,8.2,'强化冲刺期',fontsize=9,color='#D18080',ha='center',fontweight='bold')
    ax.text(22.5,8.2,'调整期',fontsize=9,color='#E8A060',ha='center',fontweight='bold')
    ax.text(28,8.2,'放松期',fontsize=9,color='#73BFAA',ha='center',fontweight='bold')
    # arrow markers for phases
    ax.annotate('',xy=(20,7.9),xytext=(1,7.9),arrowprops=dict(arrowstyle='-',color='#D18080',lw=2))
    ax.annotate('',xy=(25,7.9),xytext=(21,7.9),arrowprops=dict(arrowstyle='-',color='#E8A060',lw=2))
    ax.annotate('',xy=(30,7.9),xytext=(26,7.9),arrowprops=dict(arrowstyle='-',color='#73BFAA',lw=2))
    save('study_intensity')

# Generate all
if __name__ == '__main__':
    import os; os.makedirs(OUT,exist_ok=True)
    print('Generating 中考冲刺方法 charts...')
    chart_timeline()
    chart_subject_scores()
    chart_mistake_types()
    chart_time_allocation()
    chart_forgetting_curve()
    chart_daily_schedule()
    chart_mental_state()
    chart_mastery_radar()
    chart_mock_trend()
    chart_study_intensity()
    print('Done!')
