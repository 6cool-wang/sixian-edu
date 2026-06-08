/* 思贤学习站 · 学习积分奖励可视化 */
(function(){
var pageId='';
var sc=document.currentScript;
if(sc&&sc.getAttribute('data-page'))pageId=sc.getAttribute('data-page');
else{
  var t=document.title.replace(/[·•]\s*思贤学习站\s*$/,'').trim();
  pageId=t||'unknown';
}
if(typeof PointsSystem==='undefined')return;

var ok=PointsSystem.visitPage(pageId);
if(!ok)return;

// 浮动提示
var el=document.createElement('div');
el.style.cssText='position:fixed;top:16px;right:16px;z-index:9999;background:rgba(0,0,0,.75);color:#ffd700;padding:8px 14px;border-radius:8px;font-size:14px;font-weight:600;opacity:0;transform:translateY(-10px);transition:all .3s;pointer-events:none;box-shadow:0 2px 12px rgba(0,0,0,.15)';
el.innerHTML='📖 +1 积分';
document.body.appendChild(el);
requestAnimationFrame(function(){
  el.style.opacity='1';el.style.transform='translateY(0)';
});
setTimeout(function(){
  el.style.opacity='0';el.style.transform='translateY(-10px)';
  setTimeout(function(){el.remove()},300);
},2000);
})();
