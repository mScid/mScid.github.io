# Final local QA — 2026-10-31

## Scope and preview

Only `/home/mScid/website/new-site` was changed. Built with `python scripts/build.py`, validated with `python scripts/validate.py`, and served this exact directory using the README command `python -m http.server 8000`. Browser checks used `http://localhost:8000`. No installation, commit, push or deployment was performed.

## Pages and sizes

The following pages were checked at 1280px (desktop), 768px (tablet), and 390px (mobile):

- Home `/`
- About `/about/`
- Projects `/projects/`
- Writing `/posts/`
- Academic Review article `/posts/academic-review/`
- SPVM article `/posts/spvm-28th-national-physics-conference/`
- CV `/cv/`
- Retained Arch Linux article `/docs/collectionofideas/arch-linux-installation/`

Screenshots of the seven main public pages were visually inspected at all three widths for heading wrapping, typography, spacing, shared navigation and layout. The retained Arch article was visually inspected on mobile. The SPVM poster was opened through its Projects link and inspected at all three widths; its natural image dimensions are 3179 × 4494. It fits the viewport without distortion. Its embedded research text is necessarily small when fitted to a mobile screen; the full-resolution asset remains available.

Final DOM checks on the eight sampled pages at all three widths found no document horizontal overflow, no broken completed images, and no captured console warnings or errors. Each sampled page has one main landmark and one H1. Active navigation correctly marks About, Projects, Writing (including articles), and CV. Home and unlisted Docs have no falsely active section.

## Interaction and accessibility checks

- Pressing Tab on Home reaches the visible Skip to content link first. Enter updates the fragment and places focus on `main-content`.
- Keyboard Tab reaches About in the navigation, with a visible solid focus outline. Enter navigates to About and its current-page indicator is correct.
- All 11 code-copy controls in the Arch article were activated with Enter. Clipboard contents were compared against the corresponding command text: all 11 match without line numbers. A mouse activation of the first control also copied the expected text and displayed Copied!.
- Sampled pages have named links/buttons, image alt attributes, and shared navigation labels. Duplicate IDs are checked by the repository validator.
- A custom computed-style contrast check on visible text in `main` and navigation across the seven main public pages found no failures against 4.5:1 for ordinary text or 3:1 for large text. This check uses solid foreground/background colors, not screenshot pixels; it is not a comprehensive WCAG audit.
- No axe library was installed or injected. Checks used browser DOM/accessibility observations, computed styles, real keyboard input and local validation.
- CV print button activation was attempted. Its existing handler is `window.print()`. Browser automation timed out during the click; Escape restored the page with the print button focused. The print-dialog contents, PDF pagination and actual saved PDF remain unverified. No print-related change was made based on that automation limitation.

## Confirmed defects fixed

1. Code-copy enhancement targeted the entire highlighted block, including numbered gutters. It now copies only the `.cl` command spans, retaining whitespace and excluding line numbers. Button feedback uses a polite live region.
2. Retained code line numbers visually touched commands. Added gutter width, unselectable line numbers and flex rows, plus consistent toolbar controls. Code stays horizontally scrollable inside its block.
3. The retained Arch article's H1 used the body font and its sections skipped from H1 to H3. Applied the shared heading font to content H1s and changed that article's section tags to H2 without changing text or anchors.

Files changed for fixes: `scripts/site.js`, `personal.css`, `site-source/pages/docs/collectionofideas/arch-linux-installation/index.json`, and regenerated public HTML. No template architecture, biography, CV prose, scientific information, poster or other asset was redesigned or rewritten.

## Final local validation

`python scripts/build.py` renders 35 pages. `python scripts/validate.py` passes with zero errors and zero remaining missing local paths. The validator preserves all 100 original paths, compares the prose of 35 pages apart from date display formatting, checks 62 protected assets/feeds/redirects, and parses XML. Repeat-build output is stable.

The legacy directory was compared against the prior read-only hash inventory and remained unchanged.

## Remaining limitations

- No saved CV PDF, physical printout or print-pagination review.
- No full screen-reader or cross-browser audit; browser work used the embedded Chromium browser.
- Clipboard permission-denial fallback was not forced, and touch was simulated by viewport width rather than real hardware.
- Not every archive/test page was visually reviewed; all 35 generated pages passed local structural/path/content checks.
- Visual review covered top-of-page screenshots and sampled content, not every vertical position of every long page.
- External link availability and all in-page fragments were not exhaustively checked. Remote fonts and MathJax remain external dependencies.


## Featured conference card contrast correction — 2026-10-31

A later global `h1, h2, h3, h4 { color: var(--ink); }` declaration gave the featured card heading an explicit navy color, overriding the card's inherited white text. `.featured-writing h2` now explicitly uses `var(--surface)` (white). Typography, spacing and content are unchanged.

The card link uses navy on white on hover and keyboard focus, with a white focus outline. Its foreground/background transition is disabled to avoid a briefly low-contrast midpoint during the color swap.

Computed colors were verified at 1280, 768 and 390px: heading white (`#ffffff`) on navy (`#103153`) has 13.24:1 contrast, passing both AA thresholds (3:1 large text and 4.5:1 normal text). The card eyebrow measures 9.35:1, its descriptive text 11.00:1, and the link 13.24:1 in both its normal and inverse interaction states. Keyboard focus and actual pointer hover were observed in the browser. No horizontal overflow was found at any tested width.

A corrected computed-style audit checked dark-surface text across all 35 generated pages, including dark buttons and skip links, with no remaining failures. This supersedes the original contrast result above: the earlier audit mishandled opaque `rgb()` values without an alpha component and skipped them. The corrected audit defaults that alpha to 1 and composites translucent ancestor backgrounds before calculating contrast. It is still a sampled DOM/style audit rather than a complete WCAG certification, and excludes text embedded in image assets.

The site was rebuilt and the preservation validator passed. The preview remains running at http://localhost:8000/ at the owner's request. No commit, push, deployment, or legacy-folder changes were made.
