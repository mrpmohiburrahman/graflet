# Special Coupons & Discounts

A subscriptions-based model thrives on conversions and renewals and dies by churn rate. To ensure you fall into the former category, we’ve implemented special contextual discounts to improve the commercial experience for your users and customers.

You can access our four special discounts in the Developer Dashboard by navigating to ***Coupons*** and clicking on the **Special Coupons** tab.

There, you can set four types of special discounts using coupons:

* [Cart Abandonment Recovery Coupon](#cart_abandonment_recovery_coupon)
* [Exit Intent Coupon (+ 1 Hour FOMO)](#exit_intent_coupon_1_hour_fomo)
* [Subscription Cancellation Coupon](#subscription_cancellation_coupon)
* [Manual Subscription Renewal Recovery Coupon](#manual_subscription_renewal_recovery_coupon)

![Freemius Developer Dashboard - Special coupons settings page](/help/assets/ideal-img/freemius-dashboard-special-coupons-nav.69cc212.480.png)

note

All special coupons require a discount coupon to be created. [Click here](https://freemius.com/help/help/documentation/selling-with-freemius/coupon-discount/.md) to learn how to create discount coupons with various configurations like lifespan, types, renewals, plans, pricings, billing cycles, and eligibility.

## Cart Abandonment Recovery Coupon[​](#cart-abandonment-recovery-coupon "Direct link to Cart Abandonment Recovery Coupon")

This special coupon integrates with the [Cart Abandonment Recovery](https://freemius.com/help/help/documentation/marketing-automation/cart-abandonment-recovery/.md) mechanism. In addition to surfacing your money-back guarantee and encouraging users to subscribe for a trial (if you have one), you can offer a discount as an extra incentive to encourage more prospects to complete the checkout they've abandoned.

Simply create a coupon with the preferred discount. Then, switch to the ***Coupons*** → **Special Coupons** tab and choose the coupon you’ve created:

<!--$-->

[](/help/videos/freemius-cart-abandonment-recovery-discount-to-reduce-customer-churn.mp4)

<!--/$-->

tip

Since the search is based on the coupon codes, we recommend using a code that includes `CART_RECOVERY` in it when you create one.

Once the coupon is selected, a discount is offered in the third cart abandonment recovery email automatically as a final attempt to win the customer:

![Freemius Cart Abandonment Recovery Email With Discount to Reduce Customer Churn](/help/assets/ideal-img/Freemius-Cart-Abandonment-Recovery-Email-With-Discount-to-Reduce-Customer-Churn.dcdf0c2.480.jpg)

The special discounts logic was built on top of our coupons infrastructure to give you control of whether the discount applies to the first payment or the first payment and subscription renewals.

Clicking the purchase button opens the checkout with the context of the saved cart and automatically applies the discount without revealing the coupon’s code:

![Freemius cart abandonment recovery mechanism click to complete checkout with coupon](/help/assets/ideal-img/freemius-cart-abandonment-recovery-mechanism-click-to-complete-checkout-with-coupon.c6e1064.480.png)

## Exit Intent Coupon (+ 1 Hour FOMO)[​](#exit-intent-coupon--1-hour-fomo "Direct link to Exit Intent Coupon (+ 1 Hour FOMO)")

An average of 69% of online checkouts are left incomplete. Capturing abandoned carts is one of the biggest opportunities to meaningfully impact revenue because the prospect has already shown intent to purchase.

While we do address abandoned carts through an email campaign, an email [Cart Abandonment Recovery mechanism](https://freemius.com/help/help/documentation/marketing-automation/cart-abandonment-recovery/.md) is fully dependent on the user entering their email address before abandoning. This makes an exit intent discount a highly effective complementary method of recovering abandoned carts, there and then.

In the ***Coupons*** → **Special Coupons** tab, select the checkout exit intent coupon:

<!--$-->

[](/help/videos/freemius-exit-intent-discount-to-reduce-customer-churn.mp4)

<!--/$-->

Once set, every person who indicates an exit intent before filling out their email address will be prompted with a FOMO (Fear of Missing Out) 60-minute timer — where they can choose to apply the coupon. If the coupon is applied, a FOMO countdown timer appears right next to the coupon row:

![Freemius exit intent discount counter encouraging a purchase to reduce customer churn](/help/assets/ideal-img/freemius-developer-dashboard-special-coupons-exit-intent-coupon-counter.ee22c4f.480.png)

tip

We recommend starting with a symbolic 5% coupon and tracking the change in sales. If 5% doesn’t have any meaningful impact, try bumping up the discount by 5% increments until you get to 20%. Depending on your profit margin, you can test with even larger discounts.

If you’re concerned about potentially devaluing your offering by applying this coupon, consider assessing it from a financial perspective. Acquiring a user through paid ads or affiliate marketing for 5%, 10%, or even 20% of their total payment makes financial sense. This coupon serves as a direct means of converting new users into customers, essentially becoming part of your customer acquisition cost.

## Subscription Cancellation Coupon[​](#subscription-cancellation-coupon "Direct link to Subscription Cancellation Coupon")

This special coupon helps to maximize subscription renewals and reduce churn rate.

Simply create a coupon with the preferred discount.

tip

To leverage this coupon to its potential, we recommend defining a 20% to 30% subscription cancellation discount.

Then, switch to the ***Coupons*** → **Special Coupons** tab and choose the coupon you’ve created:

<!--$-->

[](/help/videos/freemius-developer-dashboard-coupon-renewal-manual.mp4)

<!--/$-->

Once the coupon is set, a promo is offered to customers when they initiate a subscription cancellation process by clicking the ‘Cancel auto-renew’ button in the User Dashboard. Customers can apply the promo with a single click and there’s no need to collect the payment method again.

### Important to Note[​](#important-to-note "Direct link to Important to Note")

1. You can't modify this setting once a customer applies the subscription cancellation promo discount. Therefore, if you’d like to change the coupon's behavior on future renewals, you'll need to create a new coupon and use it as a special coupon (instead of the previous one).
2. A subscription cancellation discount can only be applied once per license. It means that once a customer has received a cancellation discount for a given license, they won't see the offer for that license again.
3. The only properties in use for this special coupon are the discount (absolute or %) and whether it should be applied on the next renewal or all future subscription renewals. The redemptions limit, plans, licenses, and billing cycles are all ignored. Effectively — even if you’ve configured the coupon to only apply for a five-site license — the promo will also be shown when a customer initiates cancellation of a single-site license.

tip

If you are running a BFCM (Black Friday Cyber Monday) promotion that applies to previous customers too, some who subscribed last year would likely want to cancel and re-subscribe to secure a lower price.

By deploying this coupon, you can mitigate subscription churn, discourage cancellation, and generate more revenue by offering a slightly lower subscription renewal discount. For example, if your BFCM promotion is set at 30%, you can offer a 15-20% discount to canceling customers.

warning

Due to PayPal API limitations, if you offer a discount that is over 16% only for the next renewal (not all renewals), then a customer with an active PayPal subscription will only be offered a 16% discount.

## Manual Subscription Renewal Recovery Coupon[​](#manual-subscription-renewal-recovery-coupon "Direct link to Manual Subscription Renewal Recovery Coupon")

To retain customers who have cancelled their subscriptions, configure a manual subscription renewal discount as an incentive:

![Freemius developer dashboard manual subscription renewal coupons](/help/assets/ideal-img/freemius-developer-dashboard-manual-subscription-renewal-coupons.cee8887.480.png)

Once set, the discount is incorporated into the [manual renewal recovery email campaign](https://freemius.com/help/help/documentation/selling-with-freemius/license-renewals-mechanism/.md) automatically. This helps to capture customers who are on the fence about renewing before their license expires.

![Freemius email notice with offer for discounted subscription renewal](/help/assets/ideal-img/freemius-renewal-recovery-coupon.a459619.480.png)

Clicking the button opens the checkout with the discount applied (without revealing the coupon’s code). A countdown is displayed to encourage users to take action, clearly informing them that the discount will expire when the license expires:

![Freemius checkout with a counter for a special subscription renewal discount coupon](/help/assets/ideal-img/freemius-checkout-special-coupon-manual-renewal-discount.33cbc84.480.png)

Unlike the automatic renewal discount that you can configure in the ***Plans*** → **Renewals Discount** section (which discounts renewals for active subscriptions), this coupon serves the exact opposite purpose.

Freemius does not endorse [discounting automatic renewals](blog-renewals-discount-for-wordpress-plugins-and-themes.md), and businesses have since shifted away from this practice. If you do not offer a discount for automatic renewals, we strongly recommend utilizing this coupon to win customers back into an active subscription.

tip

If you already offer a discount for automatic renewals, we recommend avoiding the manual renewal discount. This is because we already emphasize that subscription cancellation will cause the loss of the automatic renewals discount, so offering a discount for a manual renewal will contradict that message.

If you choose to offer both, we recommend using the same discount.
