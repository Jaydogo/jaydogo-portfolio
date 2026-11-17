// node render.mjs <page.html|url> <width> <height> <out.png> [scale]
import { createRequire } from 'module';
const require = createRequire('/Users/jaydogo/elyte-club/package.json');
const { chromium } = require('playwright');
const [src, w, h, out, sc] = process.argv.slice(2);
const s = Number(sc || 2);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: Math.round(w / s), height: Math.round(h / s) }, deviceScaleFactor: s });
await p.goto(src.startsWith('http') || src.startsWith('file:') ? src : 'file://' + src.split('?')[0].split('/').map(encodeURIComponent).join('/') + (src.includes('?') ? '?' + src.split('?')[1] : ''));
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
await p.screenshot({ path: out, clip: { x: 0, y: 0, width: Math.round(w / s), height: Math.round(h / s) } });
await b.close(); console.log('ok', out);
