Freemius provides a built-in payment recovery system, commonly known as "dunning," to handle failed payments for subscriptions and one-time purchases. This system automatically retries failed payments and notifies customers about the status of their payments via email.

Customers have an easy option to update their payment details directly from the email notifications they receive, which helps reduce churn and improve customer retention.

Depending on the payment method used and the type of purchase, the dunning process may vary slightly. Below is an overview of how Freemius handles dunning for different scenarios.

## Subscriptions[​](#subscriptions "Direct link to Subscriptions")

### Initial Payment[​](#initial-payment "Direct link to Initial Payment")

When a user subscribes to a paid plan for a plugin or theme, Freemius immediately attempts to process the initial payment. If the initial payment cannot be processed for any reason, the checkout will fail and the user will receive a corresponding message.

### Renewals[​](#renewals "Direct link to Renewals")

If a renewal payment fails, Freemius will retry PayPal and credit card payments according to the following schedule:

**1st failed attempt:**

- Send a failure email to the customer.
- Retry 1 day after the 1st failed attempt.

**2nd failed attempt:**

- Send a failure email to the customer.
- Retry 3 days after the previous failed attempt.

**3rd failed attempt:**

- Send a failure email to the customer.
- Retry 5 days after the previous failed attempt.

**4th failed attempt and final:**

- Cancel the subscription.
- Cancel the associated license.
- Send a cancellation email to the customer.
- Happens 5 days after the 3rd attempt.

## One-Time Purchase[​](#one-time-purchase "Direct link to One-Time Purchase")

When a user purchases a plugin or theme using Freemius, the system immediately attempts to process the payment. If the payment cannot be processed for any reason, the checkout will fail and the user will receive a corresponding message.

## Customizing Payment Method Update Links[​](#customizing-payment-method-update-links "Direct link to Customizing Payment Method Update Links")

Emails sent to customers now include a direct link to the Freemius Checkout application. Some buyers may find it confusing to receive an email from your brand or website and yet are redirected to a third-party domain, this could be mistaken for phishing.

To avoid this, you can set a custom recovery URL on your own website. To do so,

1. Go to the **Plans** → **Customization** tab in your Freemius dashboard.
2. Enable the **Customize Payment Recovery URL** option.
3. Then, enter the URL of your website where you want to redirect customers for payment recovery.

Be sure to include the following script on the page you set as the custom recovery URL:

```
<script src="https://checkout.freemius.com/js/v1/"></script>
```

Now, our system will send customers to your custom URL instead of the default Freemius Checkout URL when they need to update their payment details.

warning

If you do not include the script tag in your custom recovery URL, the Freemius Checkout modal will not work, and customers will not be able to update their payment details. This will lead to a poor user experience and result in lost revenue.

### Listening for Events[​](#listening-for-events "Direct link to Listening for Events")

To listen for events related to the payment recovery process, you can add the event listeners to the `window.FS.paymentMethodUpdateEvents` object **before adding the script tag**.

```
<script>
  window.FS = window.FS || {};
  window.FS.paymentMethodUpdateEvents = {
    track(event, data) {
      console.log('Payment Method Update Event:', data, event);
    },
    success(data) {
      console.log('Payment Method Update Success', data);
    },
  };
</script>
<script src="https://checkout.freemius.com/js/v1/"></script>
```

All [official event listeners](help-documentation-checkout-features-tracking-analytics.md) are supported.

tip

If you're using the npm package to bundle the Freemius JS SDK within your application, then please refer to our documentation at [GitHub](https://github.com/Freemius/freemius-checkout-js/?tab=readme-ov-file#payment-update-flow-or-dunning).