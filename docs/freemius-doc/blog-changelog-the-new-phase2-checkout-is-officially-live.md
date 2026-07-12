[Changelog](https://freemius.com/changelog/) / The new phase2 Checkout is officially live

We are glad to announce the new `phase2` Checkout is officially in production starting today.

We’ve been doing a gradual rollout for quite some time and the time has finally come for the first production rollout.

[![Freemius Checkout Phase2 - Release Candidate](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate-1024x736.png)](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate.png)

If you do not use custom CSS to modify the Checkout, then the new Checkout will start showing up for you without any changes.

However, if you are using custom CSS, then you have until **August 18th** to migrate your CSS. You can read about the features, migration tips, and full rollout schedule [here](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md).

#### Frequently Asked Questions (FAQ)

### I have migrated CSS and put a new URL under Customization, but the new Checkout is still not showing up, why?

[![Freemius Developer Dashboard Checkout Customization for disabling the legacy Checkout](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-enabling-phase2-checkout-everywhere-1024x630.png)](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-enabling-phase2-checkout-everywhere.png)

Please note that after you’ve migrated your CSS, you will need to clear the field of the “(Legacy) Custom Checkout CSS file” under the “Customization” section of the “Plans” page. Only then will the new checkout start showing up everywhere (on the Customer Portal and inside the WP SDK).

### Can I have more time to migrate my CSS?

From **August 18th**, we will set the new Checkout as default. However, you can force-load the old checkout with `checkout_style: 'legacy'` in the [JS configuration](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md). Please note that you will have until September 29th, after which we will completely remove the legacy Checkout. Also, you cannot force the legacy Checkout on the Customer Portal and inside the WP SDK.

### How can I have the option in the Checkout to switch to a monthly billing cycle?

We removed the billing cycle UI from the Checkout and have introduced the “Upsells” concept. Therefore, when the Checkout is loaded with an Annual billing cycle, we do not show the UI to downgrade to a Monthly billing cycle.

[![](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-monthly-switch-1024x465.png)](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-monthly-switch.png)

However, you can use the configuration option `show_monthly_switch` and set it to `true` to show it anyway.

### What are the new configurations available to tweak the Checkout UI

You can find them [here](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#fs-phase2-checkout) inside our JavaScript SDK documentation.