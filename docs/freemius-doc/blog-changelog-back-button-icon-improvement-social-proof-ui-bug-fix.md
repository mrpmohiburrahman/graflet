[Changelog](https://freemius.com/changelog/) / Back Button Icon Improvement & Social Proof UI Bug Fix

### Back Button Icon Improvement

When using the [hosted version](https://freemius.com/help/documentation/checkout/hosted-checkout/) of [Freemius Checkout](help-documentation-checkout.md), we render a back button at the top of the page to give buyers a sense of continuity with your website. For example, if your site is `https://awesome-saas.com` and you open Freemius Checkout from there, our Checkout will automatically display a button that says **“Back to awesome-saas.com”**.

[![Freemius Checkout Back Button](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-back-button-1024x665.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-back-button.png)

Additionally, we also show an auto-detected favicon next to the back button, if one is available from your website.

[![Back button with Favicon in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-back-button-favicon-1024x690.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-back-button-favicon.png)

Previously, we noticed that when our system failed to retrieve a favicon, a generic placeholder image was shown instead. This could cause confusion or even suspicion among buyers who didn’t recognize the placeholder image.

To address this, we’ve made some enhancements to the system. Now, a favicon will only be shown if we’re able to reliably fetch one from your website. If not, we simply omit the icon altogether – avoiding any misleading visuals.

To understand how the back button works and how to customize it, please refer to our [documentation](https://freemius.com/help/documentation/checkout/hosted-checkout/#configuring_the_back_button).

### Social Proofing UI Bug Fix with Redirect Feature

We discovered a bug where the [social proofing UI](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md#social_proofing)—such as the “Money-Back Guarantee” badge and reviews, were being hidden when the checkout [redirected](https://freemius.com/help/documentation/checkout/hosted-checkout/#redirection_after_a_successful_purchase) after a successful purchase.

[![Freemius Checkout Social Proofing UI](https://freemius.com/blog/wp-content/uploads/2025/08/checkout-social-proofing-ui-1024x446.png)](https://freemius.com/blog/wp-content/uploads/2025/08/checkout-social-proofing-ui.png)

This has now been fixed, ensuring buyers continue to see relevant trust signals even during post-purchase redirection.