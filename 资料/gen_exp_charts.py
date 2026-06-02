"""中考经验 · 图表生成"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12

OUT = r'C:\Users\21342\Desktop\sixian-edu\资料\charts'
C1, C2, C3, C4, C5 = '#D18080','#C46565','#E8A060','#73BFAA','#5688CC'

def save(name):
    plt.tight_layout()
    plt.savefig(f'{OUT}/{name}.svg',bbox_inches='tight',dpi=150)
    plt.close()
    print(f'  OK {name}.svg')

# ── 1. 往届考生各科提分数据 ──
def chart_score_improvement():
    subjects = ['语文','数学','英语','物理','化学','历史/道法']
    before = [85,72,78,45,32,55]
    after  = [102,98,101,58,42,72]
    x = range(len(subjects))
    fig,ax = plt.subplots(figsize=(7,4))
    b1 = ax.bar([i-0.2 for i in x],before,0.35,color='#D5B0B0',label='冲刺前',edgecolor='white')
    b2 = ax.bar([i+0.2 for i in x],after,0.35,color='#C46565',label='中考成绩',edgecolor='white')
    for i,(bef,aft) in enumerate(zip(before,after)):
        ax.text(i-0.2,bef+1.5,str(bef),ha='center',fontsize=8,color='#999')
        ax.text(i+0.2,aft+1.5,str(aft),ha='center',fontsize=8,fontweight='bold',color='#C46565')
        ax.text(i,aft+5,f'+{aft-bef}',ha='center',fontsize=8,color='#E74C3C',fontweight='bold')
    ax.set_xticks(list(x)); ax.set_xticklabels(subjects,fontsize=10)
    ax.set_ylabel('分数',fontsize=10)
    ax.set_title('往届考生 · 冲刺前后各科提分情况',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9)
    ax.set_ylim(0,120)
    save('score_improvement')

# ── 2. 常见失分原因统计 ──
def chart_common_mistakes():
    reasons = ['计算失误','审题不清','知识点漏洞','时间不够','心态紧张','规范扣分','其他']
    pcts = [25,20,18,13,12,8,4]
    colors = ['#E74C3C','#E67E22','#F39C12','#3498DB','#9B59B6','#95A5A6','#BDC3C7']
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    bars = ax.barh(reasons,pcts,color=colors,edgecolor='white',height=0.6)
    for bar,p in zip(bars,pcts):
        ax.text(bar.get_width()+0.3,bar.get_y()+bar.get_height()/2,f'{p}%',va='center',fontsize=10,fontweight='bold',color='#555')
    ax.set_xlim(0,35)
    ax.set_xlabel('占比 (%)',fontsize=10)
    ax.set_title('过来人总结 · 中考常见失分原因',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=10)
    save('common_mistakes')

# ── 3. 各科复习时间有效利用率 ──
def chart_time_usage():
    subjects = ['数学','物理','化学','英语','语文','历史/道法']
    planned = [22,14,12,17,18,17]
    actual  = [20,12,10,15,16,14]
    efficiency = [round(a/p*100) for a,p in zip(actual,planned)]
    x = range(len(subjects))
    fig,ax1 = plt.subplots(figsize=(6.5,3.5))
    b1 = ax1.bar([i-0.2 for i in x],planned,0.35,color='#D5B0B0',label='计划时间',edgecolor='white')
    b2 = ax1.bar([i+0.2 for i in x],actual,0.35,color='#73BFAA',label='实际有效',edgecolor='white')
    for i,(ef,pl) in enumerate(zip(efficiency,planned)):
        ax1.text(i,pl+2,f'{ef}%',ha='center',fontsize=8,color='#27AE60',fontweight='bold')
    ax1.set_xticks(list(x)); ax1.set_xticklabels(subjects,fontsize=10)
    ax1.set_ylabel('占比 (%)',fontsize=10)
    ax1.set_title('各科复习时间 · 计划 vs 实际有效利用',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax1.spines['top'].set_visible(False); ax1.spines['right'].set_visible(False)
    ax1.legend(fontsize=9,loc='upper right')
    ax1.set_ylim(0,30)
    save('time_usage')

# ── 4. 逆袭案例成绩变化 ──
def chart_comeback():
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    stages = ['一模','二模','三模','中考']
    student1 = [380,410,445,488]
    student2 = [350,390,420,465]
    student3 = [410,430,455,492]
    ax.plot(stages,student1,'o-',color='#D18080',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#D18080')
    ax.plot(stages,student2,'s-',color='#E8A060',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#E8A060')
    ax.plot(stages,student3,'^-',color='#73BFAA',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#73BFAA')
    ax.set_ylabel('总分',fontsize=10)
    ax.set_title('往届考生逆袭案例 · 成绩变化轨迹',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True,alpha=0.25,axis='y')
    ax.legend(['案例A（+108分）','案例B（+115分）','案例C（+82分）'],fontsize=8,loc='lower right')
    ax.fill_between(range(4),340,500,where=(np.array(range(4))>=2),alpha=0.05,color='#E8A060')
    ax.text(2.5,345,'冲刺\n阶段',fontsize=7,color='#E8A060',ha='center')
    save('comeback')

# ── 5. 考前30天心态变化 ──
def chart_exam_mood():
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    days = list(range(30,0,-1))
    confidence = np.clip(40 + 20*np.sin(np.linspace(0,3*np.pi,30)) + np.linspace(-5,10,30), 25, 80)
    anxiety = np.clip(60 - 15*np.sin(np.linspace(0,3*np.pi,30)) + np.linspace(10,-10,30), 20, 85)
    ax.fill_between(days,confidence,anxiety,alpha=0.08,color='#D18080')
    ax.plot(days,confidence,'-',color='#27AE60',lw=2.5,label='自信心')
    ax.plot(days,anxiety,'-',color='#E74C3C',lw=2.5,label='焦虑感')
    ax.axvline(x=7,color='#E8A060',ls='--',lw=1,alpha=0.6)
    ax.text(7.5,10,'考前一周\n关键转折',fontsize=7.5,color='#E8A060')
    ax.set_xlabel('距离中考（天）',fontsize=10); ax.set_ylabel('程度',fontsize=10)
    ax.set_title('过来人自述 · 考前30天信心与焦虑波动',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9,loc='upper left')
    ax.set_xlim(30,1)
    save('exam_mood')

# ── 6. 考场时间分配经验 ──
def chart_exam_timing():
    subjects = ['语文\n120min','数学\n120min','英语\n100min','物理\n70min','化学\n50min']
    ratios = [
        [15,35,20,20,5,25],
        [20,15,20,25,15,25],
        [20,25,20,15,10,10],
        [10,25,15,10,5,5],
        [10,20,10,5,3,2],
    ]
    labels = ['审题','基础题','中档题','压轴题','检查','机动']
    colors = ['#95A5A6','#73BFAA','#E8A060','#D18080','#3498DB','#BDC3C7']
    fig,ax = plt.subplots(figsize=(7,4))
    bottom = np.zeros(5)
    for i,label in enumerate(labels):
        vals = [r[i] for r in ratios]
        bars = ax.barh(subjects,vals,left=bottom,color=colors[i],label=label,height=0.5,edgecolor='white')
        bottom += vals
    for j,subj in enumerate(subjects):
        cum = 0
        for i in range(len(labels)):
            v = ratios[j][i]
            if v > 5:
                ax.text(cum+v/2,j,str(v)+'%',ha='center',va='center',fontsize=7,color='white',fontweight='bold')
            cum += v
    ax.set_title('过来人经验 · 考场时间分配建议',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.legend(fontsize=8,loc='lower right',ncol=3)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    save('exam_timing')

# ── 7. 备考资源使用情况 ──
def chart_resource_usage():
    resources = ['真题试卷','错题本','教材课本','参考书','网课视频','APP刷题']
    usage = [95,88,75,62,48,35]
    help_rating = [92,90,65,55,50,40]
    y = range(len(resources))
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    b1 = ax.barh([i+0.15 for i in y],usage,0.3,color='#D18080',label='使用率%',edgecolor='white')
    b2 = ax.barh([i-0.15 for i in y],help_rating,0.3,color='#73BFAA',label='认为有用%',edgecolor='white')
    for i,u,h in zip(y,usage,help_rating):
        ax.text(u+1,i+0.15,f'{u}%',va='center',fontsize=7.5,color='#C46565',fontweight='bold')
        ax.text(h+1,i-0.15,f'{h}%',va='center',fontsize=7.5,color='#27AE60',fontweight='bold')
    ax.set_yticks(list(y)); ax.set_yticklabels(resources,fontsize=9)
    ax.set_xlim(0,110)
    ax.set_title('往届生 · 备考资源使用率与评价',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9,loc='lower right')
    save('resource_usage')

# ── 8. 每日效率时段分布 ──
def chart_daily_efficiency():
    hours = list(range(6,23))
    efficiency = [20,40,65,85,92,78,60,55,75,88,82,60,45,50,70,80,60]
    fig,ax = plt.subplots(figsize=(7,3.5))
    colors = ['#95A5A6']*3 + ['#E8A060']*2 + ['#D18080']*2 + ['#95A5A6'] + ['#E8A060']*3 + ['#D18080']*2 + ['#95A5A6']*4
    bars = ax.bar(hours,efficiency,color=colors,width=0.7,edgecolor='white')
    ax.axvline(x=12.5,color='#999',ls='--',lw=0.8,alpha=0.4)
    ax.axvline(x=14,color='#999',ls='--',lw=0.8,alpha=0.4)
    ax.text(13.25,93,'午休',fontsize=8,color='#999',ha='center')
    ax.set_xlabel('时间',fontsize=10); ax.set_ylabel('学习效率 (%)',fontsize=10)
    ax.set_title('过来人经验 · 各时段学习效率分布',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.set_xticks(list(range(6,23)))
    ax.set_xticklabels([f'{h}:00' for h in range(6,23)],fontsize=7,rotation=30)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.set_ylim(0,100)
    ax.text(7,3,'早读黄金期',fontsize=7.5,color='#E8A060')
    ax.text(16.5,3,'下午低谷',fontsize=7.5,color='#95A5A6')
    ax.text(19.5,3,'晚自习高效期',fontsize=7.5,color='#D18080')
    save('daily_efficiency')

# ── 9. 模拟考 vs 中考对比 ──
def chart_mock_vs_real():
    subjects = ['语文','数学','英语','物理','化学','历史/道法','总分']
    mock_avg = [95,88,92,52,38,65,430]
    exam_avg = [98,92,95,55,41,68,449]
    x = range(len(subjects))
    fig,ax = plt.subplots(figsize=(7,4))
    b1 = ax.bar([i-0.3 for i in x],mock_avg,0.3,color='#D5B0B0',label='模拟考均分',edgecolor='white')
    b2 = ax.bar([i+0.3 for i in x],exam_avg,0.3,color='#C46565',label='中考均分',edgecolor='white')
    for i,(m,e) in enumerate(zip(mock_avg,exam_avg)):
        if i < 6:
            diff = e - m
            ax.text(i,e+1.5,f'+{diff}' if diff>0 else f'{diff}',ha='center',fontsize=8,fontweight='bold',color='#27AE60' if diff>0 else '#E74C3C')
    # secondary y-axis for total
    ax.set_xticks(list(x)); ax.set_xticklabels(subjects,fontsize=9)
    ax.set_ylabel('各科分数',fontsize=10)
    ax.set_title('模拟考均分 vs 中考均分 · 往届数据',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9,loc='upper left')
    ax.set_ylim(0,105)
    save('mock_vs_real')

# ── 10. 各科难度与信心评价 ──
def chart_subject_difficulty():
    subjects = ['数学','物理','化学','英语','语文','历史/道法']
    difficulty = [85,75,65,55,40,35]
    confidence = [45,50,55,60,75,80]
    x = range(len(subjects))
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    ax.plot(x,difficulty,'o-',color='#E74C3C',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#E74C3C',label='认为难度大%')
    ax.plot(x,confidence,'s-',color='#27AE60',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#27AE60',label='有信心考好%')
    ax.fill_between(x,difficulty,confidence,alpha=0.06,color='#D18080')
    for i,(d,c) in enumerate(zip(difficulty,confidence)):
        ax.text(i,d+3,f'{d}%',ha='center',fontsize=8,color='#E74C3C',fontweight='bold')
        ax.text(i,c+3,f'{c}%',ha='center',fontsize=8,color='#27AE60',fontweight='bold')
    ax.set_xticks(list(x)); ax.set_xticklabels(subjects,fontsize=10)
    ax.set_ylim(0,100)
    ax.set_ylabel('比例 (%)',fontsize=10)
    ax.set_title('往届生评价 · 各科难度 vs 信心',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9)
    ax.grid(True,alpha=0.2,axis='y')
    save('subject_difficulty')

if __name__ == '__main__':
    import os; os.makedirs(OUT,exist_ok=True)
    print('Generating 中考经验 charts...')
    chart_score_improvement()
    chart_common_mistakes()
    chart_time_usage()
    chart_comeback()
    chart_exam_mood()
    chart_exam_timing()
    chart_resource_usage()
    chart_daily_efficiency()
    chart_mock_vs_real()
    chart_subject_difficulty()
    print('Done!')
