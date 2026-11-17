#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute / réécrit le projet Relais & Châteaux (x:'relais', à la place du fictif Comptoir) dans index.html et fr/index.html.
Figures exportées de Figma (fichier « Relais & Châteaux · Portfolio · Desktop + Mobile » vM3iN8qTvu3N8Hj2bvImhB,
page « Portfolio · Relais v1 », cadres de 1305 px), noms listés dans scripts/relais-assets.json
(suffixe = hash du contenu, à cause du cache iPhone).
Les chiffres de résultats (comparaison avec l'ancien site) sont inventés à la demande de Jay : à valider.
Relancer après modification :  python3 scripts/relais.py && python3 scripts/pages.py"""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, 'scripts/relais-assets.json'), encoding='utf-8'))
for f in A.values():
    if not os.path.exists(os.path.join(ROOT, 'projets/relais', f)): raise SystemExit('asset manquant ' + f)
MEDIA = json.dumps(A, ensure_ascii=False)
ART_RC = r""" p=>{/*relais*/const e=shade(p.c,.34),d=shade(p.c,.5),dd=shade(p.c,.64),TX=214,TY=542,R=-20,h=(f,l,r)=>f(l)+`<g clip-path="url(#rck)">${f(r)}</g>`;return `<clipPath id="rck"><rect x="0" y="-800" width="400" height="1200"/></clipPath><polygon points="${ng(10,322,78,38)}" fill="${p.a}"/><path d="M322 40L360 78 322 116Z" fill="${p.b}"/><g transform="translate(${TX} ${TY}) rotate(${R})">${h(c=>`<polygon points="${ng(8,0,-346,84,22.5)}" fill="${c}"/>`,e,d)}<polygon points="${ng(8,0,-346,44,22.5)}" fill="${p.c}"/>${h(c=>`<rect x="-19" y="-270" width="38" height="290" fill="${c}"/><polygon points="${ng(8,0,-262,26,22.5)}" fill="${c}"/>`,e,d)}<path d="M19 -82H96V0H19ZM19 -58H68V-44H19ZM52 -24H96V-12H52Z" fill="${dd}" fill-rule="evenodd"/><path d="M19 -82H96V-72H19Z" fill="${d}"/><path d="M-62 -296L-66 -246" stroke="${dd}" stroke-width="3"/><g transform="rotate(26 -66 -246)"><path d="M-96 -246H-36L-31 -156H-91Z" fill="${d}"/><path d="M-66 -246H-36L-31 -156H-61Z" fill="${dd}"/><circle cx="-66" cy="-231" r="7" fill="${p.c}"/></g></g>`},"""
TITRE = 'Relais & Châteaux'
ENCRE = '[.0415,3.55]'  # largeur de la ligne la plus longue (« Châteaux ») en em, Newsreader Light Italic

P_FR = (" {t:'Relais & Châteaux',x:'relais',ag:'Niji',k:'Hôtellerie · Luxe',y:'2022',c:'#AD9B6F',p:'#EDE6D6',on:'#F3F1EA',a:'#EDE6D6',b:'#C9B88E',"
        "d:'Le site de 580 maisons d’exception, pensé comme un magazine de voyage.',lead:'Ailleurs, autrement.',"
        "ctx:'Refondre relaischateaux.com : faire d’un catalogue de 580 hôtels et restaurants un récit de voyage, sans perdre le chemin de la réservation.',"
        "enj:[['Inspirer','L’image d’abord, la recherche dans le même écran'],['Choisir','La bonne information au bon moment'],['S’offrir','Trois écrans, du rêve au prix'],['Unifier','Un seul système pour 580 maisons']],"
        "role:'Product Designer · Audit de l’ancien site et benchmark de l’hôtellerie de luxe, entretiens voyageurs et équipes réservation, personas et parcours, architecture de l’information (maisons, destinations, inspirations), wireframes, tests utilisateurs, direction artistique éditoriale, UI desktop & mobile, tunnel de réservation (dates, voyageurs, chambres), design system et bibliothèque de composants, accessibilité, prototypes animés, suivi de développement et recette, analyse des KPI après mise en ligne',"
        "m:'928,64 €',ml:'2 nuits à Akelarre',rows:[['Inspiration','Chambres'],['Maison','Akelarre'],['Chambre','Horizon'],['Dates','25 → 27 nov.'],['Voyageurs','2'],['Total','928,64 €']],"
        "st:[['+38 %','de réservations directes en ligne'],['3 clics','de l’accueil aux disponibilités']],ab:[['Avant','7 clics'],['Après','3 clics']],bars:[34,40,46,52,58,63,68,73,78,84,90,96]},")
P_EN = (" {k:'Hospitality · Luxury',d:'The website of 580 exceptional houses, designed like a travel magazine.',lead:'Elsewhere, otherwise.',"
        "ctx:'Redesigning relaischateaux.com: turning a catalogue of 580 hotels and restaurants into a travel story, without losing the way to booking.',"
        "enj:[['Inspire','Image first, search on the same screen'],['Choose','The right information at the right time'],['Indulge','Three screens, from dream to price'],['Unify','One system for 580 houses']],"
        "role:'Product Designer · Audit of the previous site and luxury hospitality benchmark, interviews with travellers and booking teams, personas and journeys, information architecture (houses, destinations, inspirations), wireframes, user testing, editorial art direction, desktop & mobile UI, booking funnel (dates, guests, rooms), design system and component library, accessibility, animated prototypes, development follow-up and QA, post-launch KPI analysis',"
        "m:'€928.64',ml:'2 nights at Akelarre',rows:[['Inspiration','Rooms'],['House','Akelarre'],['Room','Horizon'],['Dates','25 → 27 Nov'],['Guests','2'],['Total','€928.64']],"
        "st:[['+38%','direct online bookings'],['3 clicks','from home page to availability']],ab:[['Before','7 clicks'],['After','3 clicks']]},")

CSS = r'''<style id="rlc-css">
/* Relais & Châteaux : figures exportées de Figma + intro, chiffres en HTML. Préfixe .rc — Taviraj (police éditoriale de la marque) */
#page{--rcf:Taviraj,Newsreader,Georgia,serif;--rcm:"DM Mono",ui-monospace,monospace}
.v.px.rc{background:#F2F1ED}
.rc-intro .q{font:300 italic clamp(22px,2.4vw,32px)/1.22 var(--rcf);letter-spacing:-.01em;max-width:24em;margin:16px 0 clamp(26px,4vw,48px)}
.rc-intro .pc{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.rc-intro .ck{background:var(--bg);color:var(--fg);border-radius:8px;aspect-ratio:16/10;padding:clamp(16px,2vw,28px);display:flex;flex-direction:column;justify-content:space-between;overflow:hidden}
.rc-intro .ck b{font:300 italic clamp(30px,3.6vw,52px)/1 var(--rcf);letter-spacing:-.02em}
.rc-intro .ck span{font:400 11px/1.4 var(--rcm);letter-spacing:.12em;text-transform:uppercase}
.fig figure:not(.vu) .rc-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .rc-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.fig .v.rc-res{height:auto;min-height:0;display:block;border-radius:0;overflow:hidden}
.v.rc-res{background:#0E0F10;color:#F2F1ED;padding:clamp(28px,4.4vw,56px)}
.rc-res>.lb{display:block;font:400 11px/1 var(--rcm);letter-spacing:.14em;text-transform:uppercase;color:#AD9B6F}
.rc-res .h{font:300 italic clamp(30px,3.6vw,48px)/1.08 var(--rcf);letter-spacing:-.01em;margin:clamp(18px,2.4vw,28px) 0 clamp(26px,4vw,48px);max-width:16em}
.rc-res .r{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);align-items:baseline;gap:clamp(14px,2vw,28px);border-top:1px solid rgba(242,241,237,.18);padding:clamp(16px,2vw,24px) 0}
.rc-res .r b{font:300 clamp(40px,5.4vw,76px)/1 var(--rcf);letter-spacing:-.03em;color:#AD9B6F;white-space:nowrap}
.rc-res .r b i{font-style:italic}
.rc-res .r span{font:400 11px/1.6 var(--rcm);letter-spacing:.1em;text-transform:uppercase;color:rgba(242,241,237,.78)}
.rc-res .r span em{display:block;font-style:normal;color:rgba(242,241,237,.45);margin-top:4px}
.rc-res .src{display:block;margin-top:clamp(22px,3vw,36px);font:400 10px/1.6 var(--rcm);letter-spacing:.1em;text-transform:uppercase;color:rgba(242,241,237,.45)}
.rc-intro>*,.rc-res>*{width:100%!important;max-width:none!important;margin-left:0!important;margin-right:0!important}
.rc-intro>.q,.rc-res>.h{padding-right:min(22%,10em)}
.px-chap.rc-c .pw{font:300 italic 1.08em/1.1 var(--rcf);letter-spacing:-.01em}
@media (max-width:899px){.rc-res .r{grid-template-columns:1fr;gap:10px}}
.rc-q{position:relative;background:#0E0F10;color:#F2F1ED;border-radius:8px;padding:clamp(24px,4vw,52px);margin:0 0 10px;overflow:hidden}
#page .rc-q .lb{color:#C9B88E;opacity:1}
.rc-intro .rc-q .q{color:#F2F1ED;margin:14px 0 0;font-size:clamp(22px,2.3vw,32px);line-height:1.24;max-width:none;padding-right:min(18%,7em)}
.rc-q .f{position:absolute;right:clamp(18px,3vw,40px);bottom:clamp(18px,3vw,40px);width:clamp(28px,3vw,40px);aspect-ratio:1;background:#AD9B6F;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 64'%3E%3Cpath d='M30 2C22 14 22 28 30 38 38 28 38 14 30 2ZM28 36C16 40 4 32 6 18 10 28 18 32 28 31ZM32 36C44 40 56 32 54 18 50 28 42 32 32 31ZM18 38H42V44H18ZM25 44L30 60 35 44Z'/%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 64'%3E%3Cpath d='M30 2C22 14 22 28 30 38 38 28 38 14 30 2ZM28 36C16 40 4 32 6 18 10 28 18 32 28 31ZM32 36C44 40 56 32 54 18 50 28 42 32 32 31ZM18 38H42V44H18ZM25 44L30 60 35 44Z'/%3E%3C/svg%3E") center/contain no-repeat}
#page .fig .v.rc-step{display:grid;grid-template-columns:auto 1fr auto;align-items:baseline;gap:12px clamp(12px,2vw,28px);border-top:1px solid rgba(20,20,18,.16);padding:clamp(18px,2.4vw,30px) 0 0}
#page .rc-step>*{margin:0!important;max-width:none!important;width:auto!important;position:static!important;text-align:left!important;justify-self:start}
.rc-step .n{font:400 11px/1 var(--rcm);letter-spacing:.14em;color:#AD9B6F}
.rc-step .w{margin:0;font:300 italic clamp(40px,5vw,72px)/1.12 var(--rcf);letter-spacing:-.02em;color:#141412}
.rc-step .d{font:400 11px/1.5 var(--rcm);letter-spacing:.1em;text-transform:uppercase;color:#77746B;text-align:right;max-width:18em}
@media (max-width:899px){#page .fig .v.rc-step{grid-template-columns:auto 1fr}.rc-step .d{grid-column:1/-1;text-align:left;max-width:none}.rc-intro .rc-q .q{padding-right:0;padding-bottom:44px}}
@media (max-width:899px){
#page .rc-q{padding:30px 24px 34px}
#page .rc-intro .rc-q .q{font-size:24px;line-height:1.32;margin-top:18px;padding-bottom:52px}
#page .rc-q .f{right:24px;bottom:26px;width:26px}
#page .rc-intro .pc{gap:10px}
#page .rc-intro .ck{aspect-ratio:3/4.4;padding:18px}
#page .rc-intro .ck b{font-size:32px;line-height:1.05}
#page .rc-intro .ck span{font-size:10px;line-height:1.7;letter-spacing:.1em}
}
#page .rc-intro .ck{position:relative;isolation:isolate;justify-content:flex-end;gap:10px;color:#F3F1EA}
#page .rc-intro .ck .im{position:absolute;inset:0;z-index:-2;margin:0!important;background-repeat:no-repeat;transform:scale(1.04);transition:transform 1.4s cubic-bezier(.2,.7,.2,1)}
#page .rc-intro .ck::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(14,15,16,0) 30%,rgba(14,15,16,.38) 58%,rgba(14,15,16,.82) 100%)}
.fig figure.vu .rc-intro .ck .im{transform:scale(1)}
#page .rc-intro .ck b,#page .rc-intro .ck span{color:#F3F1EA}
#page .rc-intro .ck span{opacity:.86}
@media (prefers-reduced-motion:reduce){.fig figure .rc-intro .ck{opacity:1;transform:none;transition:none}}
</style>
'''

JS = r'''/* Relais & Châteaux : figures réelles (projet marqué x:'relais'). chiffres de résultats à valider. */
const RCI='/projets/relais/',RCM=__MEDIA__;
const RCT={fr:{defi:'Le projet',q:'580 hôtels et restaurants, 65 pays. Un site qui donne envie de partir avant de faire choisir.',
 st:[['Inspirer','L’image d’abord, la recherche dans le même écran','#AD9B6F','#0E0F10'],['Choisir','La bonne information au bon moment','#F2F1ED','#0E0F10'],['S’offrir','Trois écrans, du rêve au prix','#0E0F10','#F2F1ED'],['Unifier','Un seul système pour 580 maisons','#3A3128','#EDE6D6']],
 steps:[['01','Inspirer','Des chambres, une galerie, l’envie de partir'],['02','Choisir','Les dates, les voyageurs, les critères'],['03','S’offrir','Le prix, au moment où l’envie est là']],
 chap:[['L’image','Le voyage commence par une émotion.','#AD9B6F'],['La maison','Une maison se lit comme un récit.','#3A3128'],['Le séjour','De l’inspiration au prix, en trois écrans.','#0E0F10'],['Le système','Clarté. Rythme. Précision.','#696969'],['L’univers','Magazine, coffrets, itinéraires, engagements.','#AD9B6F'],['Résultats','Ce qui a changé face à l’ancien site.','#0E0F10']],
 res:['Six mois après la mise en ligne','Moins de clics, plus d’envie, plus de réservations.',[['+38 %','réservations directes en ligne'],['3 <i>clics</i>','de l’accueil aux disponibilités','contre 7 auparavant'],['−41 %','d’abandon entre les dates et le paiement'],['+46 %','de conversion sur mobile','64 % des visites'],['+52 %','de temps passé sur les fiches maisons'],['×2,4','coffrets cadeaux vendus en ligne'],['1,6 <i>s</i>','pour afficher l’accueil','contre 4,3 s'],['96','score d’accessibilité Lighthouse','contre 68']],'Comparaison avec l’ancien site'],
 alt:['L’accueil « ailleurs autrement » sur desktop et sur iPhone, devant le mot « ailleurs » en or','Ouverture plein cadre d’Akelarre, « Au bord de l’horizon »','La fiche Akelarre qui défile dans un iPhone, la navigation reste collée en haut','Trois iPhone posés : chambres d’exception, chambre Supérieure Horizon, galerie d’Akelarre','La page chambre Supérieure Horizon sur desktop, avec une loupe sur la ligne de critères','La destination France sur desktop et sur iPhone','La galerie d’Akelarre en six photos','Noir, papier, or, ligne et brume','Taviraj et Jost, alphabet et bouton','Une même carte au repos, au survol et en focus clavier, puis les boutons et les champs','TravelBook, coffrets et Routes du Bonheur sur trois iPhone','La page « En harmonie avec le vivant » et ses engagements','Affiche « Ailleurs, autrement. » sur un mur de ville','L’accueil desktop sur un Studio Display','La fiche Akelarre sur un iPhone tenu en main','Le séjour à 928,64 € sur un iPhone tenu en main','La table d’Anne de Bretagne sur iPhone, avec le choix des dates et des voyageurs'],
 cap:{affiche:'Affichage · la campagne prolonge l’accueil',display:'Accueil · l’image ouvre, la recherche suit',immersion:'Akelarre · ouverture plein cadre',galerie:'Galerie · six vues, une maison',main:'Fiche maison · mobile',maison:'Fiche maison · défilement complet',destination:'Destination · comparer sans quitter le rêve',parcours:'Parcours · inspirer, choisir, réserver',choisir:'Choisir · la chambre au centre',"main-sejour":'Réserver · le prix au bon moment',sejour:'Disponibilités · le total, sans surprise',couleurs:'Couleurs · deux nuances et de l’or',typo:'Typographie · Taviraj et Jost',composants:'Composants · repos, survol, focus',contenus:'Univers · magazine, coffrets, itinéraires',engagements:'Engagements · en harmonie avec le vivant'}},
 en:{defi:'The project',q:'580 hotels and restaurants, 65 countries. A site that makes you want to leave before it asks you to choose.',
 st:[['Inspire','Image first, search on the same screen','#AD9B6F','#0E0F10'],['Choose','The right information at the right time','#F2F1ED','#0E0F10'],['Indulge','Three screens, from dream to price','#0E0F10','#F2F1ED'],['Unify','One system for 580 houses','#3A3128','#EDE6D6']],
 steps:[['01','Inspire','Rooms, a gallery, the urge to go'],['02','Choose','Dates, guests, criteria'],['03','Indulge','The price, right when the desire is there']],
 chap:[['The image','A journey starts with an emotion.','#AD9B6F'],['The house','A house reads like a story.','#3A3128'],['The stay','From inspiration to price, in three screens.','#0E0F10'],['The system','Clarity. Rhythm. Precision.','#696969'],['The world','Magazine, gift boxes, road trips, commitments.','#AD9B6F'],['Results','What changed compared with the previous site.','#0E0F10']],
 res:['Six months after launch','Fewer clicks, more desire, more bookings.',[['+38%','direct online bookings'],['3 <i>clicks</i>','from home page to availability','down from 7'],['−41%','drop-off between dates and payment'],['+46%','mobile conversion','64% of visits'],['+52%','time spent on house pages'],['×2.4','gift boxes sold online'],['1.6 <i>s</i>','to load the home page','down from 4.3 s'],['96','Lighthouse accessibility score','up from 68']],'Compared with the previous site'],
 alt:['The “ailleurs autrement” home page on desktop and iPhone, in front of the word “ailleurs” in gold','Full-bleed opening of Akelarre, “On the edge of the horizon”','The Akelarre house page scrolling on an iPhone, with the navigation pinned at the top','Three iPhones laid down: exceptional rooms, the Superior Horizon room, Akelarre’s gallery','The Superior Horizon room page on desktop, with a magnifier on the criteria line','The France destination page on desktop and iPhone','Akelarre’s gallery in six photos','Black, paper, gold, line and mist','Taviraj and Jost, alphabet and button','One card at rest, on hover and on keyboard focus, then buttons and fields','TravelBook, gift boxes and Routes du Bonheur on three iPhones','The “In harmony with the living” page and its commitments','“Ailleurs, autrement.” poster on a city wall','The desktop home page on a Studio Display','The Akelarre house page on a hand-held iPhone','The €928.64 stay on a hand-held iPhone','Anne de Bretagne’s restaurant on iPhone, with date and guest pickers'],
 cap:{affiche:'Out of home · the campaign extends the home page',display:'Home · the image opens, search follows',immersion:'Akelarre · full-bleed opening',galerie:'Gallery · six views, one house',main:'House page · mobile',maison:'House page · full scroll',destination:'Destination · compare without leaving the dream',parcours:'Journey · inspire, choose, book',choisir:'Choose · the room at the centre',"main-sejour":'Book · the price at the right time',sejour:'Availability · the total, no surprises',couleurs:'Colours · two shades and gold',typo:'Typography · Taviraj and Jost',composants:'Components · rest, hover, focus',contenus:'World · magazine, gift boxes, road trips',engagements:'Commitments · in harmony with the living'}}};
const RCK=[['carte-inspirer','cover','50% 60%'],['carte-choisir','cover','50% 45%'],['carte-soffrir','cover','50% 52%'],['carte-unifier','cover','62% 70%']];
const RIMG=(n,r,alt,c)=>`<div class="v rx px rc" style="aspect-ratio:${r}"><img src="${RCI}${n}" alt="${alt}" loading="lazy"></div>${c?`<p class="rc-cap"><span>${c[0]}</span>${c[1]}</p>`:''}`;
const RVID=(v,po,r,alt)=>`<div class="v rx px rc" style="aspect-ratio:${r};background:#E7E2D6 url(${RCI}${po}) center/cover no-repeat"><video class="pv" muted playsinline preload="none" loop poster="${RCI}${po}" data-src="${RCI}${v}" aria-label="${alt}"></video></div>`;
const RSTEP=s=>`<div class="v rx px-t rc-step"><span class="n">${s[0]}</span><p class="w">${s[1]}</p><span class="d">${s[2]}</span></div>`;
const RCHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap rc-c');
function rlcFigs(q){
 const T=RCT[lang]||RCT.fr,a=T.alt,M=RCM,C=T.chap,K=T.cap;let n=0;const F=()=>'Fig. '+String(++n).padStart(2,'0');
 const I=(k,r,i)=>[RIMG(M[k],r,a[i]),''];
 const intro=`<div class="v rx px-t rc-intro"><div class="rc-q"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><span class="f" aria-hidden="true"></span></div><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--bg:${s[2]};--fg:${s[3]};--d:${k*110}ms"><i class="im" aria-hidden="true" style="background-image:url(${RCI}${M[RCK[k][0]]});background-size:${RCK[k][1]};background-position:${RCK[k][2]}"></i><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const res=`<div class="v rx rc-res"><span class="lb px-t">${T.res[0]}</span><p class="h px-t">${T.res[1]}</p>${T.res[2].map(r=>`<div class="r"><b>${r[0]}</b><span>${r[1]}${r[2]?`<em>${r[2]}</em>`:''}</span></div>`).join('')}<span class="src">${T.res[3]}</span></div>`;
 return [
  I('affiche','1958/1468',12,'z-full'), [intro,'z-txt'], I('display','1958/1468',13,'z-r'),
  [RCHAP('01 / 05',C[0]),'z-ch'], I('immersion','1305/753',1,'z-full'), I('galerie','1305/722',6,'z-l'), I('main','1958/1468',14,'z-r z-up'),
  [RCHAP('02 / 05',C[1]),'z-ch'], [RVID(M.defilement,M['defilement-poster'],'1306/1000',a[2]),''], I('destination','1305/960',5,'z-l'),
  [RCHAP('03 / 05',C[2]),'z-ch'], [RSTEP(T.steps[0]),''], I('parcours','1305/1000',3,'z-full'), [RSTEP(T.steps[1]),''], I('choisir','1305/1000',16,'z-h1'), I('sejour','1305/940',4,'z-r'), [RSTEP(T.steps[2]),''], I('main-sejour','1958/1468',15,'z-h2'),
  [RCHAP('04 / 05',C[3]),'z-ch'], I('couleurs','1305/840',7,'z-h1'), I('typo','1305/980',8,'z-h2'), I('composants','1305/1029',9,'z-txt'),
  [RCHAP('05 / 05',C[4]),'z-ch'], I('contenus','1305/1000',10,'z-full'), I('engagements','1305/900',11,'z-l'),
  [RCHAP('relaischateaux.com',C[5]),'z-ch'], [res,'z-full z-res']
 ].map(([x])=>[x,'']);
}
'''.replace('__MEDIA__', MEDIA)

for name in ['index.html', 'fr/index.html']:
    p = os.path.join(ROOT, name); s = open(p, encoding='utf-8').read()
    a = s.index('const P=['); b = s.index('];', a)
    lines = s[a:b].split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith(" {t:'Comptoir'") or l.startswith(" {t:'Relais & Châteaux'"))
    lines[i] = P_FR; s = s[:a] + '\n'.join(lines) + s[b:]
    a = s.index('const EN=['); b = s.index('];', a)
    lines = s[a:b].split('\n'); en = [k for k, l in enumerate(lines) if l.startswith(' {')]
    lines[en[i - 1]] = P_EN; s = s[:a] + '\n'.join(lines) + s[b:]
    a = s.index('const ENCRE={'); b = s.index('};', a)
    enc = s[a:b]
    if "'Relais & Châteaux':[" in enc:
        import re
        enc = re.sub(r"'Relais & Châteaux':\[[^\]]*\]", "'Relais & Châteaux':" + ENCRE, enc)
    else:
        enc = enc.replace("const ENCRE={", "const ENCRE={'Relais & Châteaux':" + ENCRE + ",", 1)
    s = s[:a] + enc + s[b:]
    s = s.replace("const TT=t=>t==='Route du Rhum'?'Route du\\nRhum':t;",
                  "const TT=t=>t==='Route du Rhum'?'Route du\\nRhum':t==='Relais & Châteaux'?'Relais & \\nChâteaux':t;")
    if '<style id="rlc-css">' in s:
        a = s.index('<style id="rlc-css">'); b = s.index('</style>', a) + len('</style>\n'); s = s[:a] + CSS + s[b:]
    else:
        a = s.index('<style id="dlk-css">'); s = s[:a] + CSS + s[a:]
    mark = "/* Relais & Châteaux : figures réelles"
    if mark in s:
        a = s.index(mark); b = s.index("/* Dalkia : figures réelles"); s = s[:a] + JS + s[b:]
    else:
        b = s.index("/* Dalkia : figures réelles"); s = s[:b] + JS + s[b:]
    s = s.replace("`<figure${q.x==='relais'&&cap?` class=\"${cap}\"`:''}>${x}".replace('\\"', '"'), "`<figure>${x}")
    s = s.replace('<div class="pj l2${q.x===\'relais\'?\' rcx\':\'\'}"><div class="cols">', '<div class="pj l2"><div class="cols">')
    a = s.index('const ART=['); b = s.index('\n];', a)
    L = s[a:b].split('\n')
    k = next(i for i, l in enumerate(L) if l.startswith(" p=>{const s=[...Array(7)]") or '/*relais*/' in l)
    L[k] = ART_RC; s = s[:a] + '\n'.join(L) + s[b:]
    s = s.replace("q.x==='dalkia'?dlkFigs(q):rdrFigs(q)", "q.x==='dalkia'?dlkFigs(q):q.x==='relais'?rlcFigs(q):rdrFigs(q)")
    if 'family=Taviraj' not in s:
        s = s.replace('&family=Montserrat:', '&family=Taviraj:ital,wght@0,300;1,300&family=Montserrat:', 1)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
