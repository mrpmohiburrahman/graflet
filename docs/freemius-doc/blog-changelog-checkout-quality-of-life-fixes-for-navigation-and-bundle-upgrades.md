[Changelog](https://freemius.com/changelog/) / Checkout Quality-of-Life Fixes for Navigation and Bundle Upgrades

This week we’re deploying a few small quality-of-life fixes to our Checkout.

The [back button](help-documentation-checkout-integration-hosted-checkout.md#configuring-the-back-button) now aligns properly within the vertical space around the Checkout area. Previously, it was incorrectly pushing the Checkout form downward.

[![Freemius Checkout with the Back button](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-checkout-with-back-button-1024x541.png)](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-checkout-with-back-button.png)

The Checkout also now correctly identifies an edge case in [bundles](help-documentation-wordpress-selling-bundles-and-memberships.md) where buyers try to upgrade a child license from a child product’s context. We now block this path and prompt the buyer to use the correct Checkout instead, helping avoid a confusing upgrade flow.

[![Checkout invalid license message](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-checkout-bundle-upgrade-error-message-1024x558.png)](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-checkout-bundle-upgrade-error-message.png)