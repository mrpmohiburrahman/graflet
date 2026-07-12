[Changelog](https://freemius.com/changelog/) / Skip Confirmation Dialog in Overlay Checkout

This week we are introducing a new feature, especially tailored for SaaS makers. When using the Overlay Mode of our Checkout, you’d often want to hook into the [`success`](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/#success) callback to handle post-processing. In this UX flow, it often makes less sense to display the final success dialog from Checkout.

[![Freemius Checkout Success Dialog](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-success-dialog-1024x700.png)](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-success-dialog.png)

To address this, we’ve added an option to skip it. Simply head to **Plans → Customization** and enable the *“Skip confirmation dialog after purchase”* setting.

[![Skip Confirmation Dialog on Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-checkout-skip-confirmation-1024x567.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-checkout-skip-confirmation.png)

Once enabled, the dialog will be disabled by default for all overlay checkouts. Here’s a conceptual demo video showing how an application can hook into the `success` callback to show confettis and toast.

[https://freemius.com/blog/wp-content/uploads/2025/09/checkout-skip-dialog-demo.mp4](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-skip-dialog-demo.mp4)

However, you can still use the `show_confirmation_dialog` parameter to control it on a case-by-case basis. For more details, please read our documentation [here](https://freemius.com/help/documentation/checkout/customizing-confirmation-dialog/#skipping-the-dialog-in-overlay-mode).