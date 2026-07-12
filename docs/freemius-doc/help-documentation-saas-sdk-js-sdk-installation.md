---
title: "Installation Guide for the Freemius JS/TS SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/installation/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 412
---

This installation guide will help you get up and running with the Freemius TypeScript/JavaScript SDK in your SaaS application.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- Node.js, version 20 or higher or other platforms like Deno or Bun.
- A package manager: npm, yarn, or pnpm

We also recommend using TypeScript for type safety and an improved development experience; however, you can use the SDK in plain JavaScript projects as well.

You will also need to have a Freemius account and a product set up. If you have not done so already, please follow the [getting started guide](help-documentation-saas-saas-plans-pricing.md).

note

Support for Bun and Deno is experimental. Please [report any issues](https://github.com/Freemius/freemius-js/issues) you encounter.

## Installation[​](#installation "Direct link to Installation")

Depending on your preferred package manager, run one of the following commands in your project directory:

- npm
- Yarn
- pnpm
- Bun

```bash
npm install @freemius/sdk @freemius/checkout zod
```

```bash
yarn add @freemius/sdk @freemius/checkout zod
```

```bash
pnpm add @freemius/sdk @freemius/checkout zod
```

```bash
bun add @freemius/sdk @freemius/checkout zod
```

note

- [`@freemius/checkout`](https://github.com/Freemius/freemius-checkout-js/) is required for the checkout generation feature. You can also use it on your frontend to render the checkout modal.
- [`zod`](https://zod.dev/) is required for schema validation.

## Retrieving Keys from the Developer Dashboard[​](#retrieving-keys-from-the-developer-dashboard "Direct link to Retrieving Keys from the Developer Dashboard")

Next, please head over to the [Developer Dashboard](https://dashboard.freemius.com/) and navigate to the **Settings** page for your product and selec the **API & Keys** tab.

Now scroll down to the **Usage examples**, copy the code snippet written in the `.env` format.

You will need these keys to configure the SDK in your application. We recommend storing them in environment variables using the standard `.env` file format.

Keep Your Keys Secure

Make sure to keep your Secret Key and Bearer Token secure and do not expose them in client-side code or public repositories.

## Configuration[​](#configuration "Direct link to Configuration")

We recommend creating an instance of the Freemius SDK in a separate module and exporting it for use throughout your application.

src/lib/freemius.ts

```ts
import { Freemius } from '@freemius/sdk';

export const freemius = new Freemius({
  productId: process.env.FREEMIUS_PRODUCT_ID!,
  apiKey: process.env.FREEMIUS_API_KEY!,
  secretKey: process.env.FREEMIUS_SECRET_KEY!,
  publicKey: process.env.FREEMIUS_PUBLIC_KEY!,
});
```

To use it, simply import the `freemius` instance from the module you created.

src/app.ts

```ts
import { freemius } from './lib/freemius';

async function main() {
  const pricing = await freemius.pricing.retrieve();
  console.log(pricing);
}
```

Please continue reading to learn more about the different features of the SDK and how to use them in your application.