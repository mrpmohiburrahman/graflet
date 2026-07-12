[Changelog](https://freemius.com/changelog/) / Fixed Regression in Managing Custom Development or Localhost URL

With Freemius and our [WordPress SDK](help-documentation-wordpress-sdk.md), you can offer free localhost or development mode [activations](help-documentation-wordpress-license-utilization.md) to your customers. While our system already recognizes many known development and staging environments, we also allow you to define custom development URLs per buyer. This flexibility is especially useful for agencies or power users—for example, a buyer might have staging environments like `https://staging-123.agency.com`.

To [support such use cases,](help-documentation-wordpress-license-utilization.md#custom_staging_development_testing_localhost_patterns) you can head over to the User page in the Developer Dashboard and add a custom URL directly from the UI.

[![Custom Localhost URL - Freemius](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-custom-localhost-url-1024x620.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-custom-localhost-url.png)

Recently, we identified a regression in this UI where data from other products in your store could mistakenly appear. This led to confusion, making it seem like a URL couldn’t be updated or removed, or even that a custom URL was already configured, when in reality, it belonged to a different product.

This issue has now been resolved. You can confidently manage custom localhost or development URLs for your users without any interference across products.