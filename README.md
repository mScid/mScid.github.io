# Dinan Mariano — personal website

This repository contains the public version of Dinan Mariano’s static HTML/CSS/JavaScript website. It has no frontend framework, package manager, or runtime backend. Private Docs notes and their source copies are excluded.

## Edit and build

The original site consisted of directly edited HTML. Shared templates now keep its pages consistent:

- `site-source/pages/`: page content and metadata in JSON files, matching the public HTML paths.
- `templates/base.html`, `header.html`, `footer.html`: shared document shell and navigation.
- `personal.css`: the existing poster-inspired navy and blue design and responsive rules.
- `scripts/site.js`: progressive enhancement for the retained code-copy buttons.
- `assets/`, `img/`, `logo/`, and post image folders: original assets.

After editing a page source, template, or stylesheet, run from this folder:

```sh
python scripts/build.py
python scripts/validate.py
```

Both commands use Python's standard library. No installation is needed. The build writes the static HTML in place, versions the stylesheet by content hash, and maintains canonical links and the sitemap. Generated pages work with any static server. Do not edit generated HTML without also changing its page source, or a future build will replace the edits.

The validator checks the refactor against the original current-site preservation manifest. For intentional future content changes, review and update that manifest rather than suppressing preservation failures.

## Preview locally

From this folder run `python -m http.server 8000`, then open http://localhost:8000. Stop the server with Ctrl+C. The CV's Save CV as PDF button opens the browser print dialog.

Private Docs notes are retained only in the local authoring checkout and excluded from this public repository, including its page sources and preservation manifest.

See `REFACTOR.md` for the architecture comparison, validation results, and limitations. No publishing action is part of the build.

See `QA.md` for the final desktop, tablet, mobile, keyboard, clipboard, contrast and print-testing results.

## Thesis showcase

The single thesis listing is at `/projects/`; the dedicated showcase is at `/projects/thesis/`. Edit their matching JSON files under `site-source/pages/projects/`. Original plots remain in `assets/thesis/`; `assets/thesis/web/` contains smaller previews. Figure provenance, scientific limitations, Phase 1 commit and Phase 2 validation are recorded in `THESIS-SHOWCASE.md` and `site-source/thesis-figures.json`.

The original content-preservation checks continue to protect unrelated pages. `site-source/approved-content-changes.json` records the explicitly requested Projects revision; it does not broadly disable preservation checks.

## GitHub Pages

Pages serves the generated HTML from the `main` branch, repository root, with `.nojekyll`. Run the Python build and validator before committing public changes. Python does not run on the Pages server. See `DEPLOYMENT.md` for the public/private history boundary and deployment procedure.
