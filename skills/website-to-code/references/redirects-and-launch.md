# Redirects and launch

Read this at step 4 (SEO inventory) and step 10 (launch) of `website-to-code`.

## Building the redirect map

1. Start from the merged URL sheet: Search Console indexed pages, the sitemap, and the crawl.
2. For every old URL, write the new URL. Same path when possible; the cheapest redirect is the one you do not need.
3. A page that was merged into another page redirects to the section it went to, not the top of the site.
4. A page that is gone with no equivalent: redirect to the closest parent page if it had traffic or links; let it return 404 if it had neither.
5. Every website tool leaves its own extra URLs behind: category, tag and author archives, feeds, ID-style URLs, attachment pages, and file paths for uploads (in WordPress, `/category/*`, `/tag/*`, `/feed/`, `/?p=123`, `/wp-content/uploads/*`). Find them in the crawl and decide on each pattern. Files with inbound links, such as PDFs, keep their path or get a redirect each.
6. Trailing slashes and capital letters: pick one form for the new site and redirect the other.
7. Use 301 (permanent) redirects. Write them in the host's format: `_redirects` for Netlify and Cloudflare Pages, `vercel.json` for Vercel, the framework's redirect config otherwise.
8. Test every row before launch with a redirect checker or a script that requests each old URL and confirms a single 301 to a page that returns 200. No chains, no loops.

## Carry over per page

- Title tag and meta description, unless a rewrite was agreed.
- H1.
- Canonical URL pointing at the new URL.
- Open Graph title, description and image.
- Structured data that existed before.
- Image alt text.

## Launch checklist

Before the DNS switch:
- [ ] Scope signed off; preview signed off page by page.
- [ ] Redirect file in the repo and every row tested on the preview.
- [ ] Every form submitted on the preview and the record found in the CRM with the right source.
- [ ] Tag Manager container present on every page; Tag Assistant shows analytics and conversion tags firing.
- [ ] Sitemap and robots.txt generated; robots.txt does not block the site.
- [ ] Mobile check on every page type. Page speed checked on the home page and one landing page.
- [ ] Custom 404 page with search or links to the main pages.
- [ ] DNS records for email (MX, SPF, DKIM, DMARC) written down so the switch does not touch them.
- [ ] Old site kept on a private URL or subdomain.

Switch:
- [ ] Point the domain at the new host. Change only the web records.
- [ ] Confirm HTTPS works on the bare domain and on www, and one redirects to the other.
- [ ] Spot check ten old URLs from the top of the traffic list.

After the switch:
- [ ] Submit the new sitemap in Search Console. Request indexing for the home page and top pages.
- [ ] Watch Search Console Pages and the host's 404 log weekly for four weeks; add a redirect for each 404 that matters.
- [ ] Compare search clicks and form submissions to the month before at 30 days.
- [ ] Retire the old site and cancel the old hosting and builder licences once nothing is missing.
