# Public website deployment

GitHub repository: `mScid/mScid.github.io`.

GitHub Pages is configured to serve the `main` branch, repository root. The generated HTML and assets are committed, and `.nojekyll` disables Jekyll processing. Pages therefore does not need Python or a framework build. No additional Actions workflow is required for this deployment method.

Before publishing source changes:

```sh
python scripts/build.py
python scripts/validate.py
```

Commit the generated output together with the public sources and push a normal continuation of remote `main`. Do not force-push.

## Private authoring boundary

The local authoring repository includes personal Docs notes. The owner explicitly excluded those from publication. The public snapshot therefore omits `docs/`, `site-source/pages/docs/`, and their entries/text in the preservation manifest. Local authoring checkpoints are kept locally and were not attached to the public commit history. Do not push those local checkpoints or use a mirror push.

The public deployment commit continues the pre-existing remote `main` history. Existing remote-only files are retained. Local Phase 1 and Phase 2 checkpoints were recorded as `c1acb99` and `2875252`; the public publishing commit contains their approved website changes without importing their private-note history.

Future updates must preserve this boundary: use a public-only checkout based on the latest remote `main`, retain unrelated remote changes, build and validate that checkout, and publish only its public commit. The public validator checks 28 content pages and protects the original scientific figures.
