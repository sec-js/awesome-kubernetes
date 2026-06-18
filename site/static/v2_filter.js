document.addEventListener("DOMContentLoaded", function () {
    // Initialize the filter only if we are on a page with resource lists
    const contentArea = document.querySelector(".md-content__inner");
    if (!contentArea) return;

    // Check if there are any resource items on the page (li or details)
    const listItems = Array.from(contentArea.querySelectorAll("ul > li"));
    const detailsItems = Array.from(contentArea.querySelectorAll("details.note"));
    
    // If there are no list items and no details items, do not inject the filter
    if (listItems.length === 0 && detailsItems.length === 0) return;

    // Do not show on the homepage or video hub index page
    const h1 = contentArea.querySelector("h1");
    if (h1 && (h1.textContent.includes("Nubenetes Elite Portal (V2)") || h1.textContent.includes("Agentic Video Hub"))) {
        return;
    }

    // Build the filter container element
    const filterContainer = document.createElement("div");
    filterContainer.className = "v2-filter-container";
    filterContainer.innerHTML = `
        <div class="v2-search-wrapper">
            <input type="text" class="v2-search-input" placeholder="Search resources in this page..." />
            <span class="v2-search-clear" style="display:none;">&times;</span>
        </div>
        <div class="v2-tag-pills">
            <button class="v2-pill active" data-filter="all">All</button>
            <button class="v2-pill" data-filter="DE FACTO STANDARD">De Facto Standard</button>
            <button class="v2-pill" data-filter="ENTERPRISE-STABLE">Enterprise Stable</button>
            <button class="v2-pill" data-filter="EMERGING">Emerging</button>
            <button class="v2-pill" data-filter="GUIDE">Guide</button>
            <button class="v2-pill" data-filter="CASE STUDY">Case Study</button>
            <button class="v2-pill" data-filter="COMMUNITY-TOOL">Community Tool</button>
            <button class="v2-pill" data-filter="SPANISH">Spanish</button>
        </div>
        <div class="v2-filter-stats">
            <span>Showing <strong class="v2-visible-count">0</strong> of <strong class="v2-total-count">0</strong> resources</span>
            <span class="v2-active-filters" style="font-style: italic;"></span>
        </div>
    `;

    // Insert the filter container right after the main H1
    if (h1 && h1.nextSibling) {
        h1.parentNode.insertBefore(filterContainer, h1.nextSibling);
    } else {
        contentArea.insertBefore(filterContainer, contentArea.firstChild);
    }

    const searchInput = filterContainer.querySelector(".v2-search-input");
    const searchClear = filterContainer.querySelector(".v2-search-clear");
    const pills = filterContainer.querySelectorAll(".v2-pill");
    const visibleCountSpan = filterContainer.querySelector(".v2-visible-count");
    const totalCountSpan = filterContainer.querySelector(".v2-total-count");

    // All target elements we want to filter
    const targets = [];
    
    // Prepare list items
    listItems.forEach(item => {
        // Make sure it's a resource list item (has a link and some content)
        if (item.querySelector("a")) {
            targets.push({
                element: item,
                type: "li",
                text: item.textContent.toLowerCase(),
                tags: Array.from(item.querySelectorAll(".md-tag")).map(t => t.textContent.toUpperCase())
            });
        }
    });

    // Prepare details.note items (if any, like in some V2 structures)
    detailsItems.forEach(detail => {
        const summary = detail.querySelector("summary");
        targets.push({
            element: detail,
            type: "details",
            text: detail.textContent.toLowerCase(),
            tags: summary ? [summary.textContent.toUpperCase()] : []
        });
    });

    totalCountSpan.textContent = targets.length;
    visibleCountSpan.textContent = targets.length;

    let activeFilter = "all";
    let searchText = "";

    function updateFilters() {
        let visibleCount = 0;

        targets.forEach(item => {
            let matchesSearch = true;
            let matchesPill = true;

            // 1. Search text filter
            if (searchText) {
                matchesSearch = item.text.includes(searchText);
            }

            // 2. Pill/Category filter
            if (activeFilter !== "all") {
                if (activeFilter === "SPANISH") {
                    matchesPill = item.tags.some(tag => tag.includes("SPANISH"));
                } else {
                    matchesPill = item.tags.some(tag => tag.includes(activeFilter));
                }
            }

            if (matchesSearch && matchesPill) {
                item.element.classList.remove("v2-filtered-hidden");
                visibleCount++;
            } else {
                item.element.classList.add("v2-filtered-hidden");
            }
        });

        visibleCountSpan.textContent = visibleCount;

        // 3. Hide empty headers and subheadings
        // If a section (e.g., under h2, h3, h4) has no visible items, hide the section header
        const headings = Array.from(contentArea.querySelectorAll("h2, h3, h4"));
        headings.forEach(heading => {
            let next = heading.nextElementSibling;
            let totalItemsInSection = 0;
            let hiddenItemsInSection = 0;

            while (next && !["H1", "H2", "H3", "H4"].includes(next.tagName)) {
                if (next.tagName === "UL") {
                    const lis = Array.from(next.querySelectorAll("li"));
                    lis.forEach(li => {
                        if (targets.some(t => t.element === li)) {
                            totalItemsInSection++;
                            if (li.classList.contains("v2-filtered-hidden")) {
                                hiddenItemsInSection++;
                            }
                        }
                    });
                } else if (next.tagName === "DETAILS" && next.classList.contains("note")) {
                    totalItemsInSection++;
                    if (next.classList.contains("v2-filtered-hidden")) {
                        hiddenItemsInSection++;
                    }
                }
                next = next.nextElementSibling;
            }

            if (totalItemsInSection > 0 && totalItemsInSection === hiddenItemsInSection) {
                heading.classList.add("v2-filtered-hidden");
            } else {
                heading.classList.remove("v2-filtered-hidden");
            }
        });
    }

    // Input event listener
    searchInput.addEventListener("input", function (e) {
        searchText = e.target.value.toLowerCase().trim();
        if (searchText) {
            searchClear.style.display = "block";
        } else {
            searchClear.style.display = "none";
        }
        updateFilters();
    });

    // Clear search
    searchClear.addEventListener("click", function () {
        searchInput.value = "";
        searchText = "";
        searchClear.style.display = "none";
        updateFilters();
        searchInput.focus();
    });

    // Pill click event listener
    pills.forEach(pill => {
        pill.addEventListener("click", function () {
            pills.forEach(p => p.classList.remove("active"));
            this.classList.add("active");
            activeFilter = this.getAttribute("data-filter");
            updateFilters();
        });
    });

    // Make tag badges clickable to trigger filtering
    document.addEventListener("click", function (e) {
        const tagSpan = e.target.closest(".md-tag");
        if (!tagSpan) return;

        // Skip if inside the filter container itself to avoid loop
        if (e.target.closest(".v2-filter-container")) return;

        let tagText = tagSpan.textContent.trim().replace(/[\[\]]/g, "").toUpperCase();
        if (tagText.includes("CONTENT")) {
            tagText = tagText.replace(" CONTENT", "");
        }

        // 1. Check if the tag matches a predefined filter pill
        const matchingPill = Array.from(pills).find(p => p.getAttribute("data-filter") === tagText);
        if (matchingPill) {
            pills.forEach(p => p.classList.remove("active"));
            matchingPill.classList.add("active");
            activeFilter = tagText;
            // Reset search input
            searchInput.value = "";
            searchText = "";
            searchClear.style.display = "none";
            updateFilters();
            filterContainer.scrollIntoView({ behavior: "smooth", block: "nearest" });
        } else {
            // 2. If it's a technical stack tag, use it as search input query
            pills.forEach(p => p.classList.remove("active"));
            const allPill = Array.from(pills).find(p => p.getAttribute("data-filter") === "all");
            if (allPill) allPill.classList.add("active");
            activeFilter = "all";
            
            // Populate search input and fire input event
            searchInput.value = tagSpan.textContent.trim().toLowerCase();
            searchText = searchInput.value;
            searchClear.style.display = "block";
            updateFilters();
            filterContainer.scrollIntoView({ behavior: "smooth", block: "nearest" });
            searchInput.focus();
        }
    });
});

// Lazy Loading Video Playback Integration
document.addEventListener("DOMContentLoaded", function() {
    const lazyContainers = document.querySelectorAll(".video-lazy-container");
    lazyContainers.forEach(container => {
        container.addEventListener("click", function() {
            const videoUrl = this.getAttribute("data-video-url");
            const videoId = this.getAttribute("data-video-id");
            if (!videoUrl || !videoId) return;
            
            const iframe = document.createElement("iframe");
            iframe.setAttribute("width", "720");
            iframe.setAttribute("height", "405");
            const autoplayUrl = videoUrl.includes("?") ? `${videoUrl}&autoplay=1` : `${videoUrl}?autoplay=1`;
            iframe.setAttribute("src", autoplayUrl);
            iframe.setAttribute("title", "YouTube Video");
            iframe.setAttribute("frameborder", "0");
            iframe.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
            iframe.setAttribute("allowfullscreen", "true");
            iframe.style.border = "none";
            iframe.style.width = "100%";
            iframe.style.height = "100%";
            iframe.style.borderRadius = "8px";
            
            this.innerHTML = "";
            this.appendChild(iframe);
            this.style.cursor = "default";
        });
    });
});

