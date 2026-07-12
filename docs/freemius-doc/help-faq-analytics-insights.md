---
title: "Analytics & Insights"
url: "https://freemius.com/help/faq/analytics-insights/"
source: "docs"
section: "FAQ"
category: "Analytics & Insights"
scraped_at: "2026-04-09T19:58:46+06:00"
word_count: 465
---

## Can I use Insights in my Premium only plugin or theme?[​](#can-i-use-insights-in-my-premium-only-plugin-or-theme "Direct link to Can I use Insights in my Premium only plugin or theme?")

Yes, you can! In addition, since you are not obligated to any guidelines, you can capture all the information and skip the opt-in screen. If you do so, you would need to explicitly mention that part in your privacy and terms of use. Having said that, since no one actually reads the privacy and terms, we recommend using the opt-in screen as an ethical transparency act.

## Can I customize the opt-in screen?[​](#can-i-customize-the-opt-in-screen "Direct link to Can I customize the opt-in screen?")

We have crafted special filters to customize the messaging and buttons of the opt-in screen. You can also completely edit the PHP template file in the SDK. Make sure you keep it clear about what information is being captured and that it’s sent to *Freemius*. Otherwise, it won’t be compliant with the [WordPress.org guidelines](https://wordpress.org/plugins/about/guidelines/).

## Can I use Freemius Insights on CodeCanyon and ThemeForest?[​](#can-i-use-freemius-insights-on-codecanyon-and-themeforest "Direct link to Can I use Freemius Insights on CodeCanyon and ThemeForest?")

Yes! It’s compliant with the marketplace rules. In fact, a similar analytics product, called *PressTrends*, was widely adapted by *ThemeForest* and *CodeCanyon* developers in early 2014.

## Can I use Freemius Insights with EDD or WooCommerce?[​](#can-i-use-freemius-insights-with-edd-or-woocommerce "Direct link to Can I use Freemius Insights with EDD or WooCommerce?")

Absolutely YES! There’s no collision nor interaction between [Freemius Insights](wordpress-insights.md) and other eCommerce solutions. [Freemius Insights](wordpress-insights.md) does not depend on on our monetization solutions. You can add [Freemius Insights](wordpress-insights.md) to both your free and premium plugin versions.

## Why is the active installs metric on WordPress.org different than the one on Freemius?[​](#why-is-the-active-installs-metric-on-wordpressorg-different-than-the-one-on-freemius "Direct link to Why is the active installs metric on WordPress.org different than the one on Freemius?")

There’s a fundamental difference in the way WordPress.org and Freemius count active installs.

Based on publicly available responses from key people in the WordPress meta team, the WordPress.org active installs counter relies on the WordPress.org updates mechanism, which is sampled on a weekly basis. Updates are triggered only when there’s traffic to the site, so if a site installed your plugin or theme and did not get any traffic during that sampling period OR, if the updates mechanism is blocked (or turned off), this site will not get counted. Also, we suspect that the WordPress.org sampling relies on domains and not on IPs. In that case, for example, all of the VVV installs that installed your product will only be counted as a single site.

On the other hand, Freemius uses real actions such as an explicit opt-in or deactivation/uninstall events. One fallback of that tracking methodology is if a user hard-deletes the product from the filesystem, using FTP/SSH, it is still considered active.