/* 思贤学习站 · 统一积分系统 */
(function(){
var KEY='sx_points', CODE_KEY='sx_codes';
// 签名密钥（内置 + 老师可选自定义）
var SECRET='sx'+(2024).toString(16)+'sixian';

function data(){
  var d=localStorage.getItem(KEY);
  return d?JSON.parse(d):{total:0,log:[]};
}
function save(d){localStorage.setItem(KEY,JSON.stringify(d))}
function hash(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h)+s.charCodeAt(i);h|=0}return Math.abs(h).toString(36).slice(0,8)}

window.PointsSystem={
  get:function(){return data().total},
  info:function(){return data()},
  // 答题加分：答对题数 + 三星额外奖励
  add:function(correct,bonus){
    var d=data(),earned=correct+(bonus||0);
    d.total+=earned;
    d.log.push({t:'+'+earned,at:Date.now()});
    save(d);
    return earned;
  },
  // 扣分兑换
  spend:function(pts){
    var d=data();
    if(d.total<pts)return false;
    d.total-=pts;
    d.log.push({t:'-'+pts,at:Date.now()});
    save(d); return true;
  },
  // ---------- code ----------
  // 生成核销码：base64(itemId|ts|nonce|签名)
  genCode:function(itemId){
    var ts=Date.now(),nonce=Math.random().toString(36).slice(2,8);
    return btoa(itemId+'|'+ts+'|'+nonce+'|'+hash(itemId+'|'+ts+'|'+nonce+':'+SECRET));
  },
  // 验证核销码（老师密钥优先，降级到内置密钥）
  verifyCode:function(code,teacherSecret){
    try{
      var raw=atob(code),p=raw.split('|');
      if(p.length!==4)return{ok:false,reason:'格式错误'};
      var sig=p.pop(),payload=p.join('|');
      // 先用老师密钥验证，失败后用内置密钥
      var ok=(teacherSecret&&sig===hash(payload+':'+teacherSecret))||sig===hash(payload+':'+SECRET);
      if(!ok)return{ok:false,reason:'无效核销码'};
      var itemId=p[0],ts=+p[1];
      if(Date.now()-ts>864e5)return{ok:false,reason:'已过期（超过24小时）'};
      var used=JSON.parse(localStorage.getItem(CODE_KEY)||'[]');
      if(used.indexOf(code)>=0)return{ok:false,reason:'此码已被核销'};
      return{ok:true,itemId:itemId,ts:ts};
    }catch(e){return{ok:false,reason:'格式错误'}}
  },
  markUsed:function(code){
    var used=JSON.parse(localStorage.getItem(CODE_KEY)||'[]');
    used.push(code);localStorage.setItem(CODE_KEY,JSON.stringify(used));
  },
  shop:[
    {id:'t5',name:'免费答疑 5分钟',cost:25,icon:'⏱️',desc:'线上一对一答疑辅导'},
    {id:'t15',name:'免费答疑 15分钟',cost:70,icon:'📚',desc:'线上一对一答疑辅导'},
    {id:'report',name:'学情报告 1份',cost:30,icon:'📊',desc:'学习情况分析打印'},
    {id:'stationery',name:'文具盲盒',cost:20,icon:'🎁',desc:'随机文具小礼包'},
    {id:'sweetpotato',name:'助学地瓜 1个',cost:15,icon:'🍠',desc:'商河本地新鲜地瓜'},
    {id:'notebook',name:'定制笔记本',cost:40,icon:'📓',desc:'思贤定制笔记本'},
    {id:'homework',name:'免作业卡 1次',cost:50,icon:'🃏',desc:'免一次书面作业'},
  ]
};
})();
