# Environment Setup & Technical Research Architecture

This repository documents a two-part technical sprint: initializing a modern development environment using an AI-native code editor and constructing an automated research engine to analyze enterprise-grade AI SEO workflows.

---

## ── PHASE 1: ENVIRONMENT INITIALIZATION ──

### Installation & Account Synchronization
* **Application Ingestion:** Downloaded and initialized the Windows stable build for the AI-native development environment via `https://cursor.com`. Opted out of secondary non-essential paid tiers to maintain a streamlined core installation footprint.
* **Version Control Registration:** Created a net-new authentication identity on GitHub. Linked GitHub credentials natively within the editor interface to establish a secure, verified handshake. This synchronization serves as the foundational security layer enabling advanced programmatic tracking extensions to securely map local workspace mutations.

### Marketplace Extension Deployment
Initialized the editor command palette via `Control + Shift + P`, executed the `Extensions: Install Extensions` manager string, and programmatically deployed two primary technical components:
1. **Claude Code Extension:** Terminal-native orchestration layer for multi-file context analysis.
2. **Codex Extension:** Autocompletion and code translation engine.

### Troubleshooting & Foundational Problem Solving
* **VSIX Path Configuration Anomaly:** Attempted initial component ingestion via manual `Install from VSIX...` workflows. Encountered localized folder directory abstraction blocks. Resolved the friction by shifting execution to the native marketplace command line, bypassing manual local file-path mapping entirely.
* **Identity Verification Overlapping:** Encountered multiple duplicate listings within the marketplace ecosystem. Resolved target authenticity by systematically auditing publisher metadata credentials and cross-referencing them against primary configuration rules to isolate authorized builds.

---

## ── PHASE 2: AI-POWERED SEO CONTENT ARCHITECTURE ──

An automated data pipeline designed to extract, analyze, and map the execution engines of ten high-signal programmatic and data-driven SEO operators. This serves as a structured intelligence layer to construct an enterprise-grade execution playbook using automated data networks and LLMs.

### Project Structure
```text
├── extract_transcripts.py       # Automated Python script interfacing with Supadata API
└── research/
    ├── sources.md               # Verified master index of 10 practitioners with links & metadata
    ├── linkedin-posts/          # Extracted tactical frameworks and cross-platform case studies
    │   ├── elias_dabbas.txt
    │   ├── jake_ward.txt
    │   └── lazarina_stoy.txt
    ├── youtube-transcripts/     # Raw script data payloads generated programmatically via API
    │   ├── elias_dabbas_python_data_science_seo.txt
    │   ├── jake_ward_seo_heist_framework.txt
    │   ├── julian_goldie_programmatic_agent_setup.txt
    │   └── programmatic_seo_nextjs_engine_guide.txt
    └── other/                   # Supplemental documentation and semantic models