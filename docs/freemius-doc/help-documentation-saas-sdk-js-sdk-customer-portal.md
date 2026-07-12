---
title: "Implementing your own Customer Portal inside your SaaS with Freemius JS SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/customer-portal/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 742
---

Freemius JS SDK comes with built-in capability to help you create your own customer portal inside your SaaS application. This allows your customers to manage their subscriptions, billing information and download invoices directly from your platform.

note

If you're looking for a pre-built UI and front-end application that you can simply drop into your SaaS, check out our [React Starter Kit](help-documentation-saas-sdk-react-starter.md). It includes all the logic and UI components you need to get started quickly.

**It also uses shadcn to install components, so you can easily customize them.** You can also follow our [Starter Kit API Endpoing Guide](help-documentation-saas-sdk-js-sdk-starter-kit-api-endpoints.md) to learn more.

In this guide, we will show you how to implement your own version using the Freemius JS SDK. This is useful if your front-end stack is not React, or if you want full control over the UI and UX of your customer portal.

## How the Customer Portal Works[​](#how-the-customer-portal-works "Direct link to How the Customer Portal Works")

The process works as follows:

1. You already know the Freemius User ID of the customer (e.g., from [processing a purchase](help-documentation-saas-sdk-js-sdk-purchases.md)).
2. You have an **API endpoint** in your SaaS application that listens for requests from the customer portal.
3. You call the `freemius.customerPortal.retrieveData` method with the User ID and the endpoint URL.
4. The SDK returns data with secure signed URLs that the customer portal can use to fetch additional data (e.g., invoices, licenses, subscriptions).

## Retrieving Customer Data[​](#retrieving-customer-data "Direct link to Retrieving Customer Data")

The `freemius.customerPortal` namespace provides methods to retrieve customer data, such as subscriptions, licenses, and invoices.

```typescript
const userId = '5723112'; // Replace with your actual user ID
const primaryLicenseId = '1770522'; // Replace with your actual primary license ID if needed
const portalData = await freemius.customerPortal.retrieveData({
  userId,
  endpoint: 'https://my-saas.com/api/portal',
  primaryLicenseId,
  sandbox: true, // Optional; set to true if you want to use the sandbox environment
});

console.log('Portal Details:', portalData);
```

Here is what the options mean:

1. `userId`: The Freemius ID of the user whose data you want to retrieve. This is a required field.
2. `endpoint`: The API endpoint for which secure, authenticated signed URLs will be created. The customer portal will send requests to this endpoint to fetch additional data (e.g., invoices, licenses, subscriptions). This should be an endpoint in your SaaS application that you implement to handle these requests.
3. `primaryLicenseId`: (Optional) The ID of the primary license, in case your software has a pricing model that supports multiple active subscriptions. If not provided, the first active subscription will be used instead.
4. `sandbox`: (Optional) Set to `true` if you want to use the sandbox environment for testing purposes. Defaults to `false`.

Additionally, you can use the `retrieveDataByEmail` method to fetch data using the customer's email address instead of their user ID.

```typescript
const portalData = await freemius.customerPortal.retrieveData({
  email: '[email protected]',
  endpoint: 'https://my-saas.com/api/portal',
});

console.log('Portal Details:', portalData);
```

warning

It is not recommended to fetch user information by `email`, as it is slower. You already store the Freemius User ID while [processing purchase information](help-documentation-saas-sdk-js-sdk-purchases.md), so use that instead.

## Implementing the API Endpoint[​](#implementing-the-api-endpoint "Direct link to Implementing the API Endpoint")

Using `freemius.customerPortal.request`, you can implement the API endpoint that the customer portal will use to fetch additional data. Here is an example for a Next.js API route:

app/api/portal/route.ts

```typescript
const processor = freemius.customerPortal.request.createProcessor({
  getUser: getFsUser, // A function that returns the Freemius User ID of the currently logged-in user
  portalEndpoint: process.env.NEXT_PUBLIC_APP_URL! + '/api/portal',
});

export { processor as GET, processor as POST };
```

The `createProcessor` method returns a function that you can use as the handler for both `GET` and `POST` requests to your API endpoint.

For other fetch-compliant environments (e.g., Cloudflare Workers), you can use the `process` method instead:

workers/portal.ts

```typescript
export default {
  async fetch(request: Request): Promise<Response> {
    return await freemius.customerPortal.request.process(
      {
        getUser: getFsUser, // A function that returns the Freemius User ID of the currently logged-in user
        portalEndpoint: 'https://my-saas.com/api/portal',
      },
      request
    );
  },
};
```

note

Compatibility layers for other environments (e.g., Express, Koa, etc.) are coming soon.

## Rendering the UI[​](#rendering-the-ui "Direct link to Rendering the UI")

We will update our documentation with detailed guides on how to create a custom UI based on the portal data.

In the meantime, we recommend checking out our [React Starter Kit](help-documentation-saas-sdk-react-starter.md), which provides a complete implementation of the customer portal UI using React and shadcn components. You can use it as a reference to implement your own UI in your preferred front-end framework.