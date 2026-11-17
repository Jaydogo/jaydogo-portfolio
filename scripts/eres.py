#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute / réécrit le projet ERES (x:'eres', sixième projet, Big Youth) dans index.html et fr/index.html.
Figures exportées de Figma (fichier « ERES · Portfolio · Desktop + Mobile » gAMpiYYWpoOMddNLMNwHYo,
page « Portfolio · ERES v1 », cadres de 1305 px exportés à 1958 px), noms listés dans scripts/eres-assets.json
(suffixe = hash du contenu, à cause du cache iPhone). Mockups Display et main : kits Wannathis.
Les chiffres de résultats (comparaison avec l'ancien site) sont inventés à la demande de Jay : à valider.
Relancer après modification :  python3 scripts/eres.py && python3 scripts/pages.py"""
import os, json, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, 'scripts/eres-assets.json'), encoding='utf-8'))
for f in A.values():
    if not os.path.exists(os.path.join(ROOT, 'projets/eres', f)): raise SystemExit('asset manquant ' + f)
MEDIA = json.dumps(A, ensure_ascii=False)
# Illustration du carrousel d'accueil : un maillot une-pièce planté sous la colline, deux tons séparés sur l'axe
ART_ER = r""" p=>{/*eres*/const e=shade(p.c,.3),d=shade(p.c,.48),h=(f,l,r)=>f(l)+`<g clip-path="url(#erk)">${f(r)}</g>`,S='M0 -170L-24 -186-42 -236-50 -344H-72L-94 -236-78 -96-102 -36-24 66 0 74 24 66 102 -36 78 -96 94 -236 72 -344H50L42 -236 24 -186Z';return `<clipPath id="erk"><rect x="0" y="-800" width="400" height="1400"/></clipPath><polygon points="${ng(10,316,92,40)}" fill="${p.a}"/><path d="M316 52L356 92 316 132Z" fill="${p.b}"/><g transform="translate(200 384) rotate(-6) scale(.82)">${h(c=>`<path d="${S}" fill="${c}"/>`,e,d)}</g>`},"""
TITRE = 'ERES'
ENCRE = '[.0415,2.3965]'  # largeur de « ERES » en em, Newsreader Light Italic (mesurée dans le navigateur)

P_FR = (" {t:'ERES',x:'eres',ag:'Big Youth',k:'Mode · Luxe',y:'2019',c:'#8C2F2B',p:'#F0DDD6',on:'#F3F1EA',a:'#F0DDD6',b:'#D49A8E',"
        "d:'Le site de la maison parisienne de lingerie et de maillots de bain, pensé comme un magazine de mode.',lead:'Le corps en mouvement.',"
        "ctx:'Refondre eresparis.com : faire d’un catalogue de lingerie, de maillots et de prêt-à-porter un récit de mode, sans perdre le chemin du panier.',"
        "enj:[['Désirer','La photographie d’abord, le produit juste après'],['Choisir','Nom, coloris, prix : rien de plus sur la carte'],['Composer','La taille, le look, le panier, sans détour'],['Raconter','La Maison, ses ateliers et ses couleurs']],"
        "role:'Product Designer & UX Project Manager · Audit et benchmark luxe, ateliers avec les équipes e-commerce et marque, parcours d’achat, wireframes et tests utilisateurs, direction artistique éditoriale, UI desktop & mobile (fiche produit, guide des tailles, panier), design system, recette et suivi des KPI · Site e-commerce',"
        "m:'520 €',ml:'Nellie, combinaison',rows:[['Collection','L’activewear'],['Pièce','Nellie'],['Coloris','Indigo splash'],['Taille','S'],['Look','Graham'],['Total','1 000 €']],"
        "st:[['+34 %','de conversion e-commerce'],['−38 %','de retours liés à la taille']],ab:[['Avant','Catalogue'],['Après','Magazine']],bars:[30,36,42,46,52,58,62,68,74,80,86,92]},")
P_EN = (" {k:'Fashion · Luxury',d:'The website of the Parisian lingerie and swimwear house, designed like a fashion magazine.',lead:'The body in motion.',"
        "ctx:'Redesigning eresparis.com: turning a catalogue of lingerie, swimwear and ready-to-wear into a fashion story, without losing the way to the bag.',"
        "enj:[['Desire','Photography first, the product right after'],['Choose','Name, colour, price: nothing more on the card'],['Compose','Size, look, bag, no detours'],['Tell','The House, its workshops and its colours']],"
        "role:'Product Designer & UX Project Manager · Luxury audit and benchmark, workshops with e-commerce and brand teams, shopping journeys, wireframes and user testing, editorial art direction, desktop & mobile UI (product page, size guide, bag), design system, QA and KPI tracking · E-commerce website',"
        "ml:'Nellie, jumpsuit',rows:[['Collection','Activewear'],['Piece','Nellie'],['Colour','Indigo splash'],['Size','S'],['Look','Graham'],['Total','€1,000']],"
        "st:[['+34%','e-commerce conversion'],['−38%','size-related returns']],ab:[['Before','Catalogue'],['After','Magazine']]},")

LOGO = "M76.2193 3.60515L76.2094 0.416016C76.2094 0.416016 70.8039 0.450584 68.4612 0.583917C68.4612 0.583917 63.7234 0.725152 61.6217 2.84071C61.6217 2.84071 60.2923 3.99824 60.318 6.10589C60.3427 8.21453 61.1911 8.98688 61.7165 9.56071C61.7165 9.56071 62.4938 10.3163 64.081 10.8318C64.081 10.8318 64.8217 11.0817 67.202 11.776C67.202 11.776 71.8726 13.0214 73.118 13.7563C73.118 13.7563 75.4993 14.6135 75.5417 16.5049C75.5417 16.5049 75.6375 18.577 72.4523 19.4511C72.4523 19.4511 71.039 20.017 68.238 20.101L61.2652 20.1385L61.276 23.4234L68.3743 23.3997C68.3743 23.3997 72.6439 23.5143 75.7738 21.458C75.7738 21.458 78.9037 19.7365 78.8751 16.2234C78.8751 16.2234 79.1526 13.4471 75.596 11.4412C75.596 11.4412 74.242 10.5266 69.6257 9.29799C69.6257 9.29799 67.0281 8.60466 66.2341 8.30046C66.2341 8.30046 63.8005 7.75034 63.9032 6.05651C63.9032 6.05651 63.8084 4.72318 66.3832 4.13947C66.3832 4.13947 68.4721 3.73651 69.2119 3.75132C69.2119 3.75132 73.7521 3.53898 76.2202 3.60318L76.2193 3.60515ZM22.1314 3.79873L22.1215 0.569102C22.1215 0.569102 29.5625 0.621448 30.6252 0.65404C30.6252 0.65404 38.4593 0.3933 38.4277 6.3212C38.4277 6.3212 39.121 12.3321 30.9353 12.417C30.9353 12.417 29.0133 12.4861 27.8696 12.4644L39.603 23.5242L34.5758 23.54L22.1432 12.4812L22.1333 9.28515L31.0518 9.25355C31.0518 9.25355 35.0696 9.44811 34.9156 6.40318C34.9156 6.40318 35.2118 3.80861 30.9788 3.78589L22.1323 3.79577L22.1314 3.79873ZM18.9235 3.80466L18.9126 0.561201C18.9126 0.561201 12.3941 0.598732 12.2321 0.583917C11.9072 0.5533 0.197527 0.875275 0.266662 11.5064L0.288391 12.4802C0.288391 12.4802 0.195551 22.9948 11.7679 23.5755L19.0005 23.5518L18.9896 20.2728L12.802 20.2926C12.802 20.2926 4.13037 20.4368 4.03851 12.5256L18.958 12.4763L18.9472 9.28219L4.11851 9.33058C4.11851 9.33058 4.85234 4.28762 12.1728 3.83429L18.9254 3.80466H18.9235ZM58.3151 3.67429L58.3042 0.43083C58.3042 0.43083 51.7857 0.468361 51.6237 0.453546C51.2988 0.422929 39.5891 0.745893 39.6593 11.376L39.681 12.3498C39.681 12.3498 39.5872 22.8644 51.1575 23.4461L58.3911 23.4224L58.3802 20.1434L52.1926 20.1632C52.1926 20.1632 43.521 20.3074 43.4291 12.3963L58.3476 12.3469L58.3378 9.15281L43.5091 9.2012C43.5091 9.2012 44.243 4.15824 51.5635 3.7049L58.316 3.67528L58.3151 3.67429Z"
LOGO_URL = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 80 24'%3E%3Cpath d='" + LOGO + "'/%3E%3C/svg%3E\")"

CSS = r'''<style id="ers-css">
/* ERES : figures exportées de Figma + intro, chiffres en HTML. Préfixe .er — Jost (sans géométrique proche de la police de la marque) */
#page{--erf:Jost,"Work Sans",system-ui,sans-serif;--erm:"DM Mono",ui-monospace,monospace}
.v.px.er{background:#F2F1ED}
.er-intro .pc{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.er-q{position:relative;background:#F2F1ED;color:#080808;border-radius:8px;padding:clamp(24px,4vw,52px);margin:0 0 10px;overflow:hidden;border:1px solid rgba(8,8,8,.1)}
#page .er-q .lb{color:#8C2F2B;opacity:1;font:400 11px/1 var(--erm);letter-spacing:.14em;text-transform:uppercase}
.er-intro .er-q .q{font:300 clamp(22px,2.3vw,32px)/1.26 var(--erf);letter-spacing:-.01em;color:#080808;margin:16px 0 0;max-width:none;padding-right:min(18%,7em)}
.er-q .lg{position:absolute;right:clamp(18px,3vw,40px);bottom:clamp(20px,3vw,40px);width:clamp(54px,6vw,80px);aspect-ratio:80/24;background:#080808;-webkit-mask:__LOGO__ center/contain no-repeat;mask:__LOGO__ center/contain no-repeat}
#page .er-intro .ck{position:relative;isolation:isolate;border-radius:8px;aspect-ratio:4/5;padding:clamp(16px,2vw,28px);display:flex;flex-direction:column;justify-content:flex-end;gap:10px;overflow:hidden;color:#F3F1EA;background:#8C2F2B}
#page .er-intro .ck .im{position:absolute;inset:0;z-index:-2;margin:0!important;background-repeat:no-repeat;background-size:cover;transform:scale(1.05);transition:transform 1.6s cubic-bezier(.2,.7,.2,1)}
#page .er-intro .ck::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(8,8,8,0) 42%,rgba(8,8,8,.34) 66%,rgba(8,8,8,.78) 100%)}
#page .er-intro .ck b{font:300 clamp(28px,3.2vw,46px)/1 var(--erf);letter-spacing:.04em;text-transform:uppercase;color:#F3F1EA}
#page .er-intro .ck span{font:400 11px/1.5 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:#F3F1EA;opacity:.88}
.fig figure:not(.vu) .er-intro .ck{opacity:0;transform:translateY(36px)}
.fig figure .er-intro .ck{transition:opacity .8s var(--d),transform 1s var(--d) cubic-bezier(.2,.7,.2,1)}
.fig figure.vu .er-intro .ck .im{transform:scale(1)}
.er-intro>*,.er-res>*{width:100%!important;max-width:none!important;margin-left:0!important;margin-right:0!important}
.fig .v.er-res{height:auto;min-height:0;display:block;border-radius:0;overflow:hidden}
.v.er-res{background:#F2F1ED;color:#080808;padding:clamp(28px,4.4vw,56px);border-top:1px solid #080808}
.er-res>.lb{display:block;font:400 11px/1 var(--erm);letter-spacing:.14em;text-transform:uppercase;color:#8C2F2B}
.er-res .h{font:300 clamp(30px,3.6vw,48px)/1.1 var(--erf);letter-spacing:-.01em;margin:clamp(18px,2.4vw,28px) 0 clamp(26px,4vw,48px);max-width:16em;padding-right:min(22%,10em)}
.er-res .r{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);align-items:baseline;gap:clamp(14px,2vw,28px);border-top:1px solid rgba(8,8,8,.16);padding:clamp(16px,2vw,24px) 0}
.er-res .r b{font:200 clamp(40px,5.4vw,76px)/1 var(--erf);letter-spacing:-.02em;color:#080808;white-space:nowrap}
.er-res .r b i{font-style:normal;font-size:.5em;letter-spacing:.02em;margin-left:.15em}
.er-res .r span{font:400 11px/1.6 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:rgba(8,8,8,.78)}
.er-res .r span em{display:block;font-style:normal;color:rgba(8,8,8,.45);margin-top:4px}
.er-res .src{display:block;margin-top:clamp(22px,3vw,36px);font:400 10px/1.6 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:rgba(8,8,8,.45)}
.px-chap.er-c .pw{font:300 1em/1.1 var(--erf);letter-spacing:.06em;text-transform:uppercase}
#page .fig .v.er-step{display:grid;grid-template-columns:auto 1fr auto;align-items:baseline;gap:12px clamp(12px,2vw,28px);border-top:1px solid rgba(8,8,8,.16);padding:clamp(18px,2.4vw,30px) 0 0}
#page .er-step>*{margin:0!important;max-width:none!important;width:auto!important;position:static!important;text-align:left!important;justify-self:start}
.er-step .n{font:400 11px/1 var(--erm);letter-spacing:.14em;color:#8C2F2B}
.er-step .w{margin:0;font:300 clamp(36px,4.6vw,64px)/1.12 var(--erf);letter-spacing:.04em;text-transform:uppercase;color:#080808}
.er-step .d{font:400 11px/1.5 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:#696969;text-align:right;max-width:18em}
@media (max-width:899px){
.er-res .r{grid-template-columns:1fr;gap:10px}
#page .fig .v.er-step{grid-template-columns:auto 1fr}.er-step .d{grid-column:1/-1;text-align:left;max-width:none}
#page .er-q{padding:30px 24px 34px}
#page .er-intro .er-q .q{font-size:23px;line-height:1.34;margin-top:18px;padding-right:0;padding-bottom:40px}
#page .er-q .lg{right:24px;bottom:28px;width:56px}
#page .er-intro .ck{aspect-ratio:3/4.4;padding:18px}
#page .er-intro .ck b{font-size:26px;line-height:1.05}
#page .er-intro .ck span{font-size:10px;line-height:1.7;letter-spacing:.08em}
}
.fig .v.er-une{height:auto;min-height:0;border-radius:0;overflow:hidden}
.v.er-une,#page .fig .v.er-une{display:grid;grid-template-columns:1fr 1fr;background:#F2F1ED;color:#080808}
#page .fig .v.er-une .ph{display:block!important;width:100%!important;height:auto!important;min-height:100%;background-size:cover;background-position:50% 30%;margin:0!important}
.er-une .tx{padding:clamp(28px,4.2vw,56px);display:flex;flex-direction:column}
.er-une .lb{font:400 11px/1 var(--erm);letter-spacing:.14em;text-transform:uppercase;color:#8C2F2B}
.er-une .hero{margin:clamp(22px,3vw,38px) 0 10px;font:200 clamp(108px,13.5vw,196px)/.9 var(--erf);letter-spacing:-.04em;white-space:nowrap}
.er-une .hero small{font-size:.32em;letter-spacing:0;margin-left:.12em}
.er-une .hl{margin:0 0 clamp(36px,5vw,72px);font:400 11px/1.5 var(--erm);letter-spacing:.12em;text-transform:uppercase}
.er-une ul{list-style:none;margin:auto 0 0;padding:0;display:grid;grid-template-columns:1fr}
.er-une li{border-top:1px solid rgba(8,8,8,.16);padding:12px 0 11px;display:grid;grid-template-columns:7.2em 1fr;align-items:baseline;gap:12px}
.er-une li b{font:300 clamp(24px,2.2vw,30px)/1 var(--erf);letter-spacing:-.01em;white-space:nowrap}
.er-une li b i{font-style:normal;font-size:.62em;margin-left:.15em}
.er-une li span{font:400 10px/1.55 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:#55524D}
.er-une li span em{display:block;font-style:normal;color:rgba(8,8,8,.42)}
.er-une .src{margin-top:clamp(18px,2.4vw,28px);font:400 10px/1.6 var(--erm);letter-spacing:.1em;text-transform:uppercase;color:rgba(8,8,8,.45)}
#page .er-une>*,#page .er-une .tx>*{max-width:none!important;margin-left:0;margin-right:0;text-align:left!important;position:static!important}
@media (max-width:899px){.er-une .hero{font-size:clamp(84px,13vw,118px)}.er-une .tx{padding:28px 24px}.er-une li{grid-template-columns:5.6em 1fr;gap:8px}.er-une li b{font-size:22px}}
@media (max-width:599px){.v.er-une,#page .fig .v.er-une{grid-template-columns:1fr}#page .fig .v.er-une .ph{aspect-ratio:4/3;min-height:0}.er-une .hero{font-size:118px}.er-une li{grid-template-columns:7.2em 1fr}.er-une li b{font-size:26px}}
@media (prefers-reduced-motion:reduce){.fig figure .er-intro .ck{opacity:1;transform:none;transition:none}}
.v.er-head{padding:clamp(28px,4vw,52px) 0 clamp(8px,1.4vw,16px)}
.er-head .lb{display:block;font:400 11px/1 var(--erm);letter-spacing:.14em;text-transform:uppercase;color:#8C2F2B}
.er-head .h{margin:clamp(14px,1.8vw,22px) 0 0;font:300 clamp(34px,4.4vw,62px)/1.04 var(--erf);letter-spacing:-.01em;color:#080808}
.er-head .s{margin:clamp(12px,1.4vw,18px) 0 0;max-width:34em;font:400 12px/1.7 var(--erm);letter-spacing:.04em;color:#55524D}
#page .fig .v.er-head{display:block;text-align:left;height:auto;min-height:0}
#page .er-head>*{width:auto!important;max-width:52em!important;margin-left:0!important;margin-right:0!important;text-align:left!important;position:static!important;justify-self:start}
@media (max-width:899px){#page .fig>figure:first-child .v.mk:has(img[src*="/eres/"]){aspect-ratio:1958/1469!important}#page .fig>figure:first-child .v.mk:has(img[src*="/eres/"])>img{object-fit:contain}}
</style>
'''.replace('__LOGO__', LOGO_URL)

JS = r'''/* ERES : figures réelles (projet marqué x:'eres'). chiffres de résultats à valider. */
const ERI='/projets/eres/',ERM=__MEDIA__;
const ERT={fr:{defi:'Le projet',q:'Lingerie, maillots de bain, prêt-à-porter : une maison parisienne du corps en mouvement. Un site qui se lit comme un magazine et s’achète comme une boutique.',
 st:[['Désirer','La photographie d’abord, le produit juste après'],['Choisir','Nom, coloris, prix : rien de plus'],['Composer','La taille, le look, le panier'],['Raconter','La Maison, ses ateliers, ses couleurs']],
 steps:[['01','Voir','La pièce, ses coloris, son prix'],['02','Ajuster','Taille, filtres, recherche'],['03','Réunir','Deux pièces, un panier']],
 uni:['ERES / Collections','Six univers. Une signature.','Chaque collection s’ouvre comme une page de magazine : une image de campagne, une silhouette, trois lignes.'],
 chap:[['L’image','Le corps, avant le catalogue.','#8C2F2B'],['La collection','Choisir sans quitter l’image.','#B7AB99'],['La pièce','Lever les doutes avant le panier.','#080808'],['La Maison','Le savoir-faire, raconté comme un magazine.','#8C2F2B'],['Le système','Neutre, pour laisser parler les pièces.','#696969'],['Résultats','Ce qui a changé face à l’ancien site.','#080808']],
 res:['Un an après la mise en ligne','Plus d’envie, moins de doutes, plus de commandes.',[['+34 %','de conversion e-commerce'],['+27 %','de panier moyen','« Complétez votre look » sur chaque fiche'],['−38 %','de retours liés à la taille','avec le guide des tailles'],['+61 %','de commandes sur mobile','58 % du trafic'],['+58 %','de temps passé sur les pages de la Maison'],['2 <i>clics</i>','de la collection à la pièce','contre 4 auparavant'],['1,9 <i>s</i>','pour afficher l’accueil','contre 5,2 s'],['94','score d’accessibilité Lighthouse','contre 61'],['×2','pages vues par visite']],'Comparaison avec l’ancien site'],
 alt:['L’accueil Holiday Season sur un Studio Display, devant un fond bordeaux','La collection Nouveautés sur un iPhone tenu en main','Double page « Nuances de saison » : deux maillots métallisés et un une-pièce à pois','Six univers, six pages d’entrée de collection','Double page « L’allure dedans-dehors » : une robe longue brune et une robe au dos ouvert','La collection La lingerie sur desktop et sur iPhone','Le catalogue des combinaisons, avec une loupe sur le nom, le coloris et le prix','La fiche Nellie sur iPhone et sur desktop','Trouver votre taille : trois questions dans un panneau sur la fiche Nellie, puis la taille recommandée sur iPhone, les filtres et la recherche','Le panier sur desktop et sur iPhone : deux pièces, des suggestions, et le bouton Commander qui reste collé en bas sur mobile','L’atelier : coupe, nuanciers, couture, coloris, bobines','Trois récits de la Maison sur iPhone : l’artisanat, la couleur, le studio','Six nuances, de la photo à la pastille : noir, papier, nude, cuivre, rouge, indigo','Une sans géométrique pour les titres, une mono pour les prix et les détails','Une même carte produit au repos, au survol et au focus clavier, puis tailles, boutons et champ en erreur','Wireframes de la page L’art du geste, desktop et mobile','Holiday Season, du wireframe à l’écran final']},
 en:{defi:'The project',q:'Lingerie, swimwear, ready-to-wear: a Parisian house of the body in motion. A site that reads like a magazine and shops like a boutique.',
 st:[['Desire','Photography first, the product right after'],['Choose','Name, colour, price: nothing more'],['Compose','Size, look, bag'],['Tell','The House, its workshops, its colours']],
 steps:[['01','See','The piece, its colours, its price'],['02','Fit','Size, filters, search'],['03','Gather','Two pieces, one bag']],
 uni:['ERES / Collections','Six worlds. One signature.','Each collection opens like a magazine page: a campaign image, a silhouette, three lines.'],
 chap:[['The image','The body, before the catalogue.','#8C2F2B'],['The collection','Choosing without leaving the image.','#B7AB99'],['The piece','Clearing doubts before the bag.','#080808'],['The House','Craftsmanship, told like a magazine.','#8C2F2B'],['The system','Neutral, so the pieces can speak.','#696969'],['Results','What changed compared with the previous site.','#080808']],
 res:['One year after launch','More desire, fewer doubts, more orders.',[['+34%','e-commerce conversion'],['+27%','average basket','“Complete your look” on every product page'],['−38%','size-related returns','with the size guide'],['+61%','mobile orders','58% of traffic'],['+58%','time spent on the House pages'],['2 <i>clicks</i>','from collection to piece','down from 4'],['1.9 <i>s</i>','to load the home page','down from 5.2 s'],['94','Lighthouse accessibility score','up from 61'],['×2','pages viewed per visit']],'Compared with the previous site'],
 alt:['The Holiday Season home page on a Studio Display, against a burgundy background','The New In collection on a hand-held iPhone','“Shades of the season” spread: two metallic swimsuits and a polka-dot one-piece','Six worlds, six collection entry pages','“Inside-out allure” spread: a long brown dress and an open-back dress','The Lingerie collection on desktop and iPhone','The jumpsuit catalogue, with a magnifier on name, colour and price','The Nellie product page on iPhone and desktop','Find your size: three questions in a panel on the Nellie page, then the recommended size on iPhone, filters and search','The bag on desktop and iPhone: two pieces, suggestions, and a Checkout button pinned to the bottom on mobile','The workshop: cutting, colour charts, sewing, colourways, spools','Three House stories on iPhone: craftsmanship, colour, the studio','Six shades, from photo to swatch: black, paper, nude, copper, red, indigo','A geometric sans for headings, a mono for prices and details','One product card at rest, on hover and on keyboard focus, then sizes, buttons and a field in error','Wireframes of the Art of the gesture page, desktop and mobile','Holiday Season, from wireframe to final screen']}};
const ERK=[['carte-desirer','50% 30%'],['carte-choisir','50% 28%'],['carte-composer','50% 30%'],['carte-raconter','50% 50%']];
const ERSIMG=(n,r,alt)=>`<div class="v rx px er" style="aspect-ratio:${r}"><img src="${ERI}${n}" alt="${alt}" loading="lazy"></div>`;
const ERSHEAD=u=>`<div class="v rx px-t er-head"><span class="lb">${u[0]}</span><p class="h">${u[1]}</p><p class="s">${u[2]}</p></div>`;
const ERSSTEP=s=>`<div class="v rx px-t er-step"><span class="n">${s[0]}</span><p class="w">${s[1]}</p><span class="d">${s[2]}</span></div>`;
const ERSCHAP=(lb,c)=>PCHAP(lb,c).replace('px-chap','px-chap er-c');
function ersFigs(q){
 const T=ERT[lang]||ERT.fr,a=T.alt,M=ERM,C=T.chap;
 const I=(k,r,i)=>[ERSIMG(M[k],r,a[i]),''];
 const intro=`<div class="v rx px-t er-intro"><div class="er-q"><span class="lb">${T.defi}</span><p class="q">${T.q}</p><span class="lg" aria-hidden="true"></span></div><div class="pc">${T.st.map((s,k)=>`<div class="ck" style="--d:${k*110}ms"><i class="im" aria-hidden="true" style="background-image:url(${ERI}${M[ERK[k][0]]});background-position:${ERK[k][1]}"></i><b>${s[0]}</b><span>${s[1]}</span></div>`).join('')}</div></div>`;
 const R=T.res[2],H=R[0];const res=`<div class="v rx er-une"><div class="ph" style="background-image:url(${ERI}${M['carte-desirer']})" aria-hidden="true"></div><div class="tx"><span class="lb">${T.res[0]}</span><p class="hero">${H[0].replace(/\s?%$/,'<small>%</small>')}</p><p class="hl">${H[1]}</p><ul>${R.slice(1).map(r=>`<li><b>${r[0]}</b><span>${r[1]}${r[2]?`<em>${r[2]}</em>`:''}</span></li>`).join('')}</ul><span class="src">${T.res[3]}</span></div></div>`;
 return [
  I('display','1958/1469',0), [intro,''], I('main','1958/1469',1),
  [ERSCHAP('01 / 05',C[0]),''], I('nuances','1958/1455',2), [ERSHEAD(T.uni),''], I('univers','1958/1722',3), I('allure','1958/1455',4), I('wf-holiday','1958/1199',16),
  [ERSCHAP('02 / 05',C[1]),''], I('collection','1958/1080',5), I('catalogue','1958/1410',6),
  [ERSCHAP('03 / 05',C[2]),''], [ERSSTEP(T.steps[0]),''], I('produit','1958/1140',7), [ERSSTEP(T.steps[1]),''], I('etats','1958/2471',8), [ERSSTEP(T.steps[2]),''], I('panier','1958/1140',9),
  [ERSCHAP('04 / 05',C[3]),''], I('wf-geste','1958/1550',15), I('atelier','1958/1500',10), I('maison','1958/1350',11),
  [ERSCHAP('05 / 05',C[4]),''], I('couleurs','1958/1290',12), I('typo','1958/1350',13), I('composants','1958/1320',14),
  [ERSCHAP('eresparis.com',C[5]),''], [res,'']
 ];
}
'''.replace('__MEDIA__', MEDIA)

for name in ['index.html', 'fr/index.html']:
    p = os.path.join(ROOT, name); s = open(p, encoding='utf-8').read()
    # données projet (ajout en fin de liste, ou remplacement si déjà là)
    a = s.index('const P=['); b = s.index('\n];', a)
    lines = s[a:b].split('\n')
    k = next((i for i, l in enumerate(lines) if l.startswith(" {t:'ERES'")), None)
    if k is None: lines.append(P_FR); k = len(lines) - 1
    else: lines[k] = P_FR
    s = s[:a] + '\n'.join(lines) + s[b:]
    a = s.index('const EN=['); b = s.index('\n];', a)
    lines = s[a:b].split('\n'); en = [i for i, l in enumerate(lines) if l.startswith(' {')]
    if len(en) < k: lines.append(P_EN)
    else: lines[en[k - 1]] = P_EN
    s = s[:a] + '\n'.join(lines) + s[b:]
    # métrique du titre
    a = s.index('const ENCRE={'); b = s.index('};', a); enc = s[a:b]
    enc = re.sub(r"ERES:\[[^\]]*\],?", '', enc).replace('const ENCRE={', 'const ENCRE={ERES:' + ENCRE + ',', 1)
    s = s[:a] + enc + s[b:]
    # styles
    if '<style id="ers-css">' in s:
        a = s.index('<style id="ers-css">'); b = s.index('</style>', a) + len('</style>\n'); s = s[:a] + CSS + s[b:]
    else:
        a = s.index('<style id="rlc-css">'); s = s[:a] + CSS + s[a:]
    # script
    mark = "/* ERES : figures réelles"
    if mark in s:
        a = s.index(mark); b = s.index("/* Relais & Châteaux : figures réelles"); s = s[:a] + JS + s[b:]
    else:
        b = s.index("/* Relais & Châteaux : figures réelles"); s = s[:b] + JS + s[b:]
    # illustration d'accueil (7e entrée de ART)
    a = s.index('const ART=['); b = s.index('\n];', a)
    L = s[a:b].split('\n'); k2 = next((i for i, l in enumerate(L) if '/*eres*/' in l), None)
    if k2 is None:
        if not L[-1].rstrip().endswith(','): L[-1] = L[-1].rstrip() + ','
        L.append(ART_ER.rstrip(','))
    else: L[k2] = ART_ER.rstrip(',') if k2 == len(L) - 1 else ART_ER
    s = s[:a] + '\n'.join(L) + s[b:]
    # aiguillage des figures
    if "q.x==='eres'?ersFigs(q)" not in s:
        s = s.replace("q.x==='relais'?rlcFigs(q):rdrFigs(q)", "q.x==='relais'?rlcFigs(q):q.x==='eres'?ersFigs(q):rdrFigs(q)")
    # police
    if 'family=Jost' not in s:
        s = s.replace('&family=Taviraj:', '&family=Jost:wght@200;300;400&family=Taviraj:', 1)
    # CV : client Big Youth
    s = s.replace("'Picard,Fashion Network,Mugler,Eiffage'", "'Picard,ERES,Fashion Network,Mugler,Eiffage'")
    open(p, 'w', encoding='utf-8').write(s); print(name, 'ok')
