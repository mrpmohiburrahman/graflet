---
title: "Freemius SDK"
url: "https://freemius.com/help/faq/freemius-sdk/"
source: "docs"
section: "FAQ"
category: "Freemius SDK"
scraped_at: "2026-04-09T19:58:46+06:00"
word_count: 160
---

## What languages is your WordPress SDK translated to?[​](#what-languages-is-your-wordpress-sdk-translated-to "Direct link to What languages is your WordPress SDK translated to?")

You can check out all of the supported languages and help us translate the SDK (we know you want to be on our hall of fame 😉 ) on our [Transifex translations manager](https://www.transifex.com/freemius/wordpress-sdk/).

## Is your SDK RTL compliant?[​](#is-your-sdk-rtl-compliant "Direct link to Is your SDK RTL compliant?")

Yes, it is.

## What makes Freemius WordPress.org compliant?[​](#what-makes-freemius-wordpressorg-compliant "Direct link to What makes Freemius WordPress.org compliant?")

We’ve built a special PHP preprocessor that looks into your project’s PHP files and uses the SDK calls in your code as annotations to understand what parts of it should be excluded from the free product version. Then, the preprocessor automatically generates a free version of your plugin by striping away all of its premium code. The free version is the version that should be uploaded to WordPress.org, in order to comply with the [WordPress.org guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/).