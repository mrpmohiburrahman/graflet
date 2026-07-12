[Changelog](https://freemius.com/changelog/) / Improved License Activation API with Full Bundle Support

We’ve extended our license activation [API](https://docs.freemius.com/api) to fully support [bundle licenses](help-documentation-wordpress-selling-bundles-and-memberships.md) — an important improvement for makers building their own integrations outside the official [WordPress SDK](help-documentation-wordpress-sdk.md).

Previously, activating a bundle license through the product-level activation endpoints wasn’t supported. With this update, any bundle-issued license key will now activate correctly, when hitting a product-specific endpoint such as:

[![Freemius license activation API](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-api-license-activation-code-1024x515.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-api-license-activation-code.png)

This ensures [custom apps](help-documentation-saas-integrating-license-key-activation.md), or LiteSDK-powered WordPress plugins all get consistent activation behavior.

If you’re implementing activation outside the WP SDK, here are helpful resources:

1. [WP LiteSDK POC](https://github.com/Freemius/wp-sdk-lite) — For building custom WordPress integrations without the full SDK.
2. [API Documentation](https://docs.freemius.com/api/licenses/activate) — For Apps, or any custom implementation.