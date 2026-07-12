---
title: "Installing the Starter Kit and Integrating with JS SDK"
url: "https://freemius.com/help/documentation/saas-sdk/react-starter/installation/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 477
---

The Freemius React Starter Kit is built with [shadcn/ui](https://ui.shadcn.com/) and [Tailwind CSS](https://tailwindcss.com/). It provides a variety of components to help you quickly set up billing, subscriptions, and customer portal features in your SaaS application.

## Installing the React Starter Kit Components[​](#installing-the-react-starter-kit-components "Direct link to Installing the React Starter Kit Components")

To get started, make sure you have already installed and configured shadcn/ui in your application. Detailed instructions are available [here](https://ui.shadcn.com/docs/installation).

Once you have shadcn/ui set up, you can install the React Starter Kit components using the package manager of your choice.

- npm
- Yarn
- pnpm
- Bun

```bash
npx shadcn@latest add https://shadcn.freemius.com/all.json
```

```bash
yarn dlx shadcn@latest add https://shadcn.freemius.com/all.json
```

```bash
pnpm dlx shadcn@latest add https://shadcn.freemius.com/all.json
```

```bash
bun x shadcn@latest add https://shadcn.freemius.com/all.json
```

This command will install all necessary components and dependencies. Since the components are based on shadcn/ui, you will receive the actual component files, which you can customize as needed. The installed files can be found in the `react-starter` directory of your project.

```plaintext
react-starter/
├─ components/
├─ hooks/
├─ icons/
└─ utils/
```

The installation process will also add the [Freemius JavaScript SDK](help-documentation-saas-sdk-js-sdk-installation.md) and the [Freemius Checkout JS](help-documentation-checkout-integration-freemius-checkout-buy-button.md) libraries as dependencies.

Decoupling Application Logic

Currently, various pieces of application logic are written directly in the `hooks` and some of the `components`. In the future, we will release a more decoupled version in which the application logic will be separated from the UI components. This will allow you to use your own components while still leveraging the underlying functionality provided by the React Starter Kit.

## Setting Up the Required API Endpoints[​](#setting-up-the-required-api-endpoints "Direct link to Setting Up the Required API Endpoints")

The React Starter Kit components rely on two specific API endpoints—`/api/checkout` and `/api/portal`—to function properly. These endpoints are used to load data and perform actions securely on the backend.

The [Freemius JavaScript SDK](help-documentation-saas-sdk-js-sdk.md) makes it very easy to set up these endpoints. Please follow the instructions in the [JS SDK documentation](help-documentation-saas-sdk-js-sdk-starter-kit-api-endpoints.md) to complete the initial setup.

Framework Integration

If you are using a specific framework, such as Next.js, please refer to our [Framework Integration](help-documentation-saas-sdk-framework.md) guide for tailored instructions.

You are not required to create the endpoints at the exact paths mentioned above; however, if you choose to use different paths, you will need to update the `CheckoutProvider` and `CustomerPortal` components to point to the correct endpoints.

## Using the Components[​](#using-the-components "Direct link to Using the Components")

Now, various [components](help-documentation-saas-sdk-react-starter-components.md) are available for you to use in your application. You can import and use them as needed.

```tsx
import { type CheckoutSerialized } from '@freemius/checkout';
import { CheckoutProvider } from '@/react-starter/components/checkout-provider';
import { Subscribe } from '@/react-starter/components/subscribe';

const endpoint = process.env.PUBLIC_URL + '/api/checkout';
const checkout: CheckoutSerialized = {
  options: { product_id: process.env.PUBLIC_FREEMIUS_PRODUCT_ID! },
  link: `https://checkout.freemius.com/${process.env.PUBLIC_FREEMIUS_PRODUCT_ID}/`,
};

export default function PricingPage() {
  return (
    <CheckoutProvider endpoint={endpoint} checkout={checkout}>
      <Subscribe />
    </CheckoutProvider>
  );
}
```