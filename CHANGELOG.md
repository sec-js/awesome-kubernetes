# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-05-22

### Added
- **Official YouTube Data API v3 Integration**: Guaranteed 100% fidelity metadata extraction and elimination of bot-detection blocks.
- **Robust Multimedia Hierarchy**: 3-tier fallback (Official API > yt-dlp > Gemini Pro Grounding) for high-fidelity technical summaries.
- **Optional Cache Restoration**: Controlled via `restore_cache` flag across all V2 workflows to protect manual repository updates.
- **Mandate 58 Codification**: "Official-First" protocol for multimedia and multiline rendering standards established in `GEMINI.md`.

### Changed
- **Standardized Workflow Sequencing**: Implemented a numeric 01-08 nomenclature for all 15 workflows to clarify the execution lifecycle (Discovery -> Integrity -> Enrichment -> Portal -> Metrics -> Deploy -> Safety -> Maintenance).
- **Physical Workflow Refactoring**: Renamed all `.github/workflows/` files with numeric prefixes to enforce logical ordering in the GitHub Actions UI.
- **O'Reilly Journey Architecture**: Prioritized "Fundamentals and Documentaries" in the Video Hub to provide a logical learning flow for users.
- **Categorized Workflow Matrix**: Enhanced README section 9.1 with a "Phase / Category" column and direct clickable links to each workflow UI.

### Fixed
- **Persistent V2 Navigation**: Hardcoded Video Hub links in the V2 Index and navigation to ensure stability during automated regeneration.
- **Markdown Rendering Hardening**: Resolved indentation bugs and Mandate 19 violations (blank lines around center tags) for pristine site visualization.
- **YAML Syntax and Permissions**: Fixed duplicated keys in curation workflows and added `pull-requests: write` permissions for automated bot operations.

## [2.0.0-rc.18] - 2026-05-22

### Added
- **Official YouTube Data API v3 Integration**: Transitioned from brittle scraping to guaranteed 100% fidelity metadata extraction using official Google endpoints.
- **Robust Multimedia Hierarchy**: Implemented a 3-tier extraction fallback (Official API > yt-dlp Mobile > Gemini Pro Grounding) to eliminate generic placeholders and bot-detection blocks.
- **Optional Cache Restoration**: Introduced `restore_cache` manual flag across all V2 workflows to prevent stale automated data from overwriting manual repository updates.
- **Mandate 58 Codification**: Officially established the "Official-First" multimedia extraction protocol and rendering standards in `GEMINI.md`.

### Changed
- **O'Reilly Journey Ordering**: Reorganized the Video Hub to prioritize "Fundamentals and Documentaries" at the top, following a logical architectural learning path.
- **Standardized Workflow Inventory**: Updated documentation to reflect all 15 active automated workflows with their formal GitHub Action names.
- **Production-Grade Video Portal**: Refined Markdown rendering with mandatory multiline indentation and Mandate 19 compliance (blank lines around center tags).

### Fixed
- **Persistent Video Hub Links**: Hardcoded the "Agentic Video Hub" entry in V2 index and navigation to prevent deletion during automated regeneration cycles.
- **Markdown Linting MD058/MD039/MD051**: Resolved table spacing, link syntax, and fragment validation errors across `README.md` and index files.
- **Workflow YAML Syntax**: Fixed duplicated environment keys and indentation errors in `agentic_cron.yml` and `agentic_v2_pr_only.yml`.
- **Bot Permissions**: Added `pull-requests: write` to V2 synchronization workflows to enable automated PR creation.

## [2.0.0-rc.17] - 2026-05-22
