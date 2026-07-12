[Changelog](https://freemius.com/changelog/) / Freemius Checkout Now Supports PLN, CAD, AUD, and ILS

This week, we’re rolling out a big feature for [Freemius Checkout](help-documentation-checkout.md). Until now, the Checkout supported [USD, EUR, and GBP currencies](help-documentation-selling-with-freemius-multi-currency.md). We are now extending that support to PLN (Polish Zloty), CAD (Canadian Dollar), AUD (Australian Dollar), and ILS (Israeli New Shekel).

This is a great update for makers who are targeting local markets and want the Checkout experience to feel more familiar to their customers. For example:

- Makers from Israel can configure the Checkout in Hebrew, with RTL support and ILS currency.

<!--THE END-->

[![Checkout in RTL with local currency](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-localized-checkout-rtl-1024x640.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-localized-checkout-rtl.png)

- Similarly, makers from Poland can configure the Checkout in Polish language with PLN currency.

[![Freemius Checkout with the newly supported currencies](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-localized-checkout-1024x616.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-localized-checkout.png)

You can simply set both the `language` and `currency` parameters of the Checkout to `auto`, and Freemius will do the rest. Alternatively, you can configure them with exact values. Learn more about the best practices [here](help-documentation-checkout-features-local-languages-currencies.md#best-practices).

## Setting Up The Currencies

Just like before, navigate to the **Plan** page of the Developer Dashboard and click the **Add Currency** button.

[![showing the Add Currency button on the Plan page](https://freemius.com/blog/wp-content/uploads/2026/06/setup-multi-currency-pricing-1024x479.png)](https://freemius.com/blog/wp-content/uploads/2026/06/setup-multi-currency-pricing.png)

You will see that we’ve revamped the UI to make it easier to add and manage currencies. Select the desired currency, and Freemius will copy the value from the USD price using the proper conversion rate.

[![Selecting the new currency from the dropdown UI](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-new-currencies-dropdown-1024x578.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-new-currencies-dropdown.png)

From there, you can edit the values and pricing based on your requirements.

[![showing editable pricing fields for the newly added currency](https://freemius.com/blog/wp-content/uploads/2026/06/configured-multi-currency-pricing-1024x633.png)](https://freemius.com/blog/wp-content/uploads/2026/06/configured-multi-currency-pricing.png)

## Checkout Integration

By default, the Checkout will show all available currencies in the dropdown near the total price and in the footer.

[![showing the currency dropdown in the Checkout](https://freemius.com/blog/wp-content/uploads/2026/06/checkout-currency-selector-1024x729.png)](https://freemius.com/blog/wp-content/uploads/2026/06/checkout-currency-selector.png)

You can also preload the Checkout with a specific currency by passing [`currency`](help-documentation-checkout-features-local-languages-currencies.md#currency) as `aud`, `cad`, `ils`, and so on.

## Payouts

For the newly introduced currencies, you only need to set up the [USD payout method](help-documentation-selling-with-freemius-your-earnings.md#set-up-payout-methods).

[![Set up USD payout method](https://freemius.com/blog/wp-content/uploads/2026/06/payout-method-1024x418.png)](https://freemius.com/blog/wp-content/uploads/2026/06/payout-method.png)

While GBP and EUR payouts can be configured separately, the new currencies are converted to USD by the payment provider at the time of payment and added to your USD balance.

We hope this exciting new feature helps you get closer to your local market and customers. If you would like to see more currencies supported in Freemius, please create or upvote a feature request on our official [board](https://freemius.nolt.io).