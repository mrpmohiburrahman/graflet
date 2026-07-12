---
title: "Migrating from Easy Digital Downloads to Freemius"
url: "https://freemius.com/help/documentation/migration/migrating-from-edd-to-freemius/"
source: "docs"
section: "Docs"
category: "Migration"
scraped_at: "2026-04-09T19:58:39+06:00"
word_count: 1266
---

With over a decade of experience, we have perfected the migration of software companies from Easy Digital Downloads (EDD) to Freemius. Our efficient and robust two-step process ensures a seamless transition:

1. **Data Import:** Transfer all relevant data from EDD to Freemius.
2. **Ongoing Renewals Syncing:** For stores with active, auto-renewing subscriptions, we connect your payment processors to Freemius via webhooks. This ensures that every renewal of a migrated subscription prompts Freemius to extend the corresponding license expiry date.

warning

**Important:** If your store has a small number of active subscriptions or the potential renewal volume is low (below $1,000), setting up ongoing renewal syncing might be more effort than the potential benefits. In these cases, the migration will primarily involve the export and import of customer and license data from EDD to Freemius, without the ongoing renewal syncing setup.

### Preliminary Assessment[​](#preliminary-assessment "Direct link to Preliminary Assessment")

Each EDD store is unique, featuring various extensions, customizations, and specific needs. To tailor the migration perfectly to your requirements, we begin with a preliminary assessment. Here’s what we need from you:

01. Which version of EDD are you currently using?
02. What EDD extensions and their versions are you using?
03. Are you migrating freemium products, premium-only, or both?
04. What types of products are you dealing with? (e.g., SaaS, plugins, themes, add-ons)
05. Do you have a licensing system in place? If yes, please provide an example of a license key and confirm if it is stored in the WordPress database upon activation.
06. Should customers be able to activate expired licenses post-migration, or would you prefer to enforce valid license activation for usage?
07. How many active subscriptions with auto-renewal do you have, and what are the associated payment processors? (e.g., Stripe, PayPal)
08. Are there any specific access restrictions on your site? E.g., pages that are only accessible for active license holders?
09. How urgent is your migration timeline?
10. What is your average monthly sales volume? This helps us determine eligibility for high-volume pricing.

Your detailed responses will help ensure your transition to Freemius is as frictionless as possible.

### Migration Kick-off[​](#migration-kick-off "Direct link to Migration Kick-off")

To start the process of migration, reach out to us at [\[email protected\]](/cdn-cgi/l/email-protection#a6d5d3d6d6c9d4d2e6c0d4c3c3cbcfd3d588c5c9cb) with:

1. The link(s) to the EDD purchase/pricing page(s) of the product(s) to be migrated.
2. A short description of the product(s).
3. And the detailed answers to the [preliminary assessment above](#preliminary-assessment).

Then a dedicated migration lead will be assigned to your project, who will follow up typically within 72 hours.

Upon receiving all necessary information, we will develop a detailed, step-by-step migration plan, usually delivered within three business days.

### Migration Execution[​](#migration-execution "Direct link to Migration Execution")

Depending on the complexity of your migration and available technical resources, you should be able to follow the provided steps and execute the migration with our guidance. If you prefer a more hands-on approach from our team, just let us know! We will provide a symbolic quote for the required time and resources. This amount will be credited back to you as a fee waiver against the revenue sharing once you begin actively selling through Freemius, effectively making the migration cost-neutral.

### Migrations Queue[​](#migrations-queue "Direct link to Migrations Queue")

Due to the tailored nature of each migration, the process requires the dedicated attention of a specialized migrations engineer. Our team continuously receives migration requests, resulting in a managed queue. The timing of your migration will depend on the current queue status, which means there might be a brief waiting period. To expedite your migration, we encourage you to provide all necessary information as soon as possible. The more promptly we receive your complete details, the sooner we can schedule and begin your migration. Rest assured, our team is committed to handling each request with the utmost efficiency and care to minimize any delays and ensure a smooth transition to Freemius.

### Automatic License Activation[​](#automatic-license-activation "Direct link to Automatic License Activation")

To streamline the transition for your customers, we offer a little [code snippet](https://gist.github.com/vovafeldman/f554174b8c68e2ce8a764b8801231a27#file-fs-migrated-license-auto-activation-php) that automatically activates migrated EDD licenses from the WordPress Database. This prevents any need for your customers to re-enter their license keys after updating the product to the newest version with Freemius licensing.

### EDD Migration FAQ[​](#edd-migration-faq "Direct link to EDD Migration FAQ")

#### Will Freemius take a cut of renewals for subscriptions migrated from EDD?[​](#will-freemius-take-a-cut-of-renewals-for-subscriptions-migrated-from-edd "Direct link to Will Freemius take a cut of renewals for subscriptions migrated from EDD?")

No, we do not take a cut from renewals processed through your legacy payment gateways.

#### How would I handle refunds of EDD payments?[​](#how-would-i-handle-refunds-of-edd-payments "Direct link to How would I handle refunds of EDD payments?")

Freemius cannot process refunds or manage disputes for EDD originated transactions. These must be handled directly through your original payment processors like Stripe and PayPal.

#### Will Freemius issue invoices for renewals?[​](#will-freemius-issue-invoices-for-renewals "Direct link to Will Freemius issue invoices for renewals?")

We do not issue invoices for renewals of legacy subscriptions initiated through EDD. However, we will issue invoices for transactions processed directly through Freemius.

#### Will Freemius handle VAT and sales tax after the migration?[​](#will-freemius-handle-vat-and-sales-tax-after-the-migration "Direct link to Will Freemius handle VAT and sales tax after the migration?")

Freemius automatically manages global sales tax for all purchases and subscriptions processed through our platform. However, for subscription renewals managed through your original payment gateways, the responsibility for handling VAT and sales tax remains with you.

#### Can Freemius process renewals of subscriptions initially created via EDD?[​](#can-freemius-process-renewals-of-subscriptions-initially-created-via-edd "Direct link to Can Freemius process renewals of subscriptions initially created via EDD?")

By default, renewal payments of subscriptions initiated through EDD are synchronized with Freemius but are not directly processed by us. If you wish for Freemius to manage these renewals, there are additional steps to transition active subscriptions from your payment processors to ours. This service is available with processors like Stripe but is not supported by PayPal. Once subscriptions are successfully migrated to our payment processros, we take responsibility for managing renewals, including handling taxes, security, refunds, and disputes. Please note, the revenue-sharing will be applicable to such renewals.

#### Can I migrate my active Stripe subscriptions to Freemius?[​](#can-i-migrate-my-active-stripe-subscriptions-to-freemius "Direct link to Can I migrate my active Stripe subscriptions to Freemius?")

Yes! While not mandatory, we can help you migrate your Stripe subscriptions to Freemius.

#### Can I migrate my active PayPal subscriptions to Freemius?[​](#can-i-migrate-my-active-paypal-subscriptions-to-freemius "Direct link to Can I migrate my active PayPal subscriptions to Freemius?")

Unfortunately, PayPal does not support migrating subscriptions to other accounts.

#### Do I need to continue using EDD after the migration is complete?[​](#do-i-need-to-continue-using-edd-after-the-migration-is-complete "Direct link to Do I need to continue using EDD after the migration is complete?")

No. Once the migration to Freemius is fully completed, there is no further need for EDD or its extensions. This transition allows you to streamline your operations and focus exclusively on your products and customers. Additionally, you have the flexibility to sell from a static website, eliminating the need to run the WordPress engine, thereby simplifying your digital storefront.

#### Can I close my Stripe and PayPal accounts after the migration?[​](#can-i-close-my-stripe-and-paypal-accounts-after-the-migration "Direct link to Can I close my Stripe and PayPal accounts after the migration?")

It is advisable to keep your Stripe and PayPal accounts active as long as you have subscriptions that continue to auto-renew under these platforms. Additionally, we recommend maintaining these accounts for at least six months post-migration to address any needs that may arise for processing refunds or handling disputes associated with payments made through your legacy payment processors. This ensures a safety net during the transition period.