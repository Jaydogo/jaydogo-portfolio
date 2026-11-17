#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mockups Photoshop (affiches, panneaux, iMac) ajoutés à chaque projet.
Source : mockups-src/ (affiches HTML dans art/, PSD de ~/Documents/mockup_2 remplis par fill.jsx via run.sh, rendus dans out/).
Ce script copie out/*.jpg vers projets/<projet>/mk-<nom>-<hash>.jpg (hash = cache iPhone) et insère les figures
réparties dans la page de chaque projet (JS mkAdd autour du choix des figures). Idempotent.
Relancer :  python3 scripts/mockups.py && python3 scripts/pages.py"""
import os, json, hashlib, subprocess, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'mockups-src/out')
# projet, nom, alt FR, alt EN  (ordre = ordre d'apparition dans la page)
L = [
 ('rdr','rdr-ciel','Panneau dans le ciel « Le large, en direct. », la flotte au départ','Billboard against the sky: “Le large, en direct.”, the fleet at the start'),
 ('rdr','rdr-village','Barrières du village : SAINT-MALO en grand sur la vue aérienne du port','Race village barriers: SAINT-MALO in giant letters over the aerial view of the harbour'),
 ('rdr','rdr-arbres','Panneau « Il est là. Maintenant. » sur la carte live de l’app','“He’s here. Right now.” billboard over the app’s live map'),
 ('picard','picard-nuit','Panneau « Cueilli. Surgelé. C’est tout. », un maraîcher et sa cagette bio','“Picked. Frozen. That’s all.” billboard, a grower with an organic crate'),
 ('picard','picard-affiche','Affiche givrée « Le goût, mis au frais. », le dessert des fêtes derrière une vitre essuyée','Frosted poster “Le goût, mis au frais.”, the festive dessert behind a wiped window'),
 ('elyte','elyte-mur','Mur « Ton style a enfin un classement. » sur une photo de battle, avec le score ELO','Wall: “Your style finally has a ranking.” over a battle photo, with the ELO score'),
 ('elyte','elyte-bache','Bâche de chantier « Travaux en cours : ici se construit la première ligue de danse hip-hop. »','Construction banner: “Work in progress: the first hip-hop dance league is being built here.”'),
 ('elyte','elyte-collee','Affiche collée Nova contre Sayan','Paste-up poster: Nova vs Sayan'),
 ('elyte','elyte-stand','Chevalet « Ce soir, ça battle. » devant la salle','A-frame sign outside the venue: “Battle tonight.”'),
 ('relais','relais-poster','Affiche « Ailleurs, autrement. », une maison au lierre en plein cadre','“Ailleurs, autrement.” poster, an ivy-covered house full-bleed'),
 ('relais','relais-facade','Panneau « Des adresses qu’on ne trouve pas par hasard. », un chalet de nuit','“Places you don’t find by chance.” billboard, a chalet at night'),
 ('dalkia','dalkia-imac','L’accueil de dalkia.fr sur un iMac','The dalkia.fr home page on an iMac'),
]
MK = {}
for p, n, fr, en in L:
    src = os.path.join(SRC, n + '.jpg')
    vf = 'scale=1958:-2'
    tmp = os.path.join(ROOT, 'mockups-src', '_tmp.jpg')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-vf', vf, '-q:v', '4', tmp], check=True)
    h = hashlib.sha1(open(tmp, 'rb').read()).hexdigest()[:6]
    dst_dir = os.path.join(ROOT, 'projets', p)
    for old in glob.glob(os.path.join(dst_dir, 'mk-%s-*.jpg' % n)): os.remove(old)
    name = 'mk-%s-%s.jpg' % (n, h); os.replace(tmp, os.path.join(dst_dir, name))
    w, ht = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', os.path.join(dst_dir, name)], capture_output=True, text=True).stdout.strip().split(',')
    MK.setdefault(p, []).append(['/projets/%s/%s' % (p, name), '%s/%s' % (w, ht), fr, en])

JS = '''/* Mockups Photoshop : scripts/mockups.py */
const MKP=%s;
function mkAdd(q,f){const m=MKP[q.x];if(!m)return f;const o=f.slice(),n=m.length;
 m.map((x,k)=>[`<div class="v rx px mk" style="aspect-ratio:${x[1]}"><img src="${x[0]}" alt="${lang==='en'?x[3]:x[2]}" loading="lazy"></div>`,'']).forEach((x,k)=>{o.splice(Math.min(o.length,Math.round((k+1)*f.length/(n+1))+k),0,x)});return o}
/* fin mockups */
''' % json.dumps(MK, ensure_ascii=False)
OLD = "q.x?(q.x==='picard'?picFigs(q)"
for fn in ['index.html', 'fr/index.html']:
    pth = os.path.join(ROOT, fn); s = open(pth, encoding='utf-8').read()
    if '/* Mockups Photoshop' in s:
        a = s.index('/* Mockups Photoshop'); b = s.index('/* fin mockups */\n', a) + len('/* fin mockups */\n'); s = s[:a] + JS + s[b:]
    else:
        a = s.index('function picFigs(q){'); s = s[:a] + JS + s[a:]
    if 'mkAdd(q,' not in s.split('/* fin mockups */', 1)[1]:
        a = s.index(OLD); b = s.index(':vues(q,i)', a)
        s = s[:a] + 'q.x?mkAdd(q,' + s[a + 4:b] + ')' + s[b:]
    open(pth, 'w', encoding='utf-8').write(s); print(fn, 'ok')
