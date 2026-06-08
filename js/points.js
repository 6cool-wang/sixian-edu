/* 思贤学习站 · 统一积分系统 */
(function(){
var KEY='sx_points', CODE_KEY='sx_codes';
var SECRET='sx'+(2024).toString(16)+'sixian';

function data(){
  var d=localStorage.getItem(KEY);
  return d?JSON.parse(d):{total:0,log:[]};
}
function save(d){localStorage.setItem(KEY,JSON.stringify(d))}
function hash(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0}return Math.abs(h).toString(36).slice(0,8)}
function _btoa(s){
  if(typeof btoa!=='undefined')return btoa(s);
  try{return Buffer.from(s,'utf-8').toString('base64')}catch(e){}
  return null;
}
function _atob(s){
  if(typeof atob!=='undefined')return atob(s);
  try{return decodeURIComponent(escape(atob(s)))}catch(e){}
  try{return Buffer.from(s,'base64').toString()}catch(e){}
  return null;
}

window.PointsSystem={
  get:function(){return data().total},
  info:function(){return data()},
  add:function(correct,bonus){
    var d=data(),earned=correct+(bonus||0);
    var db=parseInt(localStorage.getItem('sx_double')||'0');
    if(db>0){earned*=2;localStorage.setItem('sx_double',String(db-1))}
    d.total+=earned;
    d.log.push({t:'+'+earned,at:Date.now()});
    save(d);
    return earned;
  },
  activateDouble:function(){
    localStorage.setItem('sx_double','3');
  },
  doubleLeft:function(){
    return parseInt(localStorage.getItem('sx_double')||'0');
  },
  // 浏览知识页奖励（每天每页限1次）
  visitPage:function(pageId){
    var key='sx_visit_'+new Date().toDateString();
    var v=JSON.parse(localStorage.getItem(key)||'[]');
    if(v.indexOf(pageId)>=0)return 0;
    v.push(pageId);localStorage.setItem(key,JSON.stringify(v));
    var d=data();d.total+=1;d.log.push({t:'学习+'+pageId,at:Date.now()});save(d);
    return 1;
  },
  spend:function(pts){
    var d=data();
    if(d.total<pts)return false;
    d.total-=pts;
    d.log.push({t:'-'+pts,at:Date.now()});
    save(d); return true;
  },
  // ==================== 每日签到 ====================
  checkIn:function(){
    var d=data(),today=new Date().toDateString();
    var last=localStorage.getItem('sx_sign_last')||'',streak=parseInt(localStorage.getItem('sx_sign_streak')||'0');
    if(last===today)return{ok:false,msg:'今日已签到',streak:streak};
    var y=new Date(Date.now()-864e5).toDateString();
    streak=last===y?streak+1:1;
    var bonus=streak>=7?3:1;
    d.total+=bonus;d.log.push({t:'签到+'+bonus,at:Date.now()});save(d);
    localStorage.setItem('sx_sign_last',today);
    localStorage.setItem('sx_sign_streak',String(streak));
    return{ok:true,points:bonus,streak:streak};
  },
  signStatus:function(){
    var today=new Date().toDateString(),last=localStorage.getItem('sx_sign_last')||'',streak=parseInt(localStorage.getItem('sx_sign_streak')||'0');
    var bonus=streak>=7?3:1;
    return{checkedIn:last===today,streak:streak,todayBonus:last===today?0:bonus};
  },
  // ==================== 每日分享 ====================
  shareStatus:function(){
    var today=new Date().toDateString();
    return{shared:localStorage.getItem('sx_share_last')===today};
  },
  doShare:function(){
    var d=data(),today=new Date().toDateString();
    if(localStorage.getItem('sx_share_last')===today)return{ok:false,msg:'今日已分享'};
    localStorage.setItem('sx_share_last',today);
    d.total+=2;d.log.push({t:'分享+2',at:Date.now()});save(d);
    return{ok:true,points:2};
  },
  // ==================== 每日重玩 ====================
  useReplay:function(){
    var key='sx_replay_'+new Date().toDateString(),n=parseInt(localStorage.getItem(key)||'0');
    if(n>=3)return false;
    localStorage.setItem(key,String(n+1));return true;
  },
  replayLeft:function(){
    return Math.max(0,3-parseInt(localStorage.getItem('sx_replay_'+new Date().toDateString())||'0'));
  },
  // ==================== 核销 ====================
  genCode:function(itemId){
    var ts=Date.now(),nonce=Math.random().toString(36).slice(2,8);
    var raw=itemId+'|'+ts+'|'+nonce+'|'+hash(itemId+'|'+ts+'|'+nonce+':'+SECRET);
    return _btoa(raw);
  },
  verifyCode:function(code,teacherSecret){
    try{
      code=(code||'').replace(/[\s\r\n]+/g,'');
      if(!code)return{ok:false,reason:'码为空'};
      var raw=_atob(code);
      if(!raw)return{ok:false,reason:'格式错误(base64)'};
      var p=raw.split('|');
      if(p.length!==4)return{ok:false,reason:'格式错误(分段)'};
      var sig=p.pop(),payload=p.join('|');
      var ok=(teacherSecret&&sig===hash(payload+':'+teacherSecret))||sig===hash(payload+':'+SECRET);
      if(!ok)return{ok:false,reason:'无效核销码'};
      var itemId=p[0],ts=+p[1];
      if(Date.now()-ts>864e5)return{ok:false,reason:'已过期（超过24小时）'};
      var used=JSON.parse(localStorage.getItem(CODE_KEY)||'[]');
      if(used.indexOf(code)>=0)return{ok:false,reason:'此码已被核销'};
      return{ok:true,itemId:itemId,ts:ts};
    }catch(e){return{ok:false,reason:'格式错误('+e.message+')'}}
  },
  markUsed:function(code){
    var used=JSON.parse(localStorage.getItem(CODE_KEY)||'[]');
    used.push(code);localStorage.setItem(CODE_KEY,JSON.stringify(used));
  },
  shop:[
    {id:'planner',name:'学习计划表 1份',cost:15,icon:'📋',desc:'定制每周学习计划表',cat:'study'},
    {id:'snack',name:'零食盲盒',cost:25,icon:'🍿',desc:'随机小零食一份',cat:'food'},
    {id:'sweetpotato',name:'助学红薯 1个',cost:25,icon:'🍠',desc:'商河本地新鲜红薯',cat:'food',tag:'hot'},
    {id:'cookie',name:'手工曲奇 1袋',cost:30,icon:'🍪',desc:'手工现烤黄油曲奇',cat:'food'},
    {id:'icecream',name:'冰淇淋券 1份',cost:35,icon:'🍦',desc:'夏日冰淇淋兑换券',cat:'food',tag:'new'},
    {id:'milktea',name:'奶茶兑换券 1杯',cost:40,icon:'🧋',desc:'合作奶茶店免费兑换',cat:'food',tag:'new'},
    {id:'cake',name:'小蛋糕 1份',cost:45,icon:'🧁',desc:'精致甜品小蛋糕',cat:'food'},
    {id:'print',name:'资料打印 10页',cost:20,icon:'🖨️',desc:'学习资料免费打印',cat:'study'},
    {id:'stationery',name:'文具盲盒',cost:20,icon:'🎁',desc:'随机文具小礼包',cat:'study',tag:'hot'},
    {id:'studyroom',name:'自习券 1次',cost:20,icon:'🏫',desc:'自习室免费使用一次',cat:'privilege',tag:'new'},
    {id:'wordbook',name:'单词听写本 1本',cost:20,icon:'📇',desc:'英语单词默写本',cat:'study'},
    {id:'t5',name:'免费答疑 5分钟',cost:25,icon:'⏱️',desc:'线上一对一答疑辅导',cat:'tutor',tag:'hot'},
    {id:'notebook',name:'错题本 1本',cost:25,icon:'📒',desc:'活页错题整理本',cat:'study'},
    {id:'poem',name:'古诗词卡片 1套',cost:25,icon:'🀄',desc:'初中必背古诗词记忆卡',cat:'study',tag:'new'},
    {id:'report',name:'学情报告 1份',cost:30,icon:'📊',desc:'学习情况分析打印',cat:'tutor'},
    {id:'weekend',name:'周末免费自习 1天',cost:30,icon:'📖',desc:'周末自习室免费使用',cat:'privilege'},
    {id:'skip',name:'免考勤卡 1次',cost:30,icon:'🎫',desc:'免一次考勤记录',cat:'privilege'},
    {id:'seat',name:'优先选座 1周',cost:35,icon:'💺',desc:'自习区自由选座',cat:'privilege'},
    {id:'mate',name:'同桌选择权 1次',cost:35,icon:'👥',desc:'自由选择同桌一次',cat:'privilege'},
    {id:'nb',name:'定制笔记本',cost:40,icon:'📓',desc:'思贤定制笔记本',cat:'study'},
    {id:'double',name:'积分双倍卡 1张',cost:40,icon:'🔄',desc:'下次闯关积分翻倍',cat:'privilege',tag:'hot'},
    {id:'notes',name:'学霸笔记 1份',cost:45,icon:'📝',desc:'优秀学长手写笔记复印',cat:'study'},
    {id:'oral',name:'英语口语测评 1次',cost:50,icon:'🎤',desc:'老师一对一英语口语测评',cat:'tutor',tag:'new'},
    {id:'tutor',name:'老师面批 1次',cost:55,icon:'✍️',desc:'老师一对一当面批改讲解',cat:'tutor'},
    {id:'hw',name:'作业优先批改 1次',cost:60,icon:'✅',desc:'作业优先批改并标注',cat:'tutor'},
    {id:'usb',name:'学习资料U盘 1个',cost:60,icon:'💾',desc:'精选学习资料U盘',cat:'study'},
    {id:'t15',name:'免费答疑 15分钟',cost:70,icon:'📚',desc:'线上一对一答疑辅导',cat:'tutor'},
    {id:'checkhw',name:'作业检查 1次',cost:40,icon:'🔍',desc:'老师逐题检查作业并标注错漏',cat:'tutor'},
    {id:'dictation',name:'单词听写辅导 1次',cost:35,icon:'✏️',desc:'老师一对一单词听写+批改',cat:'tutor',tag:'new'},
    {id:'readaloud',name:'朗读纠音辅导 1次',cost:35,icon:'🔊',desc:'英语/语文课文朗读纠音指导',cat:'tutor'},
    {id:'math_tutor',name:'数学上门辅导 1小时',cost:90,icon:'📐',desc:'数学老师免费上门一对一辅导',cat:'tutor',tag:'hot'},
    {id:'phys_tutor',name:'物理上门辅导 1小时',cost:90,icon:'⚡',desc:'物理老师免费上门一对一辅导',cat:'tutor',tag:'hot'},
    {id:'chem_tutor',name:'化学上门辅导 1小时',cost:90,icon:'🧪',desc:'化学老师免费上门一对一辅导',cat:'tutor'},
    {id:'eng_tutor',name:'英语上门辅导 1小时',cost:90,icon:'🔤',desc:'英语老师免费上门一对一辅导',cat:'tutor',tag:'new'},
    {id:'chn_tutor',name:'语文上门辅导 1小时',cost:90,icon:'📖',desc:'语文老师免费上门一对一辅导',cat:'tutor'},
    {id:'bio_tutor',name:'生物上门辅导 1小时',cost:90,icon:'🧬',desc:'生物老师免费上门一对一辅导',cat:'tutor'},
    {id:'holiday',name:'寒暑假作业辅导',cost:80,icon:'☀️',desc:'寒暑假作业集中辅导一次',cat:'tutor'},
  ]
};
})();
