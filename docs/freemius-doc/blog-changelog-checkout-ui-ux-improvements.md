[Changelog](https://freemius.com/changelog/) / Checkout UI/UX Improvements

This week, we are releasing several UI and UX improvements for our checkout. See the details below.

### VAT Number Validation UX Improvement

Freemius allows buyers to enter their business VAT number for [reverse VAT charges](https://freemius.com/blog/eu-vat-reverse-charge-guide/). Behind the scenes, Freemius validates the VAT, and if valid, it nullifies any [VAT for EU/UK buyers](https://freemius.com/wordpress/collecting-eu-vat-europe/). We noticed that in rare cases, a buyer might submit the checkout even though the VAT number validation had not yet completed. While the checkout still displayed the amount with VAT, we understand that this could be confusing for some buyers.

[![Freemius Checkout VAT number validation UX](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-vat-validation-ux-1024x669.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-vat-validation-ux.png)

To enhance the experience, we now display a spinner next to the VAT field while the system is validating the number. Additionally, if a buyer clicks the Review or Continue to PayPal button before validation completes, the form will shake, focus on the VAT number field, and display a short message: “Verifying…”.

[![Freemius Checkout Zip code validation UX](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-salex-tax-ux-1024x670.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-salex-tax-ux.png)

We also implemented similar UX improvements for the [US Sales tax](us-sales-tax-and-economic-nexus.md), where the tax amount depends on the billing details.

We hope these enhancements improve the overall buyer experience with Freemius Checkout.

### Fixed Text in Money-Back Guarantee

Freemius Checkout includes [built-in social proof elements](blog-new-freemius-checkout-drive-conversions-increase-sales-price.md#phase_two), such as a [money-back guarantee and customer reviews](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md), to boost buyer confidence.

[![Freemius Checkout money-back guarantee UI](https://freemius.com/blog/wp-content/uploads/2025/03/money-back-ui-1024x386.png)](https://freemius.com/blog/wp-content/uploads/2025/03/money-back-ui.png)

We noticed that the money-back guarantee text incorrectly referred to a plugin instead of a product. This has now been corrected.

### Fixed Mobile UI Regression

We identified a regression where the mobile UI had incorrect top padding. This issue has now been fixed.