[Changelog](https://freemius.com/changelog/) / New SaaS Feature: Restrict one subscription per user

In the SaaS world, it’s common (and often expected) for a user to have only one active subscription at a time. However, accidental duplicate subscriptions can lead to unnecessary support tickets, billing disputes, and frustrated users — all of which take time away from growing your product.

To help prevent these headaches, we’ve introduced a new feature that lets you restrict users to a single active subscription. While you could implement this logic yourself, we believe great developer experience (DX) means providing tools that reliably handle these common edge cases for you.

To enforce this simply head to your product’s **Settings** page and enable the **Restrict Single Subscription Per User** toggle.

[![Restricting single subscription per user in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-developer-dashboard-one-subscription-config-1024x825.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-developer-dashboard-one-subscription-config.png)

Since this is a common practice among SaaS products, this setting is now **enabled by default** for all newly created SaaS products. If you created your SaaS product before this update, the feature will be **disabled by default**, but you can enable it anytime from the settings page.

Once enabled, our checkout will automatically block users from purchasing multiple subscriptions and display an error message like the one below:

[![Freemius Checkout blocking multiple subscription per user](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-one-subscription-1024x901.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-one-subscription.png)

If you’d like to customize the error message, just reach out to us via support and we’ll help you set it up.

And of course, if you prefer to allow multiple subscriptions per user, you can disable this feature at any time.

At Freemius, we’re always working to reduce friction for makers, so you can focus on building, not battling support issues. If you’d like to suggest more features, please feel free to get in touch with us through support or use our [feature board](https://freemius.nolt.io/).