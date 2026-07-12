[Changelog](https://freemius.com/changelog/) / Resolved Regression in Review Submission Links

Freemius has a built-in [review system](help-documentation-marketing-automation-reviews.md) that allows your verified customers to leave a review for your product. You can choose to display those reviews automatically in the [Checkout](help-documentation-checkout-features-social-proofing-ui.md), on the [pricing page](help-documentation-wordpress-sdk-wp-admin-in-dashboard-upgrading.md#customizing-the-pricing-page), and you can also use the [API](https://docs.freemius.com/api/reviews/list) to show them on your own website or application.

[![Freemius Review Form](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-review-form-1024x889.png)](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-review-form.png)

Reviews are requested automatically a few days after the purchase. You can also go to the Developer Dashboard to generate a secure URL that allows your customers to leave a review directly.

[![Generate Review URL from the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/02/generate-review-url-1024x580.png)](https://freemius.com/blog/wp-content/uploads/2026/02/generate-review-url.png)

We identified a regression where the review URL was not functioning correctly and was incorrectly redirecting to the Freemius homepage. The root cause has been resolved and the fix has been deployed.