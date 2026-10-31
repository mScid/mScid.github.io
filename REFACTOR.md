# Current-site layout refactor

## Directory confirmation and architecture

`/home/mScid/website/new-site` is authoritative, as specified by the owner. Before this refactor it contained directly edited HTML, `personal.css`, legacy theme styles/bundles, static images, RSS feeds, a sitemap and HTML redirect aliases. It had no framework, package manager, templates or build command. Preview used Python's standard-library HTTP server.

The homepage and Projects were custom HTML. About, CV, posts, archives and local Docs pages contained recovered theme markup. Their styles, navigation variants, footers, content widths and heading levels differed. Some footers hardcoded a March 2024 build timestamp; some heads referenced development live-reload scripts or missing theme preview images.

The sibling `mScid.github.io` directory shares substantial historical content but is legacy. It has Git metadata and the previous misplaced 27-page refactor; unlike the current folder, it lacks the retained Docs tree. This refactor extracted all page content from `new-site` itself. Only generic templates, a Python builder and scoped layout/accessibility rules were reused. No legacy pages, assets or page-source data were copied over current content. The legacy folder was hashed before and after this task and remained unchanged.

## Changes in new-site

- Added shared base/header/footer templates, a Python standard-library builder and 35 page sources under `site-source/pages/`.
- Updated all 35 rendered pages to share brand/navigation, active-section indicators, footer, skip link, page margins and reading styles.
- Preserved the current homepage cards, research poster, photo, revised biography, CV, scientific descriptions and existing URLs.
- Kept all eight retained Docs pages and redirect aliases; did not add Docs back to navigation.
- Consolidated the existing navy/blue palette and homepage grid rules, retaining the site's fonts and visual identity.
- Improved mobile navigation, image scaling, long code/table overflow, focus styling, reduced-motion support and CV print styling. Contained decorative homepage orbit overflow at tablet widths.
- Replaced the obsolete theme shell scripts with a small code-copy enhancement; retained MathJax and original inline scientific markup.
- Removed exported build timestamps and development script references. Publication dates retain their values with a readable date-only display. No new update date was invented.
- Normalized canonical URLs, corrected exported RSS alternate links and missing theme-image metadata, and added missing current public pages to the existing sitemap. Existing feeds remain byte-identical.

Created `templates/`, `site-source/`, `scripts/build.py`, `scripts/validate.py`, `scripts/site.js`, this report and the updated README. Modified public content HTML, `personal.css`, and `sitemap.xml`. No original file was deleted. Legacy theme assets remain on disk for compatibility but are no longer loaded by the shared shell.

## Verification

- Build renders 35 pages without dependencies.
- The preservation validator checks all 100 original files remain, all 35 pages retain their main prose except normalized dates, and 62 protected files (assets, feeds, redirect aliases and other unchanged files) retain their original hashes.
- No missing local paths were found in rendered page link/asset attributes. XML parsing passed.
- Repeat builds produce identical public outputs.
- Browser DOM checks covered Home, About, Projects, Writing, Academic Review, SPVM conference, CV and the retained Arch Linux article at 1280, 768 and 390 pixels. No broken completed images were observed. An overflow from a decorative homepage orbit at 768px was fixed; a subsequent DOM check reported no overflow.
- A mobile screenshot of the retained Arch Linux article was inspected: shared navigation, contents links, code-copy controls and scrollable code render.

## Limits and recommended follow-up

The browser preview process stopped during final screenshot/keyboard checks, so the final screenshot pass and full keyboard interaction check were incomplete. The earlier responsive DOM checks passed after the one tablet fix. Screen-reader, full contrast, cross-browser, clipboard-permission and actual CV PDF export testing were not completed. Focus styles and the skip link are implemented, but should receive a manual keyboard check. Some retained test/Docs pages already lack a primary title; no new prose or scientific text was invented to fill them.

Google Fonts and MathJax still depend on external services. Publication dates in old source metadata retain historical information; their time zones have not been independently verified. Internal URL paths were validated; not every fragment or external URL was checked.

Recommended next steps: review the local design, test CV printing and keyboard navigation in your preferred browser, and audit legacy asset references before removing unused assets. Keep this folder as the sole content source.

No commit, push, deployment, or further modification to the legacy folder was performed in this task.

## Follow-up quality assurance

The final QA pass is documented in `QA.md`. It supersedes the earlier preview/keyboard limitations above with completed responsive and keyboard tests, and records the remaining PDF and cross-browser limitations.
