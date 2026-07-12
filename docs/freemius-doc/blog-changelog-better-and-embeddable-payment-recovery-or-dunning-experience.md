[Changelog](https://freemius.com/changelog/) / Better and Embeddable Payment Recovery or Dunning Experience

This week we are releasing a milestone project. Freemius already had a solid payment recovery (dunning) experience where our system would automatically send emails to buyers when a subscription renewal failed. These emails included a link where the buyer could promptly update their credit card.

[![Freemius Dunning or Payment Recovery Flow](https://freemius.com/blog/wp-content/uploads/2025/08/dunning-email-credit-card-1024x718.png)](https://freemius.com/blog/wp-content/uploads/2025/08/dunning-email-credit-card.png)

However, we wanted to elevate the experience by taking it several steps further:

1. Offer the same polished experience as our Checkout, making customers “feel at home” when updating their payment method.
2. Support switching payment gateways (e.g., between PayPal, Card, or iDEAL) within the same flow.
3. Allow makers to embed the payment recovery flow within their own website—just like our Checkout—boosting conversion rates by keeping buyers on a familiar, trusted brand domain instead of the Freemius subdomain.

Today, we’re excited to announce that all these improvements are now live.

[![New Payment Recovery UI by Freemius](https://freemius.com/blog/wp-content/uploads/2025/08/dunning-checkout-state-1024x878.png)](https://freemius.com/blog/wp-content/uploads/2025/08/dunning-checkout-state.png)

Our new payment recovery flow presents a clear UI where buyers can seamlessly switch between various payment gateways. No additional configuration is required on your end.

### Setting up custom recovery URL

From the Developer Dashboard → Plans → Customization page, you can now set a custom payment recovery URL.

[![Enable custom payment recovery URL from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/08/enable-custom-payment-recovery-flow-url-1024x982.png)](https://freemius.com/blog/wp-content/uploads/2025/08/enable-custom-payment-recovery-flow-url.png)

When configured, our system will link to your URL, and the Checkout JS snippet will automatically trigger the recovery flow. More details are available in our [documentation](help-documentation-marketing-automation-dunning-failed-payments.md).

### Note for the Checkout JS SDK

If you’re using the CDN method, simply ensure the script tag is included in the page, and everything else will work automatically.

```
<script src="https://checkout.freemius.com/js/v1/"></script>
```

If you’re using the `@freemius/checkout` npm package, please update to the latest version `1.3.0` and follow the [instructions in our GitHub repository](https://github.com/Freemius/freemius-checkout-js/tree/develop?tab=readme-ov-file#payment-update-flow-or-dunning).