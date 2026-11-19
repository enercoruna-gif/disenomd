"""Visita webs públicas, hace capturas propias y extrae tokens visuales (uso: python3 src/rastreo.py)."""
import asyncio, json, re, shutil, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
SITIOS = json.loads((RAIZ / "src/sitios.json").read_text())

JS = r"""() => {
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 4 && r.height > 4 && r.top < innerHeight * 2 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.1; };
  const rgb = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); if (p.length > 3 && p[3] < 0.5) return null; return '#' + p.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase(); };
  const cuenta = {}, texto = {}, fuentes = {}, radios = {};
  document.querySelectorAll('body *').forEach(e => {
    if (!vis(e)) return; const s = getComputedStyle(e), r = e.getBoundingClientRect(), area = r.width * r.height;
    const bg = rgb(s.backgroundColor); if (bg) cuenta[bg] = (cuenta[bg] || 0) + area;
    if (e.childNodes.length && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 2)) {
      const c = rgb(s.color); if (c) texto[c] = (texto[c] || 0) + 1;
      const f = s.fontFamily.split(',')[0].replace(/["']/g, '').trim(); fuentes[f] = (fuentes[f] || 0) + 1;
    }
    if (parseFloat(s.borderTopLeftRadius) > 0 && bg) radios[s.borderTopLeftRadius] = (radios[s.borderTopLeftRadius] || 0) + 1;
  });
  const top = (o, n) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, n).map(x => x[0]);
  const enPantalla = e => { const r = e.getBoundingClientRect(); return vis(e) && r.top >= 0 && r.top < innerHeight && r.left >= 0 && r.left < innerWidth; };
  const aviso = e => /cookie|consent|didomi|onetrust|privacidad|privacy|skip|saltar/i.test((e.id + ' ' + e.className + ' ' + (e.closest('[id*=cookie],[class*=cookie],[id*=consent],[class*=consent]') ? 'cookie' : '') + ' ' + e.textContent).toString());
  const h = [...document.querySelectorAll('h1')].find(enPantalla) || [...document.querySelectorAll('h1,h2')].find(vis);
  const hs = h ? getComputedStyle(h) : null;
  const botones = [...document.querySelectorAll('a,button')].filter(e => enPantalla(e) && !aviso(e)).map(e => [e, getComputedStyle(e)]).filter(([e, s]) => rgb(s.backgroundColor) && e.textContent.trim().length > 1 && e.textContent.trim().length < 40);
  const b = botones[0];
  const bodyS = getComputedStyle(document.body), htmlS = getComputedStyle(document.documentElement);
  return {
    titulo: document.title, fondo: rgb(bodyS.backgroundColor) || rgb(htmlS.backgroundColor) || '#FFFFFF',
    fondos: top(cuenta, 8), textos: top(texto, 6), fuentes: top(fuentes, 4), radios: top(radios, 5),
    h1: hs ? { texto: h.textContent.trim().slice(0, 90), familia: hs.fontFamily.split(',')[0].replace(/["']/g, ''), tam: hs.fontSize, peso: hs.fontWeight, ls: hs.letterSpacing, lh: hs.lineHeight } : null,
    cuerpo: { familia: bodyS.fontFamily.split(',')[0].replace(/["']/g, ''), tam: bodyS.fontSize, lh: bodyS.lineHeight },
    boton: b ? { texto: b[0].textContent.trim(), fondo: rgb(b[1].backgroundColor), color: rgb(b[1].color), radio: b[1].borderTopLeftRadius, padding: b[1].padding, peso: b[1].fontWeight } : null,
    enlace: (() => { const a = [...document.querySelectorAll('main a, p a')].find(vis); return a ? rgb(getComputedStyle(a).color) : null; })(),
  };
}"""

CONSENTIR = re.compile(r"^\s*(aceptar( todo| todas| y cerrar| y continuar| cookies)?|acepto|accept( all| cookies)?|allow all|permitir todas|agree|estoy de acuerdo|de acuerdo|entendido|ok)\s*$", re.I)


LIMPIAR = r"""() => {
  const patron = /cookie|consent|didomi|onetrust|gdpr|privacy|modal|overlay|backdrop|dialog|popup|banner-cookies|cmp/i;
  document.querySelectorAll('body *').forEach(e => {
    const s = getComputedStyle(e); if (s.position !== 'fixed' && s.position !== 'absolute') return;
    const r = e.getBoundingClientRect(), area = r.width * r.height / (innerWidth * innerHeight);
    const nombre = (e.id + ' ' + e.className + ' ' + (e.getAttribute('role') || '') + ' ' + (e.getAttribute('aria-label') || '')).toString();
    if ((s.position === 'fixed' && (patron.test(nombre) || /cookie/i.test((e.innerText || '').slice(0, 400)) || area > 0.5 && +s.zIndex > 10 && !e.querySelector('img,video,picture'))) || e.getAttribute('aria-modal') === 'true' || e.tagName === 'DIALOG') e.style.setProperty('display', 'none', 'important');
  });
  for (const e of [document.documentElement, document.body]) { e.style.setProperty('overflow', 'auto', 'important'); e.style.setProperty('filter', 'none', 'important'); }
  document.querySelectorAll('body > *').forEach(e => { if (getComputedStyle(e).filter !== 'none') e.style.setProperty('filter', 'none', 'important'); });
}"""


async def aceptar_cookies(pg):
  for _ in range(2):
    for fr in pg.frames:
      for sel in ["#onetrust-accept-btn-handler", "#didomi-notice-agree-button", "#sp-cc-accept", "[data-testid*=accept]"]:
        try:
          if await fr.locator(sel).count():
            await fr.locator(sel).first.click(timeout=1500); await pg.wait_for_timeout(900); return
        except Exception: pass
      try:
        bt = fr.get_by_role("button", name=CONSENTIR)
        if await bt.count():
          await bt.first.click(timeout=1500); await pg.wait_for_timeout(900); return
      except Exception: pass
    await pg.wait_for_timeout(1500)


async def uno(nav, s, sem):
  async with sem:
    destino = RAIZ / "docs/analisis" / s["slug"]; destino.mkdir(parents=True, exist_ok=True)
    ctx = await nav.new_context(viewport={"width": 1280, "height": 800}, locale="es-ES", user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36")
    pg = await ctx.new_page()
    try:
      await pg.goto(s["url"], wait_until="domcontentloaded", timeout=45000)
      await pg.wait_for_timeout(4500)
      await aceptar_cookies(pg)
      await pg.evaluate(LIMPIAR); await pg.wait_for_timeout(600)
      datos = await pg.evaluate(JS)
      png = destino / "captura.png"
      await pg.screenshot(path=str(png))
      Image.open(png).convert("RGB").resize((960, 600)).save(destino / "captura.webp", "WEBP", quality=72)
      png.unlink()
      datos.update(slug=s["slug"], url=s["url"], final=pg.url)
      (RAIZ / "src/analisis" / f"{s['slug']}.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1))
      print("ok", s["slug"], datos["fondo"], datos["cuerpo"]["familia"], flush=True)
    except Exception as e:
      print("FALLO", s["slug"], str(e)[:120], flush=True)
    finally:
      await ctx.close()

async def main():
  solo = set(sys.argv[1:])
  async with async_playwright() as p:
    nav = await p.chromium.launch(executable_path=shutil.which("google-chrome") or shutil.which("chromium"), args=["--disable-blink-features=AutomationControlled"])
    sem = asyncio.Semaphore(6)
    await asyncio.gather(*(uno(nav, s, sem) for s in SITIOS if not solo or s["slug"] in solo))
    await nav.close()

asyncio.run(main())
