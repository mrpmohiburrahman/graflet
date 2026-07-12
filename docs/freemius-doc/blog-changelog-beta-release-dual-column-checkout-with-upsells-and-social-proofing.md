[Changelog](https://freemius.com/changelog/) / Beta Release: Dual Column Checkout with Upsells and Social Proofing

We are super excited to announce the beta availability of the new checkout app we’ve been working on. It is not just a reskinning, but a complete overhaul of the UI/UX to make it more user-friendly and help more conversions. The new checkout is in the beta phase right now. To test it out right now, you can

- Add `checkout_style=phase2` in the URL parameter of the direct checkout link.
- Or use `checkout_style: 'phase2'` in the [JS integration](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) code.

[![New dual column checkout with Freemius](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-new-dual-column-checkout-1024x764.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-new-dual-column-checkout.png)

[LIVE PREVIEW](https://checkout.freemius.com/?mode=dialog&guid=e61192f6-5b7a-9e80-b051-fc83da20c846&plugin_id=311&plan_id=437&public_key=pk_a42d2ee6de0b31c389d5d11e36211&s_ctx_ts=1626969480&sandbox=5548f3de8a7e02a838427c549a588644&name=Freemius%20Checkout%20Awesome%20Plugin%20Pro&checkout_style=phase2&fullscreen=false&show_reviews=true&show_refund_badge=true)

Now let’s see some of the changes.

### A fresh new look with two columns

[![Exploring two columns in Freemius checkout](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-two-column-explanation-1024x688.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-two-column-explanation.png)

We have a nice header to communicate the pricing to the user properly. Then comes the different line items to show different discounts, breakdowns, taxes, etc, which subsequently leads to the total value.

We also present the checkout in two columns to make more of the real estate in modern screens.

### Various upsells

[![Annual upsell in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-annual-upsell-1024x538.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-annual-upsell.png)

We have three upsells built into the checkout.

- Annual upsell when the checkout is loaded with the monthly billing cycle.
- Lifetime license upsell.
- Unlimited license upsell.

[![License and Billing Cycle upsells in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-upsells-1024x440.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-upsells.png)

All of them are configurable and you can turn them off (more on it later).

### Full-Screen mode

Our checkout now supports a Full-Screen mode to take the entire real estate of the screen.

[![](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-full-screen-mode-1024x723.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-full-screen-mode.png)

- Checkout opened with the JS snippet are still sized as modal.
- Checkout opened directly through a link will be full-sized by default.
- You can set the size yourself with a configuration parameter (more on it later).
- The users can also toggle between full-size and modal-size themselves.

### Social proofing

[![](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-social-proofing-1024x828.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-social-proofing.png)

To aid in conversion, we have introduced two social proofing UIs in the checkout itself.

- Money-back guarantee: Shows the type of [refund policy](help-documentation-selling-with-freemius-refund-policy.md) you have.
- Featured Review: You can selectively show a featured review on the checkout page. Set a review as “Featured” from the Developer Dashboard and it will show up here. If you have multiple featured reviews, then the latest one will show up.

They don’t show up by default if the checkout opens with the JS integration. But they do show up if the checkout is opened as an independent page. However, you have total control to show/hide them individually, when you want.

### Improved Bundle UI

[![New bundle UI in the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-bundle-ui-1024x661.png)](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-bundle-ui.png)

We’ve improved the bundle UI by introducing a button to expand or collapse the products inside the bundle. You can control the initial state of the list. The users will always be able to expand/collapse as wanted.

### Available configuration option

This new version comes with various appearance-related configurations. All of them can be used either directly in the URL parameter or through the JS snippet as configuration properties.

For example, if your checkout URL is

```
https://checkout.freemius.com/mode/dialog/plugin/XX/plan/YY/
```

you can append the query parameters like this

```
https://checkout.freemius.com/mode/dialog/plugin/XX/plan/YY/?checkout_style=phase2&is_showing_reviews=true&is_showing_refund_badge=true
```

to open the new checkout while showing the social proofing UIs.

Similarly, if you are using the JS integration, you can add the properties while configuring or opening the checkout.

```
const handler = FS.Checkout.configure({
        plugin_id:  'plugin_id',
        plan_id:    'plan_id',
        public_key: 'pk_public_key',
        // Force load the new checkout style.
        checkout_style: 'phase2',
        show_reviews: true,
        show_refund_badge: true,
});
```

Please give this new checkout app a try and let us know of your feedback in the `#freemius-checkout` channel of our slack community.

[Learn more »](blog-freemius-release-notes-june-2024.md)