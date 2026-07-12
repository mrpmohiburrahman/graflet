[Changelog](https://freemius.com/changelog/) / Checkout Reskinning: Preparing the phase2 version for production rollout

It has been a couple of weeks since we pushed updates to the new `phase2` checkout and this week, we are starting to push it for production. Like [before](blog-changelog-checkout-redesigning-phase-1-features-migration-guide.md), we will do it gradually, without breaking any custom CSS you might be using. Please read below to learn more.

[![Freemius Checkout Phase2 - Release Candidate](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate-1024x736.png)](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate.png)

### Recap: Beta releases so far

We first released the `phase2` checkout on [May 20, 2024](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md). Since then there have been a few iterations and improvements.

- [May 28, 2024](blog-changelog-improved-paypal-subscription-failure-messages-in-the-checkout.md) & [June 2, 2024](blog-changelog-further-improvements-to-the-paypal-error-ui-in-the-checkout.md) updates: PayPal error UI improvements.
- [June 23, 2024 update](blog-changelog-beta-checkout-updates-enhancements-and-bug-fixes.md): Enhancements and bug fixes.
- [June 30, 2024 update](blog-changelog-beta-checkout-updates-flexible-discounts-and-more.md): Flexible discounts and more UI configuration parameters.

Today with a [few more bug fixes](blog.md) we are finally marking the checkout as **release-candidate** and preparing for the production switch.

### Gradual rollout

- On [**August 4th, 2024**](blog-changelog-the-new-phase2-checkout-is-officially-live.md) we will make the `phase2` checkout the default in production. However, if you have a custom checkout CSS for the `phase1` checkout but not for the `phase2` checkout, we will keep on showing the `phase1` checkout for you. Only when you clear the Custom CSS from the legacy section, the new Checkout will show up by default.
- On **August 18th, 2024** two weeks after the production rollout, we will enable it for everyone. However, you will still have the option of using `checkout_style=legacy` to force load the `phase1` checkout.
- On **September 29th, 2024** we will completely remove the legacy `phase1` checkout.

Until the rollout

1. You can switch to the new checkout by using the configuration `checkout_style=phase2` in the URL parameter or JS snippet. More on it later in.
2. You now have two different CSS configurations, one for the existing checkout and one for the new `phase2` checkout.

### Custom CSS migration

Starting today, you will notice that your existing checkout CSS style (if any) has been moved to the “(Legacy) Custom Checkout CSS file” under the plans page of the Developer Dashboard. The first input field is now empty.

[![CSS migration guide for Freemius Checkout phase 2](https://freemius.com/blog/wp-content/uploads/2024/07/new-css-url-for-phase2-checkout-1024x455.png)](https://freemius.com/blog/wp-content/uploads/2024/07/new-css-url-for-phase2-checkout.png)

To migrate your CSS for the new version, simply put the stylesheet URL in the first input field and you are good to go. Please read our [documentation](https://freemius.com/go/checkout-css-customization/) to learn about CSS customization.

Remember to clear out the `(Legacy) Custom Checkout CSS file` after you’ve migrated to have the new checkout show up by default.

### Call for testers

We would be glad to get your help to test the new checkout out in the wild.

[![Testing out phase2 checkout from the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/07/preview-phase2-checkout-from-developer-dashboard-1024x333.png)](https://freemius.com/blog/wp-content/uploads/2024/07/preview-phase2-checkout-from-developer-dashboard.png)

Kindly go to the plans page and toggle the new configuration to get URLs and JS snippets to load the new checkout.

Alternatively, you can just add `checkout_style=phase2` or `checkout_style: 'phase2'` in the URL or JS snippet to see it live. Here are some live demos:

- [Generic example](https://checkout.freemius.com/?mode=dialog&guid=e61192f6-5b7a-9e80-b051-fc83da20c846&plugin_id=311&plan_id=437&public_key=pk_a42d2ee6de0b31c389d5d11e36211&s_ctx_ts=1626969480&sandbox=5548f3de8a7e02a838427c549a588644&name=Freemius%20Checkout%20Awesome%20Plugin%20Pro&checkout_style=phase2&fullscreen=false&show_reviews=true&show_refund_badge=true) – A regular product with different pricing
- [All Discounts](https://checkout.freemius.com/mode/dialog/bundle/15900/plan/26498/?checkout_style=phase2&licenses=5) – Loads with all discounts
- [Minimalistic](https://checkout.freemius.com/mode/dialog/bundle/15900/plan/26498/?checkout_style=phase2&licenses=5&annual_discount=false&bundle_discount=false&multisite_discount=false) – Discounts free view

If you find any issues please get in touch with our [support](https://freemius.com/cdn-cgi/l/email-protection#bac9cfcacad5c8cefadcc8dfdfd7d3cfc994d9d5d7).

We will make another announcement in July when we believe the checkout is ready to go into production. Until then, please stay tuned.