---
title: "Framework Integration Guide for SaaS Applications"
url: "https://freemius.com/help/documentation/saas-sdk/framework/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 297
---

Our [JS SDK](help-documentation-saas-sdk-js-sdk.md) is written in a framework-agnostic way using standard APIs such as [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response).

This makes the SDK compatible with modern frameworks and runtimes such as [Next.js](https://nextjs.org/), [Hono](https://hono.dev/), [Deno](https://docs.deno.com/runtime/fundamentals/http_server/), and [Bun](https://bun.com/docs/api/http), as well as serverless platforms like [Vercel](https://vercel.com/docs/concepts/functions/serverless-functions) and [Cloudflare Workers](https://developers.cloudflare.com/workers/).

Refer to the [integration guide](help-documentation-saas-sdk-js-sdk-integration.md) for a general overview of how to integrate the SDK with your SaaS application.

We also provide a [React Starter Kit](help-documentation-saas-sdk-react-starter.md) that includes components for checkout, pricing tables, and customer portals etc.

note

Other Node.js frameworks such as Express, Koa, and Fastify can also be used with the SDK. However, they may require additional polyfills or middleware to fully support the web standard APIs used by the SDK. We plan to add adapters for these frameworks in the future.

In this section, we provide specific guides for integrating the SDK with popular frameworks. Each guide covers the necessary steps to:

1. Set up the SDK and the Starter Kit
2. Protect or paywall features in your SaaS application
3. Implement common use cases such as creating checkouts, rendering the customer portal, and handling webhooks

## Common Integration Patterns[​](#common-integration-patterns "Direct link to Common Integration Patterns")

Every integration guide will cover the following common patterns:

1. Two API endpoints at `/api/checkout` and `/api/portal` to facilitate checkout and customer portal operations
2. One webhook listener endpoint at `/webhook` to handle incoming webhook requests from Freemius
3. Starter Kit component to create paywalls and render pricing tables
4. Starter Kit component to render the customer portal

At the end of every guide, you will have a fully monetized SaaS application with Freemius.

Framework Not Listed?

We recommend checking out the [General Integration Guide](help-documentation-saas-sdk-js-sdk-integration.md), [Starter Kit API Endpoints](help-documentation-saas-sdk-js-sdk-starter-kit-api-endpoints.md) and [React Starter Kit](help-documentation-saas-sdk-react-starter.md) documentation to help you integrate the SDK with your preferred framework.