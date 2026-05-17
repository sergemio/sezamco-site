# Curseur custom Sezam — STANDBY (à finaliser)
> Last update: 2026-05-15

## Décision (session 2026-05-14)
Option C retenue : **point central vert + man'ouche zaatar qui traîne avec inertie**.

Pas encore implémenté en prod. À peaufiner avant push.

## Fichiers
- `_cursor-standby-snippet.html` — snippet HTML/CSS/JS prêt à coller dans toutes les pages
- `assets/images/cursor-manouche-80.png` — image 80px (15KB, déjà commitée — utilisée actuellement uniquement par le snippet)

## Paramètres validés
- Point central : `var(--green-logo)` (#417F0A), 10px rond
- Man'ouche trail : 44px → 72px sur hover
- Inertie : 0.09 (ralenti depuis 0.18 par défaut, Serge a validé après test)
- Désactivé sur tactile/mobile via `@media (hover: hover) and (pointer: fine)`
- Hover sur : `a, button, .btn, .bs-card, .avis-card, .dropdown-toggle`

## À améliorer avant push
- [ ] **Halo blanc résiduel** autour de la man'ouche — masquage actuel imparfait. Solutions à explorer : régénérer avec prompt négatif strict + post-process plus agressif (seuil blanc plus bas, edge erosion), ou éditer manuellement le PNG dans un outil graphique
- [ ] Tester sur autres pages (menu, manouche, snack, street-food) pour cohérence
- [ ] Ajuster sélecteurs hover si certains éléments manquent (panier, prix, etc.)
- [ ] Décider si actif sur les 22 pages ou seulement homepage

## Pour ré-implémenter
1. Copier les 3 blocs de `_cursor-standby-snippet.html` dans chaque page (CSS dans `<style>`, divs avant `</body>`, script ensuite)
2. Vérifier que `assets/images/cursor-manouche-80.png` est servi depuis la racine
3. Push → Cloudflare deploy auto

## Génération de l'image (rappel)
Prompt Gemini Imagen 4.0 utilisé :
```
Top-down circular photo of a single authentic Lebanese manouche zaatar flatbread on pure transparent background. Round artisan bread, golden-brown baked dough with slightly irregular edges. Top is generously covered with dark green zaatar herb mix (oregano, thyme, sumac, sesame seeds, olive oil glistening). Visible texture: small sesame seeds scattered, herbs in clumps, olive oil shine reflections. Photorealistic, sharp focus, professional food photography lighting, isolated object, no plate, no background, no shadow on background, PNG with alpha channel, square crop, centered, photographic realism, ultra detailed 4k
```

Post-process Python (PIL) appliqué :
- Détection pixels blancs (R>230, G>220, B>200) → alpha=0
- Masque circulaire (240x240) avec gaussian blur 0.8 sur bords
- Resize 80px LANCZOS + optimize PNG
