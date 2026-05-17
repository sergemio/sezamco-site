# -*- coding: utf-8 -*-
"""Generate /street-food-libanaise-lyon and /snack-libanais-lyon from shawarma-lyon.html template.
Each output keeps CSS / header / footer / JS identical, replaces head metas + body content sections.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "shawarma-lyon.html")
src = open(TEMPLATE, encoding="utf-8").read()

# Helper: replace block by tag id/comment marker — we use literal string replace on big blocks
def rep(html, old, new, label=""):
    assert old in html, f"OLD not found for {label}"
    return html.replace(old, new, 1)

# =====================================================================================
# PAGE 1 — STREET FOOD LIBANAISE LYON
# =====================================================================================
p1 = src

# --- HEAD ---
p1 = rep(p1, "<title>Meilleur Shawarma Lyon — Poulet Mariné Maison | Sezam&Co</title>",
            "<title>Street Food Libanaise Lyon 2 | Man'ouches, Shawarma, Falafel | Sezam&Co</title>")
p1 = rep(p1, '<meta name="description" content="Shawarma poulet mariné 24h, grillé au four et servi en man\'ouché cuit minute. Lyon 2, Bellecour. Sur place, à emporter ou en livraison.">',
            '<meta name="description" content="Sezam&Co, la street food libanaise de Lyon 2. Man\'ouches cuites minute, shawarma poulet mariné maison, falafels croustillants. À Bellecour, à emporter ou en livraison. 7j/7.">')
p1 = rep(p1, '<link rel="canonical" href="https://sezamandco.com/shawarma-lyon">',
            '<link rel="canonical" href="https://sezamandco.com/street-food-libanaise-lyon">')
p1 = rep(p1, '<meta property="og:title" content="Shawarma Lyon 2 | Poulet Grillé au Four | Sezam&Co">',
            '<meta property="og:title" content="Street Food Libanaise Lyon 2 | Sezam&Co">')
p1 = rep(p1, '<meta property="og:description" content="Shawarma poulet mariné aux épices, grillé au four, servi en man\'ouche libanais. 100% halal. Lyon 2.">',
            '<meta property="og:description" content="La street food libanaise au cœur de Lyon 2. Man\'ouches, shawarma, falafels, mezzes — cuits minute, halal, faits maison.">')
p1 = rep(p1, '<meta property="og:url" content="https://sezamandco.com/shawarma-lyon">',
            '<meta property="og:url" content="https://sezamandco.com/street-food-libanaise-lyon">')

# JSON-LD
p1 = rep(p1,
    '"name": "Shawarma à Lyon — Poulet Grillé au Four",\n    "description": "Le meilleur shawarma poulet à Lyon 2 : viande marinée maison, grillée au four, servie dans un man\'ouche libanais.",\n    "url": "https://sezamandco.com/shawarma-lyon",',
    '"name": "Street Food Libanaise à Lyon",\n    "description": "Sezam&Co — la street food libanaise au cœur de Lyon 2 : man\'ouches cuites minute, shawarma, falafels, mezzes. Halal, frais, faits maison.",\n    "url": "https://sezamandco.com/street-food-libanaise-lyon",')
p1 = rep(p1,
    '{ "@type": "ListItem", "position": 2, "name": "Shawarma à Lyon", "item": "https://sezamandco.com/shawarma-lyon" }',
    '{ "@type": "ListItem", "position": 2, "name": "Street Food Libanaise à Lyon", "item": "https://sezamandco.com/street-food-libanaise-lyon" }')

# --- DROPDOWN ACTIVE: remove shawarma highlight on this page ---
p1 = rep(p1,
    '<a href="shawarma-lyon.html" style="color:var(--coral);font-weight:800;">Shawarma à Lyon</a>',
    '<a href="shawarma-lyon.html">Shawarma à Lyon</a>')

# --- HERO ---
HERO_OLD = '''      <h1>Shawarma à Lyon | Sezam&amp;Co</h1>
      <p>Poulet mariné aux épices maison, grillé au four, servi en <a href="manouche.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">man'ouché</a> cuit minute. <a href="index.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">Restaurant libanais Lyon 2</a>, Bellecour.</p>
      <div style="display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;margin-top:1.2rem;">
        <a href="https://commandes.sezamandco.com" class="btn btn-primary" style="font-size:1rem;padding:.9rem 2rem;">Commander</a>
        <span style="font-family:var(--font-display);font-size:clamp(1.4rem,3vw,1.8rem);color:var(--yellow-soft);">à partir de 9,20&nbsp;€</span>
      </div>'''
HERO_NEW = '''      <h1>Street Food Libanaise à Lyon</h1>
      <p>La street food libanaise comme dans les rues de Beyrouth, au cœur de <a href="index.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">Lyon 2</a>. <a href="manouche.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">Man'ouches</a> cuites minute, shawarma grillé au four, falafels croustillants — à Bellecour, à emporter ou en livraison.</p>
      <div style="display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;margin-top:1.2rem;">
        <a href="https://commandes.sezamandco.com" class="btn btn-primary" style="font-size:1rem;padding:.9rem 2rem;">Commander</a>
        <span style="font-family:var(--font-display);font-size:clamp(1.4rem,3vw,1.8rem);color:var(--yellow-soft);">dès 5,50&nbsp;€</span>
      </div>'''
p1 = rep(p1, HERO_OLD, HERO_NEW, "hero1")

# --- MARQUEE 1 ---
MARQ_OLD = '''      <span>Shawarma</span><span class="sep">◆</span>
      <span>Poulet Mariné</span><span class="sep">◆</span>
      <span>Grillé au Four</span><span class="sep">◆</span>
      <span>Épices Maison</span><span class="sep">◆</span>
      <span>100% Halal</span><span class="sep">◆</span>
      <span>Lyon 2</span><span class="sep">◆</span>
      <span>Shawarma</span><span class="sep">◆</span>
      <span>Poulet Mariné</span><span class="sep">◆</span>
      <span>Grillé au Four</span><span class="sep">◆</span>
      <span>Épices Maison</span><span class="sep">◆</span>
      <span>100% Halal</span><span class="sep">◆</span>
      <span>Lyon 2</span><span class="sep">◆</span>'''
MARQ1_NEW = '''      <span>Street Food</span><span class="sep">◆</span>
      <span>Libanaise</span><span class="sep">◆</span>
      <span>Man\'ouche Cuit Minute</span><span class="sep">◆</span>
      <span>Shawarma</span><span class="sep">◆</span>
      <span>Falafel</span><span class="sep">◆</span>
      <span>Mezze</span><span class="sep">◆</span>
      <span>Bellecour</span><span class="sep">◆</span>
      <span>Lyon 2</span><span class="sep">◆</span>
      <span>Street Food</span><span class="sep">◆</span>
      <span>Libanaise</span><span class="sep">◆</span>
      <span>Man\'ouche Cuit Minute</span><span class="sep">◆</span>
      <span>Halal</span><span class="sep">◆</span>'''
p1 = rep(p1, MARQ_OLD, MARQ1_NEW, "marquee1-p1")

# --- PRODUCT SHOWCASE ---
PS_OLD = '''        <div class="product-img">
          <img src="assets/images/shawarma/detail.webp" alt="Shawarma poulet Sezam&Co — viande marinée, laitue, frites, pickles, sauce à l'ail" loading="lazy">
        </div>
        <div class="product-info">
          <h2>Notre Shawarma Poulet</h2>
          <p>Poulet mariné aux épices libanaises, grillé au four, garni de laitue, frites croustillantes, pickles et notre sauce à l'ail maison, le tout relevé d'une touche de sumac. Servi dans un <a href="manouche.html" style="color:var(--coral);font-weight:700;">man'ouché</a> moelleux cuit minute.</p>
          <div class="product-prices">
            <div class="price-box">
              <div class="price-box-label">Seul</div>
              <div class="price-box-amount">9,20&nbsp;€</div>
            </div>
            <div class="price-box price-box--formule">
              <div class="price-box-label">En Formule</div>
              <div class="price-box-amount">14,60&nbsp;€</div>
            </div>
          </div>
          <a href="https://commandes.sezamandco.com" class="btn btn-primary">Commander</a>
        </div>'''
PS_NEW = '''        <div class="product-img">
          <img src="assets/images/shawarma/detail.webp" alt="Street food libanaise Sezam&Co — man'ouche, shawarma, falafel" loading="lazy">
        </div>
        <div class="product-info">
          <h2>Qu\'est-ce que la Street Food Libanaise ?</h2>
          <p>La street food libanaise, c\'est la cuisine de rue de Beyrouth&nbsp;: des plats qui se mangent à la main, debout, en marchant, sans chichi. Une <a href="manouche.html" style="color:var(--coral);font-weight:700;">man\'ouche</a> chaude qu\'on plie en deux, un shawarma roulé minute, des falafels à peine sortis du bain. Du frais, du chaud, du goût — pas du fast food industriel.</p>
          <p>Chez Sezam&amp;Co, c\'est cette tradition qu\'on perpétue à Lyon 2, depuis Bellecour. Tout est fait maison, cuit minute, et halal.</p>
          <a href="https://commandes.sezamandco.com" class="btn btn-primary">Commander</a>
        </div>'''
p1 = rep(p1, PS_OLD, PS_NEW, "product-showcase-p1")

# --- "CE QUI REND DIFFÉRENT" SECTION ---
DIFF_OLD = '''      <h2 class="section-title rv">Ce Qui Rend Notre Shawarma Différent</h2>
      <p class="section-sub rv rv-d1">Du shawarma authentique (aussi écrit chawarma), comme dans les rues de Beyrouth</p>'''
DIFF_NEW = '''      <h2 class="section-title rv">Nos Spécialités Street Food à Lyon</h2>
      <p class="section-sub rv rv-d1">4 piliers de la street food libanaise — tous faits maison, tous cuits minute</p>'''
p1 = rep(p1, DIFF_OLD, DIFF_NEW, "diff-title-p1")

# Replace 5 diff cards
DIFFCARDS_OLD = '''          <h3>Marinade maison</h3>
          <p>Nos épices sont préparées chaque jour dans notre cuisine. Jamais de sauce industrielle, jamais de raccourcis.</p>'''
DIFFCARDS_NEW = '''          <h3>Man\'ouche cuite minute</h3>
          <p>Notre signature&nbsp;: la galette libanaise pétrie et cuite à la minute, garnie sous vos yeux. <a href="manouche.html" style="color:var(--coral);font-weight:700;">18 recettes</a> dès 5,50&nbsp;€.</p>'''
p1 = rep(p1, DIFFCARDS_OLD, DIFFCARDS_NEW, "diff1")

p1 = rep(p1,
    '<h3>Grillé au four</h3>\n          <p>Pas de broche rotative. Cuisson lente au four pour une viande fondante et juteuse, avec tout le jus préservé.</p>',
    '<h3>Shawarma poulet</h3>\n          <p>Poulet mariné 24h, grillé au four — pas de broche industrielle. Servi en <a href="shawarma-lyon.html" style="color:var(--coral);font-weight:700;">man\'ouché shawarma</a>, l\'icône de la street food libanaise.</p>')

p1 = rep(p1,
    '<h3>Servi en man\'ouché</h3>\n          <p>Notre spécialité&nbsp;: la <a href="manouche.html" style="color:var(--coral);font-weight:700;">galette libanaise</a> cuite minute au four. Pas de wrap industriel, pas de pita réchauffée.</p>',
    '<h3>Falafel crunch</h3>\n          <p>Pois chiches, herbes fraîches, épices — frits minute. Croustillants dehors, fondants dedans. Voir notre page <a href="falafel-lyon.html" style="color:var(--coral);font-weight:700;">falafel à Lyon</a>.</p>')

p1 = rep(p1,
    '<h3>100% halal</h3>\n          <p>Viande de poulet certifiée halal, sans exception. Ingrédients frais, sélectionnés avec soin.</p>',
    '<h3>Mezzes à partager</h3>\n          <p>Houmous bio, moutabal d\'aubergine fumée, fattouch, labné — la tradition <a href="mezze-lyon.html" style="color:var(--coral);font-weight:700;">mezze libanais</a>, version street food à emporter.</p>')

p1 = rep(p1,
    '<h3>Produits frais</h3>\n          <p>Légumes croquants, sauces faites maison — ail, tarator, houmous. Tout est préparé le jour même.</p>',
    '<h3>100% halal & frais</h3>\n          <p>Viandes certifiées halal, légumes croquants, sauces maison. La street food libanaise authentique, sans raccourcis industriels.</p>')

# --- FORMULE BANNER ---
FB_OLD = '''      <div class="formule-text rv">
        <h2>Shawarma en Formule</h2>
        <p>1 shawarma man'ouché + 1 starter au choix (houmous, fattouch, falafel crunch, moutabal...) + 1 boisson. Le déjeuner rapide idéal entre Bellecour et Cordeliers.</p>
        <span class="formule-price">14,60&nbsp;€</span>
      </div>
      <div class="formule-img rv rv-d1">
        <img src="assets/images/shawarma/formule.webp" alt="Formule shawarma — man'ouche + starter + boisson" loading="lazy">
      </div>'''
FB_NEW = '''      <div class="formule-text rv">
        <h2>Street Food Libanaise à Bellecour</h2>
        <p>Sezam&amp;Co est au 6 rue Petit David, entre <a href="index.html" style="color:var(--coral);font-weight:700;">Bellecour</a> et Cordeliers — au cœur de la Presqu\'île de Lyon. À 3 min à pied du métro Cordeliers, à 5 min de Bellecour. La street food libanaise version Lyon 2.</p>
        <span class="formule-price" style="font-size:clamp(1.6rem,3vw,2.2rem);">7j/7 — 12h&nbsp;à&nbsp;23h</span>
      </div>
      <div class="formule-img rv rv-d1">
        <img src="assets/images/shawarma/formule.webp" alt="Street food libanaise Bellecour — Sezam&Co" loading="lazy">
      </div>'''
p1 = rep(p1, FB_OLD, FB_NEW, "formule-p1")

# --- CTA SECTION ---
CTA_OLD = '''        <h2>Envie d'un Shawarma ?</h2>
        <p>Sur place au 6 rue Petit David (Lyon 2), à emporter, ou en livraison.</p>'''
CTA_NEW = '''        <h2>Envie de Street Food Libanaise ?</h2>
        <p>Sur place au 6 rue Petit David (Lyon 2), à emporter, ou en livraison à Lyon — du 1er au 7e arrondissement via <a href="livraison-libanais-lyon.html" style="color:var(--coral);font-weight:700;">Uber Eats, Deliveroo et notre commande directe</a>.</p>'''
p1 = rep(p1, CTA_OLD, CTA_NEW, "cta-p1")

# --- FOOTER SEO PARAGRAPH ---
FSEO_OLD = '<p>Sezam&amp;Co, c\'est la street food libanaise au cœur de <a href="adresse.html">Lyon 2</a>. Man\'ouches cuits minute, mezzes faits maison, <a href="falafel-lyon.html">falafel</a>, options vegan et végétariennes, viandes certifiées halal. Que vous cherchiez un <a href="index.html">restaurant libanais à Lyon</a>, un déjeuner rapide près de Bellecour, une livraison libanaise à Lyon, un <a href="shawarma-lyon.html">shawarma à Lyon</a> ou une <a href="manouche.html">man\'ouche à Lyon</a>&nbsp;— poussez la porte, ou commandez en ligne.</p>'
FSEO_NEW_P1 = '<p>Sezam&amp;Co, la <strong>street food libanaise</strong> au cœur de <a href="adresse.html">Lyon 2</a>, entre Bellecour et Cordeliers. Cuisine de rue authentique&nbsp;: <a href="manouche.html">man\'ouches</a> cuites minute, <a href="shawarma-lyon.html">shawarma</a> poulet mariné maison, <a href="falafel-lyon.html">falafels</a> croustillants, <a href="mezze-lyon.html">mezzes</a> traditionnels. Halal, frais, fait maison. Que vous cherchiez de la street food libanaise à Lyon, un <a href="index.html">restaurant libanais à Lyon 2</a>, un déjeuner street food à Bellecour, ou une <a href="livraison-libanais-lyon.html">livraison libanaise à Lyon</a>&nbsp;— Sezam&amp;Co vous accueille 7j/7, ou commandez en ligne.</p>'
p1 = rep(p1, FSEO_OLD, FSEO_NEW_P1, "footer-seo-p1")

# Write page 1
OUT1 = os.path.join(HERE, "street-food-libanaise-lyon.html")
open(OUT1, "w", encoding="utf-8").write(p1)
print(f"Wrote {OUT1} ({len(p1)} chars)")


# =====================================================================================
# PAGE 2 — SNACK LIBANAIS LYON
# =====================================================================================
p2 = src

p2 = rep(p2, "<title>Meilleur Shawarma Lyon — Poulet Mariné Maison | Sezam&Co</title>",
            "<title>Snack Libanais Lyon | Déjeuner Rapide, Halal, À Emporter | Sezam&Co</title>")
p2 = rep(p2, '<meta name="description" content="Shawarma poulet mariné 24h, grillé au four et servi en man\'ouché cuit minute. Lyon 2, Bellecour. Sur place, à emporter ou en livraison.">',
            '<meta name="description" content="Le snack libanais de Lyon 2 : man\'ouche cuite minute, shawarma, falafel — déjeuner rapide à Bellecour. Halal, frais, à emporter ou livraison. Dès 5,50€.">')
p2 = rep(p2, '<link rel="canonical" href="https://sezamandco.com/shawarma-lyon">',
            '<link rel="canonical" href="https://sezamandco.com/snack-libanais-lyon">')
p2 = rep(p2, '<meta property="og:title" content="Shawarma Lyon 2 | Poulet Grillé au Four | Sezam&Co">',
            '<meta property="og:title" content="Snack Libanais Lyon 2 | Sezam&Co">')
p2 = rep(p2, '<meta property="og:description" content="Shawarma poulet mariné aux épices, grillé au four, servi en man\'ouche libanais. 100% halal. Lyon 2.">',
            '<meta property="og:description" content="Snack libanais à Lyon 2 — déjeuner rapide halal, man\'ouche cuite minute, shawarma, falafel. Dès 5,50€. Bellecour.">')
p2 = rep(p2, '<meta property="og:url" content="https://sezamandco.com/shawarma-lyon">',
            '<meta property="og:url" content="https://sezamandco.com/snack-libanais-lyon">')

p2 = rep(p2,
    '"name": "Shawarma à Lyon — Poulet Grillé au Four",\n    "description": "Le meilleur shawarma poulet à Lyon 2 : viande marinée maison, grillée au four, servie dans un man\'ouche libanais.",\n    "url": "https://sezamandco.com/shawarma-lyon",',
    '"name": "Snack Libanais à Lyon",\n    "description": "Snack libanais à Lyon 2 — déjeuner rapide, man\'ouche cuite minute, shawarma, falafel. Halal, frais, à emporter. Dès 5,50€.",\n    "url": "https://sezamandco.com/snack-libanais-lyon",')
p2 = rep(p2,
    '{ "@type": "ListItem", "position": 2, "name": "Shawarma à Lyon", "item": "https://sezamandco.com/shawarma-lyon" }',
    '{ "@type": "ListItem", "position": 2, "name": "Snack Libanais à Lyon", "item": "https://sezamandco.com/snack-libanais-lyon" }')

p2 = rep(p2,
    '<a href="shawarma-lyon.html" style="color:var(--coral);font-weight:800;">Shawarma à Lyon</a>',
    '<a href="shawarma-lyon.html">Shawarma à Lyon</a>')

# HERO
HERO_NEW_P2 = '''      <h1>Snack Libanais à Lyon</h1>
      <p>Votre snack libanais à <a href="index.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">Lyon 2</a> — <a href="manouche.html" style="color:var(--yellow-soft);border-bottom:1px solid var(--yellow-soft);">man'ouches</a> cuites minute, shawarma poulet, falafels frais. Le déjeuner rapide qui change du sandwich. À Bellecour, dès 5,50&nbsp;€.</p>
      <div style="display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;margin-top:1.2rem;">
        <a href="https://commandes.sezamandco.com" class="btn btn-primary" style="font-size:1rem;padding:.9rem 2rem;">Commander mon déjeuner</a>
        <span style="font-family:var(--font-display);font-size:clamp(1.4rem,3vw,1.8rem);color:var(--yellow-soft);">dès 5,50&nbsp;€</span>
      </div>'''
p2 = rep(p2, HERO_OLD, HERO_NEW_P2, "hero-p2")

MARQ2_NEW = '''      <span>Snack Libanais</span><span class="sep">◆</span>
      <span>Déjeuner Rapide</span><span class="sep">◆</span>
      <span>Halal</span><span class="sep">◆</span>
      <span>À Emporter</span><span class="sep">◆</span>
      <span>Dès 5,50€</span><span class="sep">◆</span>
      <span>Bellecour</span><span class="sep">◆</span>
      <span>Lyon 2</span><span class="sep">◆</span>
      <span>Snack Libanais</span><span class="sep">◆</span>
      <span>Déjeuner Rapide</span><span class="sep">◆</span>
      <span>Halal</span><span class="sep">◆</span>
      <span>À Emporter</span><span class="sep">◆</span>
      <span>Lyon 2</span><span class="sep">◆</span>'''
p2 = rep(p2, MARQ_OLD, MARQ2_NEW, "marquee-p2")

# PRODUCT SHOWCASE
PS_NEW_P2 = '''        <div class="product-img">
          <img src="assets/images/shawarma/detail.webp" alt="Snack libanais Sezam&Co — man'ouche, shawarma, falafel à emporter" loading="lazy">
        </div>
        <div class="product-info">
          <h2>Snack Rapide, Pas Fast Food</h2>
          <p>Un snack libanais, ce n\'est pas un fast food&nbsp;: pas de viande surgelée, pas de sauce industrielle, pas de pain réchauffé. Chez Sezam&amp;Co, votre snack du midi à Bellecour, c\'est une <a href="manouche.html" style="color:var(--coral);font-weight:700;">man\'ouche pétrie et cuite minute</a> sous vos yeux, du shawarma poulet mariné maison, des falafels frits à la commande.</p>
          <div class="product-prices">
            <div class="price-box">
              <div class="price-box-label">Man\'ouche dès</div>
              <div class="price-box-amount">5,50&nbsp;€</div>
            </div>
            <div class="price-box price-box--formule">
              <div class="price-box-label">Formule Midi</div>
              <div class="price-box-amount">14,60&nbsp;€</div>
            </div>
          </div>
          <a href="https://commandes.sezamandco.com" class="btn btn-primary">Commander</a>
        </div>'''
p2 = rep(p2, PS_OLD, PS_NEW_P2, "product-p2")

# DIFF SECTION
DIFF_NEW_P2 = '''      <h2 class="section-title rv">Le Meilleur Snack à Bellecour pour le Déjeuner</h2>
      <p class="section-sub rv rv-d1">Rapide, halal, frais — le snack libanais qui change du sandwich-club</p>'''
p2 = rep(p2, DIFF_OLD, DIFF_NEW_P2, "diff-title-p2")

# Cards
p2 = rep(p2,
    '<h3>Marinade maison</h3>\n          <p>Nos épices sont préparées chaque jour dans notre cuisine. Jamais de sauce industrielle, jamais de raccourcis.</p>',
    '<h3>Servi en 5 minutes</h3>\n          <p>Pause déjeuner courte&nbsp;? On vous sert votre <a href="manouche.html" style="color:var(--coral);font-weight:700;">man\'ouche</a> ou shawarma en 5 min chrono. Vous mangez sur place, à emporter, ou à votre bureau.</p>')

p2 = rep(p2,
    '<h3>Grillé au four</h3>\n          <p>Pas de broche rotative. Cuisson lente au four pour une viande fondante et juteuse, avec tout le jus préservé.</p>',
    '<h3>100% halal</h3>\n          <p>Toutes nos viandes sont certifiées halal. Idéal pour un snack halal à Lyon 2 — viande, sauces, accompagnements, tout est tracé.</p>')

p2 = rep(p2,
    '<h3>Servi en man\'ouché</h3>\n          <p>Notre spécialité&nbsp;: la <a href="manouche.html" style="color:var(--coral);font-weight:700;">galette libanaise</a> cuite minute au four. Pas de wrap industriel, pas de pita réchauffée.</p>',
    '<h3>Snack à emporter</h3>\n          <p>Tout notre menu est <a href="livraison-libanais-lyon.html" style="color:var(--coral);font-weight:700;">à emporter</a> ou en livraison (Uber Eats, Deliveroo). Un libanais à emporter à Lyon dès 5,50&nbsp;€.</p>')

p2 = rep(p2,
    '<h3>100% halal</h3>\n          <p>Viande de poulet certifiée halal, sans exception. Ingrédients frais, sélectionnés avec soin.</p>',
    '<h3>Frais, pas industriel</h3>\n          <p>Pâte pétrie chaque matin, légumes croquants, sauces maison (tarator, ail, harissa). Un snack frais, à l\'opposé du fast food classique.</p>')

p2 = rep(p2,
    '<h3>Produits frais</h3>\n          <p>Légumes croquants, sauces faites maison — ail, tarator, houmous. Tout est préparé le jour même.</p>',
    '<h3>Snack végé / vegan</h3>\n          <p>Falafel, zaatar, houmous, moutabal — la moitié du menu est <a href="vegetarien-vegan-lyon.html" style="color:var(--coral);font-weight:700;">végétarien ou vegan</a>. Snack libanais inclusif.</p>')

# FORMULE BANNER
FB_NEW_P2 = '''      <div class="formule-text rv">
        <h2>Formule Snack Libanais — 14,60&nbsp;€</h2>
        <p>1 man\'ouché shawarma (ou autre garniture) + 1 starter au choix (houmous, fattouch, falafel crunch, moutabal...) + 1 boisson. Le déjeuner rapide complet, entre Bellecour et Cordeliers.</p>
        <span class="formule-price">14,60&nbsp;€</span>
      </div>
      <div class="formule-img rv rv-d1">
        <img src="assets/images/shawarma/formule.webp" alt="Formule snack libanais — man'ouche + starter + boisson" loading="lazy">
      </div>'''
p2 = rep(p2, FB_OLD, FB_NEW_P2, "formule-p2")

# CTA
CTA_NEW_P2 = '''        <h2>Snack Libanais Ouvert 7j/7 à Bellecour</h2>
        <p>Sezam&amp;Co est au 6 rue Petit David (Lyon 2), à 3 min de Cordeliers, 5 min de Bellecour. Ouvert tous les jours de 12h à 23h. Sur place, à emporter, ou en <a href="livraison-libanais-lyon.html" style="color:var(--coral);font-weight:700;">livraison à Lyon</a>.</p>'''
p2 = rep(p2, CTA_OLD, CTA_NEW_P2, "cta-p2")

# FOOTER SEO
FSEO_NEW_P2 = '<p>Sezam&amp;Co, le <strong>snack libanais</strong> au cœur de <a href="adresse.html">Lyon 2</a>, entre Bellecour et Cordeliers. Le snack rapide qui change du sandwich&nbsp;: <a href="manouche.html">man\'ouches</a> cuites minute dès 5,50€, <a href="shawarma-lyon.html">shawarma</a> poulet mariné, <a href="falafel-lyon.html">falafels</a> croustillants. Halal, à emporter, en livraison. Que vous cherchiez un snack à Bellecour, un déjeuner rapide à Lyon 2, un libanais à emporter, un snack halal ou un <a href="index.html">restaurant libanais à Lyon</a>&nbsp;— Sezam&amp;Co est ouvert 7j/7 de 12h à 23h.</p>'
p2 = rep(p2, FSEO_OLD, FSEO_NEW_P2, "footer-seo-p2")

OUT2 = os.path.join(HERE, "snack-libanais-lyon.html")
open(OUT2, "w", encoding="utf-8").write(p2)
print(f"Wrote {OUT2} ({len(p2)} chars)")
