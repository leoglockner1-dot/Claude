---
title: "FC-DATA-01 — Workflow: the v1 package's 367 media files were lost (gitignored, container reset)"
tags: [failure-case, workflow, assets, portability]
note_type: "failure-case"
evidence: "real failure observed in this session (2026-10-24)"
---

# Workflow: the v1 package's 367 media files were lost (gitignored, container reset)

| Field | Record |
|---|---|
| **Problem** | Workflow: the v1 package's 367 media files were lost (gitignored, container reset) |
| **Context** | Academy v1 kept third-party images and clips in `Assets/`, which `.gitignore` excluded from the public repository (correctly, for rights reasons). |
| **Observable symptoms** | In a new session, every image link in the package was broken (682 broken links to 367 files). |
| **Cause (established)** | The only copies lived in the old container's working directory and a ZIP that was also gitignored. Neither survived the container reset. |
| **Correction** | Built `_tools/asset-sources.json` (a source URL and method for each file) and `_tools/fetch_assets.py`, which re-downloads and regenerates everything. Recovered all 367 files from the original sources; derived sheets were rebuilt with the same parameters. |
| **How the correction was tested** | Ran the fetch script into an empty copy: 352 created + 15 derived, 0 failed; validator 0 broken links. |
| **Final result** | Recovered. Live thumbnails were re-fetched the same day (CDN hashes matched where checked). |
| **Reusable lesson** | Anything that cannot be committed needs a committed, tested way to rebuild it. |
| **Related** | [IMPORT_INSTRUCTIONS](../../IMPORT_INSTRUCTIONS.md) |
