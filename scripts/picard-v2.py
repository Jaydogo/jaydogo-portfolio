#!/usr/bin/env python3
"""Réécrit le module Picard (CSS #pic-css + JS picFigs/picGo) dans index.html et fr/index.html.
Relancer après modification :  python3 scripts/picard-v2.py && python3 scripts/pages.py"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.listdir(os.path.join(ROOT, 'projets/picard'))
def f(n, e):
    x = [a for a in A if a.startswith(n + '-') and a.endswith('.' + e)]
    if not x: raise SystemExit('asset manquant ' + n + '.' + e)
    return x[0]
V = lambda n: f"['{f(n,'mp4')}','{f(n,'jpg')}']"
MEDIA = ("{hero:%s,iconique:%s,fiche:%s,survol:%s,promo:%s,cc:%s,responsive:%s,pictos:%s,fondations:%s,nav:%s,wireframe:%s,"
         "menu:'%s',avantages:'%s',main:'%s',trio:'%s',duo:'%s',flocon:'%s'}") % (
    V('hero'), V('iconique'), V('fiche'), V('survol'), V('promo'), V('cc'), V('responsive'), V('pictos'), V('fondations'), V('nav'), V('wireframe'),
    f('menu','jpg'), f('avantages','jpg'), f('main','jpg'), f('app-trio','jpg'), f('app-duo','jpg'), f('flocon','svg'))

CSS = r'''<style id="pic-css">
/* Picard : figures exportées de Figma + blocs typographiques. Préfixe .px — typo d'accent dans --pxd */
#page{--pxd:Unbounded,Archivo,system-ui,sans-serif}
.fig .v.px{height:auto;min-height:0;padding:0;background:#E9E4DA;display:block}
.v.px video,.v.px img{width:100%;height:100%;object-fit:cover;display:block}
.fig .v.px-t{height:auto;min-height:0;display:block;background:transparent;border-radius:0;overflow:visible!important;padding:clamp(18px,3vw,40px) 0}
.px-t p{margin:0}
.px-t .lb{font:400 11px/1 "DM Mono",ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--cc,#141412)}
.px-t .rule{display:block;height:1px;background:var(--cc,#141412);opacity:.55;margin:12px 0 0}
.fig .v.px-chap{padding:clamp(40px,5vw,72px) 0 0}
.px-chap .cr{width:100%!important;max-width:none!important;margin:0!important;display:flex;align-items:baseline;gap:14px;letter-spacing:.14em;text-transform:uppercase}
.px-chap .cr .lb{white-space:nowrap;color:var(--cc)}
.px-chap .pw{font:400 11px/1.4 "DM Mono",ui-monospace,monospace;letter-spacing:.14em;color:#141412;margin:0;white-space:nowrap}
.px-chap .ps{font:400 11px/1.4 "DM Mono",ui-monospace,monospace;letter-spacing:.14em;color:#8a877e;margin:0 0 0 auto;text-align:right}
/* intro en cartes */
.px-intro .q{font:500 clamp(22px,2.4vw,34px)/1.12 var(--pxd);letter-spacing:-.035em;max-width:19em;margin:16px 0 clamp(26px,4vw,48px)}
.px-intro .pc{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.px-intro .ck{background:var(--cc);color:#fff;border-radius:10px;aspect-ratio:3/4.2;padding:clamp(14px,1.4vw,20px);display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.px-intro .ck b{font:400 11px/1 "DM Mono",monospace;letter-spacing:.14em;opacity:.85}
.px-intro .ck em{font:700 normal clamp(17px,1.65vw,24px)/1 var(--pxd);letter-spacing:-.04em}
.px-intro .ck span{font:400 12.5px/1.35 Archivo,system-ui,sans-serif;opacity:.88;margin-top:8px;display:block;min-height:2.7em}
.px-intro .ck::after{content:"";position:absolute;right:-28%;top:-18%;width:78%;aspect-ratio:374/399;background:url(/projets/picard/__FLOCON__) center/contain no-repeat;opacity:.13;transform:rotate(var(--r,0deg))}
.fig figure:not(.vu) .px-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .px-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
/* contraste : interrupteur et vrais taux WCAG */
.px-ac .acw,.px-intro .pc,.px-aw .awh{width:100%!important;max-width:none!important}
.px-ac .acw{background:#fff;border-radius:10px;padding:clamp(18px,2.2vw,32px);margin-top:14px}
.px-ac .ach{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-bottom:16px;border-bottom:1px solid #E7E4DD}
.px-ac .acti{font:700 clamp(20px,2.2vw,30px)/1 var(--pxd);letter-spacing:-.04em}
.px-ac .tg{display:flex;align-items:center;gap:10px;font:400 11px/1 "DM Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:#77736B}
.px-ac .sw{width:54px;height:30px;border-radius:99px;background:#D9D5CC;position:relative;transition:background .5s}
.px-ac .sw i{position:absolute;left:3px;top:3px;width:24px;height:24px;border-radius:50%;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.2);transition:transform .5s cubic-bezier(.5,1.6,.4,1)}
.px-ac.on .sw{background:#2D4999}.px-ac.on .sw i{transform:translateX(24px)}
.px-ac .acr{display:grid;grid-template-columns:1fr auto auto;align-items:center;gap:clamp(12px,2vw,28px);padding:14px 0;border-bottom:1px solid #F0EEE9}
.px-ac .acr:last-of-type{border-bottom:0}
.px-ac .s{--c:var(--a);justify-self:start;transition:background-color .6s,color .6s}
.px-ac.on .s{--c:var(--b)}
.px-ac .chip{background:var(--c);color:#fff;font:600 normal 12px/1 Archivo,sans-serif;letter-spacing:.04em;padding:7px 10px;border-radius:5px}
.px-ac .txt{color:var(--c);font:500 normal 15px/1.2 Archivo,sans-serif}
.px-ac .txt.pr{font:700 normal 22px/1.1 Archivo,sans-serif;letter-spacing:-.02em}
.px-ac .rt{font:700 clamp(22px,2.4vw,34px)/1 var(--pxd);letter-spacing:-.04em;min-width:4.2ch;text-align:right;font-variant-numeric:tabular-nums}
.px-ac .rt small{font:400 12px "DM Mono",monospace;letter-spacing:.05em;margin-left:2px}
.px-ac .bd{font:500 11px/1 "DM Mono",monospace;letter-spacing:.1em;padding:7px 9px;border-radius:99px;border:1px solid #E94F5E;color:#C23A48;min-width:74px;text-align:center;transition:all .5s}
.px-ac.on .bd{background:#1F8F55;border-color:#1F8F55;color:#fff}
.px-ac .acn{font:400 11px/1.4 "DM Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:#77736B;margin-top:14px}
/* récompenses : bento, médailles métallisées, flocon Picard */
.px-aw .awh{display:flex;align-items:flex-start;gap:.5em;padding-bottom:18px;border-bottom:1px solid rgba(20,20,18,.2);margin-bottom:12px}
.px-aw .awt{font:700 clamp(40px,6.4vw,96px)/.9 var(--pxd);letter-spacing:-.06em}
.px-aw .awn{font:400 13px/1 "DM Mono",monospace;letter-spacing:.08em;margin-top:.5em}
.px-aw .awg{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:auto auto;gap:10px;width:100%}
.px-aw .awc{position:relative;overflow:hidden;color:#fff;border-radius:12px;padding:clamp(24px,2.8vw,38px);display:flex;flex-direction:column;min-height:clamp(230px,24vw,330px);background:radial-gradient(120% 90% at 85% 10%,rgba(255,255,255,.22),transparent 55%),linear-gradient(160deg,var(--bg),var(--bg2))}
.px-aw .awc.awx{grid-row:span 2}
.px-aw .awc::before{content:"";position:absolute;right:-22%;bottom:-24%;width:82%;aspect-ratio:374/399;background:url(/projets/picard/__FLOCON__) center/contain no-repeat;opacity:.16;animation:pxspin 40s linear infinite}
.px-aw .awc.awx::before{width:95%;right:-30%;bottom:-18%}
@keyframes pxspin{to{transform:rotate(60deg)}}
.px-aw .awy{position:relative;display:flex;justify-content:space-between;font:400 11px/1 "DM Mono",monospace;letter-spacing:.14em;opacity:.9}
.px-aw .awc-n{position:relative;font:700 clamp(84px,10vw,150px)/.8 var(--pxd);letter-spacing:-.07em;margin:auto 0 0 -.04em}
.px-aw .awc.awx .awc-n{font-size:clamp(130px,17vw,250px)}
.px-aw .awc-l{position:relative;font:400 11px/1 "DM Mono",monospace;letter-spacing:.14em;text-transform:uppercase;margin:10px 0 14px}
.px-aw .awd{position:relative;display:flex;gap:8px;margin:0 0 16px;flex-wrap:wrap}
.px-aw .md{width:30px;height:30px;border-radius:50%;position:relative;box-shadow:0 4px 10px rgba(0,0,0,.25),inset 0 0 0 2px rgba(255,255,255,.35);overflow:hidden}
.px-aw .md::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.75) 45%,transparent 60%);transform:translateX(-120%);animation:pxshine 3.6s ease-in-out infinite;animation-delay:calc(var(--j)*.18s)}
@keyframes pxshine{0%,55%{transform:translateX(-120%)}80%,100%{transform:translateX(120%)}}
.px-aw .m-g{background:conic-gradient(from 200deg,#FFE8A3,#D9A931,#FFF3C8,#B8860B,#FFE8A3)}
.px-aw .m-s{background:conic-gradient(from 200deg,#FFFFFF,#AEB6C2,#F4F6F9,#8C95A3,#FFFFFF)}
.px-aw .m-b{background:conic-gradient(from 200deg,#F3C39A,#A8612E,#F7D6B8,#8A4B22,#F3C39A)}
.px-aw .awb{position:relative;border-top:1px solid rgba(255,255,255,.35);padding-top:12px;display:flex;flex-direction:column;gap:4px}
.px-aw .awb b{font:700 clamp(15px,1.4vw,19px)/1.1 var(--pxd);letter-spacing:-.03em}
.px-aw .awb span{font:400 13px/1.35 Archivo,system-ui,sans-serif;opacity:.9}
.fig figure:not(.vu) .px-aw .awc{opacity:0;transform:translateY(40px) scale(.98)}
.fig figure .px-aw .awc{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.fig figure:not(.vu) .px-aw .md{transform:scale(0) rotate(-90deg)}
.fig figure .px-aw .md{transition:transform .6s calc(var(--d) + 500ms + var(--j)*90ms) cubic-bezier(.3,1.6,.5,1)}
@media (max-width:899px){.px-intro .pc{grid-template-columns:1fr 1fr}.px-chap .cr{flex-wrap:wrap}.px-chap .ps{flex-basis:100%;margin:0;text-align:left}.px-aw .awg{grid-template-columns:1fr}.px-aw .awc.awx{grid-row:auto}.px-ac .acr{grid-template-columns:1fr auto}.px-ac .bd{grid-column:2}}
.fig figure:not(.vu) .px-t .pw{opacity:0;transform:translateY(.25em)}
.fig figure .px-t .pw{transition:opacity .9s .15s,transform 1.1s .15s cubic-bezier(.2,.7,.2,1)}
@media (prefers-reduced-motion:reduce){.px-aw .awc::before,.px-aw .md::after{animation:none}}
</style>
'''.replace('__FLOCON__', f('flocon', 'svg'))

JS = r'''/* Picard : figures réelles (projet marqué x:'picard'). Vidéos exportées de l'animation Figma, lues seulement à l'écran. */
const PI='/projets/picard/';
const PTX={fr:{q:'Faire d’un catalogue de surgelés un site qui donne faim.',defi:'Le défi',chap:[['Inspirer','Une vitrine qui donne faim, comme en magasin.','#AC6442'],['Trouver','Rayon, filtre, produit : trois gestes.','#2D4999'],['Choisir','Livraison ou retrait, avant même le panier.','#2DA0A2'],['Fidéliser','Picard & Moi, visible à chaque étape.','#F47935']],app:['Dans la poche.','L’app iOS et Android conçue chez Niji, de la recette au retrait.','App · Niji'],tous:['Pour tous, partout.','Du mobile 352 px à l’écran 2048 px, en mode contrasté.'],
 ac:{t:'Mode contrasté',tg:'Contrasté',n:'Seuil WCAG AA : 4,5:1 pour le texte',ko:'Échec AA',ok:'AA ✓',rows:[['chip','NOUVEAU','#2DA0A2','#248285','3,15','4,56'],['chip','-30 %','#E94F5E','#CB4654','3,66','4,62'],['txt pr','3,80 €','#F47935','#C75000','2,75','4,59'],['chip','BIO','#9FB838','#637F24','2,24','4,57'],['txt','La pièce de 400 g','#88898B','#636266','3,50','6,05']]},
 prix:'Récompenses',dist:['distinction','distinctions'],aw:[['W3 Awards','2020','3 Or · 2 Argent','gggss','#F47935','#C14E12'],['Lovie Awards','2020','Or · Meilleure UX','g','#2D4999','#16245C'],['Indigo Awards','2021','Or · Argent · 2 Bronze','gsbb','#2DA0A2','#14666A']],
 alt:['Carte Picard & Moi sur fond bleu Picard','Méga-menu « En ce moment chez Picard »','Page produit iconique, desktop et mobile','Fiche produit annotée','Cartes produit au survol','Carte promo qui se retourne au survol','Livraison ou retrait : trois écrans sur iPhone','Espace Mes avantages Picard & Moi sur écran','App Picard en main : accueil','App Picard : produits, accueil, recettes','Barre de navigation de l’app','App Picard : fiche produit et compte fidélité','Un rayon, quatre largeurs d’écran','Pictogrammes d’interface','Couleurs et typographies','Du wireframe à l’interface : accueil et fiche produit']},
 en:{q:'Turning a frozen-food catalogue into a site that makes you hungry.',defi:'The challenge',chap:[['Inspire','A storefront that makes you hungry, like in store.','#AC6442'],['Find','Aisle, filter, product: three taps.','#2D4999'],['Choose','Delivery or pickup, before the basket.','#2DA0A2'],['Reward','Picard & Moi, visible at every step.','#F47935']],app:['In your pocket.','The iOS and Android app designed at Niji, from recipe to pickup.','App · Niji'],tous:['For everyone, everywhere.','From 352 px mobile to 2048 px screens, with a high-contrast mode.'],
 ac:{t:'High-contrast mode',tg:'Contrast',n:'WCAG AA threshold: 4.5:1 for text',ko:'Fails AA',ok:'AA ✓',rows:[['chip','NOUVEAU','#2DA0A2','#248285','3.15','4.56'],['chip','-30 %','#E94F5E','#CB4654','3.66','4.62'],['txt pr','€3.80','#F47935','#C75000','2.75','4.59'],['chip','BIO','#9FB838','#637F24','2.24','4.57'],['txt','400 g pack','#88898B','#636266','3.50','6.05']]},
 prix:'Awards',dist:['award','awards'],aw:[['W3 Awards','2020','3 Gold · 2 Silver','gggss','#F47935','#C14E12'],['Lovie Awards','2020','Gold · Best UX','g','#2D4999','#16245C'],['Indigo Awards','2021','Gold · Silver · 2 Bronze','gsbb','#2DA0A2','#14666A']],
 alt:['Picard & Moi card on Picard blue','Mega menu “What’s new at Picard”','Iconic product page, desktop and mobile','Annotated product page','Product cards on hover','Promo card flipping on hover','Delivery or pickup: three screens on iPhone','Picard & Moi rewards area on a desktop screen','Picard app in hand: home','Picard app: products, home, recipes','App tab bar','Picard app: product page and loyalty account','One aisle, four screen widths','Interface icons','Colours and typefaces','From wireframe to interface: home and product page']}};
const PV=(n,r,alt,once)=>`<div class="v rx px" style="aspect-ratio:${r}"><video class="pv" muted playsinline preload="none" ${once?'data-once':'loop'} poster="${PI}${n[1]}" data-src="${PI}${n[0]}" aria-label="${alt}"></video></div>`;
const PIMG=(n,r,alt)=>`<div class="v rx px" style="aspect-ratio:${r}"><img src="${PI}${n}" alt="${alt}" loading="lazy"></div>`;
const PCHAP=(lb,c)=>`<div class="v rx px-t px-chap" style="--cc:${c[2]}"><div class="cr"><span class="lb">${lb}</span><p class="pw">${c[0]}</p><p class="ps">${c[1]}</p></div></div>`;
function picFigs(q){
 const T=PTX[lang]||PTX.fr,a=T.alt,M=__MEDIA__,C=T.ac;
 const intro=`<div class="v rx px-t px-intro"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><div class="pc">${q.enj.map((e,k)=>`<div class="ck" style="--cc:${T.chap[k][2]};--d:${k*110}ms;--r:${k*17}deg"><b>0${k+1}</b><div><em>${e[0]}</em><span>${e[1]}</span></div></div>`).join('')}</div></div>`;
 const ac=`<div class="v rx px-t px-ac" data-pac><span class="lb">352 → 2048 px · WCAG</span><div class="acw"><div class="ach"><p class="acti">${C.t}</p><span class="tg">${C.tg}<span class="sw"><i></i></span></span></div>${C.rows.map(r=>`<div class="acr"><span class="s ${r[0]==='chip'?'chip':r[0]}" style="--a:${r[2]};--b:${r[3]}">${r[1]}</span><span class="rt" data-a="${r[4]}" data-b="${r[5]}">${r[4]}<small>:1</small></span><span class="bd" data-ko="${C.ko}" data-ok="${C.ok}">${C.ko}</span></div>`).join('')}<p class="acn">${C.n}</p></div></div>`;
 const tot=T.aw.reduce((s,w)=>s+w[3].length,0);
 const aw=`<div class="v rx px-t px-aw"><div class="awh"><p class="awt">${T.prix}</p><span class="awn">(${tot})</span></div><div class="awg">${T.aw.map((w,k)=>`<div class="awc${k?'':' awx'}" style="--bg:${w[4]};--bg2:${w[5]};--d:${k*140}ms"><div class="awy"><span>${w[1]}</span><span>0${k+1}</span></div><p class="awc-n">${w[3].length}</p><p class="awc-l">${w[3].length>1?T.dist[1]:T.dist[0]}</p><div class="awd">${[...w[3]].map((m,j)=>`<i class="md m-${m}" style="--j:${j}"></i>`).join('')}</div><div class="awb"><b>${w[0]}</b><span>${w[2]}</span></div></div>`).join('')}</div></div>`;
 const f=[
  PV(M.hero,'870/700',a[0]), intro,
  PCHAP('01 / 04',T.chap[0]), PIMG(M.menu,'870/640',a[1]), PV(M.iconique,'870/940',a[2]),
  PCHAP('02 / 04',T.chap[1]), PV(M.fiche,'870/760',a[3],1), PV(M.survol,'870/640',a[4]), PV(M.promo,'870/600',a[5]),
  PCHAP('03 / 04',T.chap[2]), PV(M.cc,'870/760',a[6],1),
  PCHAP('04 / 04',T.chap[3]), PIMG(M.avantages,'1305/979',a[7]),
  PCHAP(T.app[2],[T.app[0],T.app[1],'#2D4999']), PIMG(M.main,'1305/979',a[8]), PIMG(M.trio,'1305/975',a[9]), PV(M.nav,'870/420',a[10]), PV(M.wireframe,'870/760',a[15]), PIMG(M.duo,'1305/975',a[11]),
  PCHAP('352 → 2048 px',[T.tous[0],T.tous[1],'#E94F5E']), PV(M.responsive,'870/520',a[12],1), ac,
  PV(M.pictos,'870/560',a[13],1), PV(M.fondations,'870/780',a[14],1), aw
 ];
 return f.map(x=>[x,'']);
}
function picGo(root){
 const calme=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const AC=root.querySelector('[data-pac]');
 if(AC){const set=on=>{AC.classList.toggle('on',on);AC.querySelectorAll('.rt').forEach(e=>e.firstChild.textContent=on?e.dataset.b:e.dataset.a);AC.querySelectorAll('.bd').forEach(e=>e.textContent=on?e.dataset.ok:e.dataset.ko)};
  if(calme)set(true);else{let on=false,vis=false;const io=new IntersectionObserver(es=>{vis=es.some(e=>e.isIntersecting)},{threshold:.3});io.observe(AC);(window._rxObs=window._rxObs||[]).push(io);RT.push(setInterval(()=>{if(!vis)return;on=!on;set(on)},2600))}}
 const vids=[...root.querySelectorAll('video.pv')];if(!vids.length||calme)return;
 const io=new IntersectionObserver(es=>es.forEach(e=>{const v=e.target;if(e.isIntersecting){if(!v.src){v.src=v.dataset.src;v.load()}if(v.hasAttribute('data-once')&&v.ended)v.currentTime=0;const p=v.play();p&&p.catch(()=>{})}else v.pause()}),{threshold:.35});
 vids.forEach(v=>io.observe(v));(window._rxObs=window._rxObs||[]).push(io);
}
'''.replace('__MEDIA__', MEDIA)

for name in ['index.html', 'fr/index.html']:
    p = os.path.join(ROOT, name); s = open(p, encoding='utf-8').read()
    a = s.index('<style id="pic-css">'); b = s.index('</style>', a) + len('</style>\n')
    s = s[:a] + CSS + s[b:]
    a = s.index("/* Picard : figures réelles"); b = s.index("/* Route du Rhum : figures réelles")
    s = s[:a] + JS + s[b:]
    if 'family=Unbounded' not in s:
        s = s.replace('&family=Montserrat:', '&family=Unbounded:wght@500;700&family=Montserrat:', 1)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
