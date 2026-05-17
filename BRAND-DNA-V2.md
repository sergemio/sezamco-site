# Sezam&Co — Brand Identity V2 (valide 2026-05-15)

> V2 = mise a jour de `BRAND-DNA.md` (V1, 2026-03-10) apres refonte direction artistique mai 2026.
> **Changements majeurs vs V1** : suppression du corail, adoption de l'orange comme accent CTA, vert profond eclairci, header blanc, pointillés SVG longs et visibles.

## Identite (inchangee vs V1)
- Nom : Sezam&Co
- Tagline : Street food libanaise
- Positionnement : street food libanaise authentique, moderne, accessible
- Vibe : chaleureux, decontracte, genereux, sans chichi
- Ce qu'on n'est PAS : fin dining, chic, formel, fusion, "healthy bowl"

---

## Palette de couleurs V2

### Fonds / Ambiance (dominants)
| Nom | Hex | Usage |
|-----|-----|-------|
| Creme | `#FFF8E1` | Fond principal sections, respiration |
| Vert pastel | `#D4EDCF` | Fond sections secondaires |
| Jaune doux | `#FFF4BD` | Fond accent, formule banner |
| Blanc pur | `#FFFFFF` | **NOUVEAU V2** — fond dropdown menu + cartes about |

### Accents forts (typo, CTAs, elements graphiques)
| Nom | Hex | Usage | Changement V2 |
|-----|-----|-------|---------------|
| Vert profond | `#3F7000` | Titres Ambery, header text, footer | **V1 etait `#1A3B06` — eclairci** |
| Vert logo | `#417F0A` | Logo, outline livraison Sezam | inchange |
| Vert "Formule" | `#2D6A0F` | Stroke des pointillés SVG | inchange |
| **Orange** | **`#FF8A00`** | **CTAs principaux, prix, badges, bouton "Commander" header** | **NOUVEAU — remplace le corail** |
| Orange hover | `#E07800` | Etat hover des CTAs orange | NOUVEAU |
| Jaune riche | `#F5D547` | Etoiles avis, accents secondaires | inchange |

### Couleurs SUPPRIMEES en V2
- ❌ Corail `#E84545` — totalement retire du site
- ❌ Corail hover `#d63333`
- ❌ Rose pastel `#F58181`

### Regle V2
- Les pastels + creme + blanc en fond
- L'**orange `#FF8A00`** est l'unique accent CTA fort (boutons, prix)
- Le **vert profond `#3F7000`** est pour les titres et textes forts
- Plus aucune trace de rouge/corail nulle part

---

## Header (changement majeur V2)

| Element | V1 | V2 |
|---------|----|----|
| Background header | `var(--cream)` (creme) | `var(--cream)` (inchange — test blanc rollback) |
| Background dropdown menu | `var(--cream)` | **`#fff`** |
| Bouton "Commander" (CTA header) | corail `#E84545` | **orange `#FF8A00`** (hover `#E07800`) |
| Shadow box CTA hover | `rgba(232,69,69,.3)` | `rgba(255,138,0,.4)` |

---

## Pointillés (changement majeur V2)

V1 utilisait `border: 2px dashed rgba(...)` (rendu CSS natif — tirets courts, peu visibles).

**V2 : SVG inline obligatoire** pour tous les encadrés visibles, pour tirets longs et bien espaces.

### Template SVG standard
```html
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25'%3E%3Crect x='1.5' y='1.5' width='99%25' height='99%25' rx='RX' ry='RX' fill='none' stroke='%232D6A0F' stroke-width='3' stroke-dasharray='14 10'/%3E%3C/svg%3E");
background-size: 100% 100%;
border: none;
```

- `RX` = la valeur `border-radius` du conteneur (14, 16, 20...)
- `stroke` = `%232D6A0F` (vert formule, visible)
- `stroke-width = 3`, `stroke-dasharray = '14 10'` (tirets longs)

### Pour inline style HTML (`style="..."`)
**Utiliser `&quot;` au lieu de `"`** autour de l'URL, sinon l'attribut HTML est casse :
```html
style="...background-image:url(&quot;data:image/svg+xml,...&quot;);background-size:100% 100%;..."
```

### Applique aux elements
- `.about-card` (3 cartes trust homepage)
- "Depuis Lyon 2" box (homepage)
- Page-hero outer box (menu, adresse, faq)
- `.vs-card--left/right` (meilleur-restaurant-libanais-lyon)
- `.also-card` (cartes "voir aussi" sur 8 pages)
- Box "Formule Sezam" (menu.html — reference d'origine, deja en SVG)

### Encadrés EXEMPTES (rester en CSS dashed natif)
- Petits separateurs horizontaux 1px (tables, dropdowns)
- `<hr ... border-top: dashed>` decoratifs
- Bordures internes de tableaux

---

## Typographie (inchangee vs V1)
| Usage | Font |
|-------|------|
| Titres & accents | **Ambery Garden** |
| Body text | **Nunito** (400, 600, 700, 800, 900) |

---

## Cartes livraison (NOUVEAU V2)

Section "Livraison" sur la home : 4 cartes fond blanc + outline 2px couleur brand de la plateforme + logo officiel.

| Plateforme | Outline color | Logo |
|------------|--------------|------|
| Commande directe Sezam | `#417F0A` (vert logo) | `logo-sezamco.webp` |
| Delicity | `#FF3D6E` (rose Delicity) | `delicity-logo.png` (officiel) |
| Uber Eats | `#06C167` (vert Uber) | Stylise : fond noir, "Uber" vert + "Eats" blanc |
| Deliveroo | `#00CCBC` (turquoise) | SVG kangourou + texte "deliveroo" |

Sous chaque carte, un tag `<span class="liv-sub">` avec le slogan (`Meilleur prix`, `Société française`, `Le classique`, `Livraison rapide`).

---

## Menu page (NOUVEAU V2)

- 26 plats avec photo thumbnail (90×90 px) a gauche de chaque item
- Clic sur la photo ouvre un **modal** (`.dish-modal-backdrop`) avec :
  - Photo grande (clamp 220-320px)
  - Nom du plat
  - Badge proteine (si applicable)
  - Prix + tag formule
  - Description
  - Section "Régime alimentaire" (tags Vegan/Veggie/Sésame)
  - Section "Allergènes connus" (auto-deduits par mot-cles)
  - Boutons "Commander" (orange `#FF8A00`) + "Fermer" (outline vert)
- Les **deux boutons** ont `border-radius: 50px` (pill) — `<button>` et `<a>` traités via `.dish-modal-cta a, .dish-modal-cta button`

### Best-sellers homepage : meme modal
Les cartes `.bs-card` sur index.html sont aussi cliquables et ouvrent le meme modal (adapte pour lire depuis `.bs-card-name`/`.bs-card-price`/`.bs-card-desc`/`.bs-card-img img`).

---

## Boutons / CTAs — Standard V2

| Type | Background | Color | Border-radius | Hover |
|------|-----------|-------|---------------|-------|
| CTA primaire (Commander) | `#FF8A00` | `#fff` | `50px` | `#E07800` + shadow orange |
| CTA secondaire (Fermer) | `transparent` | `var(--green-deep)` | `50px` | bg `var(--green-pastel)` |
| Header CTA | `#FF8A00` | `#fff` | `50px` | `#E07800` |

**Regle** : tous les boutons doivent etre **pill** (border-radius 50px). Pas de boutons carres/angulaires nulle part — un button HTML doit explicitement recevoir le radius.

---

## Structure homepage (inchangee vs V1)
1. Hero
2. Best-sellers (now clickable → modal)
3. Tradi ou Urbain
4. La Formule
5. Livraison (now: outline brand colors)
6. Avis Google ("800+" reviews, plus de chiffre exact)
7. Footer

---

## Halal — Strategie (inchangee)
- Present dans meta description, schema JSON-LD, footer SEO, FAQ
- Absent de hero, titres, marquee, visuels prominents

---

## Imagerie (inchangee)
- Photos reelles, lumiere chaude
- Stock pret : `G:\Mon Drive\6 - MARKETING\FOOD PICTURES\` (100+ photos)

---

## Technique
- Hebergement : Cloudflare Pages (auto-deploy depuis push master sur repo `sergemio/sezamco-site`)
- Deploy ~30-60s apres push
- Minification : html-minifier-terser via GitHub Actions
- Mobile-first, breakpoints 375 / 768 / 1200

---

## Reviews count (NOUVEAU V2)
Utiliser **"800+"** partout sur le site (jamais de chiffre exact). En mai 2026 on est a 819 reviews, mais le "+" donne du marge sans avoir a re-editer le site a chaque incrément.

---

## Quand creer un nouveau design V3+
- **Garder** : Ambery Garden, palette fonds pastels+blanc, orange #FF8A00, vert #3F7000, pointillés SVG `stroke-width=3 dasharray='14 10'`
- **Eviter** : corail, rouge, rose, vert tres fonce #1A3B06, header creme, boutons non-pill, CSS dashed natif sur conteneurs visibles
- **Toujours** : tester en local AVANT push, canary 1 page d'abord, ne JAMAIS promettre "0 risque" sur mass-edit

---

## Liens
- V1 historique : `BRAND-DNA.md` (10/03/2026)
- Pages source : `C:\Users\serge\Claude\topics\seo\refonte-siteweb\`
- Memoire SEO site web : `M/marketing/seo/site-web.md`
- Audit gaps : `M/marketing/seo/site-web-audit-gaps.md`
