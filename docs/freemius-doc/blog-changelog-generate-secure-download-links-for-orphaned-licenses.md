[Changelog](https://freemius.com/changelog/) / Generate Secure Download Links for Orphaned Licenses

Freemius allows makers to create licenses that are not initially associated with any user. Once a user activates the license, the association is automatically established. This feature is especially useful for sharing custom licenses with reviewers or affiliates to try out a product.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/generate-download-link-1024x926.png)](https://freemius.com/blog/wp-content/uploads/2024/11/generate-download-link.png)

The Freemius [Developer Dashboard](https://dashboard.freemius.com/) also includes a feature to generate secure download links for products directly from the Licenses page. However, we discovered a bug where the UI failed silently if the license was not associated with a user.

We’ve fixed this issue! You can now generate secure download links even for orphaned licenses.