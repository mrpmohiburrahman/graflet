[Changelog](https://freemius.com/changelog/) / Improvements to the Subscription Cancellation Coupon Trigger

Freemius supports setting up a special coupon to appear when a buyer is canceling their subscription. This feature is very helpful in reducing churn rates.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/subscription-cancellation-coupon-1024x672.png)](https://freemius.com/blog/wp-content/uploads/2024/12/subscription-cancellation-coupon.png)

As a maker, you just need to [set the coupon up](help-documentation-marketing-automation-special-coupons-discounts.md#subscription_cancellation_coupon) from the Developer Dashboard. Now, when a buyer clicks the “**Cancel Auto-Renew**” button through the [Customer Portal](help-documentation-users-account-management.md), the system will automatically show a pop-up like the one above.

However, due to limitations of payment gateways, sometimes it is impossible to apply the discount to the next immediate payment from the subscription.

To improve the system, we’ve made it smarter by detecting such scenarios and preventing the pop-up from showing. This, in turn, will help reduce disputes.