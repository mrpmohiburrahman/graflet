[Changelog](https://freemius.com/changelog/) / New Webhook: Get Notified When It’s Time to Pay Affiliates

At Freemius, we offer a robust [Affiliate Platform](help-documentation-affiliate-platform.md) for all our makers. Our system automatically generates and tracks affiliate links and calculates [affiliate payouts every month](help-documentation-affiliate-platform-paying-affiliates-commission.md). We already send an email notification when payouts are due, so you know when it’s time to reward your affiliates.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/affiliate-payout-system-notification-1024x579.png)](https://freemius.com/blog/wp-content/uploads/2025/02/affiliate-payout-system-notification.png)

To further enhance the system — especially for makers with many affiliates — we’re introducing a new webhook: `affiliate.payout.pending`. Each month, as our system calculates pending affiliate payouts, it will trigger this webhook event. You can subscribe to this webhook to automate various tasks, such as:

- Create automated payment flows within your own system
- Notify your accounting department

…and more!

[![](https://freemius.com/blog/wp-content/uploads/2025/02/webhook-affiliate-payout-890x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/webhook-affiliate-payout.png)

To get started, visit the **Custom Webhooks** page and look for the `affiliate.payout.pending` event. Check out our [documentation](help-documentation-marketing-automation-events-webhooks.md) for more details on how our webhook mechanism works.