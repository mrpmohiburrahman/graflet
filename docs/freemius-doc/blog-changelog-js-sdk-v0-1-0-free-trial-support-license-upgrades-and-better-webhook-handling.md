[Changelog](https://freemius.com/changelog/) / JS SDK v0.1.0 — Free Trial Support, License Upgrades, and Better Webhook Handling

Today we’re releasing version `0.1.0` of our [JavaScript SDK](help-documentation-saas-sdk-js-sdk.md). We’ve received valuable feedback from our makers, and this release focuses on addressing those, fixing a few bugs, and improving cross-platform compatibility. To update, simply run:

```
npm install @freemius/sdk@latest
```

Please find the key changes below.

### Alternate Webhook Authentication Method

In some serverless or managed environments, the raw request body may get automatically altered (e.g., by trimming whitespace), which could cause signature verification failures.

To resolve this, we’ve introduced an **alternative webhook authentication method** that retrieves the event directly from the Freemius API using the `event ID` included in the webhook payload.

[![Alternate authentication of the Webhook JS SDK](https://freemius.com/blog/wp-content/uploads/2025/10/webhook-js-sdk-alternate-auth-1-1024x486.png)](https://freemius.com/blog/wp-content/uploads/2025/10/webhook-js-sdk-alternate-auth-1.png)

You can read more about the change in our [documentation](help-documentation-saas-sdk-js-sdk-webhooks.md#authentication-of-webhook-requests).

**Breaking Change:** The `freemius.webhook.createListener` method now accepts a configuration object.

### Checkout Upgrade Flow

You can now initiate **checkout flows for upgrading existing licenses** simply by passing a license ID. This simplifies handling upgrades for existing customers and makes the flow more consistent with the rest of the SDK.

[![Plan upgrade code from JS SDK](https://freemius.com/blog/wp-content/uploads/2025/10/checkout-support-license-upgrade-1024x421.png)](https://freemius.com/blog/wp-content/uploads/2025/10/checkout-support-license-upgrade.png)

Read our [documentation](help-documentation-saas-sdk-js-sdk-checkout.md#handling-upgrade-flow) to learn more about the upgrade flow.

**Breaking Changes:**

- `checkout.setSandbox()` now expects sandbox parameters (created via `await freemius.checkout.getSandboxParams()`).
- `setLicenseRenewal` has been renamed to `setLicenseUpgradeByKey` for clarity and consistency.

### Support for Free Trial in Checkout

We’ve added full support for [free trial](help-documentation-wordpress-free-trials.md) flows across both [**overlay**](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/) and [**hosted**](https://freemius.com/help/documentation/checkout/hosted-checkout/) checkout modes. This allows for smoother onboarding experiences for products offering free trials—without the need for separate integration logic.

You can read our [updated guide](help-documentation-saas-sdk-js-sdk-integration.md#sending-purchase-data-to-the-backend) for more details. The same integration flow now works seamlessly for free trials too.

We will update our entitlement guide supporting trials soon.

### Checkout Redirection Bug Fix

We identified an issue where the Checkout API processor was incorrectly validating the `action` URL parameter, and the `timingSafeEqual` function could throw errors on malformed signatures. Both issues have now been fixed to ensure smoother and more reliable redirection-based checkouts.

### Want to See it in Action?

Check out our live-coding webinar where we’ve built a SaaS app and integrate it with Freemius using the new **JavaScript SDK + React Starter Kit** – from setup to checkout in under 30 minutes. [Watch the webinar replay](https://www.youtube.com/live/4rEjDf8cdv4?si=sX7peUVdZCDWcLC7&t=103)