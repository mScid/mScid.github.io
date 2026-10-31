# Phase 2 — Visual thesis showcase

## Phase 1 checkpoint

The authoritative `new-site` directory had no Git repository. A new local repository was initialized; the Phase 1 site was reviewed through the preservation checks and committed as:

`c1acb99fc0875987651ce464b890162b7d9e2c0e`

Message: `refactor: unify site templates and improve accessibility`

This is a root/baseline commit, not a diff against a pre-existing commit in this folder. The supplied `assets/thesis/` research inputs were excluded from that commit. No remote was configured and nothing was pushed. All Phase 2 changes remain uncommitted for visual review.

## Implementation

- `/projects/` remains a single-thesis listing. Its new card links to `/projects/thesis/` and retains the original poster and conference links.
- `/projects/thesis/` uses the existing shared shell, navigation, colors, fonts and responsive CSS. It presents a research introduction, the atomic model, overview, methodology, band/charge/DOS results, and conference presentation.
- All 12 supplied plots are available once each. Four primary result figures are initially shown; native `<details>` comparisons reveal the others without new JavaScript or dependencies.
- Each scientific figure links to its full-resolution PNG. Smaller lossless-WebP-encoded previews reserve their layout dimensions and use lazy loading below the hero.
- No unrelated page prose was rewritten. The shared stylesheet version changes across generated pages because the new layout rules are in the existing shared stylesheet.
- `scripts/build.py` now creates output parent directories and includes the showcase in the sitemap.
- The preservation validator now checks new generated pages as well as the original pages. The explicitly requested Projects copy change is recorded in `site-source/approved-content-changes.json`; all other original text comparisons remain enforced. Original thesis PNG hashes are checked against `site-source/thesis-figures.json`.

## Scientific source and figure audit

Primary sources: the original website poster `assets/spvm-poster.png`, the existing SPVM article and recognition certificate links, the 12 supplied PNGs in `assets/thesis/`, and the owner's Phase 2 brief.

| Source figures | Verified identity and use |
| --- | --- |
| `band_structure1.png`–`band_structure3.png` | Each image explicitly titles itself Structure 1, 2 or 3. Blue bands are plotted along Γ–M–K–Γ, with a red Fermi reference at zero. All three are used in the band section. |
| `HEA_TDOS1.png`–`HEA_TDOS3.png` | Explicit Structure 1–3 titles; total DOS with labeled spin-up/down curves and the Fermi reference. All three are used. |
| `HEA_elemental_LDOS_spin1.png`–`HEA_elemental_LDOS_spin3.png` | Explicit Structure 1–3 titles; legend identifies Mo, Nb, S, Ta, V and W and up/down spin channels. The filename suffix does **not** denote a spin channel: each plot contains both. All three are used. |
| `ChargeTransferSulfur1.png`–`ChargeTransferSulfur3.png` | Sulfur electron-population differences grouped by the three bonded metals. The figure text defines the pristine average reference, group means and individual sulfur points. No numbered configuration is labeled, so the site makes no Structure 1–3 assignment. Additional views are called comparisons B and C, not numbered structural identities. |
| `crystal-structure.png` | Accurate crop from the poster's computational-details panel, retaining the complete lattice drawing and element legend. It is not assigned to a numbered configuration. Used as the hero and listing visual. |
| Original SPVM poster | Retained unchanged at its original URL; linked from the listing, showcase and existing conference article. A smaller WebP preview is shown in the presentation section. |

### Crop provenance

Original poster: 3179 × 4494 pixels. Crop rectangle: x=2225, y=900, width=780, height=555. Output: `assets/thesis/crystal-structure.png`, 780 × 555 pixels. The crop was visually inspected at native resolution: it contains the crystal drawing and all six legend labels, with no unrelated section text. No scientific geometry, colors or labels were recreated or changed.

Command using the existing ImageMagick installation:

```sh
magick assets/spvm-poster.png -crop 780x555+2225+900 +repage assets/thesis/crystal-structure.png
```

Web previews are downscaled to fit within 1200 × 1200 pixels and encoded using WebP lossless mode. This is web optimization; the original source PNGs remain unchanged. The poster preview is 900 pixels wide.

### Descriptions and boundaries

- Band/DOS text describes visible Fermi crossings and nonzero total DOS at that reference. These are presented as evidence consistent with metallic behavior **in the calculated models**, not an experimental conductivity measurement.
- DOS captions explain that plotting the down channel below the axis is a convention, not a negative state count. No magnetic order or net magnetization is inferred.
- Element-resolved captions describe the prominent sulfur contribution below the Fermi reference and contributions from the constituent metals across energy ranges. They do not invent quantitative orbital assignments.
- Sulfur captions distinguish electron-population gains/losses relative to the chart's pristine average from a net atomic charge. The bars and dots are explained from the chart's own annotation.
- DFT, Quantum ESPRESSO and structural relaxation are supported by the poster. SQS is included as requested in the owner's methods brief; generation input files, algorithms and disorder statistics were not provided. No SQS tool, quality metric or configuration mapping is claimed.
- The award is reproduced from the existing SPVM article and certificate. The showcase does not claim that the thesis has been published.

Unresolved context: exact atomic arrangements behind Structures 1–3, an explicit mapping of the three sulfur plots to those structures, and raw computational inputs/settings beyond the poster are not independently established. These gaps are not filled by guessing from filenames. The crop illustrates the poster's model but is not identified as Structure 1 or as a particular optimized configuration.

## Validation

- `python scripts/build.py`: renders 36 pages.
- `python scripts/validate.py`: zero errors; all original paths retained, protected assets/feeds/redirects unchanged, original scientific PNGs unchanged, and all generated page local paths checked. Only the approved Projects text change is exempted from the original-text comparison.
- Responsive browser tests at 1280, 768 and 390px: one H1, correct Projects active state, no horizontal overflow, all four comparisons open via keyboard, all 15 page images loaded, no missing image alt attributes, no console warnings/errors captured.
- Tested Projects → showcase navigation and opening the Structure 1 band image at its original 2400 × 2400 resolution.
- Skip link focuses the main region; summary Enter toggles comparison panels with a visible focus outline.
- Custom computed-style contrast check on expanded showcase text and captions: 114 text-bearing elements checked, lowest ratio 5.55:1, no AA normal/large-text failures. This is not a complete WCAG audit and does not evaluate text embedded in the plots.
- Desktop hero/results, tablet charge section and mobile hero/DOS layouts were visually inspected.

## Performance and limits

The full set of WebP previews, including the cropped structure and poster, totals about 1.45 MB; the source result PNGs plus crop total about 3.06 MB, with the full poster adding about 2.38 MB. The hero is eager-loaded; other figures are lazy-loaded and secondary comparisons start collapsed. Full-resolution assets are fetched only when their links are opened.

Mobile plots fit the available width and can be opened full-size; dense scientific axis labels still require enlargement for close inspection. No full screen-reader, cross-browser, real mobile-device, slow-network performance profile or print/export audit was performed in this phase. Remote fonts remain an external dependency. No new runtime dependencies were installed.

Preview: http://localhost:8000/projects/thesis/

The server remains running for review. Phase 2 is uncommitted; there was no push, deployment, or change to the legacy website.
