[Changelog](https://freemius.com/changelog/) / API Documentation update and bug fix

We’ve added more endpoint documentation to our website, available [here](https://freemius.com/help/documentation/api/).

[![](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-api-documentation-1024x458.png)](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-api-documentation.png)

Please note that the documentation site is a “work in progress.” We’ll continue to publish updates as development progresses. The documentation follows the OpenAPI schema to ensure standardized usage.

### Bug fixes & improvements

- We identified a bug in the `/products/{product_id}/tags/latest.json` endpoint, where the returned downloadable URL was invalid. This issue has now been fixed.
- The bundle endpoint `/bundles/{bundle_id}/plugins.json` now supports a `DELETE` request to remove a product’s association with a bundle. We will add the documentation soon.