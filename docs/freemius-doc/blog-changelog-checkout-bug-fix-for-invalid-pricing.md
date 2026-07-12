[Changelog](https://freemius.com/changelog/) / Checkout Bug Fix for Invalid Pricing

We identified an issue where, if a maker intentionally left a pricing field blank, the checkout could load in an invalid state. In such cases, the checkout incorrectly displayed the price as zero, even though it wasn’t intended to show up at all.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-invalid-pricing-1024x531.png)](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-invalid-pricing.png)

For instance, a maker might choose not to offer single-unit pricing. In these scenarios, the checkout should automatically load with the nearest lower unit pricing by default.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-2-unit-by-default-1024x566.png)](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-2-unit-by-default.png)

We’ve resolved this glitch and deployed a fix to ensure the checkout behaves as expected in such cases.