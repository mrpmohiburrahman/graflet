# Multi-Currency Pricing & Support

Freemius infrastructure fully supports multi-currency transactions. Currently, we support 3 currencies:

* `USD`: `$` U.S. Dollars (Default)
* `EUR`: `€` Euros
* `GBP`: `£` British Pounds

note

More currencies will be added based on demand. If you are processing high volumes from a specific geolocation that uses a particular currency currently not supported, please contact our [support](mailto:support@freemius.com).

## Who can benefit from multi-currency the most?[​](#who-can-benefit-from-multi-currency-the-most "Direct link to Who can benefit from multi-currency the most?")

Accepting multiple currencies is particularly valuable for European sellers, who generally have a major chunk of their customers based in Europe. It may not be the best decision for developers that get their earnings paid in `USD`, due to the additional FX conversion rate costs from `EUR`/`GBP` to `USD`, however, accepting your customers’ local currency can have a positive impact on conversion rates, so the trade-off there is your decision.

## How to start accepting multiple currencies?[​](#how-to-start-accepting-multiple-currencies "Direct link to How to start accepting multiple currencies?")

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Open any of your paid plans that you’d like to offer in an additional currency.
3. In the plan’s config you’ll find a new dropdown labeled *Add Currency*.
4. Click it and select the desired currency:

<!--$-->

[](/help/videos/freemius-dashboard-plan-multi-currency.mp4)

<!--/$-->

This will replicate the `USD` prices, which then you can change as you desire.

## Multi-Currency FAQ[​](#multi-currency-faq "Direct link to Multi-Currency FAQ")

### How to automatically open the checkout with a non-USD currency?[​](#how-to-automatically-open-the-checkout-with-a-non-usd-currency "Direct link to How to automatically open the checkout with a non-USD currency?")

We introduced a new `currency` parameter to the [Freemius Checkout JavaScript API](https://freemius.com/help/help/documentation/checkout/integration/freemius-checkout-buy-button/.md) (the API behind our Buy Button). When set, the checkout will be opened with the selected currency.

### Can users change the currency during the checkout process?[​](#can-users-change-the-currency-during-the-checkout-process "Direct link to Can users change the currency during the checkout process?")

After setting up multiple currencies in the Developer Dashboard, corresponding prices will automatically appear as a dropdown in the WP Admin Dashboard pricing:

<!--$-->

[](/help/videos/freemius-sdk-pricing-currency-switcher.mp4)

<!--/$-->

Additionally, a dropdown overlay appears at the top right corner of the checkout page:

<!--$-->

[](/help/videos/freemius-checkout-currency-switcher.mp4)

<!--/$-->

### Are there any additional fees/costs for selling with non-USD currencies?[​](#are-there-any-additional-feescosts-for-selling-with-non-usd-currencies "Direct link to Are there any additional fees/costs for selling with non-USD currencies?")

We don’t take any additional fees for processing foreign currency transactions. On the contrary, we’ve structured the Freemius platform to minimize the cost of gateway fees by opening bank accounts in Europe, making it even cheaper than it would be for most plugin sellers in some cases. For example, the gateway fee for `EUR` transactions processed with a European credit card is now only 1.4% + €0.25. That said, if you like to get paid in `USD`, there are naturally going to be Foreign Exchange conversion costs involved since we’ll need to convert the `EUR` earnings into `USD`. We can provide those details at the time of payout, upon request, but the bottom line is that we don’t profit from foreign exchange in any way.

### Can I get my earnings in multiple currencies?[​](#can-i-get-my-earnings-in-multiple-currencies "Direct link to Can I get my earnings in multiple currencies?")

Yes you can! If, for example, you are selling your product(s) both with `USD` and `EUR` you can get your `USD` earnings into one account and `EUR` earnings into another (both accounts must be owned by the same legal entity). If you are interested in that option and already processing more than $3k per month through Freemius, please contact our support and we’ll help you set it up.

### Can the currency be automatically selected based on geolocation?[​](#can-the-currency-be-automatically-selected-based-on-geolocation "Direct link to Can the currency be automatically selected based on geolocation?")

By default, our checkout is set with `currency` parameter's value to `'auto'` to enable the checkout automatically choose the currency based on the geolocation of the buyer. More information on this, is available in [this guide](https://freemius.com/help/help/documentation/checkout/features/local-languages-currencies/.md#setting-the-currency).

### Is it possible to set a non-USD currency as the default for my plugin or theme?[​](#is-it-possible-to-set-a-non-usd-currency-as-the-default-for-my-plugin-or-theme "Direct link to Is it possible to set a non-USD currency as the default for my plugin or theme?")

To set the default currency of the pricing page and checkout within the WP Admin dashboard, use the `'default_currency'` filter. More information on this, including an example block of code, is available in our [Freemius Checkout JavaScript API](https://freemius.com/help/help/documentation/checkout/integration/freemius-checkout-buy-button/.md#default_currency) documentation.
