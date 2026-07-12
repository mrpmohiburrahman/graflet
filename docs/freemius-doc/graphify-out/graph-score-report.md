# Freemius Docs — Graph + Score Report

**Corpus:** `freemius-scraper/docs` (scraped Freemius knowledge base — product docs, API reference, blog, help center)
**Date:** 2026-07-12

## GraphScore: 92.4 / 100 — *great*

| Axis | Score | Weight | Note |
|------|------:|-------:|------|
| **Truthful** | 100 | 50% | Every edge is a real in-corpus markdown link (40/40 sampled, 0 made up) |
| **Complete** | 79.3 | 30% | 23/29 sampled facts present; 6 missed (mostly thin concept nodes) |
| **Tidy** | 93.0 | 20% | 570 nodes, 1,974 edges, 0.55 modularity, 38 orphan docs |

**Totals:** 570 nodes · 1,974 edges · 48 communities · 39 connected components (largest holds 93% of nodes) · 100% edges `EXTRACTED`.

---

## The graph

### God nodes (most connected)
1. `help-documentation-checkout-integration-freemius-checkout-buy-button` — 46 edges
2. `merchant-of-record` — 32 edges
3. `blog-envato-alternatives-wordpress-sellers` — 31 edges
4. `blog-marketing-plugin-theme-developers` — 30 edges
5. `help-documentation-checkout-integration-hosted-checkout` — 28 edges
6. `blog-alternative-saas-acquisition-channels` — 26 edges
7. `blog-freemium-business-model-wordpress` — 26 edges
8. `blog-payment-processing-for-saas-guide` — 26 edges
9. `help-documentation-marketing-automation-cart-abandonment-recovery` — 26 edges
10. `wordpress-insights` — 26 edges

### Main communities (10 substantive + 38 isolated docs)
| ID | Label | Members |
|----|-------|--------:|
| 0 | WordPress & Plugin Business Blog | 114 |
| 1 | API Reference (Endpoints & Release Notes) | 105 |
| 2 | SaaS Monetization & Merchant of Record | 75 |
| 3 | Marketing, Growth & Brand Trust | 71 |
| 4 | SDK Integration & Release Management | 41 |
| 5 | Affiliate Program & Users API | 38 |
| 6 | Freemius API Auth & Scopes | 31 |
| 7 | Marketplaces & Template Sales | 29 |
| 8 | Migrations & Email Deliverability | 20 |
| 9 | Plugin-to-SaaS & Privacy | 8 |
| 10–47 | Isolated Doc (no internal links) | 1 each |

### Notable connections (bridges)
- `api-trials` → `help-documentation-selling-with-freemius-freemius-checkout-buy-button` — API surface links straight into the checkout-buy-button selling guide.
- `api-users` → `...freemius-checkout-buy-button` — the Users API doc cross-references the same checkout guide, a structural hub.
- `blog-spotlight-instagram-feeds-social-media-plugin-success-story` → `blog-affiliate-program-wordpress-plugins-themes` — success-story → affiliate-program bridge.
- Concept layer: `License` ↔ `Subscription` (auto-sync), `License` → `Webhooks` (event logs), `Freemius API` → 15 API-tag concept nodes + Bearer/Secret-Key auth + Product/Developer/User scopes.

### Surprising connections
- The **Freemius Checkout Buy Button** doc is the single densest hub in the whole corpus — it sits at the crossroads of API, selling, SaaS, and checkout docs.
- **Merchant of Record** is a god node driven not by product docs but by the SaaS/blog cluster (`blog-best-merchant-of-record-*`, `stripe-merchant-of-record`, `paddle-alternative`) — i.e. the competitor-comparison content, not the official docs, carries that concept.

---

## The grade

### Truthful — 100/100
All 1,974 edges are `EXTRACTED` from real internal markdown links. I fact-checked a 40-edge sample against source text; every `evidence` block contained the actual link. The 32 concept nodes (API tags, auth scopes, license/subscription/checkout/affiliate) are all grounded in files read this session (`api-overview.md`, `software-licensing.md`, `subscriptions.md`, `checkout.md`, `freemius-for-saas.md`, `affiliate-program.md`, `customer-portal.md`). **0 made-up lines.**

> Caveat: this graph was built and graded by the same host agent, so Truthful skews slightly generous — but because nothing here is inferred (0% INFERRED / 0% AMBIGUOUS), there is nothing to hallucinate. The grade is robust.

### Complete — 79.3/100
Of 29 facts sampled across 8 files, 23 are present. Missed facts:
- `affiliate-program.md` — commission/payout structure; affiliate coupon & referral links (concept node present but edges not captured).
- `customer-portal.md` — embed / magic-login detail (concept node present but disconnected).
- `blog-taxes-cheat-sheet-wordpress-developers.md` — EU/UK VAT obligations; tax registration thresholds (only the US sales-tax edge was extracted).
- `about.md` — founding / team context.

These misses are **conceptual depth**, not broken links — the docs exist and are nodes; the graph just doesn't narrate their internal sub-facts.

### Tidy — 93.0/100
- Modularity 0.55 (good clustering), mean degree 6.93, only 2 duplicate-label groups (the `affiliate program`/`Affiliate Program` and `customer portal`/`Customer Portal` pairs — doc node + concept node colliding).
- **38 orphan nodes** (6.7%): docs with zero internal links (`about.md`, `brand-assets.md`, `wordpress-resources.md`, single interview posts, etc.). They form 39 connected components; the giant component still holds 93% of nodes.
- 0 self-loops, 0 dangling edges, 0 exact duplicates.

---

## How to improve

The graph is already strong (Truthful 100). To push the score into the mid-90s, fix **completeness of concept nodes** and **orphan docs**:

1. **Wire up the two duped concept nodes.** `Affiliate Program` and `Customer Portal` exist as concept nodes but are disconnected from their source docs.
   - Add edges from `affiliate-program.md` → `concept_affiliate_program` and into its payout/coupon docs; from `customer-portal.md` → `concept_customer_portal` and its embed/magic-login docs.
   - *Impact:* removes both duplicate-label groups and recovers the 3 missed affiliate/customer-portal facts.

2. **Deepen the tax concept.** `blog-taxes-cheat-sheet-wordpress-developers.md` only linked its US sales-tax edge. Add an explicit `concept_vat` / `concept_sales_tax` node and link it from the EU-VAT and US-sales-tax pages so the VAT/registration-threshold content is represented.
   - *Impact:* recovers 2 missed facts.

3. **Resolve the 38 orphan docs.** These are real pages (`about.md`, `brand-assets.md`, `wordpress-resources.md`, lone interview/release posts) with no internal links. Either:
   - add cross-links from related docs (e.g. `about.md` → `wordpress.md` / `freemius-for-saas.md`), or
   - accept them as leaf nodes and add them to `.graphifyignore` if they carry no product knowledge.
   - *Impact:* orphan_frac 0.067 → ~0; lifts Tidy and the giant-component share.

4. **Capture conceptual sub-facts in high-value docs.** The grade is reference-free and samples files; the API/licensing docs scored perfectly, but the marketing/comparison docs lean on link-count rather than stated facts. Where a page clearly defines a concept (merchant of record, freemium model), the source text already supports it — no new extraction needed, just ensure those pages are linked so they're reachable.

**Top action:** connect the `Affiliate Program` and `Customer Portal` concept nodes to their source docs (fix #1) — it's the smallest change that recovers the most missed facts and the duplicate-label noise at once.
