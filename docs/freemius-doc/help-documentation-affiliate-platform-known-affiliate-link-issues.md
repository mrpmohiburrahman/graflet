---
title: "Known Affiliate Link Issues"
url: "https://freemius.com/help/documentation/affiliate-platform/known-affiliate-link-issues/"
source: "docs"
section: "Docs"
category: "Affiliate Platform"
scraped_at: "2026-04-09T19:58:36+06:00"
word_count: 244
---

If a substantial amount of the affiliate traffic (affiliated link clicks) is invalid due to an `EMPTY_REFERER` error, most likely, it’s related to one of the following issues:

## rel="noreferrer"[​](#relnoreferrer 'Direct link to rel="noreferrer"')

Some content management systems or web editors, like WordPress, include a security feature that automatically adds a `rel="noreferrer"` attribute to all links. This directive instructs the browser not to share the referrer URL with the target page. If your Affiliate Program terms require a valid referrer and it’s missing, the traffic will be considered invalid. The fix is straightforward: ask your affiliates to remove the `noreferrer` tag from their affiliate links:

- **Good:**
  
  ```html
  <a href="//r.freemius.com/123/456/" target="_blank" rel="noopener">
    link label
  </a>
  ```
- **Bad:**
  
  ```html
  <a href="//r.freemius.com/123/456/" target="_blank" rel="noopener noreferrer">
    link label
  </a>
  ```

## Inconsistent Protocol with Default Referrer Policy[​](#inconsistent-protocol-with-default-referrer-policy "Direct link to Inconsistent Protocol with Default Referrer Policy")

When a [Referrer Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) is not explicitly set on the linking site, the policy defaults to `no-referrer-when-downgrade`. This policy means that the referrer is only sent when the protocol security level remains the same. Therefore, if an affiliate link is HTTP and the page is loaded via HTTPS (or vice versa), the referrer won’t be sent due to the difference in protocol security levels. To avoid this issue, advise your affiliates to use links without specifying the protocol:

- **Good:**
  
  ```html
  <a href="//r.freemius.com/123/456/" target="_blank" rel="noopener">
    link label
  </a>
  ```
- **Bad:**
  
  ```html
  <a href="https://r.freemius.com/123/456/" target="_blank" rel="noopener">
    link label
  </a>
  ```