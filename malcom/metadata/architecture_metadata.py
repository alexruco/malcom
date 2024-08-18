# malcom/metadata/architecture_metadata.py

ARCHITECTURE_METADATA = {
    # Internal Links Audits
    "all_followable_pages_with_internal_links": {
        "name": "All Followable Pages With Internal Links",
        "importance": "Ensures that all followable pages have internal links, which is essential for good site navigation and user experience.",
        "measurement_criteria": "All followable pages should have at least one internal link.",
        "fix_methods": "Add internal links to the pages that lack them.",
        "use_cases": ["SEO optimization", "Improving site structure", "Enhancing user navigation"],
    },
    "pages_max_crawl_depth": {
        "name": "Pages Max Crawl Depth",
        "importance": "Ensures pages are within a reasonable crawl depth, preventing deep pages from becoming inaccessible to search engines.",
        "measurement_criteria": "All followable pages should be within a specified crawl depth (e.g., maximum of 3).",
        "fix_methods": "Restructure the site to reduce the crawl depth of deeper pages.",
        "use_cases": ["SEO optimization", "Ensuring important pages are easily crawlable", "Improving site architecture"],
    },
    "no_follow_pages_without_internal_links": {
        "name": "No Follow Pages Without Internal Links",
        "importance": "Ensures that no-follow pages are not linked internally with followable links, maintaining the intended isolation of these pages.",
        "measurement_criteria": "No-follow pages should not have any internal followable links.",
        "fix_methods": "Remove followable links pointing to no-follow pages.",
        "use_cases": ["SEO management", "Maintaining link equity", "Preventing unintended crawling"],
    },
    "no_redirected_pages_on_internal_links": {
        "name": "No Redirected Pages on Internal Links",
        "importance": "Ensures all internal links point directly to the intended pages without causing unnecessary redirects, which can slow down the user experience.",
        "measurement_criteria": "All internal links should return a 200 OK status code without redirections.",
        "fix_methods": "Update internal links to point directly to the final URLs without intermediate redirects.",
        "use_cases": ["SEO optimization", "Improving link integrity", "Enhancing page load speed"],
    },
    "no_unavailable_pages_on_internal_links": {
        "name": "No Unavailable Pages on Internal Links",
        "importance": "Ensures that all internal links point to pages that are available and do not return a 404 error or other unsuccessful status codes.",
        "measurement_criteria": "All internal links should point to pages that return a 200 OK status code.",
        "fix_methods": "Update or remove internal links that point to unavailable pages.",
        "use_cases": ["SEO optimization", "Improving user experience", "Ensuring site integrity"],
    },

    # Sitemaps Audits
    "all_followable_pages_in_sitemaps": {
        "name": "All Followable Pages in Sitemaps",
        "importance": "Ensures all followable pages are included in at least one sitemap, aiding in search engine indexing.",
        "measurement_criteria": "All followable pages should be listed in at least one sitemap.",
        "fix_methods": "Add followable pages to the appropriate sitemaps.",
        "use_cases": ["Improving search engine indexing", "Ensuring comprehensive site coverage"],
    },
    "no_follow_pages_not_in_sitemaps": {
        "name": "No Follow Pages Not in Sitemaps",
        "importance": "Ensures that no-follow pages are not included in sitemaps, preventing them from being crawled by search engines.",
        "measurement_criteria": "No-follow pages should not be listed in any sitemaps.",
        "fix_methods": "Remove no-follow pages from all sitemaps.",
        "use_cases": ["SEO management", "Controlling page indexing"],
    },
    "no_redirected_pages_on_sitemaps": {
        "name": "No Redirected Pages on Sitemaps",
        "importance": "Ensures that all pages listed in sitemaps do not result in redirects, which can affect SEO and page load speed.",
        "measurement_criteria": "All pages listed in sitemaps should return a 200 OK status code without redirections.",
        "fix_methods": "Update sitemap entries to point directly to the final URLs without intermediate redirects.",
        "use_cases": ["SEO optimization", "Maintaining sitemap integrity", "Improving crawl efficiency"],
    },
    "no_unavailable_pages_on_sitemaps": {
        "name": "No Unavailable Pages on Sitemaps",
        "importance": "Ensures that all pages listed in sitemaps are available and do not return a 404 error or other unsuccessful status codes.",
        "measurement_criteria": "All pages listed in sitemaps should return a 200 OK status code.",
        "fix_methods": "Remove or update sitemap entries that point to unavailable pages.",
        "use_cases": ["SEO optimization", "Ensuring accurate sitemap data", "Improving search engine indexing"],
    },

    # Robots.txt Audits
    "presence_of_robots_txt": {
        "name": "Presence of Robots.txt",
        "importance": "Ensures that the robots.txt file is present, which is important for controlling search engine crawling behavior.",
        "measurement_criteria": "The website should have a robots.txt file accessible at the root.",
        "fix_methods": "Create and upload a robots.txt file to the root of the website.",
        "use_cases": ["SEO management", "Controlling crawler access"],
    },
    "sitemap_in_robots_txt": {
        "name": "Sitemap in Robots.txt",
        "importance": "Ensures that the sitemap(s) are listed in the robots.txt file, which helps search engines discover the sitemaps.",
        "measurement_criteria": "The robots.txt file should include a reference to the sitemap(s).",
        "fix_methods": "Add the sitemap URLs to the robots.txt file.",
        "use_cases": ["SEO optimization", "Improving sitemap discovery by search engines"],
    },
}

