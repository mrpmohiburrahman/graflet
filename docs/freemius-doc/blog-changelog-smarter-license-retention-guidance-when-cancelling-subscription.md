[Changelog](https://freemius.com/changelog/) / Smarter License Retention Guidance When Cancelling Subscription

The Freemius [Developer Dashboard](https://dashboard.freemius.com/) allows you to manage your subscriptions with ease. From the **Subscriptions** page, you can view all active subscriptions, drill into detailed information, and cancel subscriptions when needed.

[![Subscription Management from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-subscriptions-management-1024x388.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-subscriptions-management.png)

When cancelling a subscription, the system also prompts whether you want to cancel the associated license. While cancelling the license by default makes sense for WordPress products, given how our [WP SDK](help-documentation-wordpress-sdk.md) treats cancelled [licenses](help-documentation-wordpress-sdk-software-licensing.md)—it is not the ideal recommendation for SaaS & App products. In those cases, usability and entitlement depend on whether the license is active and not expired, rather than whether the subscription itself is cancelled.

To reduce confusion and better align with how SaaS & App licensing works, we have improved the license cancellation dialog, as shown below.

[![License cancellation dialog from cancelled subscription](https://freemius.com/blog/wp-content/uploads/2025/12/cancel-license-dialog-1024x702.png)](https://freemius.com/blog/wp-content/uploads/2025/12/cancel-license-dialog.png)

The dialog now clearly explains the implications of each option and recommends **Retain the License** as the primary action.

Please note that even if the license is retained, it will eventually expire, at which point access to the product will be revoked for the user. You can read more about license lifecycle handling and entitlements in our [SaaS](help-documentation-saas-saas-integration.md) and [App](help-documentation-saas-app-integration.md) integration guides.