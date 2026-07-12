[Changelog](https://freemius.com/changelog/) / Checkout tax and billing UX improvement

Following our last major release of [checkout tax and billing improvements](blog-changelog-improvements-to-the-tax-and-billing-ui-of-the-checkout-app.md), we’ve gathered feedback and pushed a UX improvement.

[![Freemius Checkout Tax Disclaimer](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-tax-disclaimer.jpg)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-tax-disclaimer.jpg)

We’ve shown a “disclaimer” below the billing country regarding the applicable tax. However, in the case of VAT, the tax amount is exempted by law when entering your business VAT ID. The disclaimer becomes confusing since it still says “**xx**% VAT applied…”.

[![Freemius Checkout tax disclaimer is hidden when VAT ID is entered](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-improved-tax-disclaimer.jpg)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-improved-tax-disclaimer.jpg)

As an improvement, we won’t show the disclaimer when a valid VAT ID is entered in the checkout form.