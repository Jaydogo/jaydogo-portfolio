#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute / réécrit le projet Elyte Club (x:'elyte', à la place de Noria) dans index.html et fr/index.html.
Figures exportées de Figma (fichier « Elyte Club — page projet (ébauches) », page « Portfolio · Elyte v4 »),
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
        "d:'La première plateforme de ligue de danse hip-hop en France.',lead:'Le battle, toute l’année.',"
        "ctx:'La première plateforme de ligue de danse hip-hop en France : deux groupes, des battles chaque mois, un classement ELO et des playoffs.',"
        "enj:[['Progresser','Un battle par mois, des points à chaque duel'],['Se situer','Son rang et sa zone playoffs, en un regard'],['Organiser','Le soir du battle, tout se saisit sur place'],['Partager','Un visuel prêt à poster pour chaque battle']],"
        "role:'Product Designer, développeur & photographe · Cadrage avec le staff, direction artistique, logo, design system, app web (classement, battles, playoffs, espace danseur), back-office, tests utilisateurs avec les danseurs, A/B tests, visuels de partage, vidéo explicative, photos des battles, maintenance et mises à jour régulières · App web responsive',"
        "m:'1301',ml:'ELO du leader',rows:[['1. Kaze','1301'],['2. Lyna','1268'],['3. Imani','1265'],['4. Nova','1263'],['5. Noa','1229'],['6. Yuna','1229']],"
        "st:[['2','groupes, un classement chacun'],['32','qualifiés en playoffs']],ab:[['Avant','Tableur'],['Après','Ligue']],bars:[44,48,52,50,58,62,60,68,72,70,78,84]},")
P_EN = (" {k:'Sport · Dance',d:'France’s first hip-hop dance league platform.',lead:'Battles, all year round.',"
        "ctx:'France’s first hip-hop dance league platform: two groups, monthly battles, an ELO ranking and playoffs.',"
        "enj:[['Grow','One battle a month, points on every duel'],['Know where you stand','Your rank and playoff zone at a glance'],['Run the night','Everything is entered on the spot'],['Share','A ready-to-post visual for every battle']],"
        "role:'Product Designer, developer & photographer · Scoping with the staff, art direction, logo, design system, web app (rankings, battles, playoffs, dancer area), back office, user testing with the dancers, A/B tests, share visuals, explainer video, battle photography, maintenance and regular updates · Responsive web app',"
        "ml:'leader’s ELO',st:[['2','groups, one ranking each'],['32','playoff spots']],ab:[['Before','Spreadsheet'],['After','League']]},")

CSS = r'''<style id="ely-css">
/* Elyte Club : figures exportées de Figma + intro typographique. Préfixe .ey — titres en Zalando Sans Expanded, chiffres en Doto */
#page{--eyd:"Zalando Sans Expanded",Archivo,system-ui,sans-serif}
.v.px.ey{background:#0C1116}
.ey-intro .q{font:600 clamp(21px,2.3vw,31px)/1.14 var(--eyd);letter-spacing:-.025em;max-width:24em;margin:16px 0 clamp(26px,4vw,48px)}
.ey-intro .pc{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ey-intro .ck{background:var(--bg);color:var(--fg);border-radius:14px;aspect-ratio:16/10;padding:clamp(16px,2vw,28px);display:flex;flex-direction:column;justify-content:space-between;overflow:hidden}
.ey-intro .ck{container-type:inline-size}
.ey-intro .ck b{font:700 min(clamp(54px,7.4vw,112px),33cqw)/.86 Doto,"Geist Mono",ui-monospace,monospace;letter-spacing:-.02em;white-space:nowrap}
/* résultats et verbatims (blocs HTML, traduits) */
.fig .v.ey-res,.fig .v.ey-vb{height:auto;min-height:0;display:block;border-radius:0;overflow:hidden}
.v.ey-res{background:#0C1116;color:#fff;padding:clamp(28px,4.4vw,56px)}
.ey-res>.lb,.ey-vb>.lb{display:block;font:400 11px/1 "DM Mono",ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;color:#FF6A2B}
.ey-res .g{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(28px,4vw,48px) clamp(18px,3vw,36px);margin-top:clamp(28px,4vw,48px)}
.ey-res .n{border-top:1px solid rgba(255,255,255,.18);padding-top:clamp(18px,2.2vw,28px)}
.ey-res .n b{display:block;font:700 clamp(38px,5vw,66px)/1 Doto,"Geist Mono",monospace;letter-spacing:-.02em}
.ey-res .n span{display:block;margin-top:14px;font:400 11px/1.55 "DM Mono",ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;color:#9AA0A6;max-width:22em}
.v.ey-vb{background:#EDE6DA;padding:clamp(24px,4vw,48px)}
.ey-vb .g{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:clamp(20px,3vw,32px)}
.ey-vb .c{background:#fff;color:#0C1116;border-radius:22px;padding:clamp(20px,2.6vw,32px);display:flex;flex-direction:column;gap:22px;justify-content:space-between}
.ey-vb .c.k{background:#0C1116;color:#fff}
.ey-vb q{display:block;quotes:none;font:600 clamp(15px,1.5vw,19px)/1.38 var(--eyd);letter-spacing:-.015em}
.ey-vb q::before{content:"“";display:block;font:900 54px/.7 var(--eyd);color:#FF6A2B;margin-bottom:14px}
.ey-vb .who{display:flex;align-items:center;gap:12px}
.ey-vb .who img,.ey-vb .who i{width:42px;height:42px;border-radius:50%;object-fit:cover;flex:none;background:#FF6A2B}
.ey-vb .who b{display:block;font:600 14px/1.2 var(--eyd)}
.ey-vb .who span{display:block;font:400 10px/1.4 "DM Mono",monospace;letter-spacing:.12em;text-transform:uppercase;opacity:.6;margin-top:3px}
.ey-intro .ck span{font:400 11px/1.4 "DM Mono",ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase}
.fig figure:not(.vu) .ey-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .ey-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.ey-intro>*,.ey-res>*,.ey-vb>*{width:100%!important;max-width:none!important;margin-left:0!important;margin-right:0!important}
.ey-intro>.q{padding-right:min(22%,10em)}
.px-chap.ey-c .pw{font:500 12px/1.4 var(--eyd);letter-spacing:.08em}
@media (max-width:899px){.ey-res .g{grid-template-columns:1fr 1fr}.ey-vb .g{grid-template-columns:1fr}
 /* héros recadré en portrait sur mobile : on garde le titre (à gauche) entier */
 #page .fig>figure:first-child .v.ey{aspect-ratio:870/760!important}#page .fig>figure:first-child .v.ey>video{object-position:50% 50%}}
@media (prefers-reduced-motion:reduce){.fig figure .ey-intro .ck{opacity:1;transform:none;transition:none}}
</style>
'''

JS = r'''/* Elyte Club : figures réelles (projet marqué x:'elyte'). Vidéos exportées de l'animation Figma, lues par picGo (video.pv). */
const EI='/projets/elyte/',EM=__MEDIA__;
const ETX={fr:{defi:'Le projet',q:'La première plateforme de ligue de danse hip-hop en France. Deux dimanches par mois, un classement ELO, des playoffs et, au bout, Amsterdam.',
 st:[['200+','danseurs formés','#FF6A2B','#FFFFFF'],['2','groupes, un classement chacun','#EDE6DA','#141412'],['32','qualifiés en playoffs','#5B4A41','#FFFFFF'],['500\u00a0€','et une place à Amsterdam','#123A3C','#FFFFFF']],
 chap:[['Marque','Un écusson, des points, un ticket.','#FF6A2B'],['Le classement','Chaque point se voit.','#123A3C'],['Le dimanche','Du tirage au verdict.','#5B4A41'],['Le système','Des jetons au back-office.','#0C1116']],
 res:['Saison 1 en chiffres',[['50+','danseurs par saison'],['94 %','de présence aux battles'],['300+','duels sur la saison'],['Live','résultats publiés pendant le battle'],['4,8/5','note donnée par les danseurs'],['1 200+','stories partagées sur Instagram']]],
 vb:['Ils en parlent',[['Après la formation, on avait peur de tout arrêter. Là on a une vraie ligue, on continue à se voir et à progresser.','Nova','Groupe A · Hip-hop','av-nova'],['Ça a changé l’ambiance des dimanches. On ne vient plus juste danser, on vient pour quelque chose.','Sayan','Groupe A · Popping','av-sayan'],['L’app est belle, simple, on a envie de l’ouvrir. On sent que c’est notre ligue, avec notre identité.','Kaze','Groupe A · Breaking','av-kaze'],['Elyte Club a donné une vraie suite à la formation. Les danseurs restent, et la communauté grandit.','Le staff','Elyte Studio','']]],
 alt:['Le classement Elyte Club qui défile sur un iPhone, devant un danseur sous les projecteurs','Affiche géante « La première ligue de danse hip-hop en France » sur un mur de ville','L’écusson Elyte Club sur fond orange','Construction de l’écusson','Versions minimales : écusson, marque S, logotype','Déclinaisons de couleur de l’écusson','Accréditation de battle et cordon orange sur une doudoune noire','Sticker écusson posé à la main','Affiche de battle collée sur un mur en béton','Les cinq couleurs : nuit, orange, crème, taupe, pétrole','Zalando Sans Expanded, Doto, Geist Mono et Inter Tight','Classement du groupe A sur un Studio Display','Jauge des playoffs : le curseur glisse jusqu’en haut de la zone orange','Le profil de Kaze qui défile, la courbe ELO se dessine','L’espace danseur sur un iPhone tenu en main','Profil, classement et espace danseur sur trois iPhone','Deux danseurs face à face pendant un battle','Un duel : le vainqueur passe sur l’aplat crème','Stories Instagram d’un battle et d’un vainqueur, publiées par le compte elyte.studio','Page d’un battle et playoffs sur deux iPhone','« Seuls 32 iront au bout. » sur une photo de victoire','Les composants du design system','Back-office sur un Studio Display']},
 en:{defi:'The project',q:'France’s first hip-hop dance league platform. Two Sundays a month, an ELO ranking, playoffs, and Amsterdam at the end of it.',
 st:[['200+','trained dancers','#FF6A2B','#FFFFFF'],['2','groups, one ranking each','#EDE6DA','#141412'],['32','playoff spots','#5B4A41','#FFFFFF'],['€500','and a trip to Amsterdam','#123A3C','#FFFFFF']],
 chap:[['Brand','A crest, dots and a ticket.','#FF6A2B'],['The ranking','Every point shows.','#123A3C'],['Battle Sunday','From the draw to the verdict.','#5B4A41'],['The system','From tokens to the back office.','#0C1116']],
 res:['Season 1 in numbers',[['50+','dancers per season'],['94%','attendance at battles'],['300+','duels in a season'],['Live','results published during the battle'],['4.8/5','rating from the dancers'],['1,200+','stories shared on Instagram']]],
 vb:['What they say',[['After the course, we were afraid of dropping it all. Now we have a real league, we keep seeing each other and getting better.','Nova','Group A · Hip-hop','av-nova'],['It changed the mood on Sundays. We don’t just come to dance anymore, we come for something.','Sayan','Group A · Popping','av-sayan'],['The app is beautiful and simple, you want to open it. It feels like our league, with our own identity.','Kaze','Group A · Breaking','av-kaze'],['Elyte Club gave the course a real follow-up. Dancers stay, and the community keeps growing.','The staff','Elyte Studio','']]],
 alt:['The Elyte Club ranking scrolling on an iPhone in front of a dancer under stage lights','Giant billboard “France’s first hip-hop dance league” on a city wall','The Elyte Club crest on orange','Crest construction','Minimal versions: crest, S mark, wordmark','Crest colour variations','Battle accreditation and orange lanyard on a black puffer jacket','Crest sticker applied by hand','Battle poster pasted on a concrete wall','The five colours: night, orange, cream, taupe, petrol','Zalando Sans Expanded, Doto, Geist Mono and Inter Tight','Group A ranking on a Studio Display','Playoff gauge: the marker slides to the top of the orange zone','Kaze’s profile scrolling as the ELO curve draws itself','The dancer area on an iPhone held in hand','Profile, ranking and dancer area on three iPhones','Two dancers facing off during a battle','A duel: the winner switches to the cream fill','Instagram stories for a battle and a winner, posted by the elyte.studio account','Battle page and playoffs on two iPhones','“Only 32 make it to the end” on a victory photo','Design system components','Back office on a Studio Display']}};
const EV=(n,r,alt,once)=>`<div class="v rx px ey" style="aspect-ratio:${r};background:#0C1116 url(${EI}${n[1]}) center/cover no-repeat"><video class="pv" muted playsinline preload="none" ${once?'data-once':'loop'} poster="${EI}${n[1]}" data-src="${EI}${n[0]}" aria-label="${alt}"></video></div>`;
const EIMG=(n,r,alt)=>`<div class="v rx px ey" style="aspect-ratio:${r}"><img src="${EI}${n}" alt="${alt}" loading="lazy"></div>`;
const ECHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap ey-c');
function elyFigs(q){
 const T=ETX[lang]||ETX.fr,a=T.alt,M=EM,C=T.chap;
 const intro=`<div class="v rx px-t ey-intro"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--bg:${s[2]};--fg:${s[3]};--d:${k*110}ms"><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const res=`<div class="v rx ey-res"><span class="lb px-t">${T.res[0]}</span><div class="g">${T.res[1].map(r=>`<div class="n"><b>${r[0]}</b><span>${r[1]}</span></div>`).join('')}</div></div>`;
 const vb=`<div class="v rx ey-vb"><span class="lb px-t">${T.vb[0]}</span><div class="g">${T.vb[1].map(v=>`<div class="c${v[3]?'':' k'}"><q>${v[0]}</q><div class="who">${v[3]?`<img src="${EI}${M[v[3]]}" alt="" loading="lazy">`:'<i></i>'}<div><b>${v[1]}</b><span>${v[2]}</span></div></div></div>`).join('')}</div></div>`;
 const f=[
  EV(M.hero,'870/760',a[0],1), intro, EIMG(M.mur,'1305/979',a[1]),
  ECHAP('01 / 04',C[0]), EIMG(M['logo-embleme'],'1305/978',a[2]), EIMG(M['logo-construction'],'1305/978',a[3]), EIMG(M['logo-versions'],'1305/978',a[4]), EIMG(M['logo-couleurs'],'1305/978',a[5]), EIMG(M.badge,'1305/979',a[6]), EIMG(M.sticker,'1305/979',a[7]), EIMG(M.affiche,'1305/1140',a[8]), EV(M.couleurs,'870/560',a[9]), EIMG(M.typo,'1305/930',a[10]),
  ECHAP('02 / 04',C[1]), EIMG(M.classement,'1305/978',a[11]), EV(M.jauge,'870/560',a[12]), EV(M.profil,'870/760',a[13],1), EIMG(M.main,'1305/979',a[14]), EIMG(M.trio,'1305/975',a[15]),
  ECHAP('03 / 04',C[2]), EIMG(M.faceaface,'1305/870',a[16]), EV(M.duel,'870/620',a[17]), EIMG(M.stories,'1305/1140',a[18]), EIMG(M.duo,'1305/975',a[19]), EIMG(M.playoffs,'1305/1140',a[20]),
  ECHAP('04 / 04',C[3]), EIMG(M.composants,'1305/1770',a[21]), EIMG(M.backoffice,'1305/978',a[22]), res, vb
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
        s = s.replace('&family=Montserrat:', '&family=Zalando+Sans+Expanded:wght@500;600;900&family=Doto:wght@700&family=Montserrat:', 1)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
