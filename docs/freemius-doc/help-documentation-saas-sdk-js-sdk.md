---
title: "JavaScript Software Development Kit for Freemius"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 180
---

Freemius offers a JavaScript (JS) SDK written in TypeScript to help you integrate Freemius into your SaaS applications. At a glance it has the following features:

- **API Client**: A fully typed API client to interact with the [Freemius API](https://docs.freemius.com/api).
- **Checkout**: Easily create and manage Checkout [options](help-documentation-checkout-integration-freemius-checkout-buy-button.md) and [links](help-documentation-checkout-integration-hosted-checkout.md) for your application. Also has convenience methods to process redirections from the [Hosted Freemius Checkout](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase).
- **Webhooks**: Create webhook listeners for specific events and process incoming [webhook requests](help-documentation-saas-events-webhooks.md) from Freemius.
- **Pricing**: Easily retrieve data for custom pricing tables within your software.
- **Purchase**: Securely process and manage purchases made through Freemius.

The SDK works for any JavaScript runtime platform including [Node.js](https://nodejs.org/en), [Bun](https://bun.com/), [Deno](https://deno.com/) etc. Please read the guides to get started.

Backend Use Only

The Freemius JS/TS SDK is intended for **backend use only**. It should not be used in frontend or client-side applications (browsers), as it requires access to sensitive credentials such as the Secret Key and Bearer Token. Exposing these credentials in a client-side environment can lead to security vulnerabilities and unauthorized access to your Freemius account.