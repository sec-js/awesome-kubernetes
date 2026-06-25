"""High-impact header for the V2 "Awesome Lists" page.

The Awesome Lists page (``other-awesome-lists.md``, derived from V1's
``/v1/other-awesome-lists/``) is a curated, AI-classified directory of the best
external ``awesome-*`` lists across the Cloud Native ecosystem. This module
builds the flagship hero banner + a category grid (cards that jump to each
in-page section), generated from the page's own rendered ``##`` headings so it
stays in sync no matter how the AI re-clusters the categories.

Pure stdlib so it can run inside ``src.v2_optimizer`` and be tested standalone.
"""

import re

_H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
_LINK_RE = re.compile(r"\]\(https?://")


def _slug(text: str) -> str:
    """Slug matching python-markdown/toc anchors (lowercase, no punctuation)."""
    s = text.lower().replace("&", " ")
    s = re.sub(r"[()]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def _sections(body_md: str):
    """Return [(title, anchor, link_count), ...] for each H2 section in order."""
    matches = list(_H2_RE.finditer(body_md))
    out = []
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body_md)
        count = len(_LINK_RE.findall(body_md[start:end]))
        out.append((title, _slug(title), count))
    return out


def build_awesome_lists_header(body_md: str) -> str:
    """Build the hero + category grid that precedes the Awesome Lists body."""
    sections = _sections(body_md)
    total_lists = sum(c for _, _, c in sections)
    n_cats = len(sections)

    md = (
        "<div class=\"awesome-hero\">\n"
        "  <div class=\"awesome-hero__badge\">⭐ AWESOME LISTS ⭐</div>\n"
        "  <div class=\"awesome-hero__sub\">The best curated <code>awesome-*</code> lists · AI-classified · link-validated</div>\n"
        "  <div class=\"awesome-hero__stats\">\n"
        f"    <span class=\"awesome-hero__stat\"><strong>{total_lists}</strong>curated lists</span>\n"
        f"    <span class=\"awesome-hero__stat\"><strong>{n_cats}</strong>categories</span>\n"
        "  </div>\n"
        "</div>\n\n"
        "!!! tip \"The meta-directory of the Cloud Native ecosystem\"\n"
        "    A hand-picked, AI-classified index of the most valuable community "
        "**awesome-* lists** — every one link-validated and filed by topic. Jump "
        "to a category below, or browse the full directory. For the original "
        "exhaustive archive, see the [**V1 Historical Archive**](/v1/other-awesome-lists/).\n\n"
    )

    if sections:
        md += "<div class=\"awesome-grid\">\n"
        for title, anchor, count in sections:
            md += (
                f"  <a class=\"awesome-card\" href=\"#{anchor}\">\n"
                f"    <span class=\"awesome-card__name\">{title}</span>\n"
                f"    <span class=\"awesome-card__meta\"><span class=\"awesome-card__count\">{count}</span>"
                f"<span class=\"awesome-card__stars\">lists</span></span>\n"
                f"  </a>\n"
            )
        md += "</div>\n\n"

    return md
