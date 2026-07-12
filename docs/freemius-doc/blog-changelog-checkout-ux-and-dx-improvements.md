[Changelog](https://freemius.com/changelog/) / Checkout UX and DX improvements

We’re rolling out a set of improvements to enhance the [checkout](checkout.md) experience — both for users (UI/UX) and developers (DX).

### Cart syncing issue with VAT number – fixed!

[![](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-cart-vat-number-1024x701.png)](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-cart-vat-number.png)

Freemius Checkout includes a [built-in cart system](cart-abandonment-recovery.md) to support various [marketing automation](help-documentation-marketing-automation-cart-abandonment-recovery.md) features. We discovered an edge-case bug where, due to network errors, the VAT number could become out of sync with the cart, leading to lost information. Additionally, in some cases, the cart was not updating properly when the VAT number was entered or modified. We’ve fixed both issues to ensure seamless VAT handling.

### Smarter sandbox prefill

[![](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-prefill-sandbox-1024x886.png)](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-prefill-sandbox.png)

The **Prefill** button in [sandbox checkout](help-documentation-wordpress-sdk-testing.md#testing_credit_cards) is now more intelligent. It adapts based on the full context of the checkout session. For example, if a license is already associated with the checkout, the system will no longer attempt to prefill the email field — ensuring a more accurate experience.

### Improved UI responsiveness

[![](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-ui-line-item-responsiveness-1024x818.png)](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-ui-line-item-responsiveness.png)

We’ve made subtle tweaks to improve the responsiveness of checkout line items, ensuring they adapt better to different container widths for a cleaner, more consistent layout across all the [languages](blog-changelog-freemius-checkout-now-supports-localization.md) our Checkout app supports.