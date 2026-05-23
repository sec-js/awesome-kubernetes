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
- **YouTube Mosaic Rendering**: Resolved a critical newline bug breaking the first icon (Docker) in both V1 and V2 index pages.
- **Persistent V2 Navigation**: Hardcoded Video Hub links in the V2 Index and navigation to ensure stability during automated regeneration.
- **Markdown Rendering Hardening**: Resolved indentation bugs and Mandate 19 violations (blank lines around center tags) for pristine site visualization.
- **YAML Syntax and Permissions**: Fixed duplicated keys in curation workflows and added `pull-requests: write` permissions for automated bot operations.

## [2.0.0-agentic] - 2026-05-15

### Added
- **Agentic AI Orchestration Core**: Inception of the autonomous engine for discovery and evaluation.
- **Nubenetes V2 (Agentic Elite)**: Implementation of the high-density curated edition optimized for 2026 standards.
- **Visual Health Dashboard**: Automated HTML reports and GitHub Issue notifications for curation visibility.
- **Maturity Scoring Engine**: AI-driven classification (De Facto Standard, Enterprise-Stable, etc.).

## [1.9.0] - 2024-01-16

### Changed
- **Curation Strategy Pivot**: Reorganized core repository structures and pivoted toward Kustomize and declarative management.
- **Content Pruning**: Systematic removal of dead links and legacy documentation.

## [1.8.0] - 2023-01-01

### Added
- **Maintenance & Stability Phase**: Focus on refining existing content and repository hygiene.
- **Remote Job Resources**: Integrated dedicated tracking for Cloud Native career opportunities.

## [1.5.0] - 2020-05-01

### Added
- **The Great Expansion**: Massive surge in technical references (8k+ new entries).
- **Multi-Cloud Focus**: Significant expansion into AWS, Azure, and Google Cloud platform deep-dives.
- **Serverless & Mesh**: Added dedicated sections for Istio, Knative, and emerging Cloud Native patterns.

### Changed
- **Navigation Overhaul**: Transitioned to the O'Reilly-inspired logical learning journey.

## [1.2.0] - 2019-12-09

### Added
- **Troubleshooting Masterclass**: Added learnk8s.io troubleshooting guides and high-impact debugging resources.
- **Famous Kubernetes Resources 2019**: First annual curation of the most impactful ecosystem assets.

## [1.1.0] - 2018-09-29

### Added
- **RTD Integration**: First structured deployment to readthedocs.io for improved accessibility.
- **MkDocs Foundations**: Implementation of the first `mkdocs.yml` configuration and thematic sections.

## [1.0.0] - 2018-09-24

### Added
- **Nubenetes Genesis**: Initial commit and foundational repository structure.
- **Munich Era DNA**: Establishment of industrial-grade engineering standards from the BMW IT-Zentrum environment.
- **Core Pillars**: Initial collection of Kubernetes, Terraform, and Ansible references.
