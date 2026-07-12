[Changelog](https://freemius.com/changelog/) / Cart Recovery Coupons Now Respect Your Coupon Rules

Freemius [Cart Abandonment Recovery Coupons](help-documentation-marketing-automation-special-coupons-discounts.md#cart_abandonment_recovery_coupon) are a great way to bring back hesitant buyers. Previously, these coupons could only be used in [recovery emails](help-documentation-marketing-automation-cart-abandonment-recovery.md) if they were *completely unrestricted*. That meant the coupon had to be:

- Usable by **all** users
- Valid for **all** plans, licenses, and billing cycles

[![Freemius Coupon Configuration Window](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-coupon-configuration-1024x934.png)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-coupon-configuration.png)

Many makers asked for finer-grained control, for example, offering a discount only on annual plans or only to first-time buyers. Requiring an unrestricted coupon created extra overhead and risked accidental site-wide discounts.

The recovery engine now honours every rule on your chosen coupon. If a cart-recovery coupon is limited to certain users, plans, licenses, or billing cycles, Freemius detects those restrictions and *skips* attaching the discount in recovery emails whenever the buyer doesn’t meet the criteria. You get targeted incentives without unintended giveaways.