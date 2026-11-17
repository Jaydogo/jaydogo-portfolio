#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute / réécrit le projet Dalkia (x:'dalkia', à la place de Relais) dans index.html et fr/index.html.
Figures exportées de Figma (fichier Figma Dalkia, page « Portfolio · Dalkia v1 »,
clones ×1,5 sur la page « Export mockups (temp) »), noms listés dans scripts/dalkia-assets.json
(suffixe = hash du contenu, à cause du cache iPhone). 
les chiffres d'éco-conception sont ceux publiés par Dalkia (dalkia.fr/site-web-ecologique-explications).
Relancer après modification :  python3 scripts/dalkia.py && python3 scripts/pages.py"""
import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, 'scripts/dalkia-assets.json'), encoding='utf-8'))
for f in A.values():
    if not os.path.exists(os.path.join(ROOT, 'projets/dalkia', f)): raise SystemExit('asset manquant ' + f)
MEDIA = json.dumps(A, ensure_ascii=False)

P_FR = (" {t:'Dalkia',x:'dalkia',ag:'Niji',k:'Énergie',y:'2023',c:'#4F9E30',p:'#D9EBCD',on:'#F3F1EA',a:'#D9EBCD',b:'#8CC46F',"
        "d:'Le site de Dalkia, pensé pour consommer moins sans perdre sa marque.',lead:'Moins de ressources. Toujours autant de sens.',"
        "ctx:'Le site de Dalkia, filiale d’EDF, repensé pour consommer moins : moins de pages, deux nuances, des images en trame.',"
        "enj:[['Alléger','Moins de pages, moins de poids'],['Assumer','Expliquer la sobriété dès l’arrivée'],['Unifier','Une trame verte pour toutes les photos'],['Garder','Une marque forte, sans artifice']],"
        "role:'Product Designer & responsable éco-conception · Site web desktop & mobile, design system, démarche d’éco-conception',"
        "m:'−64 %',ml:'d’émissions',rows:[['Pages','÷ 4'],['Serveurs','2 / 7'],['Nuances','2'],['Vidéo auto','0'],['Hébergement','100 % EnR'],['EcoIndex','B']],"
        "st:[['−64 %','d’émissions face à l’ancien site'],['4×','moins de pages']],ab:[['Avant','7 serveurs'],['Après','2 serveurs']],bars:[96,90,84,78,72,66,60,54,48,44,40,36]},")
P_EN = (" {k:'Energy',d:'Dalkia’s website, designed to use less without losing its brand.',lead:'Fewer resources. Just as much meaning.',"
        "ctx:'The website of Dalkia, an EDF subsidiary, redesigned to use less: fewer pages, two shades, halftone images.',"
        "enj:[['Lighten','Fewer pages, less weight'],['Own it','Explain the restraint from the first visit'],['Unify','One green halftone for every photo'],['Keep','A strong brand, no gimmicks']],"
        "role:'Product Designer & eco-design lead · Desktop & mobile website, design system, eco-design approach',"
        "ml:'emissions',st:[['−64%','emissions vs the previous site'],['4×','fewer pages']],ab:[['Before','7 servers'],['After','2 servers']]},")

CSS = r'''<style id="dlk-css">
/* Dalkia : figures exportées de Figma + intro, prix et données d'éco-conception en HTML. Préfixe .dk — Work Sans Light (police de la marque) */
#page{--dkf:"Work Sans",Archivo,system-ui,sans-serif}
.v.px.dk{background:#1D3A16}
.dk-intro .q{font:300 clamp(22px,2.4vw,32px)/1.16 var(--dkf);letter-spacing:-.02em;max-width:24em;margin:16px 0 clamp(26px,4vw,48px)}
.dk-intro .pc{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.dk-intro .ck{background:var(--bg);color:var(--fg);border-radius:8px;aspect-ratio:16/10;padding:clamp(16px,2vw,28px);display:flex;flex-direction:column;justify-content:space-between;overflow:hidden}
.dk-intro .ck b{font:300 clamp(30px,3.6vw,52px)/1 var(--dkf);letter-spacing:-.03em}
.dk-intro .ck span{font:400 11px/1.4 "DM Mono",ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase}
.fig figure:not(.vu) .dk-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .dk-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.fig .v.dk-aw,.fig .v.dk-eco{height:auto;min-height:0;display:block;border-radius:0;overflow:hidden}
.v.dk-aw{background:#F3F4E2;color:#111411;padding:clamp(28px,4.4vw,56px)}
.dk-aw .t{font:300 clamp(40px,5vw,64px)/1 var(--dkf);letter-spacing:-.03em;color:#4F9E30;margin:0 0 clamp(22px,3vw,36px)}
.dk-aw .r{display:grid;grid-template-columns:1fr 1fr;align-items:baseline;gap:16px;border-top:1px solid rgba(17,20,17,.18);padding:clamp(14px,1.8vw,22px) 0}
.dk-aw .r b{font:300 clamp(22px,2.4vw,30px)/1.1 var(--dkf)}
.dk-aw .r span{font:400 11px/1.5 "DM Mono",ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:#ED6B3E}
.dk-aw .by{display:block;margin-top:18px;font:400 11px/1 "DM Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:#77796C}
.v.dk-eco{background:#1D3A16;color:#F3F4E2;padding:clamp(28px,4.4vw,56px)}
.dk-eco>.lb,.dk-aw>.lb{display:block;font:400 11px/1 "DM Mono",ui-monospace,monospace;letter-spacing:.14em;text-transform:uppercase;color:#8CC46F}
.dk-eco .g{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(28px,4vw,48px) clamp(18px,3vw,36px);margin-top:clamp(28px,4vw,48px)}
.dk-eco .n{border-top:1px solid rgba(243,244,226,.22);padding-top:clamp(18px,2.2vw,28px)}
.dk-eco .n b{display:block;font:300 clamp(40px,5.2vw,72px)/1 var(--dkf);letter-spacing:-.04em;white-space:nowrap}
.dk-eco .n.o b{color:#ED6B3E}
.dk-eco .n span{display:block;margin-top:14px;font:400 11px/1.55 "DM Mono",ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase;color:rgba(243,244,226,.72);max-width:22em}
.dk-eco .src{display:block;margin-top:clamp(28px,4vw,48px);font:400 10px/1.6 "DM Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:rgba(243,244,226,.5)}
.dk-intro>*,.dk-aw>*,.dk-eco>*{width:100%!important;max-width:none!important;margin-left:0!important;margin-right:0!important}
.dk-intro>.q{padding-right:min(22%,10em)}
.px-chap.dk-c .pw{font:300 1.08em/1.1 var(--dkf);letter-spacing:-.02em}
@media (max-width:899px){.dk-eco .g{grid-template-columns:1fr 1fr}.dk-aw .r{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){.fig figure .dk-intro .ck{opacity:1;transform:none;transition:none}}
</style>
'''

JS = r'''/* Dalkia : figures réelles (projet marqué x:'dalkia'). Chiffres publiés par Dalkia. */
const DI='/projets/dalkia/',DM=__MEDIA__;
const DTX={fr:{defi:'Le projet',q:'Le site de Dalkia, filiale d’EDF, repensé pour consommer moins. Moins de pages, deux nuances, une trame verte sur les photos : la sobriété devient un récit de marque.',
 st:[['Alléger','Moins de pages, moins de poids','#4F9E30','#F3F4E2'],['Assumer','Expliquer la sobriété dès l’arrivée','#F3F4E2','#111411'],['Unifier','Une trame verte pour toutes les photos','#ED6B3E','#F3F4E2'],['Garder','Une marque forte, sans artifice','#1D3A16','#F3F4E2']],
 chap:[['Frugalité','Le site assume son régime dès l’arrivée.','#4F9E30'],['Image','Une photo par page, traitée en trame verte.','#ED6B3E'],['Système','Des cartes qui informent avant d’illustrer.','#1D3A16'],['Mobile','Une colonne, les mêmes repères.','#4F9E30'],['Éco-conception','Ce que Dalkia a mesuré et publié.','#1D3A16'],['Wireframes & tests','La hiérarchie d’abord, testée auprès d’utilisateurs.','#77796C']],
 aw:['Prix',[['Epica','Bronze'],['Stratégies','3 Or'],['Cas d’Or','Innovation, site responsable'],['Lisbon Ad','Shortlist']],'Dalkia × Niji'],
 eco:['L’éco-conception en chiffres',[['−64 %','d’émissions de CO₂ face à l’ancien site',1],['4×','moins de pages, hors offres d’emploi'],['2 / 7','serveurs : deux au lieu de sept'],['1','serveur au repos les soirs et les week-ends'],['100 %','d’hébergement en énergies renouvelables'],['2','nuances de couleur pour toute l’interface'],['2× / jour','mises à jour au maximum, site statique'],['0','vidéo en lecture automatique'],['B','note EcoIndex, audit de juillet 2021']],'Chiffres publiés par Dalkia · dalkia.fr/site-web-ecologique-explications'],
 alt:['Affiche « Ensemble, relevons le défi climatique » sur un mur de ville','L’accueil mobile de Dalkia sur un iPhone tenu en main, fond orange','L’accueil desktop de Dalkia sur un Studio Display','Les quatre étapes de la fenêtre d’accueil éco sur mobile','Photo d’équipe en trame verte, avec une loupe sur les points','Le vert Dalkia, le crème, l’orange et le noir','Le catalogue des références, des cartes sans photo','Les cartes de l’accueil et le bouton de contact','Références, solutions et éco-conception sur trois iPhone','Work Sans en Light et Regular, alphabet et accroche','Wireframe annoté de l’accueil desktop, avec le vrai texte','Wireframe de la fenêtre d’accueil éco','Wireframes mobile de l’accueil et des références','La page « Notre site web consomme moins » et ses quatre leviers','En-tête mobile avec la note EcoIndex et le lien « Ce site consomme moins »','Six photos Dalkia en trame verte','La page « Nos solutions » et sa photo en trame']},
 en:{defi:'The project',q:'The website of Dalkia, an EDF subsidiary, redesigned to use less. Fewer pages, two shades, a green halftone on every photo: restraint becomes part of the brand story.',
 st:[['Lighten','Fewer pages, less weight','#4F9E30','#F3F4E2'],['Own it','Explain the restraint from the first visit','#F3F4E2','#111411'],['Unify','One green halftone for every photo','#ED6B3E','#F3F4E2'],['Keep','A strong brand, no gimmicks','#1D3A16','#F3F4E2']],
 chap:[['Frugality','The site owns its diet from the first visit.','#4F9E30'],['Image','One photo per page, in green halftone.','#ED6B3E'],['System','Cards that inform before they illustrate.','#1D3A16'],['Mobile','One column, the same landmarks.','#4F9E30'],['Eco-design','What Dalkia measured and published.','#1D3A16'],['Wireframes & testing','Hierarchy first, tested with users.','#77796C']],
 aw:['Awards',[['Epica','Bronze'],['Stratégies','3 Gold'],['Cas d’Or','Innovation, responsible website'],['Lisbon Ad','Shortlist']],'Dalkia × Niji'],
 eco:['Eco-design in numbers',[['−64%','CO₂ emissions vs the previous site',1],['4×','fewer pages, job offers aside'],['2 / 7','servers: two instead of seven'],['1','server resting on evenings and weekends'],['100%','hosting powered by renewable energy'],['2','colour shades for the whole interface'],['2× / day','updates at most, static site'],['0','autoplay videos'],['B','EcoIndex grade, July 2021 audit']],'Figures published by Dalkia · dalkia.fr/site-web-ecologique-explications'],
 alt:['“Ensemble, relevons le défi climatique” poster on a city wall','Dalkia’s mobile home page on a hand-held iPhone, orange background','Dalkia’s desktop home page on a Studio Display','The four steps of the eco welcome window on mobile','Team photo in green halftone, with a magnifier on the dots','Dalkia green, cream, orange and black','The case-study catalogue, cards without photos','Home page cards and the contact button','Case studies, solutions and eco-design pages on three iPhones','Work Sans in Light and Regular, alphabet and headline','Annotated desktop home wireframe, with real copy','Wireframe of the eco welcome window','Mobile wireframes of the home and case-study pages','The “Our website uses less” page and its four levers','Mobile header with the EcoIndex grade and the “This site uses less” link','Six Dalkia photos in green halftone','The “Our solutions” page and its halftone photo']}};
const DIMG=(n,r,alt)=>`<div class="v rx px dk" style="aspect-ratio:${r}"><img src="${DI}${n}" alt="${alt}" loading="lazy"></div>`;
const DCHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap dk-c');
function dlkFigs(q){
 const T=DTX[lang]||DTX.fr,a=T.alt,M=DM,C=T.chap;
 const intro=`<div class="v rx px-t dk-intro"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--bg:${s[2]};--fg:${s[3]};--d:${k*110}ms"><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const aw=`<div class="v rx dk-aw"><p class="t px-t">${T.aw[0]}</p>${T.aw[1].map(r=>`<div class="r"><b>${r[0]}</b><span>${r[1]}</span></div>`).join('')}<span class="by">${T.aw[2]}</span></div>`;
 const eco=`<div class="v rx dk-eco"><span class="lb px-t">${T.eco[0]}</span><div class="g">${T.eco[1].map(r=>`<div class="n${r[2]?' o':''}"><b>${r[0]}</b><span>${r[1]}</span></div>`).join('')}</div><span class="src">${T.eco[2]}</span></div>`;
 const f=[
  DIMG(M.billboard,'1305/978',a[0]), intro, DIMG(M.main,'1305/978',a[1]), DIMG(M.display,'1305/978',a[2]),
  DCHAP('01 / 05',C[5]), DIMG(M['wf-accueil'],'1305/1379',a[10]), DIMG(M['wf-fenetre'],'1305/1050',a[11]), DIMG(M['wf-mobile'],'1305/960',a[12]),
  DCHAP('02 / 05',C[0]), DIMG(M.etapes,'1305/960',a[3]), DIMG(M['page-eco'],'1305/1320',a[13]), DIMG(M.ecoindex,'1305/840',a[14]),
  DCHAP('03 / 05',C[1]), DIMG(M.trame,'1305/930',a[4]), DIMG(M.mosaique,'1305/795',a[15]), DIMG(M.solutions,'1305/900',a[16]), DIMG(M.couleurs,'1305/840',a[5]), DIMG(M.typo,'1305/990',a[9]),
  DCHAP('04 / 05',C[2]), DIMG(M.references,'1305/990',a[6]), DIMG(M.composants,'1305/875',a[7]),
  DCHAP('05 / 05',C[3]), DIMG(M.trio,'1305/975',a[8]), aw,
  DCHAP('dalkia.fr',C[4]), eco
 ];
 return f.map(x=>[x,'']);
}
'''.replace('__MEDIA__', MEDIA)

for name in ['index.html', 'fr/index.html']:
    p = os.path.join(ROOT, name); s = open(p, encoding='utf-8').read()
    a = s.index('const P=['); b = s.index('];', a)
    lines = s[a:b].split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith(" {t:'Relais'") or l.startswith(" {t:'Dalkia'"))
    lines[i] = P_FR; s = s[:a] + '\n'.join(lines) + s[b:]
    a = s.index('const EN=['); b = s.index('];', a)
    lines = s[a:b].split('\n'); en = [k for k, l in enumerate(lines) if l.startswith(' {')]
    lines[en[i - 1]] = P_EN; s = s[:a] + '\n'.join(lines) + s[b:]
    if "Dalkia:[" not in s.split('const ENCRE={', 1)[1].split('};', 1)[0]:
        s = s.replace("const ENCRE={", "const ENCRE={Dalkia:[.0415,2.473],", 1)
    if '<style id="dlk-css">' in s:
        a = s.index('<style id="dlk-css">'); b = s.index('</style>', a) + len('</style>\n'); s = s[:a] + CSS + s[b:]
    else:
        a = s.index('<style id="ely-css">'); s = s[:a] + CSS + s[a:]
    mark = "/* Dalkia : figures réelles"
    if mark in s:
        a = s.index(mark); b = s.index("/* Route du Rhum : figures réelles"); s = s[:a] + JS + s[b:]
    else:
        b = s.index("/* Route du Rhum : figures réelles"); s = s[:b] + JS + s[b:]
    s = s.replace("q.x==='elyte'?elyFigs(q):rdrFigs(q)", "q.x==='elyte'?elyFigs(q):q.x==='dalkia'?dlkFigs(q):rdrFigs(q)")
    if 'family=Work+Sans' not in s:
        s = s.replace('&family=Montserrat:', '&family=Work+Sans:wght@300;400&family=Montserrat:', 1)
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
