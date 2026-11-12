#!/usr/bin/env python3
"""Génère une page par projet : /<slug>/ et /fr/<slug>/ (copies de index.html avec <base>).
À relancer après chaque modification de index.html ou fr/index.html :  python3 scripts/pages.py"""
import re, unicodedata, os, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://jaydogo.dake.studio'
def slug(t):
    t = unicodedata.normalize('NFD', t)
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in t if unicodedata.category(c) != 'Mn').lower())
src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
block = src[src.index('const P=['):src.index('];', src.index('const P=['))]
titles = re.findall(r"^\s*\{t:'([^']+)'", block, re.M)
slugs = [slug(t) for t in titles]
for old in os.listdir(ROOT):  # nettoie les anciennes pages générées
    p = os.path.join(ROOT, old)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, '.genere')): shutil.rmtree(p)
fr_root = os.path.join(ROOT, 'fr')
for old in os.listdir(fr_root):
    p = os.path.join(fr_root, old)
    if os.path.isdir(p) and os.path.exists(os.path.join(p, '.genere')): shutil.rmtree(p)
for lang, base, f in [('en', '/', 'index.html'), ('fr', '/fr/', 'fr/index.html')]:
    html = open(os.path.join(ROOT, f), encoding='utf-8').read()
    for t, s in zip(titles, slugs):
        url = f'{SITE}{base}{s}'
        h = html.replace('<head>', f'<head>\n<base href="{base}">', 1)
        h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', h)
        h = re.sub(r'(<meta property="og:url" content=")[^"]*(")', rf'\g<1>{url}\2', h)
        h = re.sub(r'<title>[^<]*</title>', f'<title>{t} · Jean-Yves Dogo</title>', h, count=1)
        out = os.path.join(ROOT, base.strip('/'), s) if base != '/' else os.path.join(ROOT, s)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
        open(os.path.join(out, '.genere'), 'w').write('')
print('pages :', ', '.join(slugs))
