---
title: "Lovable Integration Guide with Freemius"
url: "https://freemius.com/help/documentation/ai/lovable/"
source: "docs"
section: "Docs"
category: "Build with AI"
scraped_at: "2026-04-09T19:58:36+06:00"
word_count: 1960
---

Follow this guide to integrate Freemius Checkout and monetization into your apps and SaaS built on [Lovable.dev](https://lovable.dev/) with a single prompt to your AI agent.

The end result would be:

- **Integrated Pricing page and Checkout**: Your users will see the pricing you've configured at Freemius and be able to purchase your product through the Freemius checkout.
- **Gated Premium Features**: You can easily gate your premium features behind a paywall, and only allow access to users who have purchased the product.
- **Integrated Accounts Page**: Show active subscriptions and payments right within your app. Also link to the Freemius Customer Portal for more advanced account management features.

You can see a full end-to-end demo below.

[Explore the App](https://freemius-saas.lovable.app/register)[More Examples](https://lovable.dev/@freemius)

Please read on to see how you can easily do something like above with a single prompt to Lovable's AI agent.

## Setup your Product at Freemius[​](#setup-your-product-at-freemius "Direct link to Setup your Product at Freemius")

If you haven't already, please register and [create your product and plans](help-documentation-saas-saas-plans-pricing.md) at Freemius.

For this guide, we'll create a few subscription-based plans as shown below:

All plans have monthly and annual billing cycles with different pricing and features, as shown below:

## Get your API Keys[​](#get-your-api-keys "Direct link to Get your API Keys")

Now go to **Product** → **Settings** and from the **API & Keys** tab, copy your API keys as shown below:

1. **Product ID**: The AI agent will reference this as `FREEMIUS_PRODUCT_ID`.
2. **Product Public Key**: The AI agent will reference this as `FREEMIUS_PUBLIC_KEY`.
3. **Product Secret Key**: The AI agent will reference this as `FREEMIUS_SECRET_KEY`.
4. **API Bearer Authorization Token**: The AI agent will reference this as `FREEMIUS_API_KEY`.

Keep these keys handy for the next steps.

## Update Lovable Knowledge[​](#update-lovable-knowledge "Direct link to Update Lovable Knowledge")

Next, add custom instructions to Lovable's Knowledge Base so the AI agent knows how to integrate Freemius into your application.

1. While editing your lovable project, click on the **Settings** button from the top-left corner.
2. From the left sidebar, click on **Knowledge**.
3. Paste the following instructions at the end of the knowledge and click on the **Update** button.
   
   ```md
   ## Freemius Monetization
   
   Integrate Freemius end-to-end in this Lovable app using Supabase functions,
   shared backend utilities, and frontend paywall/account UX.
   
   ### Integration Guidelines
   
   When asked to integrate Freemius, follow the instructions from this URL:
   
   https://raw.githubusercontent.com/Freemius/freemius-ai/refs/heads/main/lovable-integration/subscription/prompt.md
   
   ### Protect Premium Features with Paywall
   
   - To restrict any premium operations in the API routes that requires an active
     subscription, use the shared `supabase/functions/_shared/freemius.ts` module's
     `getUserEntitlement` (for any plan) or `hasPlan` (specific plan) functions.
     Return a 403 response with `code: "subscription_required"` if the user doesn't
     have the required subscription.
   - On the frontend, handle the `subscription_required` error by reading the
     response body from `error.context.body` as a stream (since Supabase
     `functions.invoke` puts non-2xx response bodies there as a ReadableStream, not
     plain JSON). Show a lock-style paywall UI with a link to `/pricing`. You can
     disable relevant UI after the first failed attempt.
   - The front-end may also call the `functions/v1/get-entitlements` API route to
     check for active entitlements and show a paywall UI with link to `/pricing`
     through a `Subscribe` button if there is no active subscription.
   
   ---
   ```

## Do the Integration[​](#do-the-integration "Direct link to Do the Integration")

Go back to the Lovable editor and enter the following prompt:

prompt

```md
Implement the Freemius integration based on the knowledgebase content.
```

The AI agent will start working on the integration. Here's what will happen:

1. The agent might ask to enable the Cloud backend (Supabase) if you haven't already—go ahead and enable it.
2. The agent will ask to create a new database table named `user_fs_entitlement`—accept this.
3. The agent will prompt you for the four keys you copied in the [previous steps](#get-your-api-keys)—paste them in the relevant places.

Because the integration instructions are comprehensive, the agent will work through several steps. Once complete, it will output two URLs:

one for the Checkout redirection and one for the Webhooks.

### Setup Checkout Redirection[​](#setup-checkout-redirection "Direct link to Setup Checkout Redirection")

Go to **Plans** → **Customize** and set the **Checkout Success Redirection** that the AI agent gave you.

This ensures the purchase is processed immediately by your app and users get instant access to benefits. Learn more in our [documentation](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase).

### Setup Webhooks[​](#setup-webhooks "Direct link to Setup Webhooks")

Go to **Products** → **Webhooks** → **Listeners** and add the Webhook URL that the AI agent gave you.

Make sure to send the following event types:

This ensures your application knows the status of a license, for example when a subscription is renewed your application will also update the expiry date. For more information about webhooks, see our [documentation](help-documentation-saas-events-webhooks.md). For now, creating the webhook listener with the URL and event types is sufficient for the integration to work.

## Test the Integration[​](#test-the-integration "Direct link to Test the Integration")

Now let's test the integration end-to-end to ensure everything is working as expected.

1. You should now see a new **Subscribe** button in the app's navbar.
2. Clicking the action button in the paywall will take you to the pricing page which can look like this:
   
   **It will fetch all the plans, pricing and features you have configured in Freemius, in real time.**
3. Click the **Subscribe** button on any plan to test it further. This takes you to the Freemius Checkout page.
   
   For this step, you can either ask your AI agent to enable sandbox mode:
   
   prompt
   
   ```md
   Enable sandbox mode in the Freemius integration for specific user email `{yourEmail}`
   ```
   
   or use a [100% discount coupon](help-documentation-selling-with-freemius-coupon-discount.md) to test the checkout without making a production payment.
4. After checkout completes, you'll see a confirmation that the payment was successful and be redirected back to the app.
   
   The app should now show that you're subscribed with access to premium features.
5. The AI should have added or enhanced the `/accounts` page, similar to this:
6. Click the **Update Subscription** button to go to the pricing page. This time, your current plan is highlighted, and other plans are shown as upgrade or downgrade options.
7. To further test, click the **Cancel Subscription** button on the accounts page. You'll see the app cancel the subscription with Freemius, and the UI updates accordingly.
8. Click **Manage Billing** to access the Freemius Customer Portal, where you can test other features like changing plans or updating payment methods.

If all steps worked as expected, you've successfully integrated Freemius monetization with your Lovable app.

You can also customize the UI further to match your app's design and branding.

## Protect Features with Paywall[​](#protect-features-with-paywall "Direct link to Protect Features with Paywall")

In your **Knowledge** settings, Lovable is already configured with instructions for maintaining the Freemius integration and paywall. You only need to tell the AI which UI elements and API routes to protect.

For example, to protect the meme generator feature on both the backend and frontend, use this prompt:

prompt

```md
Add a paywall to the meme generation feature. Use guide from knowledgebase to protect the API route with `getUserEntitlement` and show a lock-style paywall UI with a link to `/pricing` on the frontend if the user doesn't have any active subscription. Disable the generate button after the first failed attempt.
```

The end result would look like this:

To restrict a feature to a specific plan only (for example, Pro plan users for the meme generator), use `hasPlan` instead of `getUserEntitlement` like this:

prompt

```md
Add a paywall to the meme generation feature. Use guide from knowledgebase to protect the API route with `hasPlan` for the `<planID>` and show a lock-style paywall UI with a link to `/pricing` on the frontend if the user doesn't have an active Pro subscription. Disable the generate button after the first failed attempt.
```

### Customize for Your Feature[​](#customize-for-your-feature "Direct link to Customize for Your Feature")

Customize the prompt for your use case by specifying which UI elements and API routes to protect. The **meme generator** is just an example.

Additionally if you're using the `hasPlan` function, you can find the `<planID>` from the Freemius Developer Dashboard under your product's plans as shown below:

Protecting API routes

Always remember to protect the API route. If you don't protect the API route, it can be easily abused.

## Publishing the App[​](#publishing-the-app "Direct link to Publishing the App")

After publishing, if the integration stops working, it's usually because URLs have changed. Ask the AI agent to fix it:

prompt

```md
If the app has been published, make sure to update all front-end URLs to
point to the production URL instead of the local development URL inside
`_shared/freemius.ts`.
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Thorough testing ensures everything works as expected. However, issues can still occur. Here are our recommendations and tips.

### Taking Help from the AI agent[​](#taking-help-from-the-ai-agent "Direct link to Taking Help from the AI agent")

If something breaks or doesn't work as expected, first ask the AI agent to fix it. For example, if Checkout Redirection isn't working, ask the agent:

prompt

```md
The checkout redirection is not working, check the redirection flow and make sure it works as expected.
```

Sharing screenshots of the issue is also helpful.

### Going Through the Integration Steps[​](#going-through-the-integration-steps "Direct link to Going Through the Integration Steps")

We also recommend reviewing the integration steps in our [GitHub repository](https://github.com/Freemius/freemius-ai/tree/main/lovable-integration/subscription#advanced-step-by-step-integration).

If you can identify which step has the issue, ask the agent to redo that step. For example, if the accounts page isn't working properly, ask:

prompt

```md
The accounts page is not showing the subscription status correctly, please redo the accounts page integration step and make sure it works as expected. Here is the original instruction for that step from the knowledgebase:

https://raw.githubusercontent.com/Freemius/freemius-ai/refs/heads/main/lovable-integration/subscription/05-accounts-page.md
```

Links to individual steps

For your reference, here are the links to the individual steps of the integration:

- **Step 1**:
- **Step 2**:
- **Step 3**:
- **Step 4**:
- **Step 5**:
- **Step 6**:
- **Step 7**:

### Make Sure the Webhooks and Checkout Redirections are Working[​](#make-sure-the-webhooks-and-checkout-redirections-are-working "Direct link to Make Sure the Webhooks and Checkout Redirections are Working")

Webhooks and Checkout Redirection are the two most critical parts of the integration. If they don't work properly, the integration will fail. Test these parts thoroughly. You can ask the AI agent to verify them end-to-end. Freemius also sends email notifications if webhook processing fails.

If this happens, copy the email content and ask the AI agent to fix the issue. For example:

prompt

```md
I received the following email from Freemius about webhook processing failure:

{paste the email content here}

Please fix the issue and make sure the webhooks are working as expected.
```

### Using One-off Purchases[​](#using-one-off-purchases "Direct link to Using One-off Purchases")

Our integration guide is based on subscription plans and won't work for one-off purchases or lifetime access. While it is fully possible to integrate such purchase models with Freemius, it requires a different implementation approach. We recommend contacting our [support team](/cdn-cgi/l/email-protection#e5969095958a9791a583978080888c9096cb868a88da9690878f808691d8aa8b80c88a8383c0d7d5b59097868d849680c0d7d5ac8b9180829784918c8a8bc0d7d5928c918dc0d7d5a98a9384878980) with your use case and requirements, and we can guide you through the best approach for your specific needs.

### Remixing the Demo App[​](#remixing-the-demo-app "Direct link to Remixing the Demo App")

If you are remixing the demo app, then it will ask you to enter the API keys. Please do that following the [instructions above](#get-your-api-keys).

In addition, also ask the AI agent to give you the Checkout Redirection and Webhook URLs so you can set them up in the Freemius Developer Dashboard.

prompt

```md
Please provide the Checkout Redirection and Webhook URLs for this app which I can set up in the Freemius Developer Dashboard.
```

### Contact Freemius Support[​](#contact-freemius-support "Direct link to Contact Freemius Support")

Our support team is here to help. Contact us at [\[email protected\]](/cdn-cgi/l/email-protection#92e1e7e2e2fde0e6d2f4e0f7f7fffbe7e1bcf1fdff) and we'll be happy to assist with integration and troubleshooting.