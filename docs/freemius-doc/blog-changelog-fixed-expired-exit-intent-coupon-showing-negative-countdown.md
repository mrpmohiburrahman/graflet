[Changelog](https://freemius.com/changelog/) / Fixed expired exit-intent coupon showing negative countdown

Freemius supports [Special Coupons & Discounts](help-documentation-marketing-automation-special-coupons-discounts.md), the [Exit Intent Coupon](help-documentation-marketing-automation-special-coupons-discounts.md#exit_intent_coupon_1_hour_fomo). This coupon helps in conversion by providing a coupon right when the user is about to abandon the checkout.

[![Incorrect expiration countdown Freemius Exit Intent Coupon](https://freemius.com/blog/wp-content/uploads/2024/04/incorrect-expiration-freemius-exit-intent-coupon-1024x534.png)](https://freemius.com/blog/wp-content/uploads/2024/04/incorrect-expiration-freemius-exit-intent-coupon.png)

We noticed that the checkout was showing a negative countdown timer if the coupon had an expiration set from the Developer Dashboard and if the coupon had already expired.

[![Setting expiration date of a coupon Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/04/coupon-code-expiry-date-1024x533.png)](https://freemius.com/blog/wp-content/uploads/2024/04/coupon-code-expiry-date.png)

The expiration date of any coupon can be set from the Developer Dashboard as shown in the screenshot above.

In this deployment, we have fixed this. If the exit intent coupon expires, it will no longer be applied.

[![](https://freemius.com/blog/wp-content/uploads/2024/04/correct-exit-intent-count-down-freemius-exit-intent-coupon-1024x534.png)](https://freemius.com/blog/wp-content/uploads/2024/04/correct-exit-intent-count-down-freemius-exit-intent-coupon.png)

Also like before, if the coupon expires in the future, then the FOMO counter will count down to the expiration date of the coupon.