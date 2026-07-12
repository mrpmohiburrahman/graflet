[Changelog](https://freemius.com/changelog/) / Fixed Multi-Currency Pricing UI Issues for Non-USD Plans

With Freemius, you can [configure your product’s pricing in various currencies](help-documentation-selling-with-freemius-multi-currency.md#how-to-start-accepting-multiple-currencies). This is useful whether you’re selling globally or targeting your local market.

We noticed a few edge case bugs in the Developer Dashboard, especially for plans configured only with non-USD pricing.

[![Freemius currency setup in plans](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-pricing-config-currency-1024x479.png)](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-pricing-config-currency.png)

In the Bulk Pricing section, adding a new currency was failing silently if USD pricing was not set. This has been fixed.

[![Freemius non USD plans](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-plan-with-non-usd-currency-1024x489.png)](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-plan-with-non-usd-currency.png)

The Plans page was not properly listing pricing information when USD pricing was not set. This has been fixed as well.

Please note that all of these bugs were only in the UI layer of the Developer Dashboard. Our backend systems and the Checkout continued to work correctly even when no USD pricing was configured, so no action is needed from your end.