---
title: "Creating Webhook Listeners with Freemius JS SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/webhooks/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 720
---

The Freemius SDK provides a robust system to listen and process webhook events from the Freemius platform. This guide explains how to set up, configure, and process webhooks in various environments, including Next.js, Node.js, and serverless platforms.

note

Check out the [installation guide](help-documentation-saas-sdk-js-sdk-installation.md) if you haven't set up the SDK yet.

## Create a Webhook Listener[​](#create-a-webhook-listener "Direct link to Create a Webhook Listener")

To create a webhook listener, use the `freemius.webhook.createListener` method.

```typescript
const listener = freemius.webhook.createListener();
```

You can create multiple listeners if you want to handle different sets of events separately. However for most use cases, a single listener is sufficient.

## Register Event Handlers[​](#register-event-handlers "Direct link to Register Event Handlers")

The `listener` object exposes an `on` method to register event handlers for specific Freemius events. Each handler receives the event data as a parameter.

```typescript
listener.on('license.created', async ({ objects: { license } }) => {
  await syncLicenseFromWebhook(license);
  console.log('License created:', license);
});

listener.on(
  'subscription.renewal.failed',
  async ({ objects: { subscription } }) => {
    await sendRenewalFailureEmail(subscription);
    console.log('Subscription renewal failed:', subscription);
  }
);
```

The payload of the callback function will be strictly typed based on the event type, providing you with full TypeScript support. You can register multiple handlers for the same event if needed.

tip

You can use TypeScript IntelliSense to explore all available methods on the `listener` object.

Handling Multiple Events

For events that has same payload, you can pass an array of event names to register the same handler for multiple events:

```typescript
listener.on(
  [
    'license.created',
    'license.extended',
    'license.shortened',
    'license.updated',
    'license.cancelled',
    'license.expired',
    'license.plan.changed',
  ],
  async ({ objects: { license } }) => {
    await syncLicenseFromWebhook(license);
    console.log('License updated/activated/deactivated:', license);
  }
);
```

## Process Webhook Requests[​](#process-webhook-requests "Direct link to Process Webhook Requests")

Once the listener is set up and handlers are registered, you need to process incoming webhook requests. The SDK provides two methods for this: `processFetch` for environments that support the Fetch API (like Next.js or Cloudflare Workers), and `processNodeHttp` for Node.js HTTP servers.

#### Using the Fetch API (e.g., Next.js, Cloudflare Workers)[​](#using-the-fetch-api-eg-nextjs-cloudflare-workers "Direct link to Using the Fetch API (e.g., Next.js, Cloudflare Workers)")

The `processFetch` method processes requests in environments that support the Fetch API:

```typescript
export async function POST(request: Request): Promise<Response> {
  return await webhookService.processFetch(listener, request);
}
```

You can use it in Next.js API routes, serverless functions, or any environment that supports the Fetch API.

Easy Next.js Integration

In Next.js, you can reduce boilerplate by using the `createRequestProcessor` method:

```typescript
const processor = freemius.webhook.createRequestProcessor(listener);

export { processor as POST };
```

For a more framework-specific example, see the [full Next.js integration guide](help-documentation-saas-sdk-framework-nextjs.md).

#### Using Node.js HTTP[​](#using-nodejs-http "Direct link to Using Node.js HTTP")

The `processNodeHttp` method processes requests in a Node.js HTTP server:

```typescript
import { createServer } from 'http';

const server = createServer(async (req, res) => {
  if (req.url === '/webhook') {
    await webhookService.processNodeHttp(listener, req, res);
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

## Authentication of Webhook Requests[​](#authentication-of-webhook-requests "Direct link to Authentication of Webhook Requests")

The SDK automatically verifies the [authenticity of incoming webhook requests](help-documentation-saas-events-webhooks.md#validating-webhook-signatures) using the signature sent in the `x-signature` header. This ensures that both the integrity and origin of the requests are validated.

However, in some environments—especially managed serverless platforms—the platform may not provide direct access to the raw request body, which is required for signature verification. In such cases, you can use the alternative authentication method by verifying the request against the Freemius API.

```ts
import { WebhookAuthenticationMethod } from '@freemius/sdk';

// This will use the Freemius API to authenticate the webhook request
const listener = freemius.webhook.createListener({
  authenticationMethod: WebhookAuthenticationMethod.Api,
});
```

When using this authentication method, we recommend implementing additional security measures, such as providing a secret token in the webhook URL and validating it in your listener.

Here is an example of how to implement this:

```ts
export async function POST(request: Request): Promise<Response> {
  const url = new URL(request.url);
  const secretToken = url.searchParams.get('token');

  // Validate the secret token
  if (secretToken !== process.env.WEBHOOK_SECRET_TOKEN) {
    return new Response('Unauthorized', { status: 401 });
  }

  return await webhookService.processFetch(listener, request);
}
```

Make sure to configure the webhook in the Freemius Dashboard using the URL with the token:

```text
https://your-domain.com/webhook?token=your_secret_token
```

Note that the alternative authentication method may introduce additional latency due to the API call; use it only when necessary.