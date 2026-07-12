[Changelog](https://freemius.com/changelog/) / Easier Testing for Custom Payment Recovery URL Integration

Not [so long ago](blog-changelog-better-and-embeddable-payment-recovery-or-dunning-experience.md), we introduced a feature to set up a [custom recovery URL](help-documentation-marketing-automation-dunning-failed-payments.md#customizing-payment-method-update-links) for payment recovery. This helps prevent confusion among buyers who might otherwise see a different domain when updating their payment methods.

The process required going to the [Developer Dashboard](https://dashboard.freemius.com), setting up a URL, and ensuring that the Freemius [Checkout JS SDK](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/) was included on that webpage.

However, based on feedback from our makers, we realized that testing this integration wasn’t straightforward. Since this flow involves recovering failed subscriptions, it’s only natural that our makers wanted an easy way to validate it.

[![Test button for payment recovery custom URL](https://freemius.com/blog/wp-content/uploads/2025/11/payment-recovery-flow-ux-1024x883.png)](https://freemius.com/blog/wp-content/uploads/2025/11/payment-recovery-flow-ux.png)

To address this, we’ve added a new **“Test Payment Recovery”** button in the UI. Clicking it will open the configured URL, automatically triggering the Freemius Checkout with a dummy payment recovery flow.

[![Freemius Checkout opened in mocked dunning flow](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-checkout-dunning-mock-947x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-checkout-dunning-mock.png)

If the test checkout appears as expected, you can be confident that your integration works correctly.

Regardless of whether you’ve already set it up, head over to **Developer Dashboard → Plans → Customization** to try it out.