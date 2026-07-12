---
title: "Customizing the After Purchase Confirmation Dialog"
url: "https://freemius.com/help/documentation/checkout/customization/customizing-confirmation-dialog/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 388
---

By default, Freemius provides a straightforward confirmation dialog after a successful purchase.

It displays a generic message that is relevant to most use cases. However, you can customize the content of this dialog to better fit your product and audience.

## Customizing the Confirmation Dialog[​](#customizing-the-confirmation-dialog "Direct link to Customizing the Confirmation Dialog")

Go to the **Plans** → **Customization** tab in your [Freemius Developer Dashboard](https://dashboard.freemius.com/). From there, find the **Checkout Confirmation Dialog** section and enable the **Customize after-purchase-dialog** switch to reveal the customization options.

You can now customize the following options:

- **Title**: The main title of the dialog. This will replace the **Subscription was successful** text.
- **Message**: The main message of the dialog. You can use some formatting and special placeholders. See the Developer Dashboard UI for all available options.
- **Button Text**: Customize the text of the button that closes the dialog. By default, it is **Got it**.
- **Button Link**: You can optionally set a URL that the button will link to. This is useful if you want to direct users to a specific page after purchase, such as a welcome page or a download page.

Redirecting Buyers

If you are using the [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md), you can set a redirect URL. In this case, the entire dialog will be skipped, and the user will be redirected to the specified URL immediately after purchase.

## Skipping the Dialog in Overlay Mode[​](#skipping-the-dialog-in-overlay-mode "Direct link to Skipping the Dialog in Overlay Mode")

You also have the option to completely skip the confirmation dialog in [Overlay Mode](help-documentation-checkout-integration-freemius-checkout-buy-button.md). Under the same configuration section, enable the **Skip confirmation dialog after purchase** option.

Once this option is enabled, the dialog will be skipped, and the user will be returned to your website immediately after purchase. You must hook into the `success` event of the Checkout to process the purchase.

```js
checkout.open({
  success(data) {
    console.log('Purchase was successful!', data);
    // Handle the successful purchase here, for example show some confirmation UI.
  },
});
```

If you want to display a confirmation dialog for some purchases but not for others, you can use the `show_confirmation_dialog` option when opening the checkout.

```js
checkout.open({
  show_confirmation_dialog: true,
});
```

We recommend enabling this option in the UI for the majority of your purchases and only disabling it for specific cases where you want to handle the confirmation differently.