At Freemius, we offer a robust **webhooks mechanism** that allows Makers to stay in sync with important platform activities. Webhooks enable real-time communication between Freemius and your backend systems whenever key actions occur—such as a new sale, a license deactivation, or a refund.

This system empowers you to automate workflows, sync data, trigger notifications, and more.

## What is an Event?[​](#what-is-an-event "Direct link to What is an Event?")

An **event** is a specific, predefined action or change that takes place within the Freemius platform.

Events reflect meaningful occurrences in your product’s lifecycle—like a user completing a purchase, a subscription being canceled, or a license being activated. Each event is uniquely named (e.g., `subscription.canceled`, `license.activated`) and carries structured metadata relevant to that action.

Events are the **triggers** that initiate webhook callouts. Whenever a monitored event occurs, Freemius generates a corresponding callout to your configured endpoint.

## What is a Webhook?[​](#what-is-a-webhook "Direct link to What is a Webhook?")

A **webhook** is a URL endpoint that you configure to receive HTTP `POST` requests from Freemius when certain events occur. When an event is triggered, Freemius performs a **webhook callout**—sending a signed payload with all relevant event data to your webhook endpoint. This enables your system to programmatically react to the event, such as updating a database, triggering an internal workflow, or notifying your team.

In short:

- The **webhook** is the URL endpoint you provide.
- The **webhook callout** is the actual HTTP request Freemius makes to that endpoint.

## How to create a Webhook?[​](#how-to-create-a-webhook "Direct link to How to create a Webhook?")

1. Go to the **Webhooks** section and open **Listeners**.
2. Click the **Add Webhook** button.
3. A popup with a form will appear. Add your custom URL that will receive the event callback.
4. Select whether to receive all event types or specific ones on the Callback URL.
5. Choose to immediately make the webhook active or deactivate for a future time.

tip

The Webhook can be edited later to change the url and other options. See all the [available webhooks](#types-of-events)

## How to Test Event's Payload?[​](#how-to-test-events-payload "Direct link to How to Test Event's Payload?")

If you'd like to understand the payload of a specified `event.type` follow these steps:

1. Head to the **Webhooks** section and open **Events**.
2. Filter the events based on that `event.type`.
3. Copy the ID of the 1st event shown in the filtered view.
4. Leverage the API to [fetch the event's data](https://docs.freemius.com/api/events).
5. The result's schema from the API is identical to the payload's schema you'll get by the webhook once `event.type` will be processed.

## Validating Webhook Signatures[​](#validating-webhook-signatures "Direct link to Validating Webhook Signatures")

To ensure the authenticity of incoming webhook requests, Freemius includes a signature in the `x-signature` header of each request. You can validate this signature using your product's secret key.

Here are the steps to validate the signature:

1. Get the `x-signature` header from the incoming request.
2. Get the raw request body (the payload).
3. Compute the HMAC SHA256 hash of the raw body using your product's secret key.
4. Compare the computed hash with the signature from the header.

Here are some code examples in different languages:

- Node.js
- PHP

```
import crypto from 'crypto';
const PRODUCT_SECRET_KEY = '<PRODUCT_SECRET_KEY>';
// IMPORTANT: Ensure you have access to the raw request body
const rawBody = req.rawBody;
const signature = req.headers['x-signature'];
const hash = crypto.createHmac('sha256', PRODUCT_SECRET_KEY).update(rawBody).digest('hex');
let isValid = false;
try {
    isValid = crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(signature, 'hex'));
} catch {
    // Ignore errors
}
if (isValid) {
    // Process the webhook
} else {
    // Invalid signature
}
```

## Types of Events[​](#types-of-events "Direct link to Types of Events")

This is a list of all the types of events we currently send. We may add more at any time, so you shouldn't rely on only these types existing in your code.

You'll notice that these events follow a pattern: `resource.event`. Our goal is to design a consistent system that makes things easier to anticipate and code against.

**NOTE:** Events that occur on "sub" resources like `payment.dispute.created` do not trigger the parent's `update` event.

### Affiliate Program[​](#affiliate-program "Direct link to Affiliate Program")

Occurs whenever an affiliate is approved.

Occurs whenever an affiliate is blocked.

Occurs whenever an affiliate is created.

Occurs whenever an affiliate is deleted.

Occurs once per month when our system calculates affiliate payouts. Triggered only for affiliates eligible for a payout after crossing the $100 threshold.

Occurs whenever there’s an update of an affiliate's PayPal details.

Occurs whenever an affiliate is rejected.

Occurs whenever an affiliate is suspended.

Occurs whenever an affiliate state is changed from approved to pending.

Occurs whenever there’s an update of an affiliate's details.

### Card[​](#card "Direct link to Card")

Occurs whenever a new credit or debit card is added to a user’s account.

Occurs whenever a user’s credit or debit card details have been updated.

### Cart[​](#cart "Direct link to Cart")

Occurs whenever a cart session has been abandoned.

Occurs whenever a ‘sale’ has been completed, but the payment hasn’t necessarily been completed yet.

Occurs whenever a cart session has been initiated.

Occurs whenever an abandoned cart session has been recovered and converted into a ‘sale’.

Occurs when the cart recovery feature has been deactivated in the Developer Dashboard.

Occurs when the first cart recovery email has been sent.

Occurs when the second cart recovery email has been sent.

Occurs when the third (and final) cart recovery email has been sent.

Occurs when the cart recovery feature has been reactivated in the Developer Dashboard.

Occurs when the prospect re-subscribes to the cart abandonment recovery campaign.

Occurs when the prospect unsubscribes from the cart abandonment recovery campaign.

Occurs when the cart contents have been updated.

### Coupons & Discounts[​](#coupons--discounts "Direct link to Coupons & Discounts")

Occurs whenever a coupon is created.

Occurs whenever a coupon is deleted.

Occurs whenever a coupon is updated.

### Buyer Email Tracking[​](#buyer-email-tracking "Direct link to Buyer Email Tracking")

Occurs when a link is clicked by a user. Email link click tracking is only included in cart abandonment recovery and trial-related emails.

Occurs when an email has been opened by a user. Email open tracking is only included in cart abandonment recovery, trial-related, and subscription renewal reminder emails.

### Installation (Downloadable Software)[​](#installation-downloadable-software "Direct link to Installation (Downloadable Software)")

In the context of downloadable software (like plugins or desktop apps), an installation represents a specific copy of your product that has been installed and is running on a particular device or site. The following webhook events let you track changes to each installation—covering its state, version, plan, platform details, and more.

Occurs whenever a user is opted-in, and after reactivation of a product.

Occurs whenever a product's installation is being deactivated.

Occurs whenever a product is being uninstalled.

Occurs whenever a user opts in for sharing basic device/website info after previously opting out from it.

Occurs whenever a user opts out from sharing basic device/website info after previously sharing it.

Occurs whenever a product is being installed (triggered before `install.activated`).

Occurs whenever an installation language is updated.

Occurs whenever an installation plan is changed.

Occurs whenever an installation plan is downgraded to the default plan.

Occurs whenever an installation platform version is updated (e.g., WP version; iOS version).

Occurs whenever the paid product version is activated.

Occurs whenever the paid product version is deactivated.

Occurs whenever an installation PHP version is updated.

Occurs whenever a product installation is updated with a new Freemius SDK version.

Occurs whenever an installation’s device/site title is updated.

Occurs when a trial is cancelled.

Occurs when a trial is expired.

Occurs when an email has been sent to the user notifying them the trial period is about to end.

Occurs whenever a trial is manually extended.

Occurs whenever a trial plan is updated.

Occurs when a free trial is started on an existing product install.

Occurs whenever the product is uninstalled.

Occurs whenever an installation data is updated (in addition to specific install update events).

Occurs whenever an installation’s home URL is updated.

Occurs whenever the product is downgraded to a lower version (not related to the plan).

Occurs whenever the product is upgrade to a newer version (not related to the plan).

### Licensing[​](#licensing "Direct link to Licensing")

Occurs whenever a license is activated (also triggered automatically after a successful plan upgrade).

Occurs when a license is cancelled.

Occurs whenever a license is created.

Occurs whenever a license is deactivated.

Occurs when a license has been deleted in the Developer Dashboard.

Occurs when a license expires.

Occurs when a license expired email notice has been sent to the user.

Occurs whenever a license is extended by the developer from the dashboard.

Occurs whenever a license ownership is changed by the developer from the dashboard.

Occurs whenever a license quota is changed by the developer from the dashboard.

Occurs when a license renewal reminder email has been sent to the user.

Occurs when a license has been shortened in the User/Developer Dashboard.

Occurs when a courtesy trial expiration reminder email has been sent to the user.

Occurs whenever a license is updated (in addition to specific license update events).

### Payment[​](#payment "Direct link to Payment")

Occurs whenever a successful payment is created.

Occurs whenever a payment refund is processed.

Occurs whenever we notified about a payment disputed by a customer.

Occurs whenever a payment dispute is closed by refunding the disputed payment.

Occurs whenever a payment dispute is closed in favor of the customer.

Occurs whenever a payment dispute is closed in your/seller’s favor.

### Product Team[​](#product-team "Direct link to Product Team")

Occurs whenever a developer is added as a team member.

Occurs whenever a member is removed from a team.

Occurs whenever a team member role is updated.

### Plans, Pricing and Features[​](#plans-pricing-and-features "Direct link to Plans, Pricing and Features")

Occurs whenever a plan is created.

Occurs whenever a plan is deleted.

Occurs whenever a user purchases a lifetime package (doesn’t matter which plan).

Occurs whenever a plan details are updated.

Occurs whenever a new pricing is added to a plan.

Occurs whenever one of the plan pricing is deleted.

Occurs whenever a plan pricing is updated.

### Reviews[​](#reviews "Direct link to Reviews")

Occurs when a new review has been created.

Occurs when a review has been deleted in the Developer Dashboard.

Occurs when a new review request email has been sent to the user.

Occurs when a new review has been updated in the Developer Dashboard.

### Subscription[​](#subscription "Direct link to Subscription")

Occurs whenever a subscription is cancelled.

Occurs whenever a subscription is created.

Occurs whenever an annual renewal reminder email is sent (30 days before the automatic renewal).

Occurs whenever an annual renewal reminder email is opened.

Occurs whenever a renewal payment processing is failed.

Occurs when the latest subscription renewal attempt has failed.

Occurs whenever a failure renewal processing email is sent to the buyer.

Occurs whenever a renewal payment retry is processed.

Occurs whenever a special subscription cancellation promo is applied.

### Store[​](#store "Direct link to Store")

Occurs when a new store has been created (e.g. when a new Freemius account has been created).

Occurs when the store’s dashboard URL is updated.

Occurs when a product is added to a store.

Occurs when a product is removed from a store.

Occurs when a store’s URL is updated.

### User[​](#user "Direct link to User")

Occurs when a user has opted into a product's beta program.

Occurs when a user has opted out of a product's beta program.

Occurs whenever a customer billing information is updated (e.g. address, VAT ID, company name).

Occurs whenever the tax ID associated with the user’s billing is changed.

Occurs whenever a new card is added to a user’s account.

Occurs whenever a new user is created.

Occurs whenever a user update their email address.

Occurs when a user email is verified (usually via email confirmation).

Occurs when a transactional email sent to a user bounces, which also changes the user’s email\_status property to 'bounced'.

Occurs when a transactional email sent to a user is successfully delivered and only if the user’s previous deliverability state (aka the email\_status property) was not empty before.

Occurs when a transactional email sent to a user is dropped, which also changes the user’s email\_status property to 'dropped'.

Occurs when a user has opted to receive marketing material (emails).

Occurs when a user has opted out of a receiving marketing material (emails).

Occurs when a user’s marketing status has been reset.

Occurs whenever a user update their name.

Occurs when a user registers for a trial.

### Webhook[​](#webhook "Direct link to Webhook")

Occurs whenever a webhook is created.

Occurs whenever a webhook is deleted.

Occurs whenever a webhook is updated.

### WordPress[​](#wordpress "Direct link to WordPress")

Occurs whenever a free version of an add-on is downloaded.

Occurs whenever a premium version of an add-on is downloaded.

Occurs whenever a user opts in for sharing a website’s plugins & themes list after previously opting out from it.

Occurs whenever a user opt-out from sharing a website’s plugins & themes list after previously sharing it.

Occurs whenever an account ownership transfer candidate confirms the transfer.

Occurs whenever an account ownership transfer is complete.

Occurs whenever an account ownership transfer is initiated.

Occurs whenever an account ownership transfer is confirmed by the current installation account owner.

Occurs whenever a user opts in for sharing basic website after previously opting out from it.

Occurs whenever a user opts out from sharing basic website after previously sharing it.

Occurs whenever a user opts in for sharing their basic profile info after previously opting out from it.

Occurs whenever a user opts out from sharing their basic profile info after previously sharing it.

Occurs when a site has been blacklisted in the Customer Portal.

Occurs when a blacklisted site has been removed in the Customer Portal.

Occurs when a site has been whitelisted in the Customer Portal.

Occurs when a whitelisted site has been removed in the Customer Portal.

Occurs whenever a free product version is downloaded.

Occurs whenever a paid product version is downloaded.

Occurs whenever a deployed version is deleted.

Occurs whenever a new product version is deployed to Freemius.

Occurs whenever a version is set as released.

Occurs whenever a version is released as beta.

Occurs whenever a deployment release is suspended.

Occurs whenever an existing version is re-deployed to Freemius.

Occurs when a user has visited the pricing table via the WordPress admin or popup checkout modal.