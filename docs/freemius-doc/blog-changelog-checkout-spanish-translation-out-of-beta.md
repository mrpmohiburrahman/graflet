[Changelog](https://freemius.com/changelog/) / Checkout Spanish translation out of beta

We are glad to announce that the Spanish translation of our Checkout is out of beta.

[![](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-checkout-in-spanish-1024x761.png)](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-checkout-in-spanish.png)

Long ago we introduced translation capability to our Checkout. Displaying the checkout in the buyer’s local language significantly boosts the conversion rate. At that time we used AI to generate the following translations for the Checkout:

- Spanish
- German
- French
- Italian
- Dutch

But we marked the translations as “beta” as those were not proof-read or approved by professionals.

Now we have started to hire professional translators to finalize the translation and the first language to go through the process is Spanish.

Passing the `language` parameter with an `auto` value to the Checkout ensures that if your buyers are from Spanish-speaking regions, the Checkout will automatically load in Spanish. You can also pass static values like `es` to the `language` parameter. See [here](https://checkout.freemius.com/?mode=dialog&guid=e61192f6-5b7a-9e80-b051-fc83da20c846&plugin_id=311&plan_id=437&public_key=pk_a42d2ee6de0b31c389d5d11e36211&s_ctx_ts=1626969480&sandbox=5548f3de8a7e02a838427c549a588644&name=Freemius%20Checkout%20Awesome%20Plugin%20Pro&checkout_style=phase2&fullscreen=false&show_reviews=true&show_refund_badge=true&language=es) for an example. When the Checkout is loaded in a different language or when the `language` parameter is present, we show a dropdown in the footer of the Checkout to change the language.

More information about it can be found in our [documentation](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) (search for “language”). Very soon we will finalize more languages. Please note that only the languages for the new `phase2` Checkout are being worked upon. Just a reminder on **August 4th**, we will switch the `phase2` Checkout as default. You can read more about it [here](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md).