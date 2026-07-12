We are gradually rolling out a new design for the Freemius Checkout. The new design applies to both the dialog mode and the embedded WP Admin (aka dashboard) mode. Below, we provide a breakdown of the gradual rollout plan and our roadmap.

[![Freemius Checkout Redesigning Phase 1](https://freemius.com/blog/wp-content/uploads/2023/12/new-checkout-design.png)](https://checkout.freemius.com/?mode=dialog&guid=8460bf83-6512-e857-e303-4c091b1e6775&plugin_id=311&plan_id=437&public_key=pk_a42d2ee6de0b31c389d5d11e36211&s_ctx_ts=1626969480&sandbox=5548f3de8a7e02a838427c549a588644&name=Freemius%20Checkout%20Awesome%20Plugin%20Pro&hide_billing_cycles=1&checkout_style=next)

[View a Live Demo](https://checkout.freemius.com/?mode=dialog&guid=8460bf83-6512-e857-e303-4c091b1e6775&plugin_id=311&plan_id=437&public_key=pk_a42d2ee6de0b31c389d5d11e36211&s_ctx_ts=1626969480&sandbox=5548f3de8a7e02a838427c549a588644&name=Freemius%20Checkout%20Awesome%20Plugin%20Pro&hide_billing_cycles=1&checkout_style=next)

### Gradual rollout

We deployed the new checkout design on 18 December 2023. Initially, it will be in beta mode for a week. After that, we will roll it out for a wider user base.

#### 1st Week – 18 December 2023

- The existing style will keep on showing up as default.
- **But** you will have the opportunity to test it (more on this later).

#### 3rd Week – 1 January 2024

- Starting from 1 January 2024, the new checkout design will become the default.
- However, this will only apply to the legacy checkout if you have custom CSS.
- If you have custom CSS for both the legacy and the new checkout, the new checkout will show up by default.

Developers who use custom CSS are given two extra weeks of grace to update their code.

#### 5th Week – 14 January 2024

- From 14 January 2024, the new checkout will become the default and the legacy checkout will not be shown.
- You will, however, have the option to keep using the legacy checkout for some more time.

### Custom CSS migration

Starting from the 1st week of the gradual rollout, you’ll notice that under Plans &gt; Customization, the CSS URL you had has been put under the **(Legacy) Custom Checkout CSS file** field and the regular **Custom Checkout CSS file** field is now empty.

[![Freemius Checkout CSS migration on the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2023/12/freemius-checkout-css-migration-on-dev-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2023/12/freemius-checkout-css-migration-on-dev-dashboard.png)

The CSS URL under the **Legacy** field will now only apply to the legacy checkout. To style the new checkout, you have to create another custom CSS file under your server and put it in the first field.

This way, we ensure you don’t accidentally break the new checkout design by including the incorrect CSS file.

The new design comes with several CSS variables that you can use to quickly change the colors and appearance. Please read the [Checkout CSS customization](https://freemius.com/go/checkout-css-customization/) documentation for more information.

### Previewing or using the new checkout during the beta phase

You simply need to add `checkout_style=next` to the URL query parameter. So, if your checkout URL is:

```
https://checkout.freemius.com/mode/dialog/plugin/_plugin_id_/plan/_plan_id_/
Change it to:
https://checkout.freemius.com/mode/dialog/plugin/_plugin_id_/plan/_plan_id_/?*checkout_style=next*
For the JS integration code, include checkout_style: 'next' when doing the configuration.
const handler = FS.Checkout.configure({
        plugin_id:  'plugin_id',
        plan_id:    'plan_id',
        public_key: 'pk_public_key',
        // Force load the new checkout style.
        checkout_style: 'next'
});

It’s also possible to generate code and links from the Developer Dashboard. Kindly navigate to Plans and enable the toggle Use new checkout style in code and preview links.

Now, clicking the Checkout Link or Get Checkout Code buttons will ready the URL or the code for you.
Forcing the Legacy Checkout after 1st week

If you need more time to migrate the CSS, you can force the checkout to always load in legacy mode.

Make sure checkout_style=legacy is used as a URL query parameter.
While using the JS integration, make sure to pass checkout_style: 'next' as a configuration option.

But please be aware that we do not intend to keep the legacy checkout for long. We therefore urge you to migrate your CSS ASAP.
WP Admin Embedded Checkout

The checkout that we embed inside WordPress Admin Dashboard, will strictly follow the rollout plan. You won’t be able to force-use the new or the legacy checkout.
Feature improvements

Apart from the style and appearance changes, we’ve improved many of the UI/UX components. Here are some of them.
Improved optional inputs


The license key, coupon, and VAT ID fields have been redesigned to have a better UI/UX than before.
Better UI in the review step


When reviewing before the final payment, we now do not show the user form. This helps to reduce the amount of information shown on the page.
Improvements to the meta dropdowns

The language and currency selectors have been pushed to the bottom footer to prevent distractions.

The UX of the dropdowns has also been improved.
Dunning app improvement

We’ve also reskinned the dunning app to make it look on par with the checkout.

Please note that the dunning app will not retain its legacy style during any phase of deployment.
Future roadmap

This is only Phase 1 of the checkout redesign process. In Phase 2, which we are going to start working on very soon, we intend to:

Change the checkout to two columns, and
Continue to simplify the UI and the UX

The result would look like this:

Any CSS changes you make during this first phase will be majorly backward compatible. We urge you to only work with CSS variables for now to minimize the chances of it breaking in the future.

                                                        
```