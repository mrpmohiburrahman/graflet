[Changelog](https://freemius.com/changelog/) / Checkout UI improvements and bug fixes

This week, we deployed some minor UI improvements and bug fixes for our checkout.

### Smarter back button

Recently, with **Phase 2**, we introduced a **Back** button for the standalone version of our checkout. This worked by checking the HTTP referrer or a specific URL parameter.

[![Back button on Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-back-button-1024x990.png)](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-back-button.png)

With today’s release, the **Back** button now defaults to the **marketing URL** set in your product’s configuration.

[![Set marketing page URL](https://freemius.com/blog/wp-content/uploads/2025/02/marketing-page-url-1017x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/marketing-page-url.png)

If you haven’t already, please follow the directions in the screenshot above to set your **marketing URL**. Additionally, the `cancel_url` parameter still works as expected and will override any HTTP referrer or implicit marketing URL value.

### UI glitch fix for payment method update

With Freemius, buyers can update their **payment method** anytime via the self-service [**Customer Portal**](help-documentation-users-account-management.md). Additionally, we introduced a shortcut in the **Developer Dashboard**, allowing you to manually copy and send a [**payment method update**](blog-changelog-checkout-related-enhancements-for-the-developer-dashboard.md) link to buyers.

[![Freemius Checkout payment method update](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-payment-method-update-1024x878.png)](https://freemius.com/blog/wp-content/uploads/2025/02/checkout-payment-method-update.png)

We noticed a minor UI glitch in the **payment method update** flow where the header was not aligned properly. This has now been fixed.

### Improved payment PDF

[![Freemius payment PDF with long lines](https://freemius.com/blog/wp-content/uploads/2025/02/freemius-payment-pdf-1024x360.png)](https://freemius.com/blog/wp-content/uploads/2025/02/freemius-payment-pdf.png)

We identified edge cases where long lines in the buyer’s or seller’s **billing address** could break the layout. This issue has been resolved in today’s release.