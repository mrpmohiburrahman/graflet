[Changelog](https://freemius.com/changelog/) / New API Endpoint to Generate License Upgrade Links

We’ve rolled out a new [API endpoint](https://freemius.com/help/documentation/api/) that allows you to automatically generate Freemius Checkout links for upgrading a license.

While our [Customer Portal](help-documentation-users-account-management.md) already handles license upgrades internally, this endpoint is especially useful for SaaS makers who want to implement their own billing experience.

You can read more about the endpoint in our [documentation](https://freemius.com/help/documentation/api/operations/licenses/generate-upgrade-link). In a nutshell, from your product’s scope, make a request like:

```
POST /v1/products/{product_id}/licenses/{license_id}/checkout/link.json HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: Bearer 123
Host: api.freemius.com
Content-Length: 127

{
  "plan_id": "planID",
  "billing_cycle": "annual",
  "quota": 1,
  "currency": "usd"
}
```

The response will include:

1. `url` – The URL of the Hosted Checkout
2. `settings` – Configuration parameters you can pass directly to the Checkout JS SDK
3. `expires` – The datetime when the URL will expire

We hope this new endpoint, along with [Checkout Redirection](blog-changelog-new-feature-redirect-after-successful-checkout.md) and [Webhooks](help-documentation-marketing-automation-events-webhooks.md), helps streamline your SaaS integration. As we continue improving the SaaS developer experience, please reach out via support with any questions or feature suggestions.