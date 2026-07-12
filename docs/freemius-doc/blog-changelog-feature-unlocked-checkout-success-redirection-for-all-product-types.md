[Changelog](https://freemius.com/changelog/) / Feature Unlocked: Checkout Success Redirection for All Product Types

A while ago, we announced a new feature for the Checkout allowing you to [set a redirection URL](blog-changelog-new-feature-redirect-after-successful-checkout.md) after a successful purchase. Initially, this was limited only to SaaS products.

However, based on feedback from our makers community, we’re now unlocking this feature for **all** product types supported by Freemius.

A post-checkout thank you or “purchase completed” page can be useful in many scenarios, especially when the [Hosted Checkout link](help-documentation-selling-with-freemius-hosted-checkout.md) is shared via email, social media, or other marketing channels.

[![Freemius Developer Dashboard showing configuration option to redirect to specific URL after successful Checkout](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-redirection-1024x637.png)](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-redirection.png)

To get started, head over to the **Plans → Customization** section and enable the **Checkout Success Redirection** switch. More details are available in our documentation.

### Additional Improvements

- The redirection URL now includes `amount`, `tax`, and `currency` as query parameters.
- To improve clarity the `action` query parameter has been extended to include:
  
  - `payment_method_update` – When the buyer has just updated the payment method without changing any plans or pricing.
  - `license_update` – When the buyer has updated the plan or pricing of the license.
- Fixed an edge case where redirection data wasn’t properly populated for iDEAL checkout flows.