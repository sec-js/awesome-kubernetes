# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-05-22

### Added
- **Official YouTube Data API v3 Integration**: Transitioned from brittle scraping to guaranteed 100% fidelity metadata extraction and elimination of bot-detection blocks.
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

## [2.0.0-rc.18] - 2026-05-22

### Added
- **Official YouTube API Support**: Initial implementation of the Data API v3 backend.
- **Improved Linter Logic**: Disabled MD051 to allow custom MkDocs anchors.

## [2.0.0-agentic] - 2026-05-15

### Added
- **Agentic AI Orchestration Core**: Inception of the autonomous engine for discovery and evaluation.
- **Nubenetes V2 (Agentic Elite)**: Implementation of the high-density curated edition optimized for 2026 standards.
- **Visual Health Dashboard**: Automated HTML reports and GitHub Issue notifications for curation visibility.
- **Maturity Scoring Engine**: AI-driven classification (De Facto Standard, Enterprise-Stable, etc.).
- **Flash-First High-Density Curation**: Throughput optimization using Gemini Flash for mass processing.

## [1.9.5] - 2025-01-31

### Added
- **Kanvas Snapshot Support**: Integration of emerging visualization plugins for k8s.
- **Meshery Integration**: Added service mesh management tools to core k8s inventory.
- **API Testing Expansion**: Inclusion of Mockapy and modern REST testing tools.

## [1.9.0] - 2024-01-16

### Changed
- **Structural Pivot**: Reorganized core repository structures to align with declarative management patterns.
- **Kustomize Focus**: Major surge in Kustomize-based deployment documentation and examples.
- **Content Pruning**: Systematic removal of dead links and legacy documentation from the 2020-2022 eras.

## [1.8.0] - 2023-01-01

### Added
- **Maintenance & Stability Phase**: Focus on refining existing content and repository hygiene.
- **Remote Job Resources**: Integrated dedicated tracking for Cloud Native career opportunities during the remote-work surge.
- **Jenkins Automation**: Added Jenkinsfiles for repository cleanup and daily maintenance tasks.

## [1.7.0] - 2022-01-10

### Changed
- **Ecosystem Hardening**: Massive verification cycle of 2020-2021 links to ensure archive validity.
- **Format Standardization**: Enforced strict indentation and table formats across all documentation.

## [1.6.0] - 2021-01-03

### Added
- **Post-Expansion Refinement**: Strategic consolidation of the massive 2020 "Great Expansion" surge.
- **Enterprise Patterns**: Inclusion of production-grade architectural blueprints for large-scale Kubernetes fleets.

## [1.5.0] - 2020-05-01

### Added
- **The Great Expansion Peak**: Vertical surge in technical references (8k+ new entries in a single month).
- **Multi-Cloud Supremacy**: Significant expansion into AWS Architecture, Azure DevOps, and Google Cloud platform internals.
- **Serverless and Mesh Inception**: Dedicated sections for Istio, Linkerd, Knative, and emerging Cloud Native patterns.
- **O'Reilly Journey Navigation**: Overhaul of the navigation menu to follow a logical, architectural learning journey.
- **Developer Portals**: Added Backstage and emerging internal developer platform (IDP) tools.

## [1.4.0] - 2020-01-20

### Added
- **Multi-Cloud Foundations**: Initial dedicated sections for AWS, Azure, and DigitalOcean.
- **Kubernetes Alternatives**: Inclusion of Nomad, Swarm, and other orchestrators for architectural comparison.

## [1.3.0] - 2020-01-09

### Added
- **CI/CD Pillar**: Major expansion into Jenkins alternatives, GitOps (Flux/Argo), and modern pipeline tools.
- **Database Evolution**: Significant additions to NoSQL, NewSQL, and cloud-native database management.

## [1.2.0] - 2019-12-09

### Added
- **Troubleshooting Masterclass**: Integration of learnk8s.io troubleshooting guides and high-impact debugging resources.
- **Famous Kubernetes Resources 2019**: First annual curation of the most impactful ecosystem assets.
- **Deep-Link Focus**: Shifted from project roots to specific technical deep-dives (wikis, RFCs, PRs).

## [1.1.0] - 2019-06-18

### Changed
- **Official Repository Migration**: Consolidated all Nubenetes assets under the official `nubenetes` organization account.
- **MkDocs Integration**: First deployment of the structured MkDocs site for better web accessibility.

## [1.0.0] - 2018-10-21

### Added
- **Munich Era Baseline**: Establishment of industrial-grade engineering standards from the Deloitte/BMW IT-Zentrum environment.
- **Architectural Relevance Protocol**: First implementation of the star (🌟) rating system to identify high-impact resources.
- **Core Technology Foundations**: Consolidated collection of Kubernetes, Terraform, Ansible, and Java Performance Optimization.
- **Monitoring and Observability**: Initial inclusion of Prometheus, Grafana, and ELK stack references.

## [0.5.0] - 2018-09-29

### Added
- **Documentation Foundations**: First implementation of `mkdocs.yml` and ReadTheDocs integration.
- **Thematic Segmentation**: Separation of content into specialized `.md` files (Docker, Ansible, Java).

## [0.1.0] - 2018-09-24

### Added
- **Alpha Inception**: Initial repository creation and experimental collection of Cloud Native links.
- **Foundational Structure**: First draft of the README-based knowledge directory.
- **Genesis Pillars**: First references for Kubernetes (Borg origins), Terraform, and DevOps methodology.
