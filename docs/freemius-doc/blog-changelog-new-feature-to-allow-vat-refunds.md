[Changelog](https://freemius.com/changelog/) / New feature to allow VAT Refunds

This has been one of the big feature requests from our partners. Being a merchant of record, Freemius handles taxes for  [EU/UK](https://freemius.com/wordpress/collecting-eu-vat-europe/) customers on behalf of our partners.

[![Freemius checkout collecting tax](https://freemius.com/blog/wp-content/uploads/2024/04/freemius-checkout-collecting-tax-id-1024x541.png)](https://freemius.com/blog/wp-content/uploads/2024/04/freemius-checkout-collecting-tax-id.png)

Sometimes a customer would purchase a product and forget to enter their VAT number. In such cases, the customer will not get any tax exemption. Later the customer could contact the developer asking for a VAT refund.

So far, the only way to do this is to cancel the original subscription or lifetime purchase and recreate it to ensure the customer properly puts their VAT number.

To ease the process, Freemius now supports VAT refunds against a valid VAT number, right out of the box.

[![](https://freemius.com/blog/wp-content/uploads/2024/04/accessing-refund-freemius-dashboard-payments-page-1024x614.png)](https://freemius.com/blog/wp-content/uploads/2024/04/accessing-refund-freemius-dashboard-payments-page.png)

Navigate to the “Payments” section of your Developer Dashboard and click on the “Refund” button. You will find a new option to do a “Tax refund”.

[![Doing tax refund from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/04/doing-tax-refund-freemius-developer-dashboard-659x1024.png)](https://freemius.com/blog/wp-content/uploads/2024/04/doing-tax-refund-freemius-developer-dashboard.png)

Not only have we enhanced the user experience for buyers and simplified the process for you, but we’ve also devised a behind-the-scenes implementation that ensures you won’t lose the gateway fee for the entire transaction. Instead, you’ll only forfeit a partial percentage of the VAT. This not only streamlines the entire process but also saves you money.

Please note that

1. Right now we support only EU/UK VAT refunds.
2. You must supply a valid VAT number for the customer for a tax refund.
3. If the payment is associated with a subscription, the subscription will be automatically updated to exempt taxes for renewals.

The option to do a tax refund will only show up if the associated payment has a tax. If you don’t see this option, it simply means Freemius did not collect any taxes for that payment.

It is worth mentioning that the process will

1. Do a full refund of the original payment.
2. Create a new payment, excluding the VAT.

[![Payment entities after doing a tax refund in Freemius Dveloper Dashboard](https://freemius.com/blog/wp-content/uploads/2024/04/payment-entities-after-tax-refund-1024x394.png)](https://freemius.com/blog/wp-content/uploads/2024/04/payment-entities-after-tax-refund.png)

This will also be reflected in the Developer Dashboard after you’ve done a tax refund.