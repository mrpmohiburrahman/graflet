[Changelog](https://freemius.com/changelog/) / Fixed Bundle Checkout Preloading With License Keys

We saw a bug in the Checkout where preloading a bundle checkout with a [license key](help-documentation-checkout-integration-freemius-checkout-buy-button.md#license_key) for [manual renewal or upgrade](help-documentation-checkout-integration-generate-renewal-payment-method-update-link.md) did not work in some cases. The Checkout incorrectly reported that the license key was invalid.

[![Checkout bundle upgrade UI](https://freemius.com/blog/wp-content/uploads/2026/05/checkout-bundle-upgrade-1024x711.png)](https://freemius.com/blog/wp-content/uploads/2026/05/checkout-bundle-upgrade.png)

We found the root cause and have deployed a fix. This now allows bundle renewal and upgrade flows to correctly preload the Checkout with the relevant license key.