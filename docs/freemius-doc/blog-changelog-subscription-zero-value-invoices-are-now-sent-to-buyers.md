[Changelog](https://freemius.com/changelog/) / Subscription Zero-Value Invoices Are Now Sent to Buyers

We noticed a bug in our system where we did not send invoices for a subscription’s first payment when the payment value was zero. A zero-value payment can occur for several reasons, such as:

1. License upgrades with a full proration discount.
2. Purchases with a full first-payment discount due to coupons.

However, we understand that it is important to continue sending emails and invoices, as they serve as a record of the action taken by the buyer and help explain future renewal payments for the subscription.

Starting with today’s deployment, our system will now send invoices for zero-value subscription payments via the [payment email](help-documentation-marketing-automation-transactional-emails.md#purchase-payment-and-subscription-emails) buyers receive.

[![Zero value payment email sent to buyers from Freemius](https://freemius.com/blog/wp-content/uploads/2025/12/zero-value-payment-email-696x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/12/zero-value-payment-email.png)

Clicking the invoice link will show the exact reason why the invoice amount is zero. For example, an invoice may reflect a zero value due to a 100% proration discount.

[![Invoice zero value breakdown](https://freemius.com/blog/wp-content/uploads/2025/12/zero-value-invoice-breakdown-1024x565.png)](https://freemius.com/blog/wp-content/uploads/2025/12/zero-value-invoice-breakdown.png)

The Developer Dashboard will also begin showing these zero-value payments. In an upcoming update, the Dashboard will additionally support generating and downloading invoices for such payments, consistent with the experience for regular payments.