[Changelog](https://freemius.com/changelog/) / Release: Freemius JavaScript SDK & React Starter Kit

We understand that most MoR or payment providers stop their integration guide at “now you can charge your customers.” That leaves you, the maker, to figure out all the glue code for:

1. Checkout
2. Purchase processing
3. Validation and storage of purchases
4. Entitlement logic
5. Syncing licenses or entitlements with outside changes
6. Creating Customer Portals for self-management of billing and purchases

At Freemius, we care about your time. That’s why we set out to create not just another “Billing SDK,” but a solution that provides patterns and components to solve these problems end-to-end.

With that in mind, today we’re shipping a major unlock: our [**JavaScript SDK**](help-documentation-saas-sdk-js-sdk.md) and **[React Starter Kit](help-documentation-saas-sdk-react-starter.md).**

[![Paywall provided by the Freemius JS SDK & React Starter Kit](https://freemius.com/blog/wp-content/uploads/2025/09/react-starter-kit-paywall-1024x776.png)](https://freemius.com/blog/wp-content/uploads/2025/09/react-starter-kit-paywall.png)

By using our SDKs and Starter Kits, you’ll get all of this integration for free, so you can focus on what truly matters—the business logic of your product. As we like to say: “Your product shouldn’t be blocked by subscription plumbing. Now it isn’t.”

[![Freemius Customer Portal provided by the JS SDK and the React Starter Kit](https://freemius.com/blog/wp-content/uploads/2025/09/customer-portal-react-starter-kit-1024x950.png)](https://freemius.com/blog/wp-content/uploads/2025/09/customer-portal-react-starter-kit.png)

Please check our [official documentation](help-documentation-saas-sdk.md) for the full details. Below are some highlights.

### [Backend JS/TS SDK](help-documentation-saas-sdk-js-sdk.md)

- Fully typed API client (licenses, subscriptions, users, payments, pricing).
- Checkout builder: generate overlay options & hosted links (with sandbox & redirect verification).
- Purchase + entitlement helpers (`retrievePurchaseData`, `entitlement.getActive`, upgrade authorization).
- Strongly typed webhook listener + request processors (Fetch runtimes, Node HTTP, serverless, edge).
- Signature verification & secure redirect handling (no copy-pasting HMAC code).
- Runtime flexible: Node.js, Bun, Deno.

### [React Starter Kit](help-documentation-saas-sdk-react-starter.md)

- Pre-built UI: Pricing Table, Overlay Checkout trigger, Feature Gating helpers (Paywalls), and a fully working Customer Portal.
- Seamless server → client handoff: serialized checkout + purchase data patterns.

Our system works with all modern JavaScript [frameworks](help-documentation-saas-sdk-framework.md) like [Next.js](help-documentation-saas-sdk-framework-nextjs.md), [Nuxt](help-documentation-saas-sdk-framework-nuxt.md), [Hono](help-documentation-saas-sdk-framework-hono.md), and more.

If you’re just starting out, we highly recommend using our SDK as your foundation. If you already have a working integration, try it out in a side branch and replace your existing “duct-tape” billing glue. Tell us what shaved the most time off your build—and what’s still rough.