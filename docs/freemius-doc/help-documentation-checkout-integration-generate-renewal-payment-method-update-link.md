---
title: "Generating License Renewal & Payment Method Update Links"
url: "https://freemius.com/help/documentation/checkout/integration/generate-renewal-payment-method-update-link/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:38+06:00"
word_count: 249
---

Our platform provides a [Customer Portal](help-documentation-users-account-management.md) from where your customers can self-serve to renew expired licenses or update billing methods. However, sometimes sharing a direct link helps in quicker conversion.

## No Code Link Generation[​](#no-code-link-generation "Direct link to No Code Link Generation")

To help you quickly generate such links without any code:

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the **Products** tab and select your product.
3. Go to the ***Licenses*** section.
4. Search for the relevant license using the customer's license ID or key.
5. Scroll horizontally to license row and click the 3-dot option icon to expose the available actions.
6. Click on the **Copy Renewal Link** button that will copied to your clipboard.
7. Share the link with your customer.

When the customer clicks the link, a secure page will open the checkout with the license key prefilled for the customer to renew their license or update their payment method.

## Generate Links with API[​](#generate-links-with-api "Direct link to Generate Links with API")

You can automate the link generation using the API. There are a variety of parameters with which you can specify new plans, quota or billing cycles (See the [API endpoint](https://docs.freemius.com/api/licenses/generate-upgrade-link) documentation).

If you skip all those parameters, then a manual renewal link will be generated instead.

```http
POST /v1/products/{product_id}/licenses/{license_id}/checkout/link.json HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: Bearer 123
Host: api.freemius.com
Content-Length: 127

{}
```

Using our JS SDK?

If you're using our [JS SDK](help-documentation-saas-sdk-js-sdk.md), please check the [retrieving upgrade authorization](help-documentation-saas-sdk-js-sdk-api.md#retrieving-upgrade-authorization) method.