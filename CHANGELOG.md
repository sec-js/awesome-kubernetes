# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0-rc.17] - 2026-05-22

### Changed
- **Centralized YouTube Enrichment**: Standardized YouTube metadata extraction across all curation pipelines (V1 and V2). All workflows now fetch real titles and descriptions from YouTube to ensure high-fidelity AI summaries.
- **Workflow Modularization**: Reverted the consolidation of the Video Hub into the Publisher pipeline, maintaining it as a standalone workflow (`agentic_v2_videos.yml`) for better operational flexibility.
- **Improved Video Hub Design**: Redesigned the V2 Elite Video Hub with high-fidelity categorization, technology tags, and individual collapsible blocks for better user experience and flow.

## [2.0.0-rc.14] - 2026-05-22

### Fixed
- **YouTube Mosaic Corrected**: Moved @mouredev to the final position in the mosaic as requested.
- **YouTube Icon Extraction**: Extracted and integrated the actual profile picture for @mouredev from his YouTube channel, replacing the placeholder icon.

## [2.0.0-rc.13] - 2026-05-22

### Added
- **GEMINI Mandate Codification**: Officially codified architectural and UI standards in `GEMINI.md`, including the V1 vs V2 metrics protocol and branding protection rules.

## [2.0.0-rc.12] - 2026-05-22

### Fixed
- **YouTube Mosaic Exemption**: Implemented high-precision detection for the YouTube mosaic in `docs/index.md`, ensuring that only the primary high-density block is exempt from health checks.
- **README Metrics Restoration**: Fixed the git checkout depth (`fetch-depth: 0`) in the V2 publisher workflow to restore accurate historical metric generation.
- **Iframe Health Checks**: Added support for detecting and checking YouTube links within `<iframe>` tags in the index file.

## [2.0.0-rc.11] - 2026-05-22

### Added
- **YouTube Mosaic Update**: Added YouTuber @mouredev (Brais Moure) to the YouTube mosaic in both V1 and V2 index portals.

## [2.0.0-rc.10] - 2026-05-22

### Added
- **V2 Elite Synchronization**: Successfully synchronized the curated elite edition and updated README metrics via the automated publisher pipeline.

## [2.0.0-rc.9] - 2026-05-22

### Changed
- **UI Branding Optimization**: Removed redundant brand mentions in the V2 Portal header for a cleaner and more professional appearance.

## [2.0.0-rc.8] - 2026-05-22
