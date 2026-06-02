"""中考时间规划 · 图表生成"""
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

# ── 1. 初三全年时间轴 ──
def chart_year_timeline():
    fig,ax = plt.subplots(figsize=(10,3.8))
    ax.set_xlim(0,12); ax.set_ylim(0,3.5)
    phases = [
        (0,2,'9-10月\n新课收尾+基础铺垫\n适应复习节奏','#5688CC','新课收尾期'),
        (2,5,'11-1月\n一轮基础复习\n构建知识框架','#73BFAA','一轮复习'),
        (5,7,'1-2月\n寒假逆袭期\n专项突破+弱科补漏','#E8A060','寒假黄金期'),
        (7,9.5,'3-5月\n二轮专题+三轮模拟\n真题实战+查漏补缺','#C46565','冲刺期'),
        (9.5,11,'5-6月\n考前调整+回归基础\n心态调适+状态保持','#D18080','考前调整期'),
        (11,12,'6月\n中考!','#E74C3C','中考'),
    ]
    for x1,x2,label,c,title in phases:
        h = 0.9
        y = 1.5
        bar = mpatches.FancyBboxPatch((x1,y),x2-x1,h,boxstyle="round,pad=0.05",facecolor=c,alpha=0.8,edgecolor='none')
        ax.add_patch(bar)
        ax.text((x1+x2)/2,y+h/2,label,ha='center',va='center',fontsize=7.5,color='white',fontweight='bold')
        # marker
        ax.plot([(x1+x2)/2],[y-0.2],'v',color=c,markersize=6,alpha=0.5)
    # time axis
    months = ['9月','10月','11月','12月','1月','2月','3月','4月','5月','6月']
    for i in range(10):
        ax.plot([i,i],[0.6,0.9],color='#ccc',lw=0.8)
        ax.text(i,0.3,months[i],ha='center',fontsize=8,color='#888')
    ax.plot([0,9],[0.9,0.9],color='#999',lw=1.5)
    ax.set_title('初三全年复习时间轴 · 从9月到中考',fontsize=14,fontweight='bold',color='#1a1a2e',pad=10)
    ax.axis('off')
    # avg score annotation
    ax.text(9.5,2.4,'注：以上为\n通用时间线\n具体根据\n学校进度\n灵活调整',fontsize=6.5,color='#aaa',va='center')
    save('year_timeline')

# ── 2. 各阶段学习重点与强度 ──
def chart_phase_intensity():
    phases = ['新课收尾\n9-10月','一轮复习\n11-1月','寒假\n1-2月','二轮专题\n3-4月','三轮模拟\n4-5月','考前调整\n5-6月']
    intensity = [3,4.5,6,5.5,5,3.5]
    focus_breadth = [4,5,3,3,2,1.5]
    x = range(len(phases))
    fig,ax1 = plt.subplots(figsize=(7,3.8))
    b1 = ax1.bar(x,intensity,0.4,color='#D18080',label='学习强度',edgecolor='white')
    for i,v in enumerate(intensity):
        ax1.text(i,v+0.1,f'{"★"*int(v)}{"☆"*(6-int(v))}',ha='center',fontsize=7,color='#C46565')
    ax1.set_xticks(list(x)); ax1.set_xticklabels(phases,fontsize=8.5)
    ax1.set_ylabel('强度（1-6）',fontsize=10); ax1.set_ylim(0,7)
    ax1.set_title('各阶段学习强度与复习广度变化',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax1.spines['top'].set_visible(False); ax1.spines['right'].set_visible(False)
    # second axis
    ax2 = ax1.twinx()
    ax2.plot(x,focus_breadth,'o-',color='#5688CC',lw=2.5,markersize=8,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#5688CC')
    for i,v in enumerate(focus_breadth):
        ax2.text(i,v+0.15,f'{v:.1f}',ha='center',fontsize=8,color='#5688CC',fontweight='bold')
    ax2.set_ylabel('复习广度',fontsize=10)
    ax2.set_ylim(0,7)
    ax1.legend(fontsize=8,loc='upper left')
    ax2.legend(['复习广度'],fontsize=8,loc='upper right')
    save('phase_intensity')

# ── 3. 寒暑假每日时间分配 ──
def chart_holiday_schedule():
    categories = ['学习','睡眠','休息\n娱乐','运动\n锻炼','用餐','其他']
    weekday = [8,7.5,4,1,1.5,2]
    weekend = [5,8,6,1.5,2,1.5]
    holiday = [7,8,4.5,1.5,1.5,1.5]

    x = range(len(categories))
    fig,ax = plt.subplots(figsize=(7,3.8))
    b1 = ax.bar([i-0.3 for i in x],weekday,0.25,color='#5688CC',label='平日',edgecolor='white')
    b2 = ax.bar([i for i in x],weekend,0.25,color='#73BFAA',label='周末',edgecolor='white')
    b3 = ax.bar([i+0.3 for i in x],holiday,0.25,color='#E8A060',label='寒暑假',edgecolor='white')
    ax.set_xticks(list(x)); ax.set_xticklabels(categories,fontsize=9)
    ax.set_ylabel('小时/天',fontsize=10); ax.set_ylim(0,10)
    ax.set_title('不同时段每日时间分配对比',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9)
    ax.text(1.5,-0.7,'寒暑假是"弯道超车"的黄金期——每天多出3-4小时学习时间',fontsize=8,color='#999',ha='center')
    save('holiday_schedule')

# ── 4. 考前100天每周重点 ──
def chart_100days():
    weeks = list(range(14,0,-1))
    focus_areas = []
    for w in range(14,0,-1):
        if w > 10: focus_areas.append('基础梳理')
        elif w > 6: focus_areas.append('专题突破')
        elif w > 3: focus_areas.append('真题模拟')
        else: focus_areas.append('状态调整')
    color_map = {'基础梳理':'#73BFAA','专题突破':'#E8A060','真题模拟':'#C46565','状态调整':'#5688CC'}
    colors = [color_map[f] for f in focus_areas]
    hours = [5.5,6,6,6.5,6.5,7,7,7,7,6.5,6,5.5,5,4.5]

    fig,ax = plt.subplots(figsize=(8,3.8))
    bars = ax.bar(weeks,hours,color=colors,width=0.7,edgecolor='white')
    # annotations on bars
    for i,(w,h,f) in enumerate(zip(weeks,hours,focus_areas)):
        if w % 2 == 0 or w == 14 or w == 1:
            ax.text(w,h+0.2,f'{f}',ha='center',fontsize=7,color='#555',fontweight='bold',rotation=30)

    ax.axvline(x=10.5,color='#999',ls='--',lw=0.8,alpha=0.4)
    ax.axvline(x=6.5,color='#999',ls='--',lw=0.8,alpha=0.4)
    ax.axvline(x=3.5,color='#999',ls='--',lw=0.8,alpha=0.4)
    ax.text(12.25,7.5,'一轮→',fontsize=7,color='#73BFAA',ha='center')
    ax.text(8.5,7.5,'二轮→',fontsize=7,color='#E8A060',ha='center')
    ax.text(5,7.5,'三轮→',fontsize=7,color='#C46565',ha='center')
    ax.text(2,7.5,'调整→',fontsize=7,color='#5688CC',ha='center')

    ax.set_xlabel('距离中考（周）',fontsize=10); ax.set_ylabel('日均学习时长 (h)',fontsize=10)
    ax.set_title('考前100天 · 每周重点与学习强度规划',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.set_xlim(0.5,14.5); ax.set_ylim(0,8.5)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    # legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#73BFAA',label='基础梳理'),
                       Patch(facecolor='#E8A060',label='专题突破'),
                       Patch(facecolor='#C46565',label='真题模拟'),
                       Patch(facecolor='#5688CC',label='状态调整')]
    ax.legend(handles=legend_elements,fontsize=8,loc='upper left',ncol=2)
    ax.set_xticks([14,12,10,8,6,4,2,1])
    ax.set_xticklabels(['14周','12周','10周','8周','6周','4周','2周','1周前'],fontsize=7,rotation=20)
    save('100days')

# ── 5. 周计划模板示例 ──
def chart_weekly_plan():
    days = ['周一','周二','周三','周四','周五','周六','周日']
    subjects = ['数学','物理','化学','英语','语文','文综']
    np.random.seed(42)
    data = np.random.randint(1,4,(len(days),len(subjects)))
    # Make Sunday lighter
    data[-1] = [1,0,1,1,0,1]

    fig,ax = plt.subplots(figsize=(8,4))
    cmap = plt.cm.Reds
    norm = plt.Normalize(0,3)
    for i,day in enumerate(days):
        for j,subj in enumerate(subjects):
            v = data[i,j]
            color = cmap(0.1 + v*0.25) if v > 0 else '#f5f5f5'
            rect = mpatches.FancyBboxPatch((j-0.4,i-0.4),0.8,0.8,boxstyle="round,pad=0.05",facecolor=color,edgecolor='white')
            ax.add_patch(rect)
            if v > 0:
                ax.text(j,i,f'★'*v,ha='center',va='center',fontsize=9,color='white' if v>2 else '#C46565')
    ax.set_xlim(-0.5,len(subjects)-0.5); ax.set_ylim(-0.5,len(days)-0.5)
    ax.set_xticks(range(len(subjects))); ax.set_xticklabels(subjects,fontsize=10)
    ax.set_yticks(range(len(days))); ax.set_yticklabels(days,fontsize=10)
    ax.set_title('周计划模板 · 各科每日学习单元数（★=1单元≈45min）',fontsize=12,fontweight='bold',color='#1a1a2e',pad=10)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0)
    # annotation
    ax.text(2.5,7,'周日安排：\n本周复盘+错题整理\n下周计划+适度放松',ha='center',fontsize=8,color='#999',
            bbox=dict(boxstyle='round,pad=0.3',facecolor='#fcfcfc',edgecolor='#ddd'))
    save('weekly_plan')

# ── 6. 科学作息时间表 ──
def chart_scientific_routine():
    activities = ['晨读记忆\n（黄金记忆期）','上午主攻\n（理科/难题）','午休充电\n（必须休息）','下午复习\n（文科/阅读）','体育锻炼\n（激活身体）','晚间自习\n（整理/错题）','睡前回顾\n（巩固记忆）']
    start_times = [6,8,12.5,14,17,19.5,22]
    durations = [1.5,3.5,1,2.5,0.5,2.5,0.75]
    colors = ['#E8A060','#D18080','#95A5A6','#5688CC','#27AE60','#C46565','#8E44AD']
    fig,ax = plt.subplots(figsize=(8,3.5))
    y_pos = range(len(activities))
    bars = ax.barh(y_pos,durations,left=start_times,color=colors,height=0.55,edgecolor='white')
    for i,(s,d,a) in enumerate(zip(start_times,durations,activities)):
        ax.text(s+d/2,i,f'{int(s)}:00-{int(s+d)}:00\n{d:.1f}h',ha='center',va='center',fontsize=7.5,color='white',fontweight='bold')
    ax.set_yticks(list(y_pos)); ax.set_yticklabels(activities,fontsize=8.5)
    ax.set_xlim(5.5,23.5); ax.set_xlabel('时间',fontsize=10)
    ax.set_title('科学作息时间表 · 基于大脑节律',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.set_xticks([6,8,10,12,14,16,18,20,22])
    ax.set_xticklabels(['6:00','8:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00'],fontsize=7)
    ax.text(23,1.2,'一天\n合计\n约12h',fontsize=7.5,color='#999',va='center')
    save('scientific_routine')

# ── 7. 计划执行率统计 ──
def chart_execution_rate():
    weeks = ['第1周','第2周','第3周','第4周','第5周','第6周','第7周','第8周']
    plan_rate = [85,78,82,75,80,85,88,90]
    actual_rate = [72,68,70,62,71,78,82,86]
    x = range(len(weeks))
    fig,ax = plt.subplots(figsize=(6.5,3.5))
    ax.plot(x,plan_rate,'o-',color='#5688CC',lw=2,markersize=7,label='计划完成率%')
    ax.plot(x,actual_rate,'s-',color='#D18080',lw=2,markersize=7,label='实际执行率%')
    ax.fill_between(x,plan_rate,actual_rate,alpha=0.08,color='#D18080')
    for i,(p,a) in enumerate(zip(plan_rate,actual_rate)):
        ax.text(i,p+2,f'{p}%',ha='center',fontsize=7.5,color='#5688CC')
        ax.text(i,a-4,f'{a}%',ha='center',fontsize=7.5,color='#D18080')
    ax.set_xticks(list(x)); ax.set_xticklabels(weeks,fontsize=8)
    ax.set_ylim(40,100); ax.set_ylabel('百分比',fontsize=10)
    ax.set_title('计划执行率追踪 · 前8周变化趋势',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9); ax.grid(True,alpha=0.2,axis='y')
    ax.axhline(y=80,color='#E8A060',ls='--',lw=0.8,alpha=0.5)
    ax.text(7.5,81,'80%目标线',fontsize=7,color='#E8A060')
    save('execution_rate')

# ── 8. 各月模拟考分数走势 ──
def chart_monthly_scores():
    months = ['9月','10月','11月','12月','1月','3月','4月','5月']
    scores = [380,395,405,410,420,440,455,468]
    avg_line = [450]*len(months)
    fig,ax = plt.subplots(figsize=(7,3.5))
    ax.fill_between(range(len(months)),380,500,where=(np.array(scores)>=450),alpha=0.06,color='#27AE60')
    ax.fill_between(range(len(months)),380,500,where=(np.array(scores)<450),alpha=0.06,color='#E8A060')
    ax.plot(months,scores,'o-',color='#C46565',lw=2.5,markersize=9,markerfacecolor='white',markeredgewidth=2,markeredgecolor='#C46565')
    ax.plot(months,avg_line,'--',color='#95A5A6',lw=1,alpha=0.6)
    for m,s in zip(months,scores):
        ax.text(months.index(m),s+6,f'{s}',ha='center',fontsize=9,fontweight='bold',color='#C46565')
    ax.text(4.5,453,'目标线 450',fontsize=7.5,color='#95A5A6')
    ax.set_ylim(360,500); ax.set_ylabel('总分',fontsize=10)
    ax.set_title('各月模拟考分数追踪 · 让进步可视化',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(True,alpha=0.25,axis='y')
    # phase annotations
    ax.annotate('一轮复习',xy=(0,382),xytext=(2,365),fontsize=8,color='#73BFAA',ha='center',
                arrowprops=dict(arrowstyle='->',color='#73BFAA',lw=1))
    ax.annotate('二轮冲刺',xy=(5,442),xytext=(6.5,430),fontsize=8,color='#D18080',ha='center',
                arrowprops=dict(arrowstyle='->',color='#D18080',lw=1))
    save('monthly_scores')

# ── 9. 各科阶段性重点变化 ──
def chart_subject_focus():
    subjects = ['语文','数学','英语','物理','化学','历史/道法']
    phase1 = [3,3,3,3,3,3]
    phase2 = [3,4,3,4,3,3]
    phase3 = [4,3,3,2,2,4]
    x = range(len(subjects))
    fig,ax = plt.subplots(figsize=(7,3.5))
    b1 = ax.bar([i-0.3 for i in x],phase1,0.25,color='#73BFAA',label='一轮·全面覆盖',edgecolor='white')
    b2 = ax.bar([i for i in x],phase2,0.25,color='#E8A060',label='二轮·重点突破',edgecolor='white')
    b3 = ax.bar([i+0.3 for i in x],phase3,0.25,color='#D18080',label='三轮·查漏补缺',edgecolor='white')
    ax.set_xticks(list(x)); ax.set_xticklabels(subjects,fontsize=9)
    ax.set_ylabel('投入等级（1-5）',fontsize=10); ax.set_ylim(0,5.5)
    ax.set_title('各科在不同阶段的重点投入变化',fontsize=13,fontweight='bold',color='#1a1a2e')
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.legend(fontsize=8,ncol=3,loc='upper right')
    ax.set_yticks([1,2,3,4,5])
    save('subject_focus')

# ── 10. 每日时间块分配 ──
def chart_time_blocks():
    fig,ax = plt.subplots(figsize=(8,2.5))
    ax.set_xlim(0,24); ax.set_ylim(0,2)
    blocks = [
        (6,7,'早读','#E8A060'),
        (7,8,'早餐/上学','#95A5A6'),
        (8,12,'学校课程','#5688CC'),
        (12,13.5,'午餐/午休','#95A5A6'),
        (13.5,17,'学校课程','#5688CC'),
        (17,18,'运动/放松','#27AE60'),
        (18,19,'晚餐','#95A5A6'),
        (19,21.5,'晚间自习','#D18080'),
        (21.5,22.5,'自由/洗漱','#BDC3C7'),
        (22.5,23,'睡前回顾','#8E44AD'),
        (23,6,'睡眠','#34495E'),
    ]
    for start,end,label,color in blocks:
        w = end-start
        bar = mpatches.FancyBboxPatch((start,0.3),w,1.2,boxstyle="round,pad=0.05",facecolor=color,alpha=0.85,edgecolor='white')
        ax.add_patch(bar)
        fontsize = 6.5 if w < 1 else 7.5
        ax.text(start+w/2,0.9,label,ha='center',va='center',fontsize=fontsize,color='white',fontweight='bold')
    done = sum(e-s for s,e,_,_ in blocks if '睡眠' not in label and '休息' not in label)
    ax.set_title('在校生 · 每日24小时时间块规划',fontsize=13,fontweight='bold',color='#1a1a2e',pad=8)
    ax.set_xlabel('时间',fontsize=10)
    ax.set_xticks(range(0,25,2))
    ax.set_xticklabels([f'{h}:00' for h in range(0,25,2)],fontsize=7)
    ax.set_yticks([])
    ax.spines[:].set_visible(False)
    # time blocks legend
    for i,(c,lbl) in enumerate([('#5688CC','学校时间'),('#D18080','自习时间'),('#E8A060','早读'),('#27AE60','运动'),('#34495E','睡眠'),('#8E44AD','回顾')]):
        ax.text(i*3.8+1,1.55,'■',fontsize=8,color=c,va='center')
        ax.text(i*3.8+1.3,1.55,lbl,fontsize=7,color='#555',va='center')
    save('time_blocks')

if __name__ == '__main__':
    import os; os.makedirs(OUT,exist_ok=True)
    print('Generating 中考时间规划 charts...')
    chart_year_timeline()
    chart_phase_intensity()
    chart_holiday_schedule()
    chart_100days()
    chart_weekly_plan()
    chart_scientific_routine()
    chart_execution_rate()
    chart_monthly_scores()
    chart_subject_focus()
    chart_time_blocks()
    print('Done!')
