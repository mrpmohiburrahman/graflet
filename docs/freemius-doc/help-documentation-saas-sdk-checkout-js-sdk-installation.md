---
title: "Freemius Checkout JS SDK Installation"
url: "https://freemius.com/help/documentation/saas-sdk/checkout-js-sdk/installation/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 308
---

There are two primary ways to include the Checkout JS SDK in your project:

## Using the hosted CDN[​](#using-the-hosted-cdn "Direct link to Using the hosted CDN")

This is the quickest and recommended way to get started. It requires no build steps and you automatically get the latest version of the SDK.

Start by including the script tag in your HTML:

```html
<script
  type="text/javascript"
  src="https://checkout.freemius.com/js/v1/"
></script>
```

The script exposes a global `FS.Checkout` class that you can instantiate.

```js
const checkout = new FS.Checkout({
  product_id: '1234',
});
```

### Loading the script asynchronously[​](#loading-the-script-asynchronously "Direct link to Loading the script asynchronously")

You can load the script using the `async` or `defer` attribute on the script tag.

```html
<script
  type="text/javascript"
  src="https://checkout.freemius.com/js/v1/"
  async
  defer
></script>
```

This ensures that the script does not block HTML parsing, improving page-load performance.

note

With asynchronous loading, any API calls must be made only after the script finishes executing. To ensure this, hook into the `load` event of `window` or use `window.onload`.

Example using the `async` or `defer` attribute

```html
<script type="text/javascript">
  window.addEventListener('load', () => {
    const checkout = new FS.Checkout({
      product_id: '1234',
    });

    checkout.open({
      // plan
      plan_id: 9999,
      // number of sites
      licenses: 1,
      // billing cycles
      billing_cycle: 'annual',
    });
  });
</script>
```

## Bundling using the npm package[​](#bundling-using-the-npm-package "Direct link to Bundling using the npm package")

Install the official [npm](https://www.npmjs.com/package/@freemius/checkout) package, and use a bundler such as [Vite](https://vite.dev/) or [Webpack](https://webpack.js.org/) to manage your application.

- npm
- Yarn
- pnpm
- Bun

```bash
npm i @freemius/checkout
```

```bash
yarn add @freemius/checkout
```

```bash
pnpm add @freemius/checkout
```

```bash
bun add @freemius/checkout
```

The main class exported by the package is `Checkout`.

```js
import { Checkout } from 'freemius-checkout-js';

// instantiate
const checkout = new Checkout({
  product_id: '0001',
});
```

* * *

To learn how to use the SDK, proceed to the [Usage Guide](help-documentation-saas-sdk-checkout-js-sdk-usage.md).