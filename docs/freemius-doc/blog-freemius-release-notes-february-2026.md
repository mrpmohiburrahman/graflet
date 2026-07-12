A lot happens between checkout and renewal. February’s release brings more visibility and control to that space — the emails buyers receive, the portal they use to manage their account, and the tools makers rely on behind the scenes.

Alongside the headlining features, a set of targeted fixes and improvements keeps the Freemius platform consistent and reliable under the hood.

With downloadable software, the default [Customer Portal](customer-portal.md) login works well. Buyers don’t create an account to purchase, so a separate password is a reasonable ask when they need to manage something later.

SaaS is different. Users already have an account with you before they upgrade. Asking them to remember a separate Freemius login to manage billing creates avoidable friction.

[The customer portal magic links login](blog-changelog-one-click-customer-portal-login-via-api.md) is a lightweight fix. An API call generates a secure link you can place behind any “Billing” or “Manage my account” link in your product. When a customer clicks it, they’re logged straight into the portal to:

- Cancel or upgrade their subscription
- Update billing details
- Change payment methods
- Join the affiliate program

![One click Customer Portal login for Freemius SaaS products](https://freemius.com/blog/wp-content/uploads/2026/02/one-click-customer-portal-login-for-freemius-saas-products.jpeg)

The link expires after five minutes and is only generated on request — no separate password required.

## Custom Content for Key Transactional Emails

Freemius [transactional emails](help-documentation-marketing-automation-transactional-emails.md) are optimized for buyers, but makers had no way of adding anything to them.

For app and SaaS products, the gap was most painful. Without a way to include a download link in the purchase email, buyers ended up with three emails after a single purchase: confirmation, receipt, and download link — the last of which often meant a webhook integration.

[Custom content for transactional emails](blog-changelog-customize-key-transactional-emails-with-custom-content.md) removes that fragmentation. Makers can now add a custom section to:

- New subscription emails
- New one-off & lifetime purchase emails
- Subscription renewal emails

![Custom content for key transactional emails sent by Freemius](https://freemius.com/blog/wp-content/uploads/2026/02/custom-content-for-key-transactional-emails-sent-by-freemius.jpeg)

[![](https://freemius.com/blog/wp-content/uploads/2026/03/Example-of-Freemius-transactional-email-with-custom-content.jpg)](https://freemius.com/blog/wp-content/uploads/2026/03/Example-of-Freemius-transactional-email-with-custom-content.jpg)

Content supports Markdown with a live preview, so formatting stays consistent with your brand without requiring another integration.

WordPress products can use it for usage instructions or post-activation next steps. Renewal emails are a natural place to highlight new features and reinforce ongoing value.

## Redesigned Cart Recovery Unsubscribe Page

Freemius’s [built-in cart recovery system](help-documentation-marketing-automation-cart-abandonment-recovery.md) sends reminder emails to buyers who didn’t complete a purchase. Until recently, the unsubscribe page behind those emails hadn’t kept pace with the rest of the platform.

![Redesigned Freemius cart recovery unsubscribe page](https://freemius.com/blog/wp-content/uploads/2026/02/redesigned-freemius-cart-recovery-unsubscribe-page.jpeg)

[The page has been redesigned](blog-changelog-redesigned-cart-recovery-unsubscribe-page.md) to match Freemius’s current visual language, as part of the ongoing effort to align every customer-facing touchpoint with the [broader rebrand](blog-freemius-rebrand-website-developer-dashboard-redesign.md). The experience and functionality remain the same.

## Email History: See Every Email Freemius Sends Your Buyers

Makers already had some visibility into buyer communications:

- A notification center for toggling email types on or off
- A 30-day SendGrid log with subject lines, addresses, deliverability status, open rates, and error messages

What was missing were the actual emails. There was no way to see content without waiting for a specific event to trigger one.

![Email History to see every email Freemius sends](https://freemius.com/blog/wp-content/uploads/2026/02/email-history-to-see-every-email-freemius-sends.jpeg)

[Email History fixes that](blog-changelog-see-all-buyer-emails-sent-by-freemius-in-one-place.md). A new tab in the Emails section lists every email sent on behalf of your product, with HTML and plain-text previews for each (previews currently available for 7 days).

![HTML and plain-text preview of Freemius email in Email History](https://freemius.com/blog/wp-content/uploads/2026/02/html-and-plain-text-preview-of-freemius-email-in-email-history.jpeg)

This is the first phase. The longer-term goal is to centralize all email types — purchases, renewal reminders, payment notifications, cart recovery — in one place.

## Multiple Domain Support for Embedded Customer Portal

The embedded Customer Portal was restricted to a single whitelisted domain. If the domain didn’t match, the portal blocked rendering entirely.

That created friction in two scenarios:

- **Testing across environments.** Switching to staging or localhost meant breaking the production embed, and vice versa.
- **Multi-brand setups.** No way to embed the portal across multiple domains at the same time.

[Support for multiple whitelisted domains removes both restrictions](blog-changelog-support-for-multiple-domains-when-embedding-the-customer-portal.md) so the portal loads securely across all your environments and properties without any manual switching. You can now add multiple domains in Store Settings under “Additional Whitelisted Domains.”

![Multiple whitelisted domain support for embedded Freemius Customer Portal](https://freemius.com/blog/wp-content/uploads/2026/02/multiple-whitelisted-domain-support-for-embedded-freemius-customer-portal.jpeg)

## New Side Panel View for Licenses in the Developer Dashboard

The Licenses page showed everything in a table — functional, but dense. Full context on a license meant navigating away to separate pages, adding unnecessary steps to routine tasks.

The [new side panel view](blog-changelog-new-side-panel-view-for-licenses-in-the-developer-dashboard.md) brings it all into one place:

- Connected user and subscription details
- Common actions: extending the license, changing the quota, or adjusting per-license settings
- Mobile-friendly navigation between licenses without leaving the page

![Side panel view for licenses in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/02/side-panel-view-for-licenses-in-freemius-developer-dashboard.jpeg)

The experience is now consistent across licenses and subscriptions. On mobile, the same panel means no more jumping between screens.

![Side panel view for subscriptions in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/02/side-panel-view-for-subscriptions-in-freemius-developer-dashboard.jpeg)

## Staying Current With WordPress.org Compliance

Following updated guidelines from the WordPress Plugin Review Team, the `is_org_compliant` flag in the SDK integration snippet is now included by default regardless of its value. As it defaults to `true`, previously, it only appeared if explicitly set to `false`.

The issue surfaced when a plugin being relisted after delisting was rejected, with the missing flag cited as a reason. Freemius reached out directly to the review team, confirmed the requirement, and updated the SDK.

That proactive coordination reduces friction for every maker shipping through WordPress.org.

Keeping Freemius-powered products aligned with WordPress.org standards is an ongoing commitment — one that helps ensure smooth submissions as those standards evolve.

## The B-Side Hits

While not chart-toppers, these smaller fixes round out the record. This month’s smaller updates cover security, reliability, and consistency across checkout, the Customer Portal, the Developer Dashboard, and the API — the kind of work that keeps everything running as it should.

**Analytics**

- [Analytics performance improvements for large products](blog-changelog-analytics-performance-improvements-for-large-products.md)

**Developer Dashboard and Admin**

- [Extra security for “Login as User” in the Developer Dashboard](blog-changelog-extra-security-for-login-as-user-in-the-developer-dashboard.md)
- [Improved sidebar sorting and icon validation](blog-changelog-improved-sidebar-sorting-and-icon-validation-in-the-developer-dashboard.md)
- [Clearer templates, kits, and small dashboard improvements](blog-changelog-clearer-templates-kits-and-small-dashboard-improvements.md)
- [API and backend stability improvements](blog-changelog-api-backend-stability-improvements.md)
- [Bug fixes for weekly reports and license activation](blog-changelog-bug-fixes-for-weekly-reports-and-license-activation.md)

**Customer Portal**

- [Renewal now disabled for cancelled licenses](blog-changelog-customer-portal-now-blocks-renewal-of-cancelled-licenses.md)
- [Refinements and layout fixes](blog-changelog-refinements-and-layout-fixes-in-the-customer-portal.md)

**Checkout and Payments**

- [Smarter billing cycle selection and coupon fixes](blog-changelog-smarter-billing-cycle-selection-and-coupon-fixes-in-checkout.md)
- [New checkout events for tracking coupon interactions](blog-changelog-new-checkout-events-for-tracking-coupon-interactions.md)
- [Trial reminder consent now accurately shown at review step](blog-changelog-trial-reminder-consent-now-accurately-shown-in-review-step.md)
- [Resolved regression in review submission links](blog-changelog-resolved-regression-in-review-submission-links.md)

**Emails**

- [Email tone preferences now applied consistently](blog-changelog-email-tone-preferences-now-applied-consistently.md)

**Webhooks**

- [Enriched payloads for plugin version release events](blog-changelog-enriched-webhook-payloads-for-plugin-version-release-events.md)

## The Details That Keep Buyers Coming Back

Retention isn’t just a pricing problem. It’s shaped by every email a buyer receives, every time they need to manage their account, and every interaction they have with your product after the sale. Every update this month touches that experience in some way.

Small improvements in these areas compound over time. What we build next is shaped by what you’re running into, [so keep the feedback coming](https://freemius.nolt.io/).