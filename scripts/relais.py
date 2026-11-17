#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute / réécrit le projet Relais & Châteaux (x:'relais', à la place du fictif Comptoir) dans index.html et fr/index.html.
Figures exportées de Figma (fichier « Relais & Châteaux · Portfolio · Desktop + Mobile » vM3iN8qTvu3N8Hj2bvImhB,
page « Portfolio · Relais v1 », cadres de 1305 px), noms listés dans scripts/relais-assets.json
(suffixe = hash du contenu, à cause du cache iPhone). Écrans reconstitués à partir du site public.
Les chiffres de résultats (comparaison avec l'ancien site) sont inventés à la demande de Jay : à valider.
Relancer après modification :  python3 scripts/relais.py && python3 scripts/pages.py"""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, 'scripts/relais-assets.json'), encoding='utf-8'))
for f in A.values():
    if not os.path.exists(os.path.join(ROOT, 'projets/relais', f)): raise SystemExit('asset manquant ' + f)
MEDIA = json.dumps(A, ensure_ascii=False)
ART_RC = r""" p=>{/*relais*/const d=shade(p.c,.46),e=shade(p.c,.32),m=shade(p.c,.16),dd=shade(p.c,.6),cx=196,cy=360,h=(f,l,r)=>f(l)+`<g clip-path="url(#rck)">${f(r)}</g>`;return `<clipPath id="rck"><rect x="200" y="-400" width="600" height="1400"/></clipPath><polygon points="${ng(10,322,78,38)}" fill="${p.a}"/><path d="M322 40L360 78 322 116Z" fill="${p.b}"/><g transform="translate(6 34)"><g transform="rotate(-35 ${cx} ${cy})">${h(c=>`<polygon points="${ng(8,200,96,84,22.5)}" fill="${c}"/>`,m,e)}<polygon points="${ng(8,200,96,44,22.5)}" fill="${p.c}"/>${h(c=>`<rect x="181" y="172" width="38" height="270" fill="${c}"/><polygon points="${ng(8,200,180,26,22.5)}" fill="${c}"/>`,m,e)}<path d="M219 360H296V442H219ZM219 384H268V398H219ZM252 418H296V430H252Z" fill="${d}" fill-rule="evenodd"/><path d="M219 360H296V370H219Z" fill="${e}"/></g><path d="M46 184L48 234" stroke="${dd}" stroke-width="3"/><g transform="rotate(6 48 234)"><path d="M18 234H78L83 324H23Z" fill="${p.a}"/><path d="M48 234H78L83 324H53Z" fill="${p.b}"/><circle cx="48" cy="249" r="7" fill="${p.c}"/></g></g>`},"""
TITRE = 'Relais & Châteaux'
ENCRE = '[.0415,3.55]'  # largeur de la ligne la plus longue (« Châteaux ») en em, Newsreader Light Italic

P_FR = (" {t:'Relais & Châteaux',x:'relais',ag:'Niji',k:'Hôtellerie · Luxe',y:'2022',c:'#AD9B6F',p:'#EDE6D6',on:'#F3F1EA',a:'#EDE6D6',b:'#C9B88E',"
        "d:'Le site de 580 maisons d’exception, pensé comme un magazine de voyage.',lead:'Ailleurs, autrement.',"
        "ctx:'Refondre relaischateaux.com : faire d’un catalogue de 580 hôtels et restaurants un récit de voyage, sans perdre le chemin de la réservation.',"
        "enj:[['Inspirer','L’image d’abord, la recherche dans le même écran'],['Choisir','La bonne information au bon moment'],['Réserver','Trois écrans, du rêve au prix'],['Unifier','Un seul système pour 580 maisons']],"
        "role:'Product Designer · Audit de l’ancien site et benchmark de l’hôtellerie de luxe, entretiens voyageurs et équipes réservation, personas et parcours, architecture de l’information (maisons, destinations, inspirations), wireframes, tests utilisateurs, direction artistique éditoriale, UI desktop & mobile, tunnel de réservation (dates, voyageurs, chambres), design system et bibliothèque de composants, accessibilité, prototypes animés, suivi de développement et recette, analyse des KPI après mise en ligne',"
        "m:'928,64 €',ml:'2 nuits à Akelarre',rows:[['Inspiration','Chambres'],['Maison','Akelarre'],['Chambre','Horizon'],['Dates','25 → 27 nov.'],['Voyageurs','2'],['Total','928,64 €']],"
        "st:[['+38 %','de réservations directes en ligne'],['3 clics','de l’accueil aux disponibilités']],ab:[['Avant','7 clics'],['Après','3 clics']],bars:[34,40,46,52,58,63,68,73,78,84,90,96]},")
P_EN = (" {k:'Hospitality · Luxury',d:'The website of 580 exceptional houses, designed like a travel magazine.',lead:'Elsewhere, otherwise.',"
        "ctx:'Redesigning relaischateaux.com: turning a catalogue of 580 hotels and restaurants into a travel story, without losing the way to booking.',"
        "enj:[['Inspire','Image first, search on the same screen'],['Choose','The right information at the right time'],['Book','Three screens, from dream to price'],['Unify','One system for 580 houses']],"
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
@media (prefers-reduced-motion:reduce){.fig figure .rc-intro .ck{opacity:1;transform:none;transition:none}}
</style>
'''

JS = r'''/* Relais & Châteaux : figures réelles (projet marqué x:'relais'). Écrans reconstitués à partir du site public ; chiffres de résultats à valider. */
const RCI='/projets/relais/',RCM=__MEDIA__;
const RCT={fr:{defi:'Le projet',q:'Relais & Châteaux réunit 580 hôtels et restaurants dans 65 pays. Le site devait donner envie de partir avant de faire choisir : l’image ouvre chaque page, la réservation reste à portée de main.',
 st:[['Inspirer','L’image d’abord, la recherche dans le même écran','#AD9B6F','#0E0F10'],['Choisir','La bonne information au bon moment','#F2F1ED','#0E0F10'],['Réserver','Trois écrans, du rêve au prix','#0E0F10','#F2F1ED'],['Unifier','Un seul système pour 580 maisons','#3A3128','#EDE6D6']],
 chap:[['L’image','Le voyage commence par une émotion.','#AD9B6F'],['La maison','Une maison se lit comme un récit.','#3A3128'],['Le séjour','De l’inspiration au prix, en trois écrans.','#0E0F10'],['Le système','Clarté. Rythme. Précision.','#696969'],['L’univers','Magazine, coffrets, itinéraires, engagements.','#AD9B6F'],['Résultats','Ce qui a changé face à l’ancien site.','#0E0F10']],
 res:['Six mois après la mise en ligne','Moins de clics, plus d’envie, plus de réservations.',[['+38 %','réservations directes en ligne'],['3 <i>clics</i>','de l’accueil aux disponibilités','contre 7 auparavant'],['−41 %','d’abandon entre les dates et le paiement'],['+46 %','de conversion sur mobile','64 % des visites'],['+52 %','de temps passé sur les fiches maisons'],['×2,4','coffrets cadeaux vendus en ligne'],['1,6 <i>s</i>','pour afficher l’accueil','contre 4,3 s'],['96','score d’accessibilité Lighthouse','contre 68']],'Comparaison avec l’ancien site'],
 alt:['L’accueil « ailleurs autrement » sur desktop et sur iPhone, devant le mot « ailleurs » en or','Ouverture plein cadre d’Akelarre, « Au bord de l’horizon »','La fiche Akelarre qui défile dans un iPhone, la navigation reste collée en haut','Trois iPhone posés : chambres d’exception, chambre Supérieure Horizon, galerie d’Akelarre','La page chambre Supérieure Horizon sur desktop, avec une loupe sur la ligne de critères','La destination France sur desktop et sur iPhone','La galerie d’Akelarre en six photos','Noir, papier, or, ligne et brume','Taviraj et Jost, alphabet et bouton','Une même carte au repos, au survol et en focus clavier, puis les boutons et les champs','TravelBook, coffrets et Routes du Bonheur sur trois iPhone','La page « En harmonie avec le vivant » et ses engagements','Affiche « Ailleurs, autrement. » sur un mur de ville','L’accueil desktop sur un Studio Display','La fiche Akelarre sur un iPhone tenu en main','Le séjour à 928,64 € sur un iPhone tenu en main','La table d’Anne de Bretagne sur iPhone, avec le choix des dates et des voyageurs'],
 cap:{affiche:'Affichage · la campagne prolonge l’accueil',display:'Accueil · l’image ouvre, la recherche suit',immersion:'Akelarre · ouverture plein cadre',galerie:'Galerie · six vues, une maison',main:'Fiche maison · mobile',maison:'Fiche maison · défilement complet',destination:'Destination · comparer sans quitter le rêve',parcours:'Parcours · inspirer, choisir, réserver',choisir:'Choisir · la chambre au centre',"main-sejour":'Réserver · le prix au bon moment',sejour:'Disponibilités · le total, sans surprise',couleurs:'Couleurs · deux nuances et de l’or',typo:'Typographie · Taviraj et Jost',composants:'Composants · repos, survol, focus',contenus:'Univers · magazine, coffrets, itinéraires',engagements:'Engagements · en harmonie avec le vivant'}},
 en:{defi:'The project',q:'Relais & Châteaux brings together 580 hotels and restaurants in 65 countries. The site had to make people want to travel before asking them to choose: an image opens every page, booking stays within reach.',
 st:[['Inspire','Image first, search on the same screen','#AD9B6F','#0E0F10'],['Choose','The right information at the right time','#F2F1ED','#0E0F10'],['Book','Three screens, from dream to price','#0E0F10','#F2F1ED'],['Unify','One system for 580 houses','#3A3128','#EDE6D6']],
 chap:[['The image','A journey starts with an emotion.','#AD9B6F'],['The house','A house reads like a story.','#3A3128'],['The stay','From inspiration to price, in three screens.','#0E0F10'],['The system','Clarity. Rhythm. Precision.','#696969'],['The world','Magazine, gift boxes, road trips, commitments.','#AD9B6F'],['Results','What changed compared with the previous site.','#0E0F10']],
 res:['Six months after launch','Fewer clicks, more desire, more bookings.',[['+38%','direct online bookings'],['3 <i>clicks</i>','from home page to availability','down from 7'],['−41%','drop-off between dates and payment'],['+46%','mobile conversion','64% of visits'],['+52%','time spent on house pages'],['×2.4','gift boxes sold online'],['1.6 <i>s</i>','to load the home page','down from 4.3 s'],['96','Lighthouse accessibility score','up from 68']],'Compared with the previous site'],
 alt:['The “ailleurs autrement” home page on desktop and iPhone, in front of the word “ailleurs” in gold','Full-bleed opening of Akelarre, “On the edge of the horizon”','The Akelarre house page scrolling on an iPhone, with the navigation pinned at the top','Three iPhones laid down: exceptional rooms, the Superior Horizon room, Akelarre’s gallery','The Superior Horizon room page on desktop, with a magnifier on the criteria line','The France destination page on desktop and iPhone','Akelarre’s gallery in six photos','Black, paper, gold, line and mist','Taviraj and Jost, alphabet and button','One card at rest, on hover and on keyboard focus, then buttons and fields','TravelBook, gift boxes and Routes du Bonheur on three iPhones','The “In harmony with the living” page and its commitments','“Ailleurs, autrement.” poster on a city wall','The desktop home page on a Studio Display','The Akelarre house page on a hand-held iPhone','The €928.64 stay on a hand-held iPhone','Anne de Bretagne’s restaurant on iPhone, with date and guest pickers'],
 cap:{affiche:'Out of home · the campaign extends the home page',display:'Home · the image opens, search follows',immersion:'Akelarre · full-bleed opening',galerie:'Gallery · six views, one house',main:'House page · mobile',maison:'House page · full scroll',destination:'Destination · compare without leaving the dream',parcours:'Journey · inspire, choose, book',choisir:'Choose · the room at the centre',"main-sejour":'Book · the price at the right time',sejour:'Availability · the total, no surprises',couleurs:'Colours · two shades and gold',typo:'Typography · Taviraj and Jost',composants:'Components · rest, hover, focus',contenus:'World · magazine, gift boxes, road trips',engagements:'Commitments · in harmony with the living'}}};
const RIMG=(n,r,alt,c)=>`<div class="v rx px rc" style="aspect-ratio:${r}"><img src="${RCI}${n}" alt="${alt}" loading="lazy"></div>${c?`<p class="rc-cap"><span>${c[0]}</span>${c[1]}</p>`:''}`;
const RVID=(v,po,r,alt)=>`<div class="v rx px rc" style="aspect-ratio:${r};background:#E7E2D6 url(${RCI}${po}) center/cover no-repeat"><video class="pv" muted playsinline preload="none" loop poster="${RCI}${po}" data-src="${RCI}${v}" aria-label="${alt}"></video></div>`;
const RCHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap rc-c');
function rlcFigs(q){
 const T=RCT[lang]||RCT.fr,a=T.alt,M=RCM,C=T.chap,K=T.cap;let n=0;const F=()=>'Fig. '+String(++n).padStart(2,'0');
 const I=(k,r,i)=>[RIMG(M[k],r,a[i]),''];
 const intro=`<div class="v rx px-t rc-intro"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--bg:${s[2]};--fg:${s[3]};--d:${k*110}ms"><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const res=`<div class="v rx rc-res"><span class="lb px-t">${T.res[0]}</span><p class="h px-t">${T.res[1]}</p>${T.res[2].map(r=>`<div class="r"><b>${r[0]}</b><span>${r[1]}${r[2]?`<em>${r[2]}</em>`:''}</span></div>`).join('')}<span class="src">${T.res[3]}</span></div>`;
 return [
  I('affiche','1958/1468',12,'z-full'), [intro,'z-txt'], I('display','1958/1468',13,'z-r'),
  [RCHAP('01 / 05',C[0]),'z-ch'], I('immersion','1305/753',1,'z-full'), I('galerie','1305/722',6,'z-l'), I('main','1958/1468',14,'z-r z-up'),
  [RCHAP('02 / 05',C[1]),'z-ch'], [RVID(M.defilement,M['defilement-poster'],'1306/1000',a[2]),''], I('destination','1305/960',5,'z-l'),
  [RCHAP('03 / 05',C[2]),'z-ch'], I('parcours','1305/1000',3,'z-full'), I('choisir','1305/1000',16,'z-h1'), I('main-sejour','1958/1468',15,'z-h2'), I('sejour','1305/940',4,'z-r'),
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
