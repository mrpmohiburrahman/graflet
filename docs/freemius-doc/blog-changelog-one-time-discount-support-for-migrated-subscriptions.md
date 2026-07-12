[Changelog](https://freemius.com/changelog/) / One-Time Discount Support for Migrated Subscriptions

We are happy to announce that Freemius now supports a new coupon configuration designed to help you migrate your legacy subscriptions while offering first-time discounts to your buyers.

For example, you can create a coupon restricted to “[Migrated customers](blog-changelog-new-coupon-type-for-migrated-customers-and-other-coupon-related-bug-fixes.md)”, and under the same coupon, configure it to apply a discount on the **First payment only**.

[![Freemius Coupon Configuration](https://freemius.com/blog/wp-content/uploads/2025/06/coupon-configuration-for-migrated-subscriptions-885x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/06/coupon-configuration-for-migrated-subscriptions.png)

When your buyer chooses to migrate their subscription, they’ll not only receive the usual **proration discount**, but also this new **one-time discount**. This creates an extra incentive for your buyers to move to the new billing system powered by Freemius — ultimately benefitting both them and you.

[![Coupon discount applied to first payment while migrating legacy subscriptions](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout-with-migrated-payment-coupon-1024x386.png)](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout-with-migrated-payment-coupon.png)

As shown in the example above, the discount applies only to the **first payment Freemius collects**, and not to subsequent renewal payments.

Until now, coupons used for migration had to support both the first payment and renewals. With this update, our coupon system is far more flexible — giving you finer control over how and when discounts are applied.

Please note that the coupon discount is calculated **relative to the non-prorated period**. For example, if for an annual subscription 5 months have already been used and are prorated, then the coupon applies only to the remaining 7 months — ensuring that discounts are not compounded unintentionally.

If your coupon also supports renewal discounts, the UI will display a tooltip explaining the discount breakdown — both for the current payment and for the renewal.

[![Coupon showing relative first time discount and full renewal discount](https://freemius.com/blog/wp-content/uploads/2025/06/migrated-license-discount-with-renewal-1024x426.png)](https://freemius.com/blog/wp-content/uploads/2025/06/migrated-license-discount-with-renewal.png)

### Why We Built This

Freemius not only helps you sell your software with ease, but also makes it simple to [**migrate your existing subscriptions and licenses**](help-documentation-migration.md) from a legacy system. Our migration process is **non-breaking by design** — you don’t need to cancel everything immediately or force your buyers to resubscribe. Freemius keeps itself in sync with your legacy system, allowing you to centralize licensing in a single source of truth while gradually moving subscriptions over.

Of course, migrating to Freemius comes with multiple benefits: **global sales tax handling** like [EU VAT](eu-vat-uk-vat-europe.md) or [US Sales Tax](us-sales-tax-and-economic-nexus.md), [**automated invoicing**](help-documentation-users-account-management-orders-history.md#generate_a_printable_invoice), [**email marketing automation**](help-documentation-marketing-automation.md), and more.

To support this migration path, we also offer features like [**renewal reminder emails**](help-documentation-selling-with-freemius-license-renewals-mechanism.md#sending_renewal_email_from_freemius) and **coupons** to help encourage users to move over.

With this newly added flexibility, you can now offer **a one-time discount** during migration to further motivate buyers to switch — helping you increase adoption of the Freemius billing system.