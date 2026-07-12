[Changelog](https://freemius.com/changelog/) / RTL Language Support Comes to Freemius Checkout

This week, we are rolling out a major localization update for our Checkout. As your [Merchant of Record](merchant-of-record.md), Freemius supports selling not only in international markets, but also in your buyers’ local markets. This is why our Checkout supports local languages and currencies out of the box.

With today’s deployment, we are opening our Checkout for RTL (right-to-left) languages.

[![Freemius Checkout in Hebrew Language (RTL)](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-checkout-rtl-1024x646.png)](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-checkout-rtl.png)

Hebrew is the first RTL language we are releasing. It is currently available in beta while we gather feedback from our makers. We expect to move it to production mode very soon.

In the meantime, if you want to use it, simply add the [`language`](help-documentation-checkout-features-local-languages-currencies.md#language) parameter with the value `he`.

Once the translation is finalized, it will automatically show up for buyers from Israel when you use `language=auto` in your Checkout configuration. You can learn more about it in our [documentation](help-documentation-checkout-features-local-languages-currencies.md).

We also fixed a Checkout bug that could affect products without USD pricing configured. In some cases, the Checkout could fail to load when an explicit [`currency`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#currency) parameter was not passed. This has now been fixed.