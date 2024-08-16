# malcom/metadata/architecture_metadata.py

ARCHITECTURE_METADATA = {
    "presence_of_robots_txt": {
        "name": "Presence of robots.txt",
        "importance": "Ensures that the website is properly instructing search engines on which pages to crawl or not.",
        "measurement_criteria": "Check if the robots.txt file exists in the root of the domain.",
        "fix_methods": "Create a robots.txt file in the root directory of the website with appropriate directives.",
        "use_cases": [
            "Preventing search engines from indexing certain parts of the website",
            "Ensuring that search engines have guidance on which pages to crawl"
        ]
    },
    "sitemap_in_robots_txt": {
        "name": "At least one sitemap listed on robots.txt",
        "importance": "Helps search engines discover all important pages on the website.",
        "measurement_criteria": "Check if the robots.txt file lists at least one sitemap.",
        "fix_methods": "Add the location of at least one sitemap to the robots.txt file.",
        "use_cases": [
            "Ensuring that all important pages are discoverable by search engines",
            "Improving the efficiency of search engine crawls"
        ]
    },
    "all_followable_pages_in_sitemap": {
        "name": "All followable pages on at least one sitemap",
        "importance": "Ensures that all pages meant to be crawled by search engines are included in sitemaps.",
        "measurement_criteria": "Verify that every followable page is listed in at least one sitemap.",
        "fix_methods": "Add any missing followable pages to the appropriate sitemap.",
        "use_cases": [
            "Maximizing the chances of important pages being indexed",
            "Maintaining a complete and accurate sitemap"
        ]
    },
    "followable_pages_with_internal_links": {
        "name": "All followable pages with at least one followable internal hyperlink",
        "importance": "Ensures that every followable page is accessible via internal links, improving SEO and user navigation.",
        "measurement_criteria": "Check that each followable page is linked from at least one other followable page.",
        "fix_methods": "Add internal links to any followable pages that lack them.",
        "use_cases": [
            "Enhancing the crawlability and discoverability of content",
            "Improving user experience through better site navigation"
        ]
    },
    "no_follow_pages_without_internal_links": {
        "name": "All no-followable pages with no internal followable hyperlinks",
        "importance": "Prevents pages that should not be crawled from being accessible via internal links.",
        "measurement_criteria": "Verify that no-followable pages are not linked to by followable internal links.",
        "fix_methods": "Remove or change internal links pointing to no-followable pages.",
        "use_cases": [
            "Controlling which pages are accessible and crawlable by search engines",
            "Preventing the dilution of link equity"
        ]
    },
    "no_follow_pages_not_in_sitemaps": {
        "name": "All no-followable pages not in sitemaps",
        "importance": "Ensures that pages that should not be followed by search engines are not included in sitemaps.",
        "measurement_criteria": "Check that no-followable pages are not listed in any sitemaps.",
        "fix_methods": "Remove no-followable pages from sitemaps.",
        "use_cases": [
            "Keeping sitemaps focused on pages intended for indexing",
            "Improving the relevance and efficiency of sitemaps"
        ]
    },
    "followable_pages_max_crawl_depth": {
        "name": "All followable pages with max 3 crawl depth",
        "importance": "Ensures that important content is not buried deep within the website's structure, making it harder for search engines to crawl.",
        "measurement_criteria": "Verify that followable pages can be reached within a maximum of 3 clicks from the homepage.",
        "fix_methods": "Adjust the site's architecture to reduce the crawl depth of important pages.",
        "use_cases": [
            "Improving the visibility of key content to search engines",
            "Enhancing user experience by making important pages easier to find"
        ]
    }
}
