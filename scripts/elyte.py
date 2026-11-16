#!/usr/bin/env python3
"""Ajoute / réécrit le projet Elyte Club (x:'elyte', à la place de Noria) dans index.html et fr/index.html.
Figures exportées de Figma (fichier « Elyte Club — page projet (ébauches) », page « Portfolio · Elyte v2 »),
noms de fichiers listés dans scripts/elyte-assets.json (suffixe = hash du contenu, à cause du cache iPhone).
Relancer après modification :  python3 scripts/elyte.py && python3 scripts/pages.py"""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, 'scripts/elyte-assets.json'), encoding='utf-8'))
for k, v in A.items():
    for f in (v if isinstance(v, list) else [v]):
        if not os.path.exists(os.path.join(ROOT, 'projets/elyte', f)): raise SystemExit('asset manquant ' + f)
MEDIA = json.dumps(A, ensure_ascii=False)

P_FR = (" {t:'Elyte Club',x:'elyte',ag:'Daké',k:'Sport · Danse',y:'2026',c:'#FF6A2B',p:'#FFD8C4',on:'#F3F1EA',a:'#FFD8C4',b:'#F6956A',"
        "d:'La plateforme de la ligue de battle des anciens d’Elyte Studio.',lead:'Le battle, toute l’année.',"
        "ctx:'Elyte Studio forme des danseurs en six mois. Elyte Club leur donne une ligue : deux groupes, des battles chaque mois, un classement ELO et des playoffs.',"
        "enj:[['Progresser','Un battle par mois, des points à chaque duel'],['Se situer','Son rang et sa zone playoffs, en un regard'],['Organiser','Le soir du battle, tout se saisit sur place'],['Partager','Un visuel prêt à poster pour chaque battle']],"
        "role:'Product Designer & développeur · Cadrage avec le staff, direction artistique, design system, app web (classement, battles, playoffs, espace danseur), back-office, visuels de partage, vidéo explicative · App web responsive',"
        "m:'1301',ml:'ELO du leader',rows:[['1. Kaze','1301'],['2. Lyna','1268'],['3. Imani','1265'],['4. Nova','1263'],['5. Noa','1229'],['6. Yuna','1229']],"
        "st:[['2','groupes, un classement chacun'],['32','qualifiés en playoffs']],ab:[['Avant','Tableur'],['Après','Ligue']],bars:[44,48,52,50,58,62,60,68,72,70,78,84]},")
P_EN = (" {k:'Sport · Dance',d:'The platform for the Elyte Studio alumni battle league.',lead:'Battles, all year round.',"
        "ctx:'Elyte Studio trains dancers in six months. Elyte Club gives them a league: two groups, monthly battles, an ELO ranking and playoffs.',"
        "enj:[['Grow','One battle a month, points on every duel'],['Know where you stand','Your rank and playoff zone at a glance'],['Run the night','Everything is entered on the spot'],['Share','A ready-to-post visual for every battle']],"
        "role:'Product Designer & developer · Scoping with the staff, art direction, design system, web app (rankings, battles, playoffs, dancer area), back office, share visuals, explainer video · Responsive web app',"
        "ml:'leader’s ELO',st:[['2','groups, one ranking each'],['32','playoff spots']],ab:[['Before','Spreadsheet'],['After','League']]},")

CSS = r'''<style id="ely-css">
/* Elyte Club : figures exportées de Figma + intro typographique. Préfixe .ey — titres en Zalando Sans Expanded, chiffres en Doto */
#page{--eyd:"Zalando Sans Expanded",Archivo,system-ui,sans-serif}
.v.px.ey{background:#0C1116}
.ey-intro .q{font:600 clamp(21px,2.3vw,31px)/1.14 var(--eyd);letter-spacing:-.025em;max-width:24em;margin:16px 0 clamp(26px,4vw,48px)}
.ey-intro .pc{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.ey-intro .ck{background:var(--bg);color:var(--fg);border-radius:10px;aspect-ratio:3/3.9;padding:clamp(14px,1.4vw,20px);display:flex;flex-direction:column;justify-content:space-between;overflow:hidden}
.ey-intro .ck b{font:700 clamp(34px,4.2vw,60px)/.9 Doto,"Geist Mono",ui-monospace,monospace;letter-spacing:-.02em}
.ey-intro .ck span{font:400 11px/1.4 "DM Mono",ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase}
.fig figure:not(.vu) .ey-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .ey-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.px-chap.ey-c .pw{font:500 12px/1.4 var(--eyd);letter-spacing:.08em}
@media (max-width:899px){.ey-intro .pc{grid-template-columns:1fr 1fr}}
@media (prefers-reduced-motion:reduce){.fig figure .ey-intro .ck{opacity:1;transform:none;transition:none}}
</style>
'''

JS = r'''/* Elyte Club : figures réelles (projet marqué x:'elyte'). Vidéos exportées de l'animation Figma, lues par picGo (video.pv). */
const EI='/projets/elyte/',EM=__MEDIA__;
const ETX={fr:{defi:'Le projet',q:'Une ligue de battle pour les anciens d’Elyte Studio. Deux dimanches par mois, un classement ELO, et au bout, Amsterdam.',
 st:[['200+','anciens élèves','#FF6A2B','#FFFFFF'],['2','groupes, un classement chacun','#EDE6DA','#141412'],['32','qualifiés en playoffs','#5B4A41','#FFFFFF'],['500 €','et une place à Amsterdam','#123A3C','#FFFFFF']],
 chap:[['Marque','Un écusson, des points, un ticket.','#FF6A2B'],['Le classement','Chaque point se voit.','#123A3C'],['Le dimanche','Du tirage au verdict.','#5B4A41'],['Le système','Des jetons au back-office.','#0C1116']],
 alt:['« Elyte Club » défile sur fond orange autour de la marque en S','L’écusson Elyte Club et la marque en S','Accréditation de battle portée au cou, dérivée du ticket du site','Les cinq couleurs : nuit, orange, crème, taupe, pétrole','Zalando Sans Expanded, Doto et Geist Mono','Trois directions graphiques comparées sur le même classement','Classement du groupe A sur desktop','Jauge des playoffs : le curseur glisse jusqu’à « Qualifié. »','Classement, profil et espace danseur sur trois iPhone','Un duel : le vainqueur passe sur l’aplat crème','Feuille de match d’un battle','Stories de partage d’un battle et d’un danseur','Page d’un battle et playoffs sur deux iPhone','Page des playoffs sur desktop','Six composants du design system','Fondations du design system : couleurs et contrastes','Vue d’ensemble du back-office','Saisie des résultats d’un battle']},
 en:{defi:'The project',q:'A battle league for Elyte Studio alumni. Two Sundays a month, an ELO ranking, and Amsterdam at the end of it.',
 st:[['200+','alumni','#FF6A2B','#FFFFFF'],['2','groups, one ranking each','#EDE6DA','#141412'],['32','playoff spots','#5B4A41','#FFFFFF'],['€500','and a trip to Amsterdam','#123A3C','#FFFFFF']],
 chap:[['Brand','A crest, dots and a ticket.','#FF6A2B'],['The ranking','Every point shows.','#123A3C'],['Battle Sunday','From the draw to the verdict.','#5B4A41'],['The system','From tokens to the back office.','#0C1116']],
 alt:['“Elyte Club” scrolling on orange around the S mark','The Elyte Club crest and S mark','Battle accreditation on a lanyard, based on the site’s ticket','The five colours: night, orange, cream, taupe, petrol','Zalando Sans Expanded, Doto and Geist Mono','Three art directions compared on the same ranking','Group A ranking on desktop','Playoff gauge: the marker slides to “Qualifié.”','Ranking, profile and dancer area on three iPhones','A duel: the winner switches to the cream fill','Battle match sheet','Share stories for a battle and a dancer','Battle page and playoffs on two iPhones','Playoffs page on desktop','Six design system components','Design system foundations: colours and contrast','Back office overview','Entering a battle’s results']}};
const EV=(n,r,alt)=>`<div class="v rx px ey" style="aspect-ratio:${r};background:#0C1116 url(${EI}${n[1]}) center/cover no-repeat"><video class="pv" muted playsinline preload="none" loop poster="${EI}${n[1]}" data-src="${EI}${n[0]}" aria-label="${alt}"></video></div>`;
const EIMG=(n,r,alt)=>`<div class="v rx px ey" style="aspect-ratio:${r}"><img src="${EI}${n}" alt="${alt}" loading="lazy"></div>`;
const ECHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap ey-c');
function elyFigs(q){
 const T=ETX[lang]||ETX.fr,a=T.alt,M=EM,C=T.chap;
 const intro=`<div class="v rx px-t ey-intro"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--bg:${s[2]};--fg:${s[3]};--d:${k*110}ms"><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const f=[
  EV(M.hero,'870/700',a[0]), intro,
  ECHAP('01 / 04',C[0]), EIMG(M.ecusson,'1305/780',a[1]), EV(M.accreditation,'870/760',a[2]), EV(M.couleurs,'870/560',a[3]), EIMG(M.typo,'1305/930',a[4]), EIMG(M.directions,'1305/1050',a[5]),
  ECHAP('02 / 04',C[1]), EIMG(M.classement,'1305/1080',a[6]), EV(M.jauge,'870/560',a[7]), EIMG(M.trio,'1305/975',a[8]),
  ECHAP('03 / 04',C[2]), EV(M.duel,'870/620',a[9]), EIMG(M.feuille,'1305/1140',a[10]), EIMG(M.stories,'1305/1140',a[11]), EIMG(M.duo,'1305/975',a[12]), EIMG(M.playoffs,'1305/840',a[13]),
  ECHAP('04 / 04',C[3]), EIMG(M.composants,'1305/1245',a[14]), EIMG(M.fondations,'1305/900',a[15]), EIMG(M.backoffice,'1305/960',a[16]), EIMG(M.saisie,'1305/1080',a[17])
 ];
 return f.map(x=>[x,'']);
}
'''.replace('__MEDIA__', MEDIA)

for name in ['index.html', 'fr/index.html']:
    p = os.path.join(ROOT, name); s = open(p, encoding='utf-8').read()
    # données projet : Noria (ou Elyte déjà présent) → Elyte
    a = s.index('const P=['); b = s.index('];', a)
    blk = s[a:b]; lines = blk.split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith(" {t:'Noria'") or l.startswith(" {t:'Elyte Club'"))
    lines[i] = P_FR; s = s[:a] + '\n'.join(lines) + s[b:]
    a = s.index('const EN=['); b = s.index('];', a)
    lines = s[a:b].split('\n'); en = [k for k, l in enumerate(lines) if l.startswith(' {')]
    lines[en[i - 1]] = P_EN; s = s[:a] + '\n'.join(lines) + s[b:]
    # mesure du titre (Newsreader 300 italique, -.055em)
    if "'Elyte Club':" not in s: s = s.replace("const ENCRE={", "const ENCRE={'Elyte Club':[.0415,3.694],", 1)
    # CSS
    if '<style id="ely-css">' in s:
        a = s.index('<style id="ely-css">'); b = s.index('</style>', a) + len('</style>\n'); s = s[:a] + CSS + s[b:]
    else:
        a = s.index('<style id="pic-css">'); s = s[:a] + CSS + s[a:]
    # JS
    mark = "/* Elyte Club : figures réelles"
    if mark in s:
        a = s.index(mark); b = s.index("/* Route du Rhum : figures réelles"); s = s[:a] + JS + s[b:]
    else:
        b = s.index("/* Route du Rhum : figures réelles"); s = s[:b] + JS + s[b:]
    s = s.replace("q.x==='picard'?picFigs(q):rdrFigs(q)", "q.x==='picard'?picFigs(q):q.x==='elyte'?elyFigs(q):rdrFigs(q)")
    # polices : Zalando Sans Expanded (titres) et Doto (chiffres)
    if 'family=Zalando+Sans+Expanded' not in s:
        s = s.replace('&family=Montserrat:', '&family=Zalando+Sans+Expanded:wght@500;600&family=Doto:wght@700&family=Montserrat:', 1)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
