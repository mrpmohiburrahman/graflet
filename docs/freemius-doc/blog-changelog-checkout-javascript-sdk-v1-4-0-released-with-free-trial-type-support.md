[Changelog](https://freemius.com/changelog/) / Checkout JavaScript SDK v1.4.0 Released with Free Trial Type Support

We are releasing a new version **1.4.0** of our [Checkout JavaScript SDK](https://www.npmjs.com/package/@freemius/checkout). This update introduces proper type support for [**Free Trial**](help-documentation-wordpress-free-trials.md) flows.

Previously, in the [`success`](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/#success) callback, you couldn’t access structured data when a free trial was triggered. With this release, the data is now available under the `data.trial` property with full type annotations, making it easier to build consistent post-trial experiences.

[![Checkout JS with success callback](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-checkout-js-sdk-1024x698.png)](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-checkout-js-sdk.png)

Please note that this enhancement applies only to free trials. For paid trials, you should continue using the `data.purchase` property.

If you’re using the CDN version, no action is required — the update is already live. For NPM installations, please upgrade by running:

```
npm install @freemius/checkout@latest
```

For more details, please visit our [GitHub repository](https://github.com/Freemius/freemius-checkout-js/).