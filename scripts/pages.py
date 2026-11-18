#!/usr/bin/env python3
"""Génère une page par projet : /<slug>/ et /fr/<slug>/ (copies de index.html avec <base>),
avec leurs métadonnées SEO (titre, description, hreflang, Open Graph, JSON-LD, texte indexable),
puis sitemap.xml et 404.html. Met aussi à jour le bloc de liens projets des deux accueils.
À relancer après chaque modification de index.html ou fr/index.html :  python3 scripts/pages.py"""
import re, unicodedata, os, shutil, json, html as H, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://jaydogo.dake.studio'
TODAY = datetime.date.today().isoformat()

def slug(t):
    t = unicodedata.normalize('NFD', t)
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in t if unicodedata.category(c) != 'Mn').lower())

def rd(f): return open(os.path.join(ROOT, f), encoding='utf-8').read()
def wr(f, s): open(os.path.join(ROOT, f), 'w', encoding='utf-8').write(s)

def objets(src, start):
    """Lit les objets de premier niveau d'un tableau JS (const P=[ … ];) : champs texte de premier niveau."""
    j = src.index(start) + len(start)
    out, depth, cur = [], 0, ''
    while True:
        c = src[j]
        if c == "'":  # chaîne : recopiée telle quelle
            k = j + 1
            while src[k] != "'":
                k += 2 if src[k] == '\\' else 1
            cur += src[j:k + 1]; j = k + 1; continue
        if c in '[{': depth += 1
        if c in ']}': depth -= 1
        if depth < 0: break
        cur += c
        if depth == 0 and c == '}': out.append(cur); cur = ''
        j += 1
    res = []
    for o in out:
        d, depth = {}, 0
        for m in re.finditer(r"([{\[\]}])|(\w+):'((?:[^'\\]|\\.)*)'", o):
            if m.group(1): depth += 1 if m.group(1) in '{[' else -1; continue
            if depth == 1: d.setdefault(m.group(2), m.group(3).replace("\\'", "'"))
        res.append(d)
    return res

src = rd('index.html')
P = objets(src, 'const P=[')
EN = objets(src, 'const EN=[')
slugs = [slug(p['t']) for p in P]
def texte(v):  # les champs peuvent contenir du balisage (<b>…) et des entités
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', v))).strip()
P = [{k: texte(v) for k, v in p.items()} for p in P]
EN = [{k: texte(v) for k, v in e.items()} for e in EN]
for p, e in zip(P, EN):
    p['en'] = {**p, **e}

LIB = {
    'en': {'cas': 'Product design case study', 'par': 'Case study by Jean-Yves Dogo', 'accueil': 'Home', 'projets': 'Projects'},
    'fr': {'cas': 'Étude de cas product design', 'par': 'Étude de cas de Jean-Yves Dogo', 'accueil': 'Accueil', 'projets': 'Projets'},
}
def url(lang, s=''):
    return f"{SITE}{'/fr/' if lang == 'fr' else '/'}{s + '/' if s else ''}"

def role_court(r): return r.split(' · ')[0].strip()
def annee(y): return y.replace(' → ', '–')

def nav(lang):
    """Liens projets en dur dans le HTML, pour que les moteurs trouvent chaque page sans exécuter le JS."""
    liens = ''.join(f'<li><a href="{url(lang, s)}" tabindex="-1">{H.escape(p["t"])}</a></li>' for p, s in zip(P, slugs))
    return f'<!--seo-nav--><nav class="vh" aria-label="{LIB[lang]["projets"]}"><ul>{liens}</ul></nav><!--/seo-nav-->'

def item_list(lang):
    return {"@type": "ItemList", "@id": url(lang) + '#projects', "name": LIB[lang]['projets'],
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(lang, s), "name": p['t']}
                                for i, (p, s) in enumerate(zip(P, slugs))]}

def set_meta(h, attr, key, val):
    pat = rf'(<meta {attr}="{re.escape(key)}" content=")[^"]*(">)'
    return re.sub(pat, lambda m: m.group(1) + H.escape(val, quote=True) + m.group(2), h, count=1)

def ld_get(h):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    return m, json.loads(m.group(1))

def ld_put(h, m, data):
    return h[:m.start(1)] + json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + h[m.end(1):]

# 1. Accueils : bloc de liens projets + liste JSON-LD + date
for lang, f in [('en', 'index.html'), ('fr', 'fr/index.html')]:
    h = rd(f)
    h = re.sub(r'<!--seo-nav-->.*?<!--/seo-nav-->', '', h, flags=re.S)
    h = re.sub(r'(<h1 class="vh">[^<]*</h1>)', lambda m: m.group(1) + nav(lang), h, count=1)
    m, data = ld_get(h)
    g = [n for n in data['@graph'] if n.get('@type') != 'ItemList']
    for n in g:
        if n.get('@type') == 'ProfilePage':
            n['dateModified'] = TODAY
            n['hasPart'] = {'@id': url(lang) + '#projects'}
    g.append(item_list(lang))
    data['@graph'] = g
    wr(f, ld_put(h, m, data))

# 2. Pages projets
for d in (ROOT, os.path.join(ROOT, 'fr')):  # nettoie les anciennes pages générées
    for old in os.listdir(d):
        p = os.path.join(d, old)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, '.genere')): shutil.rmtree(p)

for lang, base, f in [('en', '/', 'index.html'), ('fr', '/fr/', 'fr/index.html')]:
    home = rd(f)
    L = LIB[lang]
    for p0, s in zip(P, slugs):
        p = p0['en'] if lang == 'en' else p0
        u, u_en, u_fr = url(lang, s), url('en', s), url('fr', s)
        titre = f"{p['t']} · {L['cas']} · Jean-Yves Dogo"
        desc = f"{p['d']} {L['par']}, {role_court(p['role'])}, {annee(p['y'])}."
        img = f'{SITE}/og/{s}.jpg'
        h = home.replace('<head>', f'<head>\n<base href="{base}">', 1)
        h = re.sub(r'<title>[^<]*</title>', lambda m: f'<title>{H.escape(titre, quote=False)}</title>', h, count=1)
        h = set_meta(h, 'name', 'description', desc)
        h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{u}">', h)
        h = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">', f'<link rel="alternate" hreflang="en" href="{u_en}">', h)
        h = re.sub(r'<link rel="alternate" hreflang="fr" href="[^"]*">', f'<link rel="alternate" hreflang="fr" href="{u_fr}">', h)
        h = re.sub(r'<link rel="alternate" hreflang="x-default" href="[^"]*">', f'<link rel="alternate" hreflang="x-default" href="{u_en}">', h)
        h = set_meta(h, 'property', 'og:type', 'article')
        h = re.sub(r'<meta property="profile:(first|last)_name" content="[^"]*">\n?', '', h)
        h = set_meta(h, 'property', 'og:title', titre)
        h = set_meta(h, 'property', 'og:description', desc)
        h = set_meta(h, 'property', 'og:url', u)
        h = set_meta(h, 'property', 'og:image', img)
        h = set_meta(h, 'property', 'og:image:alt', f"{p['t']} · {p['d']}")
        h = set_meta(h, 'name', 'twitter:title', titre)
        h = set_meta(h, 'name', 'twitter:description', desc)
        h = set_meta(h, 'name', 'twitter:image', img)
        # Texte indexable : titre du projet en h1 et son résumé (le même texte que celui affiché par la page)
        corps = (f'<h1 class="vh">{H.escape(p["t"])} · {H.escape(L["cas"])}</h1>'
                 f'<div class="vh"><p>{H.escape(p["d"])}</p><p>{H.escape(p.get("ctx", ""))}</p>'
                 f'<p>{H.escape(p["role"])}</p><p>{H.escape(p.get("k", ""))} · {H.escape(annee(p["y"]))}</p></div>')
        h = re.sub(r'<h1 class="vh">[^<]*</h1>', lambda m: corps, h, count=1)
        m, data = ld_get(h)
        person = next(n for n in data['@graph'] if n.get('@type') == 'Person')
        site = next(n for n in data['@graph'] if n.get('@type') == 'WebSite')
        agences = [a.strip() for a in re.sub(r'\s*\([^)]*\)', '', p.get('ag', '')).split('·') if a.strip()]
        data['@graph'] = [
            {"@type": "WebPage", "@id": u + '#page', "url": u, "name": titre, "description": desc,
             "inLanguage": lang, "dateModified": TODAY, "isPartOf": {"@id": SITE + '/#site'},
             "primaryImageOfPage": {"@type": "ImageObject", "url": img, "width": 1200, "height": 630},
             "mainEntity": {"@id": u + '#work'}, "breadcrumb": {"@id": u + '#crumbs'}},
            {"@type": "CreativeWork", "@id": u + '#work', "name": p['t'], "headline": f"{p['t']} · {L['cas']}",
             "description": f"{p['d']} {p.get('ctx', '')}".strip(), "url": u, "image": img, "inLanguage": lang,
             "dateCreated": p['y'][:4], "genre": p.get('k', ''),
             "creator": {"@id": SITE + '/#person'}, "author": {"@id": SITE + '/#person'},
             "about": {"@type": "Organization", "name": p['t']},
             "contributor": [{"@type": "Organization", "name": a} for a in agences]},
            {"@type": "BreadcrumbList", "@id": u + '#crumbs', "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": L['accueil'], "item": url(lang)},
                {"@type": "ListItem", "position": 2, "name": p['t'], "item": u}]},
            site, person]
        h = ld_put(h, m, data)
        out = os.path.join(ROOT, base.strip('/'), s) if base != '/' else os.path.join(ROOT, s)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
        open(os.path.join(out, '.genere'), 'w').write('')

# 3. 404 : l'accueil, non indexé (GitHub Pages le sert avec un statut 404)
h = rd('index.html').replace('<head>', '<head>\n<base href="/">', 1)
h = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex,follow">', h)
h = re.sub(r'<link rel="(canonical|alternate)"[^>]*>\n?', '', h)
wr('404.html', h)

# 4. Sitemap avec les paires de langues et les images de partage
def alts(s):
    return ''.join(f'<xhtml:link rel="alternate" hreflang="{hl}" href="{url(l, s)}"/>'
                   for hl, l in (('en', 'en'), ('fr', 'fr'), ('x-default', 'en')))
def image(s): return f'<image:image><image:loc>{SITE}/{"og/" + s if s else "og"}.jpg</image:loc></image:image>'
lignes = [f'<url><loc>{url(lang, s)}</loc><lastmod>{TODAY}</lastmod>{alts(s)}{image(s)}</url>'
          for s in [''] + slugs for lang in ('en', 'fr')]
wr('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" '
   'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(lignes) + '\n</urlset>\n')
print('pages :', ', '.join(slugs))
