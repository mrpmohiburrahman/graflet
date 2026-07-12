[Changelog](https://freemius.com/changelog/) / Checkout coupon and billing UI-related bug fixes

### Lifetime Billing Cycle UI bug fix

We received a report from our partners that the checkout billing cycle UI for a ‘Lifetime’ purchase wasn’t responding to the coupon code.

[![](https://freemius.com/blog/wp-content/uploads/2023/12/Freemius-Checkout-Billing-UI-Coupon-Issue.png)](https://freemius.com/blog/wp-content/uploads/2023/12/Freemius-Checkout-Billing-UI-Coupon-Issue.png)

We fixed the issue and all billing cycle UI will now respond to the entered coupon code if supported.

[![](https://freemius.com/blog/wp-content/uploads/2023/12/Freemius-Checkout-Billing-UI-Coupon-Resolved.png)](https://freemius.com/blog/wp-content/uploads/2023/12/Freemius-Checkout-Billing-UI-Coupon-Resolved.png)

### Supported coupon filtering in the Billing Cycle UI

We also received feedback from partners that a coupon code’s discount is shown in all billing cycles even if they are not supported. For example, if a particular coupon was applied to the annual billing cycle only, the monthly billing cycle would also show the (wrongly) discounted price after applying the coupon as long as the annual billing cycle was selected. We identified the root cause and fixed this.