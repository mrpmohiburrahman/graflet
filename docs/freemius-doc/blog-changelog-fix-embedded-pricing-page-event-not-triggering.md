[Changelog](https://freemius.com/changelog/) / Fix: Embedded Pricing Page Event Not Triggering

[![WP SDK Pricing Page](https://freemius.com/blog/wp-content/uploads/2025/10/wp-sdk-pricing-page-1024x650.png)](https://freemius.com/blog/wp-content/uploads/2025/10/wp-sdk-pricing-page.png)

When someone visits the [embedded pricing page](help-documentation-getting-started-making-your-first-sale.md#in-dashboard-upgrading-in-wp-admin) from our [WordPress SDK](help-documentation-wordpress-sdk.md), our system triggers a `pricing.visit` event. This event can be used to automate marketing campaigns.

[![Logged pricing.visit webhook event](https://freemius.com/blog/wp-content/uploads/2025/10/pricing-visit-event-logged-1024x476.png)](https://freemius.com/blog/wp-content/uploads/2025/10/pricing-visit-event-logged.png)

However, we noticed that due to a regression in our system, this event was no longer being triggered for some time. We have identified the issue and rolled out a fix to restore the event’s functionality.

No SDK update is required on your end, as the fix has been applied directly to our API.