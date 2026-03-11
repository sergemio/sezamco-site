# Refonte Site Web Sezam&Co — Wix > Site statique

## Objectif
Remplacer le site Wix (sezamandco.com) par un site statique code main, optimise SEO, rapide, gratuit a heberger.

## Pourquoi switcher
- **Performance** : Wix genere du JS/CSS bloat. Site statique = LCP <1s, PageSpeed 95+
- **SEO** : controle total du HTML (Hn, schema, meta, URLs, sitemap)
- **Cout** : Wix = abonnement mensuel. Cloudflare Pages = gratuit
- **Controle** : plus de limitations Wix sur le markup, les redirects, le schema JSON-LD

## Stack technique
- **HTML / CSS / JS** statique (pas de framework)
- **Hebergement** : Cloudflare Pages (gratuit, CDN, HTTPS auto, deploy via Git)
- **Formulaire** : Formspree ou equivalent (gratuit)
- **Domaine** : garder sezamandco.com, changer uniquement le DNS
- **Repo** : `C:\Users\serge\Claude\refonte-siteweb\`

---

# INVENTAIRE DES PAGES

## Pages actuelles (site Wix)
| # | URL | Meta title | Focus KW | Statut |
|---|---|---|---|---|
| 1 | `/` (homepage) | Sezam&Co \| Restaurant Libanais & Street Food Lyon 2 | restaurant libanais Lyon 2 | a recoder |
| 2 | `/menu` | [non verifie] | menu libanais lyon | a recoder |
| 3 | `/mission` | restaurant libanais a Lyon 2 - Sezam&Co \| Notre mission | restaurant libanais Lyon 2 | a recoder |
| 4 | `/adresse` | Restaurant Libanais Lyon 2 Bellecour \| Adresse & Horaires \| Sezam&Co | Cuisine libanaise Lyon 2 | a recoder |
| 5 | `/restaurant-libanais-lyon-1` | Restaurant Libanais Lyon 1 — Terreaux & Presqu'ile \| Sezam&Co | Restaurant Libanais Lyon 1 | a recoder |
| 6 | `/faq` | FAQ \| Sezam&Co \| Vos questions \| Livraison Libanais Lyon | restaurant halal lyon 2 | a recoder |
| 7 | `/notre-histoire` | Notre Histoire \| Cuisine Libanaise a Lyon \| Sezam&co | Street food Libanaise Lyon | a recoder |
| 8 | `/manouche` | Man'ouche Lyon 2 \| Galette Libanaise Artisanale \| Sezam&Co | manouche Lyon | a recoder |
| 9 | `/shawarma-lyon` | Shawarma Lyon 2 \| Poulet Grille au Four \| Sezam&Co | shawarma Lyon | a recoder |
| 10 | `/falafel-lyon` | Falafel Lyon 2 \| Falafels Maison Croustillants \| Sezam&Co | falafel Lyon | a recoder |

## Pages a creer (opportunites SEO identifiees)
| # | URL | Focus KW | Imp GSC | Position | Priorite |
|---|---|---|---|---|---|
| 11 | `/livraison-libanais-lyon` | livraison libanais lyon | 76 | 27.2 | HAUTE |
| 12 | `/restaurant-libanais-lyon-7` | restaurant libanais lyon 7 | 125 | 11.3 | HAUTE |
| 13 | `/restaurant-libanais-vieux-lyon` | restaurant libanais vieux lyon | 37 | 9.3 | HAUTE |
| 14 | `/restaurant-libanais-confluence` | restaurant libanais confluence | 8 | 21 | MOYENNE |
| 15 | `/mezze-lyon` | mezze lyon | 107 GBP + 7 GSC | 8.6 | MOYENNE |
| 16 | `/meilleur-restaurant-libanais-lyon` | meilleur libanais lyon | 143 GBP + 20 GSC | 16.4 | MOYENNE |
| 17 | `/restaurant-libanais-lyon-5` | restaurant libanais lyon 5 | -- | -- | BASSE |

---

# SEO — REGLES A APPLIQUER

## Structure Hn
- **H1** = 1 seul par page, exact match du keyword principal, court
- **H2** = keywords secondaires / sections
- **H3** = sous-sections
- NE JAMAIS diluer le H1 avec plusieurs keywords

## Meta tags
- **Title** : `Keyword Principal | Detail | Sezam&Co` (max 60 chars)
- **Description** : 150-160 chars, inclure keyword + CTA + localisation
- Chaque page = 1 keyword principal unique

## Schema JSON-LD
Chaque page doit inclure le schema appropriate :
```json
// Sur TOUTES les pages : LocalBusiness
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Sezam&Co",
  "image": "photo-restaurant.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "6 rue Petit David",
    "addressLocality": "Lyon",
    "postalCode": "69002",
    "addressCountry": "FR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": "45.7578", "longitude": "4.8320" },
  "url": "https://sezamandco.com",
  "telephone": "[a completer]",
  "servesCuisine": "Lebanese",
  "priceRange": "€",
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "12:00",
    "closes": "23:00"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "723"
  }
}
```

```json
// Sur /menu : Menu schema
{
  "@context": "https://schema.org",
  "@type": "Menu",
  "hasMenuSection": [...]
}
```

```json
// Sur /faq : FAQPage schema
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [...]
}
```

## Maillage interne
- Footer SEO sur toutes les pages avec liens vers pages cles
- Liens contextuels entre pages plats (shawarma <> falafel <> manouche)
- Menu > liens vers pages plats individuelles
- Homepage > liens H2 vers chaque section

## Images
- Noms de fichiers SEO : `shawarma-lyon-sezamco.jpg` (pas IMG_1234)
- Alt text descriptif avec keyword : `Shawarma poulet grille au four chez Sezam&Co Lyon 2`
- Format WebP pour la performance, avec fallback JPG
- Lazy loading sur les images below the fold

## Vitesse
- 0 framework JS (vanilla uniquement si besoin)
- CSS inline critique dans le `<head>`, reste en fichier externe
- Images compressees + WebP
- Preload des fonts
- Objectif : PageSpeed 95+ mobile, LCP <1.5s

---

# MENU COMPLET (source de verite pour /menu)

## Starters & Mezze — 5,90 EUR
| Plat | Description |
|---|---|
| Hummus & Crackers | Pois chiches, creme de sesame, sumac, citron, huile d'olive, crackers |
| Moutabal & Crackers | Caviar d'aubergine fumee, sesame, citron, huile d'olive, crackers |
| Labne & Crackers | Fromage blanc sale, huile d'olive, crackers, zaatar |
| Fattouch | Grenade, laitue, tomate, concombre, radis, menthe, crackers, melasse de grenade |
| Mozza Sticks | 5 mozzarellas panees, zaatar, sauce au choix |
| Frites Signature | Frites croustillantes, melange epice maison |
| Falafel Crunch | Falafels, radis, tomates, concombre, laitue, crackers, sumac, creme de sesame |

## Man'ouche Wrap — Formule +5,40 EUR (starter + boisson)
| Plat | Proteine | Seul | Formule |
|---|---|---|---|
| Honey-Mustard Dinde | Dinde | 8,50 | 13,90 |
| Hummus Kafta | Boeuf | 9,20 | 14,60 |
| Cheesy Kafta | Boeuf | 9,50 | 14,90 |
| Garlic Chicken | Poulet | 9,20 | 14,60 |
| Spicy Chicken | Poulet | 9,20 | 14,60 |
| Shawarma | Poulet | 9,20 | 14,60 |
| Spicy Sojok | Boeuf | 8,90 | 14,30 |
| Crispy Chicken | Poulet | 9,20 | 14,60 |
| Falafel Wrap | Veggie | 8,90 | 14,30 |
| Halloumi Bacon | Dinde | 8,80 | 14,20 |

## Man'ouche Traditionnel — Formule = starter + boisson inclus
| Plat | Seul | Formule |
|---|---|---|
| Zaatar | 5,50 | 10,90 |
| Zaatar Extra | 6,50 | 11,90 |
| Zatar Duo | 7,00 | 12,40 |
| Jebne | 7,00 | 12,40 |
| Jebne Extra | 7,50 | 12,90 |
| Labne-Zaatar | 7,40 | 12,80 |
| Halloumi Fromage | 7,90 | 13,30 |
| Lahmajine | 8,00 | 13,40 |
| Sojok Jebne | 7,90 | 13,30 |

## Boissons
| Boisson | Prix |
|---|---|
| Eau 50cl | 1,70 |
| Citronnade maison 30cl | 2,90 |
| Coca Cola 33cl | 2,70 |
| Coca Zero 33cl | 2,70 |
| Ice Tea Peach 33cl | 2,70 |
| Sprite 33cl | 2,70 |
| Orangina 33cl | 2,70 |
| Ayran maison 30cl | 2,90 |
| Biere libanaise 33cl | 5,00 |
| Ristretto | 2,70 |
| Espresso | 2,70 |
| Lungo | 2,90 |

## Desserts
| Dessert | Prix |
|---|---|
| Nutella Banane | 5,50 |
| Speculoos Banane | 5,50 |
| Choco-Tahini Twist | 6,00 |

---

# CONTENU PAGES PLATS (pret a integrer)

## /shawarma-lyon
- **H1** : Shawarma Lyon | Sezam&Co
- **H2s** : Notre Shawarma Poulet / Ce Qui Rend Notre Shawarma Different / Shawarma en Formule / Commander
- **Points cles** : marinade maison, grille au four (PAS broche), man'ouche, 100% halal
- **Prix** : 9,20 EUR seul / 14,60 EUR formule
- Contenu complet : `M/pages/shawarma.md`

## /falafel-lyon
- **H1** : Falafel a Lyon - Croustillant, fait maison, chez Sezam&Co
- **H2s** : Nos falafels / Pourquoi differents / Formule / Pour tous / Commander
- **Points cles** : fait maison chaque jour, frit a la commande, 100% vegetarien & vegan
- **Prix** : 8,90 EUR seul / 14,30 EUR formule
- Contenu complet : `M/pages/falafel.md`

## /manouche
- **H1** : Man'ouche a Lyon - La galette libanaise artisanale de Sezam&Co
- **H2s** : Traditionnels / Specialites signature / Formule / Savoir-faire / Commander
- **Points cles** : pate au levain, cuisson minute, four traditionnel
- **Prix** : a partir de 5,50 EUR / formule des 10,90 EUR
- Contenu complet : `M/pages/manouche.md`

---

# HOMEPAGE — Structure Hn validee

```
H1: Restaurant Libanais Lyon 2 | Sezam&Co
  H2: Nos Man'ouches a Lyon — Galettes Libanaises Cuites Minute
    H3: Nos Mezzes Libanais
    H3: Man'ouches Urbains
    H3: Man'ouches Traditionnels
  H2: Shawarma, Houmous et Mezzes Maison a Lyon
  H2: Livraison Libanaise a Lyon — Commandez en Ligne
```

---

# INFOS BUSINESS (pour header/footer/schema)

- **Nom** : Sezam&Co
- **Type** : Restaurant street food libanaise
- **Adresse** : 6 rue Petit David, 69002 Lyon
- **Horaires** : 7j/7, 12h-23h
- **Note Google** : 4.8/5 (723 avis)
- **Livraison** : Uber Eats, Deliveroo, Delicity + site web
- **Commande en ligne** : commandes.sezamandco.com
- **100% halal**
- **Formule des** : 10,90 EUR

---

# MAILLAGE INTERNE

## Footer SEO (toutes pages)
Liens vers : Menu | Shawarma Lyon | Falafel Lyon | Man'ouche Lyon | Livraison | Adresse & Horaires | FAQ

## Liens croises entre pages plats
- /shawarma-lyon <> /falafel-lyon <> /manouche (liens dans le contenu)
- /menu > lien vers chaque page plat
- Homepage H2s > liens vers pages plats

---

# BACKLINKS EXISTANTS (a preserver)
- 80 liens externes, 52 sites (Moz DA 10)
- Top referrers : wanderlog, tripadvisor (~35 TLDs), cylex, lyon-food, mappy, rankeat, tribunedelyon
- Page la plus linkee : /menu (55 liens, 38 sites)
- IMPORTANT : ne pas casser les URLs existantes sous peine de perdre ces backlinks

---

# CITATIONS / NAP (a integrer dans le schema)
| Plateforme | Statut |
|---|---|
| Google Business Profile | OK |
| Instagram (@sezamandco) | OK |
| Facebook | OK |
| TripAdvisor | OK |
| Uber Eats | OK (4.7/5, 150 avis) |
| Pages Jaunes | OK |
| Mappy | OK |
| Bing | OK (sitemap soumis) |

---

# PLAN DE MIGRATION

## Phase 1 — Preparation
1. [ ] Crawl complet du site Wix actuel (toutes URLs, redirects existants)
2. [ ] Recuperer toutes les images du site Wix
3. [ ] Lister tous les liens entrants (GSC > Liens) pour verifier les URLs
4. [ ] Preparer la structure de fichiers du nouveau site

## Phase 2 — Developpement
5. [ ] Coder le layout commun (header, nav, footer SEO)
6. [ ] Coder la homepage
7. [ ] Coder la page /menu (avec tous les prix a jour)
8. [ ] Coder les pages plats (/shawarma-lyon, /falafel-lyon, /manouche)
9. [ ] Coder les pages info (/adresse, /mission, /notre-histoire, /faq)
10. [ ] Coder la page /restaurant-libanais-lyon-1
11. [ ] Creer les nouvelles pages (/livraison, /lyon-7, /vieux-lyon, etc.)
12. [ ] Integrer schema JSON-LD sur toutes les pages
13. [ ] Generer sitemap.xml
14. [ ] Tester PageSpeed, accessibilite, mobile

## Phase 3 — Migration
15. [ ] Deployer sur Cloudflare Pages (test sur sous-domaine staging)
16. [ ] Verifier 1:1 que chaque URL Wix existe sur le nouveau site
17. [ ] Changer le DNS : sezamandco.com > Cloudflare Pages
18. [ ] Soumettre le nouveau sitemap sur GSC
19. [ ] Demander la reindexation des pages cles
20. [ ] Surveiller GSC pendant 2 semaines post-migration

## Phase 4 — Post-migration
21. [ ] Verifier que toutes les pages sont indexees
22. [ ] Comparer positions GSC avant/apres
23. [ ] Supprimer l'abonnement Wix (apres 30j de validation)

---

# DESIGN — Principes

- **Dark theme** : fond sombre, texte clair (preference Serge)
- **Mobile-first** : 78% du trafic GBP = Maps mobile
- **CTA clair** : bouton "Commander en ligne" visible sur chaque page
- **Photos food** : grandes, appetissantes, hero section
- **Couleurs** : a definir (reprendre la charte Sezam&Co ou en creer une)
- **Typo** : moderne, lisible, sans serif pour le body
- **Vibe** : street food, chaleureux, authentique, pas chic/guinde
