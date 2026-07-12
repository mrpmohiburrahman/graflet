---
title: "Checkout with the TypeScript Node.js SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/checkout/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 1126
---

The `freemius.checkout` namespace is designed to facilitate various methods for producing checkout options and links from the backend. It provides a set of methods to create and manage checkout processes for your product, supporting the generation of checkout links, overlay options, sandbox testing, and processing redirects.

## Creating Checkout Options or Links[​](#creating-checkout-options-or-links "Direct link to Creating Checkout Options or Links")

Use the `freemius.checkout.create` method to start creating a checkout option or link. The `create` method includes several convenient configuration options. For example:

```ts
const checkout = await freemius.checkout.create({
  user: { email: '[email protected]', name: 'Jane Doe' },
  planId: '1234',
});
```

This returns a `Checkout` instance, which you can further customize.

```ts
checkout.setAffiliate(1234).setTrial('paid').setCoupon({ code: 'SAVE10' });

const link = checkout.getLink();
console.log('Customized Checkout Link:', link);
```

### Generating Checkout Options[​](#generating-checkout-options "Direct link to Generating Checkout Options")

Use the `getOptions` method to generate checkout options for embedding in your application.

```ts
const options = checkout.getOptions();
console.log('Checkout Options:', options);
```

The checkout options are configuration objects that can be passed directly to the [Freemius Overlay Checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md). Here is an example demonstrating how to use them in frameworks like Next.js with our `CheckoutProvider` component, which is included in the [React Starter Kit](help-documentation-saas-sdk-react-starter.md).

pages/checkout.tsx (Server Component)

```tsx
import { CheckoutProvider } from '@/saas-starter/components/checkout-provider';
import { CheckoutPricingTable } from '@/components/checkout-pricing-table';
import { freemius } from '@/lib/freemius';

export default async function CheckoutPage() {
  const checkout = await freemius.checkout.create({
    user: { email: '[email protected]', name: 'Jane Doe' },
    planId: '1234',
  });

  // Pass the options to the client component
  return (
    <CheckoutProvider checkout={checkout.serialize()}>
      <CheckoutPricingTable />
    </CheckoutProvider>
  );
}
```

components/checkout-pricing-table.tsx (Client Component)

```tsx
'use client';

import { useCheckout } from '@/saas-starter/hooks/checkout';

export function CheckoutPricingTable() {
  const checkout = useCheckout();

  return <Button onClick={() => checkout.open()}>Subscribe Now</Button>;
}
```

warning

Please be mindful of how you pass the configuration object from the backend to the front end. The Freemius SDK holds sensitive information that should not be exposed to the client side. Always use the `.serialize()` method to filter out any sensitive data before passing it to the client.

### Generating Checkout Links[​](#generating-checkout-links "Direct link to Generating Checkout Links")

You can also generate a [direct checkout link](help-documentation-checkout-integration-hosted-checkout.md) using the `getLink` method:

```ts
const link = checkout.getLink();
console.log('Checkout Link:', link);
```

## Generating Sandbox Links or Options[​](#generating-sandbox-links-or-options "Direct link to Generating Sandbox Links or Options")

When testing your checkout flow, you can use sandbox mode to simulate transactions without affecting your live environment. To enable sandbox mode, use the `isSandbox` option in the `create` method.

```ts
const checkout = await freemius.checkout.create({
  isSandbox: true,
  user: { email: '[email protected]', name: 'Test User' },
  planId: '1234',
});
console.log('Sandbox Checkout Options:', checkout.getOptions());
```

### Retrieving Sandbox Parameters[​](#retrieving-sandbox-parameters "Direct link to Retrieving Sandbox Parameters")

For more advanced testing, you can retrieve sandbox parameters directly using the `getSandboxParams` method. This method generates a secure token for sandbox transactions.

```ts
const sandboxParams = await freemius.checkout.getSandboxParams();
checkout.setSandbox(sandboxParams);

console.log('Sandbox Link:', checkout.getLink());
```

note

Sandbox mode is intended for testing purposes only and should not be used in production environments.

## Processing Redirects[​](#processing-redirects "Direct link to Processing Redirects")

If you use the [hosted checkout](help-documentation-checkout-integration-hosted-checkout.md), you can use redirects to return users to your application after they complete the checkout process.

The Freemius SDK provides an easy way to handle these redirects using the `processRedirect` method. This method verifies the redirect URL and extracts relevant information about the checkout session.

```ts
const redirectInfo = await freemius.checkout.processRedirect(currentUrl);

if (redirectInfo) {
  console.log('Redirect Info:', redirectInfo);
  // Handle successful checkout
} else {
  console.error('Invalid or missing redirect info');
  // Handle errors or incomplete checkout
}
```

The method will return a `RedirectInfo` object only when it is able to verify the signature and URL parameters. The object will contain a `licenseId` property, which you can use to fetch the full [purchase details](help-documentation-saas-sdk-js-sdk-purchases.md).

### Fixing Proxy URLs[​](#fixing-proxy-urls "Direct link to Fixing Proxy URLs")

In most Node.js applications, the app itself typically uses URLs like `http://localhost:3000`, while it is served to the end user as `https://yourdomain.com` through some type of proxy. As a result, the app always sees its own URL as `http://localhost:3000` and not the actual URL the user is viewing.

This can cause issues when trying to verify redirects. Freemius signs the `https://yourdomain.com` URL, but your app is trying to verify the `http://localhost:3000` URL.

To solve this, the `processRedirect` method accepts an optional second parameter where you can pass the proxy URL. Here are some examples of how to do this in different frameworks.

- Express
- Next.js (App Router)

```ts
app.get('/process-purchase', function (req, res) {
  const currentUrl = `${req.protocol}://${req.get('host')}${req.originalUrl}`;
  const proxyUrl = 'https://yourdomain.com'; // The actual URL seen by the user

  const redirectInfo = await freemius.checkout.processRedirect(
    currentUrl,
    proxyUrl
  );

  if (redirectInfo) {
    console.log('Redirect Info:', redirectInfo);
    // Handle successful checkout
  } else {
    console.error('Invalid or missing redirect info');
    // Handle errors or incomplete checkout
  }
});
```

```ts
export async function GET(request: Request) {
  const currentUrl = request.url;
  const proxyUrl = 'https://yourdomain.com'; // The actual URL seen by the user

  const redirectInfo = await freemius.checkout.processRedirect(
    currentUrl,
    proxyUrl
  );

  if (redirectInfo) {
    console.log('Redirect Info:', redirectInfo);
    // Handle successful checkout
  } else {
    console.error('Invalid or missing redirect info');
    // Handle errors or incomplete checkout
  }
}
```

Under-the-hood the SDK takes care of parsing the URL and verifying the signature for you.

## Handling Upgrade Flow[​](#handling-upgrade-flow "Direct link to Handling Upgrade Flow")

Once users have an active subscription, you may want to provide an upgrade path to a higher‑tier plan.

To do this, you need to create an authorized checkout instance that includes the user's existing `licenseId`.

You can generate an upgrade checkout link or options by supplying the associated `licenseId` when creating the checkout instance.

```ts
// Get the stored entitlement of the user which would have the licenseId
const entitlement = getUserEntitlement();

const checkoutUpgrade = await freemius.checkout.create({
  licenseId: entitlement.licenseId,
  planId: 'upgraded-plan-id',
});

const upgradeLink = checkoutUpgrade.getLink();
```

This opens Freemius Checkout in the context of an upgrade, allowing the user to seamlessly upgrade the existing subscription.

Notice that, when upgrading, Checkout automatically handles proration and billing adjustments based on the user's current subscription. It also no longer asks for user details such as email or name, since these are already known from the existing subscription.

note

By default, Freemius restricts users to a single active subscription (unless you configure [otherwise](help-documentation-saas-saas-integration.md#restricting-or-relaxing-single-subscription-per-user)).

Using the React Starter Kit?

The [React Starter Kit](help-documentation-saas-sdk-react-starter.md) includes a [Customer Portal](help-documentation-saas-sdk-react-starter-components.md#customer-portal-component) the comes with built-in support for handling upgrades.

## Getting Pricing Information[​](#getting-pricing-information "Direct link to Getting Pricing Information")

To retrieve the pricing information for your product, you can use the `freemius.pricing` namespace. This is useful for displaying pricing tables or options on your site.

```ts
async function fetchPricing() {
  return await freemius.pricing.retrieve();
}
```

The [React Starter Kit](help-documentation-saas-sdk-react-starter-components.md#subscription-plans-table) can be fed this data to display a pricing table.