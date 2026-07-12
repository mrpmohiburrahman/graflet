---
title: "Automate Your Workflows with Events & Webhooks"
url: "https://freemius.com/help/documentation/saas/events-webhooks/"
source: "docs"
section: "Docs"
category: "Setup for SaaS & Apps"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 3221
---

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

```ts
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

```php
const PRODUCT_SECRET_KEY = '<PRODUCT_SECRET_KEY>';

$signature = $_SERVER['HTTP_X_SIGNATURE'] ?? '';
$rawBody = file_get_contents('php://input');

$calculatedSignature = hash_hmac('sha256', $rawBody, PRODUCT_SECRET_KEY);

$isValid = hash_equals($calculatedSignature, $signature);

if ($isValid) {
    // Process the webhook
} else {
    // Invalid signature
}
```

Using a JavaScript Environment?

Do check our [JS SDK Webhooks Documentation](help-documentation-saas-sdk-js-sdk-webhooks.md) for an easier integration.

## Types of Events[​](#types-of-events "Direct link to Types of Events")

This is a list of all the types of events we currently send. We may add more at any time, so you shouldn't rely on only these types existing in your code.

You'll notice that these events follow a pattern: `resource.event`. Our goal is to design a consistent system that makes things easier to anticipate and code against.

**NOTE:** Events that occur on "sub" resources like `payment.dispute.created` do not trigger the parent's `update` event.

### Affiliate Program[​](#affiliate-program "Direct link to Affiliate Program")

`affiliate.approved`[](#affiliate-approved "Direct link to affiliate.approved")

Occurs whenever an affiliate is approved.

`affiliate.blocked`[](#affiliate-blocked "Direct link to affiliate.blocked")

Occurs whenever an affiliate is blocked.

`affiliate.created`[](#affiliate-created "Direct link to affiliate.created")

Occurs whenever an affiliate is created.

`affiliate.deleted`[](#affiliate-deleted "Direct link to affiliate.deleted")

Occurs whenever an affiliate is deleted.

`affiliate.payout.pending`[](#affiliate-payout-pending "Direct link to affiliate.payout.pending")

Occurs once per month when our system calculates affiliate payouts. Triggered only for affiliates eligible for a payout after crossing the $100 threshold.

`affiliate.paypal.updated`[](#affiliate-paypal-updated "Direct link to affiliate.paypal.updated")

Occurs whenever there’s an update of an affiliate's PayPal details.

`affiliate.rejected`[](#affiliate-rejected "Direct link to affiliate.rejected")

Occurs whenever an affiliate is rejected.

`affiliate.suspended`[](#affiliate-suspended "Direct link to affiliate.suspended")

Occurs whenever an affiliate is suspended.

`affiliate.unapproved`[](#affiliate-unapproved "Direct link to affiliate.unapproved")

Occurs whenever an affiliate state is changed from approved to pending.

`affiliate.updated`[](#affiliate-updated "Direct link to affiliate.updated")

Occurs whenever there’s an update of an affiliate's details.

### Card[​](#card "Direct link to Card")

`card.created`[](#card-created "Direct link to card.created")

Occurs whenever a new credit or debit card is added to a user’s account.

`card.updated`[](#card-updated "Direct link to card.updated")

Occurs whenever a user’s credit or debit card details have been updated.

### Cart[​](#cart "Direct link to Cart")

`cart.abandoned`[](#cart-abandoned "Direct link to cart.abandoned")

Occurs whenever a cart session has been abandoned.

`cart.completed`[](#cart-completed "Direct link to cart.completed")

Occurs whenever a ‘sale’ has been completed, but the payment hasn’t necessarily been completed yet.

`cart.created`[](#cart-created "Direct link to cart.created")

Occurs whenever a cart session has been initiated.

`cart.recovered`[](#cart-recovered "Direct link to cart.recovered")

Occurs whenever an abandoned cart session has been recovered and converted into a ‘sale’.

`cart.recovery.deactivated`[](#cart-recovery-deactivated "Direct link to cart.recovery.deactivated")

Occurs when the cart recovery feature has been deactivated in the Developer Dashboard.

`cart.recovery.email_1_sent`[](#cart-recovery-email_1_sent "Direct link to cart.recovery.email_1_sent")

Occurs when the first cart recovery email has been sent.

`cart.recovery.email_2_sent`[](#cart-recovery-email_2_sent "Direct link to cart.recovery.email_2_sent")

Occurs when the second cart recovery email has been sent.

`cart.recovery.email_3_sent`[](#cart-recovery-email_3_sent "Direct link to cart.recovery.email_3_sent")

Occurs when the third (and final) cart recovery email has been sent.

`cart.recovery.reactivated`[](#cart-recovery-reactivated "Direct link to cart.recovery.reactivated")

Occurs when the cart recovery feature has been reactivated in the Developer Dashboard.

`cart.recovery.subscribed`[](#cart-recovery-subscribed "Direct link to cart.recovery.subscribed")

Occurs when the prospect re-subscribes to the cart abandonment recovery campaign.

`cart.recovery.unsubscribed`[](#cart-recovery-unsubscribed "Direct link to cart.recovery.unsubscribed")

Occurs when the prospect unsubscribes from the cart abandonment recovery campaign.

`cart.updated`[](#cart-updated "Direct link to cart.updated")

Occurs when the cart contents have been updated.

### Coupons & Discounts[​](#coupons--discounts "Direct link to Coupons & Discounts")

`coupon.created`[](#coupon-created "Direct link to coupon.created")

Occurs whenever a coupon is created.

`coupon.deleted`[](#coupon-deleted "Direct link to coupon.deleted")

Occurs whenever a coupon is deleted.

`coupon.updated`[](#coupon-updated "Direct link to coupon.updated")

Occurs whenever a coupon is updated.

### Buyer Email Tracking[​](#buyer-email-tracking "Direct link to Buyer Email Tracking")

`email.clicked`[](#email-clicked "Direct link to email.clicked")

Occurs when a link is clicked by a user. Email link click tracking is only included in cart abandonment recovery and trial-related emails.

`email.opened`[](#email-opened "Direct link to email.opened")

Occurs when an email has been opened by a user. Email open tracking is only included in cart abandonment recovery, trial-related, and subscription renewal reminder emails.

### Installation (Downloadable Software)[​](#installation-downloadable-software "Direct link to Installation (Downloadable Software)")

In the context of downloadable software (like plugins or desktop apps), an installation represents a specific copy of your product that has been installed and is running on a particular device or site. The following webhook events let you track changes to each installation—covering its state, version, plan, platform details, and more.

`install.activated`[](#install-activated "Direct link to install.activated")

Occurs whenever a user is opted-in, and after reactivation of a product.

`install.deactivated`[](#install-deactivated "Direct link to install.deactivated")

Occurs whenever a product's installation is being deactivated.

`install.deleted`[](#install-deleted "Direct link to install.deleted")

Occurs whenever a product is being uninstalled.

`install.connected`[](#install-connected "Direct link to install.connected")

Occurs whenever a user opts in for sharing basic device/website info after previously opting out from it.

`install.disconnected`[](#install-disconnected "Direct link to install.disconnected")

Occurs whenever a user opts out from sharing basic device/website info after previously sharing it.

`install.installed`[](#install-installed "Direct link to install.installed")

Occurs whenever a product is being installed (triggered before `install.activated`).

`install.language.updated`[](#install-language-updated "Direct link to install.language.updated")

Occurs whenever an installation language is updated.

`install.plan.changed`[](#install-plan-changed "Direct link to install.plan.changed")

Occurs whenever an installation plan is changed.

`install.plan.downgraded`[](#install-plan-downgraded "Direct link to install.plan.downgraded")

Occurs whenever an installation plan is downgraded to the default plan.

`install.platform.version.updated`[](#install-platform-version-updated "Direct link to install.platform.version.updated")

Occurs whenever an installation platform version is updated (e.g., WP version; iOS version).

`install.premium.activated`[](#install-premium-activated "Direct link to install.premium.activated")

Occurs whenever the paid product version is activated.

`install.premium.deactivated`[](#install-premium-deactivated "Direct link to install.premium.deactivated")

Occurs whenever the paid product version is deactivated.

`install.programming_language.version.updated`[](#install-programming_language-version-updated "Direct link to install.programming_language.version.updated")

Occurs whenever an installation PHP version is updated.

`install.sdk.version.updated`[](#install-sdk-version-updated "Direct link to install.sdk.version.updated")

Occurs whenever a product installation is updated with a new Freemius SDK version.

`install.title.updated`[](#install-title-updated "Direct link to install.title.updated")

Occurs whenever an installation’s device/site title is updated.

`install.trial.cancelled`[](#install-trial-cancelled "Direct link to install.trial.cancelled")

Occurs when a trial is cancelled.

`install.trial.expired`[](#install-trial-expired "Direct link to install.trial.expired")

Occurs when a trial is expired.

`install.trial_expiring_notice.sent`[](#install-trial_expiring_notice-sent "Direct link to install.trial_expiring_notice.sent")

Occurs when an email has been sent to the user notifying them the trial period is about to end.

`install.trial.extended`[](#install-trial-extended "Direct link to install.trial.extended")

Occurs whenever a trial is manually extended.

`install.trial.plan.updated`[](#install-trial-plan-updated "Direct link to install.trial.plan.updated")

Occurs whenever a trial plan is updated.

`install.trial.started`[](#install-trial-started "Direct link to install.trial.started")

Occurs when a free trial is started on an existing product install.

`install.uninstalled`[](#install-uninstalled "Direct link to install.uninstalled")

Occurs whenever the product is uninstalled.

`install.updated`[](#install-updated "Direct link to install.updated")

Occurs whenever an installation data is updated (in addition to specific install update events).

`install.url.updated`[](#install-url-updated "Direct link to install.url.updated")

Occurs whenever an installation’s home URL is updated.

`install.version.downgrade`[](#install-version-downgrade "Direct link to install.version.downgrade")

Occurs whenever the product is downgraded to a lower version (not related to the plan).

`install.version.upgraded`[](#install-version-upgraded "Direct link to install.version.upgraded")

Occurs whenever the product is upgrade to a newer version (not related to the plan).

### Licensing[​](#licensing "Direct link to Licensing")

`license.activated`[](#license-activated "Direct link to license.activated")

Occurs whenever a license is activated (also triggered automatically after a successful plan upgrade).

`license.cancelled`[](#license-cancelled "Direct link to license.cancelled")

Occurs when a license is cancelled.

`license.created`[](#license-created "Direct link to license.created")

Occurs whenever a license is created.

`license.deactivated`[](#license-deactivated "Direct link to license.deactivated")

Occurs whenever a license is deactivated.

`license.deleted`[](#license-deleted "Direct link to license.deleted")

Occurs when a license has been deleted in the Developer Dashboard.

`license.expired`[](#license-expired "Direct link to license.expired")

Occurs when a license expires.

`license.expired_notice.sent`[](#license-expired_notice-sent "Direct link to license.expired_notice.sent")

Occurs when a license expired email notice has been sent to the user.

`license.extended`[](#license-extended "Direct link to license.extended")

Occurs whenever a license is extended by the developer from the dashboard.

`license.ownership.changed`[](#license-ownership-changed "Direct link to license.ownership.changed")

Occurs whenever a license ownership is changed by the developer from the dashboard.

`license.quota.changed`[](#license-quota-changed "Direct link to license.quota.changed")

Occurs whenever a license quota is changed by the developer from the dashboard.

`license.renewal_reminder.sent`[](#license-renewal_reminder-sent "Direct link to license.renewal_reminder.sent")

Occurs when a license renewal reminder email has been sent to the user.

`license.shortened`[](#license-shortened "Direct link to license.shortened")

Occurs when a license has been shortened in the User/Developer Dashboard.

`license.trial_expiring_notice.sent`[](#license-trial_expiring_notice-sent "Direct link to license.trial_expiring_notice.sent")

Occurs when a courtesy trial expiration reminder email has been sent to the user.

`license.updated`[](#license-updated "Direct link to license.updated")

Occurs whenever a license is updated (in addition to specific license update events).

### Payment[​](#payment "Direct link to Payment")

`payment.created`[](#payment-created "Direct link to payment.created")

Occurs whenever a successful payment is created.

`payment.refund`[](#payment-refund "Direct link to payment.refund")

Occurs whenever a payment refund is processed.

`payment.dispute.created`[](#payment-dispute-created "Direct link to payment.dispute.created")

Occurs whenever we notified about a payment disputed by a customer.

`payment.dispute.closed`[](#payment-dispute-closed "Direct link to payment.dispute.closed")

Occurs whenever a payment dispute is closed by refunding the disputed payment.

`payment.dispute.lost`[](#payment-dispute-lost "Direct link to payment.dispute.lost")

Occurs whenever a payment dispute is closed in favor of the customer.

`payment.dispute.won`[](#payment-dispute-won "Direct link to payment.dispute.won")

Occurs whenever a payment dispute is closed in your/seller’s favor.

### Product Team[​](#product-team "Direct link to Product Team")

`member.created`[](#member-created "Direct link to member.created")

Occurs whenever a developer is added as a team member.

`member.deleted`[](#member-deleted "Direct link to member.deleted")

Occurs whenever a member is removed from a team.

`member.updated`[](#member-updated "Direct link to member.updated")

Occurs whenever a team member role is updated.

### Plans, Pricing and Features[​](#plans-pricing-and-features "Direct link to Plans, Pricing and Features")

`plan.created`[](#plan-created "Direct link to plan.created")

Occurs whenever a plan is created.

`plan.deleted`[](#plan-deleted "Direct link to plan.deleted")

Occurs whenever a plan is deleted.

`plan.lifetime.purchase`[](#plan-lifetime-purchase "Direct link to plan.lifetime.purchase")

Occurs whenever a user purchases a lifetime package (doesn’t matter which plan).

`plan.updated`[](#plan-updated "Direct link to plan.updated")

Occurs whenever a plan details are updated.

`pricing.created`[](#pricing-created "Direct link to pricing.created")

Occurs whenever a new pricing is added to a plan.

`pricing.deleted`[](#pricing-deleted "Direct link to pricing.deleted")

Occurs whenever one of the plan pricing is deleted.

`pricing.updated`[](#pricing-updated "Direct link to pricing.updated")

Occurs whenever a plan pricing is updated.

### Reviews[​](#reviews "Direct link to Reviews")

`review.created`[](#review-created "Direct link to review.created")

Occurs when a new review has been created.

`review.deleted`[](#review-deleted "Direct link to review.deleted")

Occurs when a review has been deleted in the Developer Dashboard.

`review.requested`[](#review-requested "Direct link to review.requested")

Occurs when a new review request email has been sent to the user.

`review.updated`[](#review-updated "Direct link to review.updated")

Occurs when a new review has been updated in the Developer Dashboard.

### Subscription[​](#subscription "Direct link to Subscription")

`subscription.cancelled`[](#subscription-cancelled "Direct link to subscription.cancelled")

Occurs whenever a subscription is cancelled.

`subscription.created`[](#subscription-created "Direct link to subscription.created")

Occurs whenever a subscription is created.

`subscription.renewal_reminder.sent`[](#subscription-renewal_reminder-sent "Direct link to subscription.renewal_reminder.sent")

Occurs whenever an annual renewal reminder email is sent (30 days before the automatic renewal).

`subscription.renewal_reminder.opened`[](#subscription-renewal_reminder-opened "Direct link to subscription.renewal_reminder.opened")

Occurs whenever an annual renewal reminder email is opened.

`subscription.renewal.failed`[](#subscription-renewal-failed "Direct link to subscription.renewal.failed")

Occurs whenever a renewal payment processing is failed.

`subscription.renewal.failed.last`[](#subscription-renewal-failed-last "Direct link to subscription.renewal.failed.last")

Occurs when the latest subscription renewal attempt has failed.

`subscription.renewal.failed_email.sent`[](#subscription-renewal-failed_email-sent "Direct link to subscription.renewal.failed_email.sent")

Occurs whenever a failure renewal processing email is sent to the buyer.

`subscription.renewal.retry`[](#subscription-renewal-retry "Direct link to subscription.renewal.retry")

Occurs whenever a renewal payment retry is processed.

`subscription.renewals.discounted`[](#subscription-renewals-discounted "Direct link to subscription.renewals.discounted")

Occurs whenever a special subscription cancellation promo is applied.

### Store[​](#store "Direct link to Store")

`store.created`[](#store-created "Direct link to store.created")

Occurs when a new store has been created (e.g. when a new Freemius account has been created).

`store.dashboard_url.updated`[](#store-dashboard_url-updated "Direct link to store.dashboard_url.updated")

Occurs when the store’s dashboard URL is updated.

`store.plugin.added`[](#store-plugin-added "Direct link to store.plugin.added")

Occurs when a product is added to a store.

`store.plugin.removed`[](#store-plugin-removed "Direct link to store.plugin.removed")

Occurs when a product is removed from a store.

`store.url.updated`[](#store-url-updated "Direct link to store.url.updated")

Occurs when a store’s URL is updated.

### User[​](#user "Direct link to User")

`user.beta_program.opted_in`[](#user-beta_program-opted_in "Direct link to user.beta_program.opted_in")

Occurs when a user has opted into a product's beta program.

`user.beta_program.opted_out`[](#user-beta_program-opted_out "Direct link to user.beta_program.opted_out")

Occurs when a user has opted out of a product's beta program.

`user.billing.updated`[](#user-billing-updated "Direct link to user.billing.updated")

Occurs whenever a customer billing information is updated (e.g. address, VAT ID, company name).

`user.billing.tax_id.updated`[](#user-billing-tax_id-updated "Direct link to user.billing.tax_id.updated")

Occurs whenever the tax ID associated with the user’s billing is changed.

`user.card.created`[](#user-card-created "Direct link to user.card.created")

Occurs whenever a new card is added to a user’s account.

`user.created`[](#user-created "Direct link to user.created")

Occurs whenever a new user is created.

`user.email.changed`[](#user-email-changed "Direct link to user.email.changed")

Occurs whenever a user update their email address.

`user.email.verified`[](#user-email-verified "Direct link to user.email.verified")

Occurs when a user email is verified (usually via email confirmation).

`user.email_status.bounced`[](#user-email_status-bounced "Direct link to user.email_status.bounced")

Occurs when a transactional email sent to a user bounces, which also changes the user’s email\_status property to 'bounced'.

`user.email_status.delivered`[](#user-email_status-delivered "Direct link to user.email_status.delivered")

Occurs when a transactional email sent to a user is successfully delivered and only if the user’s previous deliverability state (aka the email\_status property) was not empty before.

`user.email_status.dropped`[](#user-email_status-dropped "Direct link to user.email_status.dropped")

Occurs when a transactional email sent to a user is dropped, which also changes the user’s email\_status property to 'dropped'.

`user.marketing.opted_in`[](#user-marketing-opted_in "Direct link to user.marketing.opted_in")

Occurs when a user has opted to receive marketing material (emails).

`user.marketing.opted_out`[](#user-marketing-opted_out "Direct link to user.marketing.opted_out")

Occurs when a user has opted out of a receiving marketing material (emails).

`user.marketing.reset`[](#user-marketing-reset "Direct link to user.marketing.reset")

Occurs when a user’s marketing status has been reset.

`user.name.changed`[](#user-name-changed "Direct link to user.name.changed")

Occurs whenever a user update their name.

`user.support.contacted`[](#user-support-contacted "Direct link to user.support.contacted")

Occurs when a user submits a support ticket via the contact form in the Customer Portal.

`user.trial.started`[](#user-trial-started "Direct link to user.trial.started")

Occurs when a user registers for a trial.

### Webhook[​](#webhook "Direct link to Webhook")

`webhook.created`[](#webhook-created "Direct link to webhook.created")

Occurs whenever a webhook is created.

`webhook.deleted`[](#webhook-deleted "Direct link to webhook.deleted")

Occurs whenever a webhook is deleted.

`webhook.updated`[](#webhook-updated "Direct link to webhook.updated")

Occurs whenever a webhook is updated.

### WordPress[​](#wordpress "Direct link to WordPress")

`addon.free.downloaded`[](#addon-free-downloaded "Direct link to addon.free.downloaded")

Occurs whenever a free version of an add-on is downloaded.

`addon.premium.downloaded`[](#addon-premium-downloaded "Direct link to addon.premium.downloaded")

Occurs whenever a premium version of an add-on is downloaded.

`install.extensions.opt_in`[](#install-extensions-opt_in "Direct link to install.extensions.opt_in")

Occurs whenever a user opts in for sharing a website’s plugins & themes list after previously opting out from it.

`install.extensions.opt_out`[](#install-extensions-opt_out "Direct link to install.extensions.opt_out")

Occurs whenever a user opt-out from sharing a website’s plugins & themes list after previously sharing it.

`install.ownership.candidate.confirmed`[](#install-ownership-candidate-confirmed "Direct link to install.ownership.candidate.confirmed")

Occurs whenever an account ownership transfer candidate confirms the transfer.

`install.ownership.completed`[](#install-ownership-completed "Direct link to install.ownership.completed")

Occurs whenever an account ownership transfer is complete.

`install.ownership.initiated`[](#install-ownership-initiated "Direct link to install.ownership.initiated")

Occurs whenever an account ownership transfer is initiated.

`install.ownership.owner.confirmed`[](#install-ownership-owner-confirmed "Direct link to install.ownership.owner.confirmed")

Occurs whenever an account ownership transfer is confirmed by the current installation account owner.

`install.site.opt_in`[](#install-site-opt_in "Direct link to install.site.opt_in")

Occurs whenever a user opts in for sharing basic website after previously opting out from it.

`install.site.opt_out`[](#install-site-opt_out "Direct link to install.site.opt_out")

Occurs whenever a user opts out from sharing basic website after previously sharing it.

`install.user.opt_in`[](#install-user-opt_in "Direct link to install.user.opt_in")

Occurs whenever a user opts in for sharing their basic profile info after previously opting out from it.

`install.user.opt_out`[](#install-user-opt_out "Direct link to install.user.opt_out")

Occurs whenever a user opts out from sharing their basic profile info after previously sharing it.

`license.site.blacklisted`[](#license-site-blacklisted "Direct link to license.site.blacklisted")

Occurs when a site has been blacklisted in the Customer Portal.

`license.blacklisted_site.deleted`[](#license-blacklisted_site-deleted "Direct link to license.blacklisted_site.deleted")

Occurs when a blacklisted site has been removed in the Customer Portal.

`license.site.whitelisted`[](#license-site-whitelisted "Direct link to license.site.whitelisted")

Occurs when a site has been whitelisted in the Customer Portal.

`license.whitelisted_site.deleted`[](#license-whitelisted_site-deleted "Direct link to license.whitelisted_site.deleted")

Occurs when a whitelisted site has been removed in the Customer Portal.

`plugin.free.downloaded`[](#plugin-free-downloaded "Direct link to plugin.free.downloaded")

Occurs whenever a free product version is downloaded.

`plugin.premium.downloaded`[](#plugin-premium-downloaded "Direct link to plugin.premium.downloaded")

Occurs whenever a paid product version is downloaded.

`plugin.version.deleted`[](#plugin-version-deleted "Direct link to plugin.version.deleted")

Occurs whenever a deployed version is deleted.

`plugin.version.deployed`[](#plugin-version-deployed "Direct link to plugin.version.deployed")

Occurs whenever a new product version is deployed to Freemius.

`plugin.version.released`[](#plugin-version-released "Direct link to plugin.version.released")

Occurs whenever a version is set as released.

`plugin.version.beta.released`[](#plugin-version-beta-released "Direct link to plugin.version.beta.released")

Occurs whenever a version is released as beta.

`plugin.version.release.suspended`[](#plugin-version-release-suspended "Direct link to plugin.version.release.suspended")

Occurs whenever a deployment release is suspended.

`plugin.version.updated`[](#plugin-version-updated "Direct link to plugin.version.updated")

Occurs whenever an existing version is re-deployed to Freemius.

`pricing.visit`[](#pricing-visit "Direct link to pricing.visit")

Occurs when a user has visited the pricing table via the WordPress admin or popup checkout modal.